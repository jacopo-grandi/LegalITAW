"""`legalitaw valuta`: valutazione standard di una run LegalITAW in un comando.

Fase 1, in parallelo: Jev su tutti gli incarichi e Luna divisa in N parti.
Fase 2, quando entrambi hanno finito: la terna (Jev + Luna + arbitro), che
riusa i loro voti e chiama l'arbitro solo sui disaccordi.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Sequence, TextIO

from .parallel import split_blocks

COMMON = [
    "--expected", "all",
    "--judge-batch-size", "10",
    "--judge-audit-sample-rate", "0",
    "--judge-context", "compact",
]
JEV = ["--judge-a-provider", "typesafe", "--judge-a-model", "jev-1.13.0"]
LUNA = ["--judge-a-provider", "openai", "--judge-a-model", "gpt-5.6-luna"]
DEFAULT_ARBITRO = "claude-opus-5-5"


def arbitro_provider(model: str) -> str:
    name = model.lower()
    if name.startswith("claude-"):
        return "anthropic"
    if name.startswith(("gpt-", "o1", "o3", "o4")):
        return "openai"
    if name.startswith("gemini-"):
        return "gemini"
    raise ValueError(f"arbitro {model!r}: provider non riconosciuto (usa un modello claude-, gpt- o gemini-)")


def _latest_or_new(folder: Path, today: str, nuova: bool) -> Path:
    """Riusa l'ultima cartella datata (così lo scoring riprende dai checkpoint)."""
    if not nuova and folder.is_dir():
        dated = sorted(p for p in folder.iterdir() if p.is_dir())
        if dated:
            return dated[-1]
    return folder / today


@dataclass
class Job:
    label: str
    argv: list[str]
    out: Path
    log: Path
    n_tasks: int
    process: Any = None
    handle: TextIO | None = None
    returncode: int | None = None

    def progress(self) -> str:
        scored = len(list((self.out / "scores").glob("*.json"))) if (self.out / "scores").is_dir() else 0
        errors = len(list((self.out / "errors").glob("*.json"))) if (self.out / "errors").is_dir() else 0
        text = f"{self.label} {scored}/{self.n_tasks}"
        if errors:
            text += f" ({errors} con errori)"
        if self.returncode not in (None, 0):
            text += f" [codice {self.returncode}]"
        return text

    def summary_line(self) -> str:
        try:
            lines = self.log.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            return "(log non leggibile)"
        found = [line for line in lines if line.startswith("overall_score=")]
        return found[-1] if found else "(nessun riepilogo nel log)"


def build_jobs(args: argparse.Namespace, task_ids: Sequence[str], *, today: str | None = None) -> tuple[list[Job], Job, Path]:
    """Prepara i processi della fase 1 (Jev, Luna a parti) e quello della terna."""
    from .v2 import _default_results_base, _slug

    day = today or dt.date.today().isoformat()
    base = (args.risultati or _default_results_base()).expanduser()
    name = _slug(args.nome or f"{args.modello}-{args.ragionamento}")
    source = base / f"{name}-wf2-100"
    scores = base / "v2-scores"
    logs = base / "logs" / f"{day}_{name}"
    prefix = [sys.executable, "-m", "legalitaw.cli.v2", "--root", str(args.root), "score", str(source), "--model", args.modello]

    def out(suffix: str) -> Path:
        return _latest_or_new(scores / f"{name}-wf2-100-{suffix}", day, args.nuova)

    jev_out = out("jev")
    phase1 = [
        Job("jev", prefix + COMMON + ["--judge-strategy", "batched_single", *JEV, "--out", str(jev_out)],
            jev_out, logs / "score_jev.log", len(task_ids)),
    ]
    parts = split_blocks(list(task_ids), args.parti_luna)
    luna_outs: list[Path] = []
    for index, part in enumerate(parts, start=1):
        suffix = "luna" if len(parts) == 1 else f"luna-p{index}"
        luna_out = out(suffix)
        luna_outs.append(luna_out)
        argv = prefix + COMMON + ["--judge-strategy", "batched_single", *LUNA, "--out", str(luna_out)]
        if len(parts) > 1:
            argv += ["--tasks", *part]
        label = "luna" if len(parts) == 1 else f"luna p{index}"
        phase1.append(Job(label, argv, luna_out, logs / f"score_{suffix.replace('-', '_')}.log", len(part)))

    provider = arbitro_provider(args.arbitro)
    terna_suffix = "terna-disaccordi" if args.arbitro == DEFAULT_ARBITRO else f"terna-{_slug(args.arbitro)}"
    terna_out = out(terna_suffix)
    terna_argv = prefix + COMMON + [
        "--judge-strategy", "paired_consensus",
        *JEV,
        "--judge-b-provider", "openai", "--judge-b-model", "gpt-5.6-luna",
        "--judge-c-provider", provider, "--judge-c-model", args.arbitro,
        "--reuse-votes", str(jev_out), *map(str, luna_outs),
        "--tie-breaker-scope", "disagreements",
        "--max-estimated-judge-cost-usd", "100",
        "--out", str(terna_out),
    ]
    terna = Job("terna", terna_argv, terna_out, logs / "score_terna.log", len(task_ids))
    return phase1, terna, source


