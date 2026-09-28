"""Small logging heartbeat for long synchronous operations."""

from __future__ import annotations

from contextlib import contextmanager
import logging
from threading import Event, Thread
import time
from typing import Iterator


@contextmanager
def progress_heartbeat(
    logger: logging.Logger,
    message: str,
    *,
    interval_seconds: float = 30.0,
) -> Iterator[None]:
    """Log elapsed time while a blocking provider call is still running."""
    if interval_seconds <= 0:
        yield
        return

    stopped = Event()
    started_at = time.monotonic()

    def report() -> None:
        while not stopped.wait(interval_seconds):
            elapsed = int(round(time.monotonic() - started_at))
            logger.info("%s — %ss trascorsi", message, elapsed)

    thread = Thread(target=report, name="legalita-progress-heartbeat", daemon=True)
    thread.start()
    try:
        yield
    finally:
        stopped.set()
        thread.join(timeout=min(interval_seconds, 1.0))

