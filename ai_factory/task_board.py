"""Parse the project task board stored in ``TASKS.md``.

The task board uses GitHub-flavored Markdown checkboxes:

    ## Milestone 1: Repository foundation
    - [x] Add PROJECT_SPEC.md.
    - [ ] Add DECISIONS.md.

Only the standard library is used so the parser runs anywhere for free.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

# Matches a Markdown checkbox line, capturing the state and the task text.
_CHECKBOX_RE = re.compile(r"^\s*[-*]\s+\[(?P<mark>[ xX])\]\s+(?P<text>.+?)\s*$")
# Matches an "## Heading" section line.
_SECTION_RE = re.compile(r"^\s*#{1,6}\s+(?P<title>.+?)\s*$")


@dataclass(frozen=True)
class Task:
    """A single task parsed from the board."""

    text: str
    done: bool
    section: str = ""


def parse_task_board(markdown: str) -> list[Task]:
    """Return every checkbox task found in ``markdown``, in file order.

    Tasks inherit the most recent heading as their ``section``. Checkbox lines
    that appear before any heading get an empty section.
    """
    tasks: list[Task] = []
    section = ""
    for line in markdown.splitlines():
        section_match = _SECTION_RE.match(line)
        if section_match:
            section = section_match.group("title")
            continue
        checkbox_match = _CHECKBOX_RE.match(line)
        if checkbox_match:
            mark = checkbox_match.group("mark").lower()
            tasks.append(
                Task(
                    text=checkbox_match.group("text"),
                    done=mark == "x",
                    section=section,
                )
            )
    return tasks


def tasks_in_section(tasks: list[Task], section: str) -> list[Task]:
    """Return the tasks whose ``section`` matches ``section``.

    Matching ignores surrounding whitespace and letter case. An unknown section
    returns an empty list rather than raising, which keeps callers simple.
    """
    wanted = section.strip().casefold()
    return [task for task in tasks if task.section.strip().casefold() == wanted]


def summarize(tasks: list[Task]) -> dict[str, object]:
    """Return counts and completion ratio for ``tasks``.

    The ratio is ``done / total`` and is ``0.0`` when there are no tasks, which
    keeps callers free of division-by-zero handling.
    """
    total = len(tasks)
    done = sum(1 for task in tasks if task.done)
    return {
        "total": total,
        "done": done,
        "todo": total - done,
        "ratio": (done / total) if total else 0.0,
    }
