"""Run LegalITAW divisa in blocchi lanciati in parallelo.

`legalitaw run --model X --parallel 4` divide gli incarichi selezionati in 4
blocchi contigui e lancia un processo `run --tasks ...` per blocco: ogni blocco
scrive la propria run in `<results>/v2-runs/` e il proprio log, come quando si
aprono 4 terminali a mano. Il processo principale mostra l'avanzamento.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Sequence, TextIO

# Opzioni di `run` passate tali e quali a ogni blocco.
FORWARDED_OPTIONS = (
    ("--profile", "profile"),
    ("--max-agent-steps", "max_agent_steps"),
    ("--timeout-seconds", "timeout_seconds"),
    ("--max-agent-cost-usd", "max_agent_cost_usd"),
    ("--max-task-attempts", "max_task_attempts"),
)


def split_blocks(items: Sequence[Any], n: int) -> list[list[Any]]:
    """Divide in n blocchi contigui; le dimensioni differiscono al massimo di 1."""
    if n < 1:
        raise ValueError("--parallel deve essere almeno 1")
    if not items:
        return []
    n = min(n, len(items))
    size, extra = divmod(len(items), n)
    blocks: list[list[Any]] = []
    start = 0
    for index in range(n):
        end = start + size + (1 if index < extra else 0)
        blocks.append(list(items[start:end]))
        start = end
    return blocks


def _read_json(path: Path) -> dict[str, Any] | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return data if isinstance(data, dict) else None


def _run_manifests(results_root: Path) -> list[Path]:
    return sorted((results_root / "v2-runs").glob("*/run_manifest.json"))


def done_task_ids(results_root: Path, *, model: str | None = None) -> set[str]:
    """Incarichi che hanno già un esito (consegnato o fallito) in `results_root`.

    Non conta l'incarico su cui una run si è fermata per un errore non
    ripetibile (es. limite di spesa): quello va rifatto.
    """
    done: set[str] = set()
    for path in _run_manifests(results_root):
        manifest = _read_json(path)
        if not manifest or (model and manifest.get("model") != model):
            continue
        done.update(manifest.get("completed_task_ids") or [])
        failed = set(manifest.get("failed_task_ids") or [])
        failed.discard(manifest.get("aborted_task_id"))
        done.update(failed)
    return done


def child_argv(args: argparse.Namespace, task_ids: Sequence[str]) -> list[str]:
    argv = [
        sys.executable,
        "-m",
        "legalitaw.cli.v2",
        "--root",
        str(args.root),
        "run",
        "--model",
        args.model,
        "--results",
        str(args.results),
    ]
    for flag, attr in FORWARDED_OPTIONS:
        value = getattr(args, attr, None)
        if value is not None:
            argv += [flag, str(value)]
    return argv + ["--tasks", *task_ids]


@dataclass
class _Block:
    index: int
    task_ids: list[str]
    log_path: Path
    process: Any = None
    log_handle: TextIO | None = None
    run_root: Path | None = None
    returncode: int | None = None
    costs: dict[str, float] = field(default_factory=dict)

    @property
    def label(self) -> str:
        return f"b{self.index}"

    @property
    def span(self) -> str:
        return f"{self.task_ids[0]}–{self.task_ids[-1]}"


def _attempt_cost(directory: Path) -> float | None:
    for name in ("submission.json", "failure.json"):
        path = directory / name
        if path.exists():
            data = _read_json(path) or {}
            metrics = data.get("model_call_metrics") or {}
            return float(metrics.get("estimated_cost_usd") or 0.0)
    return None


def _block_status(block: _Block) -> dict[str, Any]:
    status = {"done": 0, "failed": 0, "cost": 0.0, "state": "avvio"}
    if block.run_root is None:
        return status
    manifest = _read_json(block.run_root / "run_manifest.json")
    if not manifest:
        return status
    status["done"] = len(manifest.get("completed_task_ids") or [])
    status["failed"] = len(manifest.get("failed_task_ids") or [])
    status["state"] = manifest.get("run_status", "running")
    for attempts in (manifest.get("attempts") or {}).values():
        for relative in attempts:
            if relative not in block.costs:
                cost = _attempt_cost(block.run_root / relative)
                if cost is not None:
                    block.costs[relative] = cost
    status["cost"] = sum(block.costs.values())
    return status


def _find_run_root(block: _Block, results_root: Path, known: set[Path]) -> Path | None:
    for path in _run_manifests(results_root):
        if path in known:
            continue
        manifest = _read_json(path)
        if manifest and manifest.get("requested_task_ids") == block.task_ids:
            known.add(path)
            return path.parent
    return None


def _fmt_block(block: _Block, status: dict[str, Any]) -> str:
    text = f"{block.label} {status['done'] + status['failed']}/{len(block.task_ids)}"
    if status["failed"]:
        text += f" ({status['failed']} falliti)"
    if block.returncode not in (None, 0):
        text += f" [uscito con codice {block.returncode}]"
    return text


def _fmt_duration(seconds: float) -> str:
    minutes = int(seconds // 60)
    return f"{minutes // 60}h{minutes % 60:02d}m" if minutes >= 60 else f"{minutes}m"


def run_parallel(
    args: argparse.Namespace,
    tasks: Sequence[Any],
    *,
    popen: Callable[..., Any] = subprocess.Popen,
    sleep: Callable[[float], None] = time.sleep,
    clock: Callable[[], float] = time.monotonic,
    out: TextIO | None = None,
) -> int:
    """Lancia i blocchi, mostra l'avanzamento e restituisce il codice d'uscita."""
    out = out or sys.stdout
    results_root = Path(args.results)
    log_dir = getattr(args, "log_dir", None) or (
        results_root / "logs" / dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    )
    log_dir = Path(log_dir).expanduser()
    log_dir.mkdir(parents=True, exist_ok=True)
    every = max(1, int(getattr(args, "progress_every", 60) or 60))

    known = set(_run_manifests(results_root))
    blocks: list[_Block] = []
    for index, chunk in enumerate(split_blocks(list(tasks), args.parallel), start=1):
        ids = [task.spec.task_id for task in chunk]
        block = _Block(index, ids, log_dir / f"b{index}.log")
        block.log_handle = open(block.log_path, "a", encoding="utf-8")
        block.process = popen(
            child_argv(args, ids),
            stdout=block.log_handle,
            stderr=subprocess.STDOUT,
        )
        blocks.append(block)
        print(f"{block.label}: {block.span} ({len(ids)} incarichi) -> {block.log_path}", file=out)
    print(f"{args.model}: {len(tasks)} incarichi in {len(blocks)} blocchi paralleli.", file=out, flush=True)

    started = clock()
    last_report = started

    def report() -> None:
        statuses = [_block_status(block) for block in blocks]
        done = sum(s["done"] + s["failed"] for s in statuses)
        cost = sum(s["cost"] for s in statuses)
        parts = " · ".join(_fmt_block(b, s) for b, s in zip(blocks, statuses))
        stamp = dt.datetime.now().strftime("%H:%M")
        print(f"{stamp}  {parts}  |  {done}/{len(tasks)}  ${cost:.2f}", file=out, flush=True)

    try:
        while True:
            for block in blocks:
                if block.run_root is None:
                    block.run_root = _find_run_root(block, results_root, known)
                if block.returncode is None:
                    code = block.process.poll()
                    if code is not None:
                        block.returncode = code
                        if block.run_root is None:
                            block.run_root = _find_run_root(block, results_root, known)
                        esito = "finito" if code == 0 else f"fermo con codice {code}, vedi {block.log_path}"
                        print(f"{block.label} {esito}.", file=out, flush=True)
            if all(block.returncode is not None for block in blocks):
                break
            if clock() - last_report >= every:
                report()
                last_report = clock()
            sleep(2)
    except KeyboardInterrupt:
        # Ctrl+C dal terminale arriva anche ai blocchi, che segnano la run come
        # interrotta: li aspettiamo un poco prima di chiuderli.
        print("\nInterruzione: attendo che i blocchi salvino lo stato…", file=out, flush=True)
        for block in blocks:
            if block.returncode is None:
                try:
                    block.returncode = block.process.wait(timeout=30)
                except Exception:
                    block.process.terminate()
                    block.returncode = block.process.wait()
        _close_logs(blocks)
        print("Per riprendere rilancia lo stesso comando con --skip-done.", file=out, flush=True)
        return 130

    _close_logs(blocks)
    statuses = [_block_status(block) for block in blocks]
    done = sum(s["done"] for s in statuses)
    failed = sum(s["failed"] for s in statuses)
    cost = sum(s["cost"] for s in statuses)
    print(
        f"\nFatto in {_fmt_duration(clock() - started)}: {done} consegnati, "
        f"{failed} falliti, ${cost:.2f}.",
        file=out,
    )
    for block, status in zip(blocks, statuses):
        run = block.run_root if block.run_root is not None else "(nessuna run creata)"
        print(
            f"{block.label} {block.span}: {status['done']}/{len(block.task_ids)} consegnati, "
            f"{status['failed']} falliti, ${status['cost']:.2f}, codice {block.returncode} -> {run}",
            file=out,
        )
    print(f"log: {log_dir}", file=out, flush=True)
    return 0 if all(block.returncode == 0 for block in blocks) else 1


def _close_logs(blocks: Sequence[_Block]) -> None:
    for block in blocks:
        if block.log_handle is not None and not block.log_handle.closed:
            block.log_handle.close()