def _run_jobs(
    jobs: Sequence[Job],
    *,
    popen: Callable[..., Any],
    sleep: Callable[[float], None],
    clock: Callable[[], float],
    every: int,
    out: TextIO,
) -> bool:
    for job in jobs:
        job.out.mkdir(parents=True, exist_ok=True)
        job.log.parent.mkdir(parents=True, exist_ok=True)
        job.handle = open(job.log, "a", encoding="utf-8")
        job.process = popen(job.argv, stdout=job.handle, stderr=subprocess.STDOUT)
        print(f"{job.label}: -> {job.out}  (log {job.log.name})", file=out, flush=True)
    last = clock()
    try:
        while True:
            for job in jobs:
                if job.returncode is None:
                    code = job.process.poll()
                    if code is not None:
                        job.returncode = code
                        esito = "finito" if code == 0 else f"fermo con codice {code}, vedi {job.log}"
                        print(f"{job.label} {esito}.", file=out, flush=True)
            if all(job.returncode is not None for job in jobs):
                break
            if clock() - last >= every:
                stamp = dt.datetime.now().strftime("%H:%M")
                print(f"{stamp}  " + " · ".join(job.progress() for job in jobs), file=out, flush=True)
                last = clock()
            sleep(2)
    except KeyboardInterrupt:
        print("\nInterruzione: attendo che i giudici salvino i checkpoint…", file=out, flush=True)
        for job in jobs:
            if job.returncode is None:
                try:
                    job.returncode = job.process.wait(timeout=30)
                except Exception:
                    job.process.terminate()
                    job.returncode = job.process.wait()
        raise
    finally:
        for job in jobs:
            if job.handle is not None and not job.handle.closed:
                job.handle.close()
    return all(job.returncode == 0 for job in jobs)


def valuta(
    args: argparse.Namespace,
    task_ids: Sequence[str],
    *,
    popen: Callable[..., Any] = subprocess.Popen,
    sleep: Callable[[float], None] = time.sleep,
    clock: Callable[[], float] = time.monotonic,
    out: TextIO | None = None,
    today: str | None = None,
) -> int:
    out = out or sys.stdout
    phase1, terna, source = build_jobs(args, task_ids, today=today)
    if not source.is_dir():
        print(f"Cartella della run non trovata: {source}\nUsa --nome come in `legalitaw lancia`.", file=out)
        return 2
    every = max(1, int(args.progress_every))
    started = clock()
    print(f"{args.modello}: valuto {source}", file=out)
    print(f"Fase 1: Jev e Luna in {len(phase1) - 1} parti, in parallelo.", file=out, flush=True)
    try:
        ok = _run_jobs(phase1, popen=popen, sleep=sleep, clock=clock, every=every, out=out)
        if not ok:
            print("\nUn giudice si è fermato: la terna non parte. Rilancia lo stesso comando per riprendere.", file=out)
            return 1
        print(f"\nFase 2: terna con arbitro {args.arbitro} sui disaccordi.", file=out, flush=True)
        ok = _run_jobs([terna], popen=popen, sleep=sleep, clock=clock, every=every, out=out)
    except KeyboardInterrupt:
        print("Per riprendere rilancia lo stesso comando: i giudici ripartono dai checkpoint.", file=out)
        return 130
    minutes = int((clock() - started) // 60)
    print(f"\nFatto in {minutes // 60}h{minutes % 60:02d}m.", file=out)
    for job in [*phase1, terna]:
        print(f"{job.label:8} {job.summary_line()}", file=out)
    print(f"risultato finale (terna): {terna.out}", file=out, flush=True)
    return 0 if ok else 1
