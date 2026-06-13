# Design Patterns for Live Correction

The Correction Window Test is diagnostic. It identifies whether protection can act in time.

This guide translates common failures into design patterns.

## Pattern 1: Notice before hardening

Affected people should know that a consequential selection has occurred before the opportunity to challenge it becomes useless.

Weak version:

- notice buried in policy wording;
- generic notice that automation may be used;
- notice after the consequence has already hardened.

Stronger version:

- specific notice of the consequential selection;
- plain explanation of what changed;
- clear route to challenge;
- enough time for challenge to matter.

## Pattern 2: Pause during credible challenge

Where a consequence may harden quickly, a credible challenge should pause the pathway unless there is a stronger countervailing risk.

Weak version:

- appeal exists but action continues;
- enforcement continues during dispute;
- decision is reviewed after the deadline passes.

Stronger version:

- pause or safe interim state;
- triage for urgent harm;
- deadline for the corrector;
- record of whether pause was granted.

## Pattern 3: Corrector deadline

A system often gives affected people deadlines but gives the corrector no matching deadline.

Weak version:

- affected person must respond in 14 days;
- authority may take months;
- no consequence for late correction.

Stronger version:

- correction authority has a deadline inside the hardening window;
- late correction triggers escalation;
- pending state is visible;
- unresolved cases are not silently normalised.

## Pattern 4: Independent evidence access

The person challenging a system needs access to the evidence that shaped the selection.

Weak version:

- decision notice without reasons;
- model output without inputs;
- internal evidence inaccessible;
- audit logs visible only to the operator.

Stronger version:

- input record;
- output record;
- reason or basis;
- timestamp;
- downstream recipients;
- human override record;
- repair outcome.

## Pattern 5: Reversible staging

AI or institutional action should remain reversible until correction can act where stakes are high.

Weak version:

- direct production action;
- irreversible record write;
- downstream propagation before review;
- rollback not tested.

Stronger version:

- draft state;
- queue state;
- pending state;
- approval gate;
- rollback route;
- no downstream propagation before release.

## Pattern 6: Affected-person trigger

A safeguard is weaker if only the operator can trigger it.

Weak version:

- internal review only;
- discretionary escalation;
- regulator only after exhaustion;
- affected person cannot see the route.

Stronger version:

- affected person can trigger review;
- proxy can trigger review where needed;
- route is visible;
- trigger is protected from retaliation;
- trigger produces a tracked pending state.

## Pattern 7: External escalation

Operator-controlled safeguards may fail under pressure.

Weak version:

- same actor makes decision, controls evidence, reviews appeal, and declares closure.

Stronger version:

- independent reviewer;
- regulator;
- tribunal;
- ombudsman;
- public audit route;
- transparent closure record.

## Pattern 8: False-negative review

Many systems review visible people who were flagged, blocked, selected, or rejected.

They may miss people wrongly ignored, deprioritised, not escalated, or excluded.

Stronger version:

- sample negative cases;
- review near misses;
- check missed escalation;
- measure who never reaches the route;
- inspect downstream silence, not only visible complaints.

## Pattern 9: Downstream propagation control

A correction route is weak if the original error has already spread.

Weak version:

- score copied into other systems;
- label shared across agencies;
- record used for future decisions;
- correction does not reach downstream holders.

Stronger version:

- propagation map;
- correction broadcast;
- downstream deletion or amendment;
- proof of update;
- recurrence prevention.

## Pattern 10: Scar ledger

Some harm cannot be undone even after correction.

A system should record what could not be restored.

Stronger version:

- original loss recorded;
- delay recorded;
- compensation considered;
- recurrence control assigned;
- affected-person record corrected;
- public or audit-visible learning where appropriate.

## Design rule

Do not describe a safeguard by what it is called.

Describe it by what it can still do before hardening.
