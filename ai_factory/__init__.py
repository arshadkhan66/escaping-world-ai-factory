"""Minimal, standard-library-only foundation for the Escaping World AI Factory.

The package provides small, testable helpers that inspect the project's own
memory files. It deliberately avoids third-party dependencies and network
access so it can run anywhere for free.
"""

from .memory import REQUIRED_MEMORY_FILES, MemoryFileStatus, check_memory_files
from .task_board import Task, parse_task_board, summarize

__all__ = [
    "REQUIRED_MEMORY_FILES",
    "MemoryFileStatus",
    "Task",
    "check_memory_files",
    "parse_task_board",
    "summarize",
]

__version__ = "0.1.0"
