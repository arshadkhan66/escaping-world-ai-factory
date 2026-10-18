# escaping-world-ai-factory
Zero-budget hybrid AI software factory with persistent project memory, automated coding, and testing.

## Project memory
- `PROJECT_SPEC.md` — mission, goals, constraints.
- `ARCHITECTURE.md` — planned system design.
- `TASKS.md` — task board and status.
- `DECISIONS.md` — recorded decisions.
- `HANDOFF.md` — current progress and next actions.
- `TEST_REPORT.md` — commands run and observed results.

## Python foundation
The `ai_factory` package uses only the Python standard library.

```bash
# Run the unit tests
python -m unittest discover -s tests -v

# Print the project memory status
python -m ai_factory
```

No paid APIs, billing, secrets, or third-party packages are required.
Tests also run automatically via GitHub Actions (`.github/workflows/tests.yml`).
