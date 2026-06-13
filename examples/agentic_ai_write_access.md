# Worked Example: Agentic AI With Write Access

## Scenario

An AI agent can take actions in a software environment: edit files, open pull requests, execute commands, update records, send messages, or trigger workflow changes.

The system has logs and human supervision.

## 1. Selection

The system selects and executes an action, not merely a recommendation.

Examples:

- edits code;
- deletes or rewrites files;
- changes configuration;
- opens a pull request;
- updates a customer record;
- sends a message;
- triggers a deployment workflow.

## 2. Affected person or system

Affected parties may include:

- users of the software;
- maintainers;
- customers;
- people represented in records;
- downstream systems relying on the changed state;
- the organisation legally responsible for the action.

## 3. Hardening point

Hardening may occur when:

- a change is merged;
- a deployment goes live;
- a record is copied downstream;
- a notification is sent;
- an external system acts on the changed data;
- logs are incomplete or overwritten;
- a rollback no longer restores the affected person's state.

## 4. Correction carrier

Possible carriers:

- sandboxing;
- permission limits;
- staged commits;
- human approval before merge or deployment;
- reversible transactions;
- tamper-evident logs;
- automated diff checks;
- affected-person notice;
- rollback path;
- kill switch;
- independent audit trail.

A log is not enough. A warning is not enough. A human reviewer is not enough if the action can harden before review.

## 5. Timing fit

The system is safer when write access is staged so correction can act before the world-effect boundary.

Examples of stronger timing fit:

- agent drafts but cannot merge;
- agent opens pull request but cannot deploy;
- agent modifies temporary state but cannot overwrite source records;
- agent action is reversible until human or rule-based release;
- downstream propagation waits for approval.

Examples of weak timing fit:

- agent can directly alter production;
- rollback is manual and slow;
- logs show only final action, not reasoning or input state;
- human sees the action after propagation;
- affected person cannot challenge before external effects.

## 6. Classification

Likely result where agent has direct write access and post-hoc logs only:

**FALSE SAFEGUARD or AFTER-THE-FACT REVIEW**

Likely result where write access is staged with approval before propagation:

**PARTIAL or LIVE PROTECTION**, depending on authority, timing, and reversibility.

## 7. Minimum repair

A stronger route would include:

- least-privilege access;
- world-effect boundary clearly marked;
- reversible staging area;
- human or independent release gate before irreversible action;
- record of input state, selected action, reason, authority, and rollback status;
- automated stop conditions;
- tested rollback before deployment;
- affected-party route where records about people are changed.

## One-sentence result

An agentic AI safeguard is not real because the system logs what it did; it is real only if the action cannot harden before review, rollback, or refusal can still change the outcome.
