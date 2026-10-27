# Case 4. GitLab's 2017 database outage: what makes a recovery route usable?

*Historical technical case, 31 January–10 February 2017; source and editorial review updated 27 October 2026. An online casebook addition, **not part of the dated 26 October three-case PDF**. No user testimony, service testing or independent operator audit was conducted. Existing reliability/SRE methods are the first comparator, not competitors to dismiss.*

Historical operator reports are distinguished below from subsequent tracking statements and our engineering analysis. The key question is whether a stored copy can become **usable and reconcilable service** while retaining what the copy cannot restore.

## 1. The decision under examination

The central engineering decision is which recovery route to pursue after expected protection has failed. Selecting the newest available copy is an incomplete rule. A copy also has to be readable, transferable, usable by the restoration tools, and reconcilable with the application that will resume writing. Its destination must become operational before the route provides service. These requirements make recovery a problem of feasible transitions rather than a count of nominal safeguards.

The GitLab incident supplies a concrete instance. The operator's 10 February account describes accidental removal on the primary while repairing replication, unavailable expected recovery paths, and recovery using an older staging copy. Its account separates preservation of Git repositories from loss of database changes. [S1] The 1 February account is an earlier report from the same organisation, not independent corroboration. It describes interrupted service, incomplete recovery and measures taken while the incident was unfolding. [S2]

This analysis asks a narrower question than whether the organisation became reliable afterwards: what made one recovery route preferable and what did completing it leave unresolved? The evidence can support an attributed mechanism study without proving every operator diagnosis or the effectiveness of later reforms. There are no command logs, independently timed transfers, database images or affected-user interviews in this record set.

## 2. Evidence inventory and clock boundaries

The following inventory compresses the two operator reports. It describes reported availability during recovery, not a present-day assessment of GitLab's infrastructure. “Unavailable” means unavailable for the specified recovery purpose; it does not mean every component of that system failed.

| Candidate copy or route | Reported age, purpose and location | Prerequisite or obstruction | Recovery consequence |
|---|---|---|---|
| Primary and standby [S2] | Live production and failover | Standby cleared for rebuild; primary removed mistakenly | Neither supplied the needed restore |
| Scheduled logical dumps [S2] | Daily export to S3 | No usable recent dump; tool-version failure | Expected route unavailable |
| Cloud disk snapshots [S2] | Protection used elsewhere | Not enabled on database hosts | No database recovery route |
| Routine LVM copy [S1] | Almost a day old; staging refresh | Transfer and restoration | Larger data gap |
| Manual LVM copy [S1] | About six hours old; staging work | Staging storage limited transfer; webhooks needed reconciliation | Selected; sequence values also advanced |

Sources: [S1], recovery sections; [S2], incident and problems sections. The destructive command was reportedly stopped within seconds. [S2] That short intervention window contrasts with a much longer restoration route; it is not a measured response-time requirement. Missing changes after the selected recovery point remained outside what loading that copy could recover.

The operator's accounts contain different endpoints. They should remain visible rather than being averaged into an apparently precise chronology.

| Report passage | Endpoint actually stated | Meaning retained here |
|---|---|---|
| 1 February update | 17:20–23:25 UTC, 31 January | Early account's lost-change interval |
| 1 February update | 18:14 UTC, 1 February | Reported return online |
| 10 February introduction | 17:20–00:00 UTC | Later introduction's lost-change interval |
| 10 February impact section | 17:20–23:30 UTC | Later impact section's lost-change interval |
| 10 February recovery section | 17:00, then approximately 18:00 UTC, 1 February | Database restoration without webhooks, then final procedures |

Sources: [S2], opening update; [S1], introduction, impact and recovery sections. These are stated endpoints, not interchangeable measurements. The midnight wording is reproduced without repairing its calendar ambiguity. The early account also places stopping the destructive action at 23:27; that is a different event from a declared loss boundary. [S2]

An outage clock, a recovery-point clock and a user-work clock answer different questions. An availability interval measures when a specified service could be used. A restored-state timestamp describes the age of the selected state. A lost-change interval describes changes absent from that state. Subtracting one pair of endpoints does not establish the others. Exact timestamps would not remove this conceptual distinction.

## 3. A feasible-route model, without a fictional optimum

Consider the choice between the two LVM routes in the inventory. This is the actual decision the model clarifies. Define a candidate route as a source copy, a destination, the operations needed to restore it, and the reconciliation needed before that destination accepts ordinary work. The model compares routes, not storage products.

