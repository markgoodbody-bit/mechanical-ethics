# Part 4 — Harm, Time, and Future-Space

Status: first draft. Incomplete. Not canon.

## 4.1 Future-Space

A life is not only what is happening now.

A system is not only its current state.

A person standing at a door has more than a location. They have reachable paths. They have information about those paths. They have some ability, however limited, to move through them. A patient waiting for treatment, a worker facing an algorithmic score, an animal population in a changing habitat, a child in a school record, a future person inheriting a damaged world — each exists partly through the future still available to them.

Mechanical Ethics uses the term future-space for this field of possible continuation.

The canonical TRACE representation remains TRACE-owned:

```trace
F_x(t) := (O_x(t), R_x(t), I_x(t))
```

In this book, the human explanation is simple:

```trace
future_space :=
  options
  + reachability
  + usable_information
```

Options are not enough. A door that exists but cannot be reached is not meaningfully open. Reachability is not enough. A route that can be reached but not understood may still be unusable. Information is not enough. Knowing about a path does not mean having the power, time, health, money, safety, or permission to take it.

Future-space is why harm cannot be reduced to pain.

Pain matters. Fear matters. Hunger matters. Humiliation matters. But a person can be harmed without immediate pain if their future is narrowed. A person can be harmed by a record they do not see, a delay they cannot contest, a lost opportunity, a false classification, a route that exists only on paper, or a correction that arrives after the window has closed.

This is also why benefit cannot be reduced to pleasure.

A system may benefit a scope by expanding options, increasing practical reachability, or improving usable information. But even expansion needs caution. One scope's expansion may be bought by another scope's contraction. Mechanical Ethics must not hide that exchange.

## 4.2 Options, Reachability, and Information

The three parts of future-space separate mistakes that are often confused.

Options answer: what paths exist?

Reachability answers: which paths can this scope actually use?

Information answers: does this scope know enough to navigate?

```trace
O := option_topology
R := practical_reachability
I := usable_navigational_information
```

A welfare appeal may exist as an option. If the person cannot understand the letter, access advice, survive the waiting period, or gather the demanded evidence, reachability is low.

A medical treatment may exist as an option. If the patient is not told in time, usable information is low.

A job may technically remain open. If a false record blocks the application route, reachability is narrowed.

A democratic right may exist in law. If exercising it carries intimidation, cost, exclusion, or procedural impossibility, the option is not practically reachable in the same way.

The separation matters because repair must touch the right layer.

If options were removed, restore options.

If reachability was narrowed, restore reachability.

If information was hidden, restore usable information.

A system that gives someone a leaflet when the problem is cost has not repaired reachability. A system that gives someone a right when the problem is delay has not repaired timing. A system that corrects a record after the opportunity is gone has not returned the lost opportunity.

## 4.3 Harm as Narrowing

Harm is a narrowing of future-space.

That does not mean all harm can be measured cleanly. It does not mean pain is irrelevant. It does not mean every narrowing is unjustified. It means that when action closes options, reduces reachability, destroys usable information, or forces another scope into a smaller future, Mechanical Ethics has something to inspect.

```trace
harm_signal :=
  O_narrowed
  | R_narrowed
  | I_narrowed
  | mixed_contraction
```

A harm may be direct: injury, confinement, deprivation, exclusion.

A harm may be procedural: a route that cannot be used, a review that cannot arrive in time, a burden shifted to someone already exposed.

A harm may be informational: a person is not told, a record is hidden, evidence is destroyed, uncertainty is misrepresented as certainty.

A harm may be temporal: correction arrives after hardening, opportunity expires, delay consumes the future it claims to protect.

A harm may be relational: trust is damaged, recognition is denied, contradiction is erased, a person is made illegible to the system that controls them.

Mechanical Ethics should not pretend all these harms are the same. But it can ask the same first question:

```trace
harm_question :=
  whose_future_space_narrowed
  + how
  + how_fast
  + by_whose_action_or_inaction
  + can_repair_arrive_in_time
  + what_residue_remains
```

The point is not to inflate every inconvenience into catastrophe. The point is to stop serious narrowing from hiding inside ordinary administrative, technical, or institutional language.

## 4.4 Benefit as Expansion

Benefit is also real.

Mechanical Ethics is not a book only about injury. Systems act because they seek, preserve, build, repair, coordinate, feed, protect, learn, and improve. A good intervention can expand future-space. A warning can improve information. A bridge can increase reachability. A medicine can restore options. A school can open paths. A law can slow arbitrary power. A model can identify a risk early enough to prevent loss.

```trace
benefit_signal :=
  O_expanded
  | R_expanded
  | I_expanded
  | mixed_expansion
```

The question is not whether expansion is good. Often it is.

The question is whether expansion is being used to hide contraction elsewhere.

