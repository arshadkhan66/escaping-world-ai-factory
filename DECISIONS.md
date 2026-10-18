# Architecture and Project Decisions

## Decision 1: Zero-budget operation
Status: Accepted
Reason: The project must be usable without purchasing credits or subscribing to paid services.
Consequence: Verify pricing, free-tier limits, and billing conditions before using external AI services.

## Decision 2: GitHub as the persistent source of truth
Status: Accepted
Reason: Version-controlled files preserve project instructions and progress across sessions.
Consequence: Keep plans, decisions, handoffs, and test reports in the repository.

## Decision 3: Small, verifiable changes
Status: Accepted
Reason: Small changes are easier to inspect, test, and recover on a phone.
Consequence: Review changes and record actual test outcomes.

## Decision 4: Android-first workflow
Status: Accepted
Reason: The primary device is an Android phone.
Consequence: Prefer browser-accessible tools and avoid assuming desktop software is available.

## Decision 5: Local model is an experiment, not an assumption
Status: Pending validation
Reason: Hardware and runtime limits may affect which models can run well.
Consequence: Measure compatibility, memory use, speed, and practical quality before relying on a local model.

## Decision 6: No unverified claims
Status: Accepted
Reason: Reliable progress requires evidence.
Consequence: Never claim a test passed, a connection works, or a feature is available without verification.