**Do not confuse three gates.** A route that might physically work, a route whose capability has been established well enough to rely on, and a route somebody may legitimately attempt are not the same set.

1. **Physical candidate feasibility:** the source copy is in fact readable, necessary tools and destination capacity can perform the transfer, and required application-state reconciliation can be achieved. A real route may be feasible before anyone has tested it. Conversely, confidence or permission cannot make a physically impossible route work.
2. **Evidential sufficiency for a particular decision:** which of those prerequisites was observed, reported, inferred, failed or untested? Which time and workload assumptions were actually checked? When the answer is unknown, retain UNKNOWN rather than placing the route inside or outside a known feasible set by decree.
3. **Authority and uncertainty acceptance:** who can authorise the attempt, what consequences could reach other users, what can be staged or reversed, and who is entitled to accept the residual risk? An authorised attempt is not proof it will succeed; a technically feasible route is not automatically authorised.

These are analytical distinctions, **not a claim that GitLab used this three-gate model**. The evidence from [S1] and [S2] supports an operator-reported preference among surviving copies; it does not show that all prerequisites were independently verified or that risk acceptance guaranteed physical feasibility. The smallest honest decision record names *the route*, *what is established about it*, and *what remains to be decided by an authorised actor*.

Compare feasible routes on three separate dimensions: expected missing work, expected time to a usable service, and uncertainty about successful completion. Do not combine them into an unexplained weighted score. A score would require an authorised valuation of delay against missing work, plus estimates that these sources do not supply. Keeping the dimensions separate reveals the tradeoff instead of concealing it in arithmetic.

| Comparison for this decision | More recent manual copy | Older routine copy |
|---|---|---|
| State age | Favours this route | Disfavours this route |
| Transfer and preparation duration | No defensible complete forecast obtained | No defensible complete forecast obtained |
| Successful restoration probability | No numerical estimate obtained | No numerical estimate obtained |
| Application reconciliation | Must be established | Must be established |
| Overall quantitative optimum | Not calculable from this evidence | Not calculable from this evidence |

The age comparison supports a reason to prefer the newer copy if both routes are otherwise workable. It does not prove that preference minimised total damage. A much slower or much less credible route could reverse the choice; the necessary comparison data are absent. No hypothetical reversal is being presented as something the operator overlooked.

The model's principal assumption is that each listed copy can be evaluated without destroying the other options. If evaluation consumes the only remaining source, the decision changes: information gathering itself can reduce recoverability. A prudent procedure would preserve the original where feasible and perform restoration against a separate target. Whether every historical operation satisfied that condition is unknown here.

A second assumption is that missing changes cannot simply be recovered through an unexamined source. If another journal, client cache or independent record were available, it could alter the feasible set. The model does not declare such a source nonexistent merely because the reviewed accounts do not establish it. Its conclusion is conditional: the newer surviving copy offers the smaller apparent state-age gap among the documented alternatives.

## 4. Location and purpose become recovery constraints

A backup's location is often treated as an inventory attribute. During recovery it becomes part of the execution path. Source read speed, intermediate storage, destination writes and preparation steps can dominate elapsed time even when the copy itself is sound. A nominally available object therefore does not imply promptly available service.

The later account reports approximately 18 hours copying, attributing the bottleneck to staging's network disks, limited to about 60 Mbps, rather than CPU or network capacity. [S1] These are operator-reported measurements and attribution. Multiplying the rate by elapsed time would not independently validate the diagnosis: the record does not supply the sustained-rate trace, transfer overhead or exact copied byte count required for that calculation.

This is not an argument for selecting an expensive storage tier without measurement. Before choosing a design, an engineer would need representative restoration measurements at the relevant database size and under the relevant throttling conditions. A small-file copy test might establish connectivity while missing the limiting behaviour of a large restore. Conversely, a slow observation during an incident does not identify the performance of every alternative architecture.

The same distinction applies to purpose. Development copies may be intentionally altered to prevent interactions with production. That modification can be correct for development and inconvenient for disaster recovery. The engineering question is which transformations separate the source from the required target, and whether those transformations can be reversed safely. Calling the copy “a backup” does not answer it.

The useful deliverable is a restoration dependency map: preserved source, required transformations, destination prerequisites and evidence for completion. Its advantage over an asset list is falsifiability. An asset list can remain accurate while every practical recovery route is blocked. A dependency map can be challenged at the specific step where the route stops working.

## 5. Restoration is also reconciliation

Starting a database establishes that a process can read some state. It does not establish that the application can safely resume all behaviours associated with that state. Restoration needs an explicit boundary between data loading, application validation and renewed external effects.

