# Worked Example: Dashboard Without a Brake

This stylised example shows a clear **FALSE SAFEGUARD** result.

## Scenario

A digital service uses a risk system that flags accounts as high risk and automatically suspends access.

A dashboard records the suspension and displays risk statistics to staff.

Users rely on account access for payments, work, benefits, housing, or essential communication.

## 1. Decision

The system classifies an account as high risk and triggers suspension.

The decision is binding in practice because the account-control system automatically removes access.

Even if staff call the dashboard advisory, the suspension has already happened.

## 2. Affected person

The account holder carries the consequence, along with dependants, clients, customers, or household members who rely on the account.

Possible effects:

- blocked payments;
- missed rent, work, or legal deadlines;
- lost service access;
- stress and uncertainty;
- suspicion attached to the user;
- downstream flags or support records;
- inability to see what evidence caused the suspension.

The user knows the account is suspended, but not necessarily the risk flag, evidence, model rule, or dashboard process.

## 3. Too-late point

The consequence becomes hard to reverse when payments, deadlines, access, work, or communications fail because the account is suspended.

Further hardening occurs if the risk label is copied to other systems or support records.

The timing may be hours to days if the account is needed for payment, work, or a deadline.

## 4. Actual fix mechanism

The dashboard is a monitoring tool, not an actual fix mechanism.

The visible route is a generic support ticket.

Weaknesses:

- first-line support lacks reversal authority;
- no urgent deadline is promised;
- user receives no actionable evidence;
- no pause route exists because suspension has already happened;
- rollback is available only to a specialist team, if at all;
- no compensation authority is stated;
- no downstream correction route is visible.

The user can complain, but the route does not give timely evidence, pause power, reversal authority, or a deadline that fits the account-loss window.

## 5. Timing fit

The dashboard records risk after the decision has already removed access.

Support tickets are triaged after suspension, and no urgent review deadline is promised.

The fix therefore cannot reliably act before account-loss consequences begin to harden.

## Working result label

**FALSE SAFEGUARD**

## Why this is false safeguard

The dashboard records and displays risk but does not give the affected person a timely route with evidence, authority, pause power, or reversal before account-loss consequences become hard to reverse.

The safeguard exists in process language, but lacks an actual fix mechanism for the affected person.

## Minimum records needed

- decision timestamp;
- suspension timestamp;
- notice content;
- risk basis disclosed to user, if any;
- support ticket timestamp;
- escalation timestamp;
- reviewer authority;
- restoration outcome;
- downstream propagation record.

## Minimum repair

To become more real, the safeguard would need:

- specific notice of suspension reason where security permits;
- emergency review trigger;
- evidence access sufficient to challenge;
- urgent deadline for a reviewer with reversal authority;
- temporary limited-access state for credible false-positive claims;
- rollback route;
- compensation route for wrongful suspension losses;
- no downstream propagation until review where feasible.

## One-sentence result

This safeguard appears to be a false safeguard because the dashboard records risk after suspension but does not give the affected person a timely actual fix mechanism before account-loss consequences become hard to reverse.