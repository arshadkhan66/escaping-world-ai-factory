"""Smoke tests: the package imports and the status CLI runs end to end.

These confirm the foundation is wired together, independent of the detailed
unit tests in the other modules.
"""

import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import ai_factory
from ai_factory.__main__ import main


class SmokeTests(unittest.TestCase):
    def test_package_exposes_version(self):
        self.assertEqual("0.1.0", ai_factory.__version__)

    def test_public_api_is_importable(self):
        for name in ai_factory.__all__:
            self.assertTrue(hasattr(ai_factory, name), name)

    def test_cli_reports_ok_on_real_repository(self):
        root = Path(__file__).resolve().parent.parent
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            exit_code = main([str(root)])
        output = buffer.getvalue()
        self.assertEqual(0, exit_code)
        self.assertIn("AI Factory memory check", output)
        self.assertNotIn("MISSING", output)

    def test_cli_returns_failure_for_empty_directory(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            buffer = io.StringIO()
            with redirect_stdout(buffer):
                exit_code = main([tmp])
            self.assertEqual(1, exit_code)
            self.assertIn("MISSING", buffer.getvalue())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
