"""Verify that the project's persistent memory files are present.

The AI Factory keeps its plans and progress in Markdown files at the repository
root. This module gives the test suite a single, standard-library-only way to
confirm those files exist and are non-empty.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

# The memory files described in ARCHITECTURE.md.
REQUIRED_MEMORY_FILES: tuple[str, ...] = (
    "PROJECT_SPEC.md",
    "ARCHITECTURE.md",
    "TASKS.md",
    "DECISIONS.md",
    "HANDOFF.md",
    "TEST_REPORT.md",
)


@dataclass(frozen=True)
class MemoryFileStatus:
    """Existence and size of one memory file."""

    name: str
    exists: bool
    size: int

    @property
    def ok(self) -> bool:
        """True when the file exists and contains at least one non-space byte."""
        return self.exists and self.size > 0


def check_memory_files(root: str | Path) -> list[MemoryFileStatus]:
    """Return a status entry for each required memory file under ``root``."""
    base = Path(root)
    statuses: list[MemoryFileStatus] = []
    for name in REQUIRED_MEMORY_FILES:
        path = base / name
        if path.is_file():
            statuses.append(
                MemoryFileStatus(name=name, exists=True, size=path.stat().st_size)
            )
        else:
            statuses.append(MemoryFileStatus(name=name, exists=False, size=0))
    return statuses
