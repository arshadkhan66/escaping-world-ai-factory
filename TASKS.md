# AI Factory Task Board

Task statuses: DONE = completed and verified; TODO = not yet completed.

## Milestone 1: Repository foundation
- [x] Create the private GitHub repository.
- [x] Add PROJECT_SPEC.md.
- [x] Add HANDOFF.md.
- [x] Add ARCHITECTURE.md.
- [x] Add TASKS.md and verify it appears in the repository.
- [x] Add DECISIONS.md.
- [x] Add TEST_REPORT.md.

## Milestone 2: Testing
- [x] Create a minimal Python smoke-test module.
- [x] Create a standard-library unit test.
- [x] Run the test and record the actual result.
- [x] Fix any failures and rerun the test. (No failures occurred; tests were
  rerun after the suite grew to confirm they still pass.)

## Milestone 3: Automated checks
- [x] Add a GitHub Actions workflow for Python tests.
- [ ] Check workflow permissions and applicable free usage limits.
  (Workflow sets `permissions: contents: read`; free usage limits are not yet
  confirmed.)
- [ ] Trigger the workflow and inspect its actual result.

## Milestone 4: AI coding agent
- [ ] Verify that OpenHands can access this repository.
- [ ] Verify model pricing and billing conditions before running any agent.
- [ ] Confirm the agent can inspect and safely modify a small task.
- [ ] Review its changes and test results.

## Milestone 5: Hybrid operation
- [ ] Document a reliable session-resume process.
- [ ] Evaluate Android-compatible local-model options.
- [ ] Measure real memory use and performance before selecting a local model.
- [ ] Document free-tier limits and quota-recovery procedures.

## Operating rules
- Keep spending at zero unless the owner explicitly approves otherwise.
- Never commit secrets or credentials.
- Work on one small task at a time.
- Mark a task DONE only after its completion is verified.
- Update HANDOFF.md after meaningful progress.
- Never invent test results or claim unverified capabilities.