**The historical account reports two concrete reconciliation operations** rather than only theoretical risks. Because the staging-copy procedure removed webhooks to prevent accidental triggering during development, GitLab reports restoring webhook configuration from a separate database assembled from the retained snapshot; the main database was reportedly available without webhooks by around 17:00 UTC on 1 February, with final webhook procedures finished around 18:00 [S1]. The published recovery plan also calls for increasing database sequence values by 100,000 to avoid reusing identifiers that may have been exposed before the outage [S1]. This is a reported plan/intervention in the operator account, **not proof that all external actions or client references were reconciled**.

These actions expose two general recovery questions. First, a restored webhook configuration can refer to an event that already happened outside the database, an event that should still happen, or a call that must not be repeated. Those cases require different decisions. Neither [S1] nor [S2] supplies an independently verified ledger of external deliveries, so no actual duplicate effect is inferred here. Second, an older database may forget identifiers already exposed to clients or external systems. Increasing sequence values is one protective technique reported in this incident; it does not alone establish everything remembered by those external consumers.

The lesson is not that reconciliation was absent: **it was explicitly attempted and partially described**. The unresolved question is the evidence necessary to conclude that each relevant application and external effect was safe to resume.

A restoration acceptance procedure would consequently separate at least three questions: can the database serve the application, are relationships and identifiers safe for renewed writes, and can externally effective operations resume? An affirmative answer to the first should not silently answer the other two. This is an analytical acceptance structure; it is not a certification that the historical recovery was incomplete or unsafe.

There is also a distinction between reconstructing an object and reconstructing its history. A replacement project entry may restore access to surviving material without reproducing missing discussion, ordering, permissions or decisions. Even where some reconstruction is technically possible, its evidential status matters: a reconstructed entry should not acquire the authority of an original event merely because it occupies the same interface position.

These considerations do not justify withholding service indefinitely. They justify staged acceptance conditions. Read access, new writes and outbound effects may require different evidence. If staged restoration is chosen, the operator should state which capabilities are available and which remain constrained, so that users do not interpret one successful interaction as evidence of complete restoration.

## 6. Destructive repair and the shrinking option set

The destructive-operation window in the inventory is much shorter than the recovery interval. That asymmetry changes where safeguards are useful. A warning noticed after destructive execution can have limited protective value even if the operator reacts promptly. Safeguards placed before execution can act while the source still exists.

Host differentiation is one candidate safeguard, not a complete solution. A visible label helps only if it is noticed, understood and connected to the command's target. A stronger design might verify the target independently, restrict destructive operations, require a preserved recovery point or separate the relevant privileges. Each measure also has a failure mode and operational cost. This evidence does not compare their performance or authorise a universal two-person requirement.

The relevant failure class is a repair action that removes an option before the replacement is established. It appears in many domains, but that resemblance does not establish a shared causal model. Here it yields a concrete question: what remains recoverable after each step if the next step fails? A procedure that answers only how to complete the intended sequence omits its own interrupted states.

Diagnosis can also become consequential before an explicit deletion. Silence from a tool can mean waiting, blocking, failure or insufficient instrumentation. Treating those states as equivalent invites corrective actions against the wrong condition. The operational improvement is to distinguish them with evidence or a documented uncertainty boundary. It is not to assume every quiet process is healthy.

This analysis does not infer an individual's competence, motivation or emotional state. It identifies properties a repair procedure can expose to testing: target discrimination, visibility of progress, preservation of alternatives and behaviour after interruption. Responsibility for these properties is broader than responsibility for pressing a particular key.

## 7. What changed afterwards: bounded evidence

The original restore-testing issue proposes recovering a recent backup, examining meaningful application tables, and reporting failures through another channel. It also proposes using the same underlying tooling as manual recovery. [S3] The separate durability-owner issue proposes explicit responsibility and authority to interrupt work when durability is endangered. [S4] These descriptions establish proposals, not demonstrated outcomes.

Additional reading changes the scout's evidential ceiling. Tracking issue 1684 reports several completed measures and describes transitions between proposed solutions. It also distinguishes streaming-backup implementation from missing monitoring and carries unfinished restore-related work forward. [S5] Streaming issue 1152 has checked items for backup use, configuration tooling and documentation; its rationale couples backup restoration to development use. [S6] Issue 1265's retrieved description retains unchecked host-creation, configuration and restoration tasks. [S7] The hourly-snapshot issue states a proposed frequency and retention change. [S8]

