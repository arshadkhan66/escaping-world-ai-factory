"""Unit tests for :mod:`ai_factory.task_board`."""

import unittest

from ai_factory.task_board import (
    Task,
    parse_task_board,
    summarize,
    tasks_in_section,
)


class ParseTaskBoardTests(unittest.TestCase):
    def test_parses_done_and_todo_tasks(self):
        markdown = (
            "# Board\n"
            "## Milestone 1\n"
            "- [x] Finished task.\n"
            "- [ ] Pending task.\n"
        )
        tasks = parse_task_board(markdown)
        self.assertEqual(2, len(tasks))
        self.assertEqual("Finished task.", tasks[0].text)
        self.assertTrue(tasks[0].done)
        self.assertFalse(tasks[1].done)

    def test_uppercase_x_counts_as_done(self):
        tasks = parse_task_board("- [X] Shouty checkbox.\n")
        self.assertEqual(1, len(tasks))
        self.assertTrue(tasks[0].done)

    def test_task_inherits_most_recent_section(self):
        markdown = (
            "## First\n"
            "- [ ] A.\n"
            "## Second\n"
            "- [ ] B.\n"
        )
        tasks = parse_task_board(markdown)
        self.assertEqual(["First", "Second"], [task.section for task in tasks])

    def test_task_before_any_heading_has_empty_section(self):
        tasks = parse_task_board("- [ ] Orphan.\n")
        self.assertEqual("", tasks[0].section)

    def test_ignores_non_checkbox_lines(self):
        markdown = (
            "Task statuses: DONE = completed.\n"
            "Plain text with [x] inside it.\n"
            "* [ ] Real task.\n"
            "1. [ ] Not a supported bullet.\n"
        )
        tasks = parse_task_board(markdown)
        self.assertEqual(1, len(tasks))
        self.assertEqual("Real task.", tasks[0].text)

    def test_empty_input_returns_no_tasks(self):
        self.assertEqual([], parse_task_board(""))

    def test_task_is_immutable(self):
        task = Task(text="x", done=False)
        with self.assertRaises(Exception):
            task.text = "changed"  # type: ignore[misc]


class SummarizeTests(unittest.TestCase):
    def test_counts_and_ratio(self):
        tasks = [Task("a", True), Task("b", False), Task("c", True)]
        summary = summarize(tasks)
        self.assertEqual(
            {"total": 3, "done": 2, "todo": 1, "ratio": 2 / 3}, summary
        )

    def test_empty_list_does_not_divide_by_zero(self):
        summary = summarize([])
        self.assertEqual({"total": 0, "done": 0, "todo": 0, "ratio": 0.0}, summary)


class TasksInSectionTests(unittest.TestCase):
    def test_returns_only_matching_section(self):
        board = (
            "# Board\n\n"
            "## Alpha\n"
            "- [x] a1\n"
            "- [ ] a2\n\n"
            "## Beta\n"
            "- [ ] b1\n"
        )
        tasks = tasks_in_section(parse_task_board(board), "Alpha")
        self.assertEqual(["a1", "a2"], [t.text for t in tasks])

    def test_section_name_is_case_insensitive(self):
        board = "## Alpha\n- [ ] a1\n"
        tasks = tasks_in_section(parse_task_board(board), "alpha")
        self.assertEqual(1, len(tasks))

    def test_unknown_section_returns_empty_list(self):
        board = "## Alpha\n- [ ] a1\n"
        self.assertEqual([], tasks_in_section(parse_task_board(board), "Missing"))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
