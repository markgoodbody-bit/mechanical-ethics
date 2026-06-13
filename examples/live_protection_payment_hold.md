# Worked Example: Payment Hold With Live Challenge

This stylised example shows a clear **LIVE PROTECTION** result.

## Scenario

A payment platform flags a high-value payment as suspicious.

Instead of cancelling the payment, freezing the account, or reporting the user downstream immediately, the system places the payment in a reversible pending state for up to 24 hours.

The affected user receives notice, can trigger urgent review, can submit evidence, and the reviewer has authority to release the payment before the user's deadline.

## 1. Decision

The system flags a payment for suspicion review.

The decision does not complete the harmful action. It creates a reversible pending state.

## 2. Affected person

The payer and payee carry the consequence.

Possible effects:

- payment delay;
- missed invoice or rent deadline;
- account uncertainty;
- business interruption.

## 3. Too-late point

The consequence becomes hard to reverse when the payment deadline passes or when the payee acts on non-payment.

In this scenario, the relevant deadline is 48 hours away.

## 4. Actual fix mechanism

The safeguard has actual fix mechanisms:

- immediate notice to the user;
- clear reason category;
- urgent challenge route;
- evidence upload;
- pending state rather than cancellation;
- reviewer with release authority;
- 12-hour review deadline;
- automatic escalation if the deadline is missed;
- record of the decision and outcome.

## 5. Timing fit

The fix can act before the too-late point.

The review deadline is 12 hours. The payment deadline is 48 hours.

The reviewer can release the payment, request more evidence, or maintain the hold with reasons.

## Working result label

**LIVE PROTECTION**

## Why this is live protection

The system does not let the suspicious-payment decision become irreversible before challenge.

The affected person receives notice, can trigger review, can provide evidence, and the reviewer has authority to release the payment inside the relevant window.

## Remaining limits

This result does not prove the payment platform is fair or safe overall.

It does not prove the suspicion model is accurate.

It does not prove the hold cannot cause hardship.

It only shows that this safeguard appears to provide live correction for this payment path.

## Minimum records needed

- decision timestamp;
- notice timestamp;
- challenge timestamp;
- evidence received;
- reviewer identity or role;
- decision time;
- release/hold outcome;
- missed-deadline escalation record;
- whether the payment deadline was met.

## One-sentence result

This safeguard appears to be live protection because the system holds the action in a reversible pending state, gives the affected user a challenge route, and gives a reviewer authority to release the payment before the deadline becomes hard to reverse.
