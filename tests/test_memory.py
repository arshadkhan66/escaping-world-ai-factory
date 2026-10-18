"""Unit tests for :mod:`ai_factory.memory`."""

import tempfile
import unittest
from pathlib import Path

from ai_factory.memory import (
    REQUIRED_MEMORY_FILES,
    check_memory_files,
)


class CheckMemoryFilesTests(unittest.TestCase):
    def test_reports_missing_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            statuses = check_memory_files(tmp)
            self.assertEqual(len(REQUIRED_MEMORY_FILES), len(statuses))
            self.assertTrue(all(not status.exists for status in statuses))
            self.assertTrue(all(not status.ok for status in statuses))

    def test_reports_present_and_non_empty_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            for name in REQUIRED_MEMORY_FILES:
                (Path(tmp) / name).write_text("content", encoding="utf-8")
            statuses = check_memory_files(tmp)
            self.assertTrue(all(status.ok for status in statuses))
            self.assertTrue(all(status.size == len("content") for status in statuses))

    def test_empty_file_is_not_ok(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "PROJECT_SPEC.md").write_text("", encoding="utf-8")
            statuses = {s.name: s for s in check_memory_files(tmp)}
            self.assertTrue(statuses["PROJECT_SPEC.md"].exists)
            self.assertFalse(statuses["PROJECT_SPEC.md"].ok)

    def test_status_names_follow_required_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            names = [s.name for s in check_memory_files(tmp)]
            self.assertEqual(list(REQUIRED_MEMORY_FILES), names)

    def test_accepts_path_object(self):
        with tempfile.TemporaryDirectory() as tmp:
            statuses = check_memory_files(Path(tmp))
            self.assertEqual(len(REQUIRED_MEMORY_FILES), len(statuses))


class RealRepositoryTests(unittest.TestCase):
    """Checks the actual repository layout, not a temporary directory."""

    def setUp(self):
        self.root = Path(__file__).resolve().parent.parent

    def test_all_memory_files_exist_in_repository(self):
        statuses = check_memory_files(self.root)
        missing = [status.name for status in statuses if not status.ok]
        self.assertEqual([], missing, f"missing or empty memory files: {missing}")

    def test_package_and_workflow_exist(self):
        self.assertTrue((self.root / "ai_factory" / "__init__.py").is_file())
        self.assertTrue(
            (self.root / ".github" / "workflows" / "tests.yml").is_file()
        )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
