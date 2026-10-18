# AI Factory Architecture

## Overview
Escaping World AI Factory is planned as a low-cost, hybrid software development workflow. GitHub stores the source code, documentation, task history, and test reports. AI coding agents may assist with implementation when their access and costs are verified.

## Components

### 1. GitHub repository
- Stores project files and version history.
- Provides a place to review and recover work.
- Hosts automated checks through GitHub Actions when configured.

### 2. Project memory
- PROJECT_SPEC.md: mission, goals, and constraints.
- ARCHITECTURE.md: system design and component responsibilities.
- TASKS.md: prioritized work and task status.
- DECISIONS.md: important choices and their reasons.
- HANDOFF.md: current progress and next action.
- TEST_REPORT.md: commands actually run and observed results.

### 3. AI coding agent
- Inspects the repository before changing files.
- Works on small, reviewable tasks.
- Runs available tests and reports failures honestly.
- Must not use paid services or credits without explicit approval.

### 4. Automated testing
- Begin with a minimal Python unit test.
- Use GitHub Actions to run tests after the workflow is configured.
- Record real test results; never assume a workflow passed.

### 5. Local-model fallback
- Investigate Android-compatible local inference only after checking model size, runtime compatibility, memory use, and performance.
- Treat local inference as a future option, not a capability already verified.

## Proposed workflow
1. Read project memory.
2. Select one task from TASKS.md.
3. Inspect the relevant files.
4. Make a small change.
5. Run the relevant tests when possible.
6. Review the diff and record the result.
7. Update HANDOFF.md with the next action.

## Constraints and open questions
- Keep spending at zero.
- Confirm AI model billing before running an agent.
- Verify repository permissions before delegating changes.
- Confirm applicable GitHub Actions free limits before relying on automation.
- Validate local-model feasibility on the actual Android device.

## Current implementation status
This document describes the intended architecture. It does not mean an AI agent, tests, automation, or local inference are already running.