A city may expand mobility for many while displacing a few. A safety system may reduce general risk while concentrating burden on those least able to contest. A platform may create opportunity while extracting attention, data, and stability. A cull may protect crops and ecosystems while killing adaptive animals. A medical triage rule may save more lives while leaving a residue that must not be described as clean.

Benefit must be recorded. So must cost.

Mechanical Ethics should resist two opposite lies.

The first lie says: because there is harm, there can be no benefit.

The second says: because there is benefit, the harm has disappeared.

Neither is good enough.

## 4.5 Loss Clocks

Timing changes harm.

Some losses remain repairable for a while. Some harden quickly. Some harden before anyone outside the affected scope notices. Some never fully harden but become more expensive, less reachable, or more damaging with each delay.

A loss clock asks whether correction can arrive before the loss becomes irreversible or practically unrecoverable.

In simplified form:

```trace
loss_clock_question :=
  can_detection_routing_and_correction_arrive_before_hardening?
```

The exact TRACE clock representation belongs to the operator schema. The human point is this: a right that can be exercised only after the damage has hardened is not the same right in practice.

A review after eviction is not the same as a review before eviction.

A correction after a medical window closes is not the same as a correction before treatment becomes impossible.

A record fix after a job, visa, benefit, or school place is lost is not the same as a correction before the decision is made.

A human apology after evidence has disappeared is not the same as preserving the contradiction when it could still be tested.

The actor who controls or benefits from a harmful path is not a neutral judge of the clock. If the system says, "there is time," Mechanical Ethics asks: time for whom, measured by whom, and before what hardening?

This will later become a gate: do not let the assessed actor set every clock.

## 4.6 Opportunity Clocks

Loss is not the only timed structure.

Opportunity also expires.

A person may need access before a deadline. A child may need support before a developmental window closes. A patient may need diagnosis before treatment loses effect. A worker may need correction before a hiring cycle ends. A community may need warning before displacement becomes unavoidable. A future generation may need restraint before damage becomes inheritance.

```trace
opportunity_clock_question :=
  can_access_uptake_and_integration_arrive_before_expiry?
```

An opportunity is not real for a scope merely because it exists somewhere in the world. It must be reachable and usable in time.

This matters because institutions often count opportunity at the wrong level. They say a route exists, a form exists, a grant exists, a review exists, a mitigation exists, a consultation exists. But the affected scope may not be able to access, understand, use, or integrate it before the window closes.

Mechanical Ethics treats expired opportunity as a serious form of residue.

If correction comes after the door has closed, the record should not say only "corrected." It should say what opportunity was lost, whether it can be replaced, and who bears the remaining duty.

## 4.7 Correction That Arrives Too Late

Correction is not magic.

A system can admit error and still fail to repair. It can reverse a decision and still leave the person worse off. It can compensate and still not return time. It can apologise and still preserve the machinery that caused the harm. It can create a review route that arrives after the path is already hardened.

```trace
late_correction :=
  correction_exists
  + correction_after_hardening
```

Late correction matters because it often allows systems to look fair from the inside.

The file was reviewed. The appeal was heard. The decision was corrected. The payment was made. The apology was issued. The case was closed.

But the life did not rewind.

Mechanical Ethics insists on the difference between correction and repair. Correction changes the official state. Repair changes the harmed path as far as possible. Residue records what remains after both.

A correction route can also become a harm carrier. If it consumes the time, energy, evidence, money, credibility, or health of the affected scope faster than it repairs the path, then the correction mechanism is part of the harm structure.

This is why the later gate is earned: do not let correction channels become harm carriers.

## 4.8 Opportunity That Arrives Too Late

Opportunity can arrive as theatre.

A consultation after the decision. A support offer after exclusion. A chance to appeal after the deadline matters. A mitigation after the damage becomes permanent. A warning after the cost has already been routed. A right that becomes visible only after it can no longer be used.

```trace
late_opportunity :=
  opportunity_exists
  + opportunity_after_expiry
```

This is not always malicious. Systems are slow. People are overloaded. Evidence emerges late. Institutions have queues. The world is messy.

But Mechanical Ethics does not ask only whether the lateness was understandable. It asks who carried the cost of that lateness and whether the system is allowed to call the matter clean afterward.

When opportunity arrives too late, the remaining duty may be disclosure, compensation, restoration where possible, changed machinery, preserved contradiction, or explicit residue.

The chapter ends with a simple rule of attention:

```trace
time_rule :=
  do_not_count_a_route_as_real
  unless_it_can_arrive_while_it_still_matters
```

Part 4 gives the book its main pressure: action changes future-space, and time decides whether correction and opportunity are real or ceremonial.

The next part keeps the human firewall clear.

Seeing this structure does not authorize action.

Description is not permission.