The earned result is therefore narrower than “all improvements unknown” but weaker than “recovery proved reliable.” There is public operator-maintained evidence reporting some implementation. There is no retrieved execution history or independent test record establishing end-to-end recovery capability, and the visible descriptions do not provide a reliable completion chronology. A checked box can identify a claim to investigate; it cannot substitute for the result of a restore under specified conditions.

Coupling restoration to development has a plausible mechanism: recurring useful work creates opportunities to discover broken tools and incompatibilities before an emergency. It also has a possible blind spot. A development restore may omit production traffic, effect handling, privilege boundaries or the destination constraints that matter in an actual incident. Routine reuse improves the relevance of a test only to the extent that the exercised path overlaps the required recovery path.

An owner can likewise improve escalation without controlling every dependency. The necessary evidence would connect responsibility to an observed ability to stop, repair or resource the failing route. Merely naming an owner would not establish that ability. Neither limitation makes the proposals worthless; both specify what would distinguish a paper control from a working one.

## 8. Reliability objectives and the remaining consequences

Ordinary database reliability supplies the strongest comparator. A recovery point objective specifies a target for acceptable data loss or recovery-point age. A recovery time objective specifies a target duration for restoring a defined service. These are objectives, not descriptions of whatever happened. The reviewed material does not establish the adopted objectives needed to judge compliance quantitatively.

Even an objective met exactly would leave questions about distribution. A bounded interval of missing state can contain very different amounts of work for different users. Duration is not a measure of effort, replaceability or consequence. Those differences do not require an invented harm score; they require evidence about affected activities before making claims about them.

Service restoration is a real result and should not be rhetorically erased. It makes further work possible. At the same time, restored access does not imply recovered discussion, repeated effort or reversed downstream decisions. This draft has no user-level evidence with which to estimate those consequences, and makes no allegation about particular users' subsequent outcomes.

Mechanical Ethics can direct attention to that separation, but database reliability, human factors and incident management already support much of the analysis. Nothing here demonstrates theoretical novelty or an advantage from applying ME. The case's contribution is a specific, inspectable recovery decision and its residual uncertainties, not a claim that familiar engineering has been newly explained.

The defensible conclusion is conditional and operational: evaluate recovery as a route through preserved state, executable dependencies and application reconciliation. Record what becomes usable, what remains missing and what evidence supports each claim. Repeatedly exercised recovery can strengthen that route; an inventory, a returned homepage or a completed issue alone cannot establish its full capability.


## 9. How to falsify the extra Mechanical Ethics contribution

Existing database-reliability practice already distinguishes recovery point and time objectives, verified restores, application consistency, accountable postmortems and safer deployment. This case does **not** establish that applying Mechanical Ethics led GitLab to recover faster or differently. In a future comparable real-world recovery exercise, the stronger comparison is with an experienced incident team using its ordinary SRE procedure. Before adding ME terminology, record which hidden dependencies, external effects, possible losses, affected parties and decision clocks the team already identified. Then ask whether the extra boundary/burden/residue questions uncover anything missing *and consequential*. **EXISTING_METHOD_BETTER** and **NO_MATERIAL_DIFFERENCE** are permissible results. An attractive model with more fields and no changed finding may impose cost without benefit.

The case's positive construction is the restoration of service and the subsequent work to create a **maintained, testable recovery capability**. That capability needs ordinary practice, ownership, exercises, tools, people and budgets; an after-action checklist or completed issue is not the same as a tested recovery path. Rebuilding these routes matters even though the missed database changes from this particular incident cannot be put back by a later successful restore.

## Source key

- **S1:** GitLab, 10 February 2017, [Postmortem of database outage of January 31](https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/).
- **S2:** GitLab, 1 February 2017, [GitLab.com database incident](https://about.gitlab.com/blog/gitlab-dot-com-database-incident/).
- **S3:** Original infrastructure issue [1102, automated recovery testing](https://gitlab.com/gitlab-com/infrastructure/issues/1102).
- **S4:** Original infrastructure issue [1163, durability ownership](https://gitlab.com/gitlab-com/infrastructure/issues/1163).
- **S5:** Original infrastructure issue [1684, incident follow-up tracker](https://gitlab.com/gitlab-com/infrastructure/issues/1684).
- **S6:** Original infrastructure issue [1152, streaming backup](https://gitlab.com/gitlab-com/infrastructure/issues/1152).
- **S7:** Original infrastructure issue [1265, automated restoration](https://gitlab.com/gitlab-com/infrastructure/issues/1265).
- **S8:** Original infrastructure issue [1098, hourly snapshots](https://gitlab.com/gitlab-com/infrastructure/issues/1098).
