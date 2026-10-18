"""Command-line status report for the AI Factory project memory.

Run with::

    python -m ai_factory

It prints whether each required memory file is present and a short summary of
the task board. Exit code is 0 when every memory file is present and non-empty,
otherwise 1.
"""

from __future__ import annotations

import sys
from pathlib import Path

from .memory import check_memory_files
from .task_board import parse_task_board, summarize


def _repo_root() -> Path:
    """Return the repository root, assuming this file lives in ``ai_factory/``."""
    return Path(__file__).resolve().parent.parent


def main(argv: list[str] | None = None) -> int:
    """Print the project memory status and return a process exit code."""
    args = list(sys.argv[1:] if argv is None else argv)
    root = Path(args[0]) if args else _repo_root()

    print(f"AI Factory memory check: {root}")
    statuses = check_memory_files(root)
    for status in statuses:
        mark = "OK " if status.ok else "MISSING"
        print(f"  [{mark}] {status.name} ({status.size} bytes)")

    tasks_path = root / "TASKS.md"
    if tasks_path.is_file():
        summary = summarize(parse_task_board(tasks_path.read_text(encoding="utf-8")))
        print(
            "Task board: {done}/{total} done "
            "({todo} remaining, {ratio:.0%} complete)".format(**summary)
        )

    return 0 if all(status.ok for status in statuses) else 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
