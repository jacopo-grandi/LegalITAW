# LegalITA v2: Evaluating Agentic Legal Work on Italian Matters

> **Working paper draft, 25 September 2026**  
> This is the canonical working version of the paper. It isolates the benchmark's scientific methodology from its software implementation. Corpus figures refer to the current working snapshot and must be frozen when the experiment is run. The results section remains deliberately open: this draft makes no empirical claims in advance of the evidence.

## Abstract

Legal benchmarks built as collections of questions and answers capture some capabilities well. They can test whether a system recalls a rule, recognizes an issue, or explains a conclusion. Much of legal work remains outside that frame. A practitioner receives a mandate and opens a disorderly matter file. The work then depends on selecting the decisive documents, connecting facts found in different sources, and preserving uncertainties left open by the record. It ends with an artifact that somebody can use. LegalITA v2 is designed to measure this broader performance at the system level.

The benchmark contains 100 synthetic matters in Italian law and covers sixteen legal areas. The matters fall into three workflow families: dossier analysis, document review and revision, and procedural computation. Each task specifies a mandate, an as-of date, a closed document set, and the required professional deliverables. The system works in an isolated workspace with generic file tools. Evaluation begins after the run has ended. A private envelope containing the case map and scoring materials remains separate from the public environment throughout execution.

Performance is decomposed into atomic binary criteria. Mechanical requirements are checked deterministically. Semantic requirements are assessed one criterion at a time, and every verdict must point to evidence that can be located in the submission. A judge may also return an explicit unresolved outcome. The primary metric, `all_pass`, asks whether the entire work product is deliverable under the rubric. The `criterion_rate` retains diagnostic resolution. Aggregation gives equal weight to each task. The protocol records run stability and operational measures, including cost and human review burden.

A closed-world design makes runs comparable because every system receives the same information. This design also fixes the present boundary of the benchmark. LegalITA v2 measures a bounded kind of agency centered on matter-file management and artifact production. Open-ended legal research and autonomous interaction with clients or counterparties remain outside its scope. The benchmark makes the distance between a plausible answer and verifiable professional work observable. That distance can then be examined and criticized.

## 1. Research question and argument

LegalITA v2 begins with a question that is easy to ask and difficult to measure: **can an AI system complete an Italian legal assignment by working through a matter file and producing a deliverable that a practitioner could use?**

This question changes the object of evaluation. The unit is the mandate as a whole. Depending on the experiment, the comparison may concern models operating under a common harness or complete systems that combine a model with their own instructions, tools, and execution environment. Legal correctness remains one part of the performance. A sound conclusion can still be unusable when it attributes a fact to the wrong document or misses a dependent clause. The wrong file type can defeat the assignment as well. So can unwarranted certainty where the record is incomplete.

The paper advances three claims. Complex legal work should be evaluated through **situated tasks**. Within each task, the facts and available sources belong to the same performance contract as the client position, the relevant date, and the expected product. Substantive reliability and professional usefulness require separate measurement. Legal error remains an error even in polished prose. A correct output may still impose extensive review. Finally, tool use becomes evaluatively meaningful when its traces can be observed and its relation to the outcome can be tested. The mere presence of a shell or file reader provides no evidence of agency.

Five empirical questions follow:

1. How often do systems complete a multi-step, multi-document legal assignment without error?
2. Do dossier analysis, document revision, and procedural computation produce different failure profiles?
3. How do common-harness model comparisons differ from evaluations of complete systems in their native environments?
4. What relationship holds among correctness, run-to-run stability, operating cost, and human review burden?
5. Which failures become diagnosable only when the tool trace is examined alongside the final deliverable?

## 2. What “agentic” means in LegalITA v2

In this paper, a system is agentic when it controls a sequence of actions within an environment. It inspects the matter, chooses which files to open, and runs local searches. It may create or edit artifacts before deciding that the work is complete. The harness leaves these choices to the system. The resulting object of observation is an entire workflow.

The definition is intentionally narrow. Current tasks are **closed-world**. The information needed to solve them sits inside the matter file and the admitted source pack. Tools support the work, and native-document outputs sometimes depend on them. In most cases, however, the substantive information could also be recovered from a complete textual serialization of the package. We therefore describe the present object as *tool-mediated legal workflow evaluation*. A later edition could test stronger forms of agency by placing selected facts behind a lookup or a document request. Temporal-validity checks and simulated interactions offer two further extensions.

This distinction guards against two errors. The presence of an agentic harness tells us how a task was executed. Whether the task actually required agency remains a separate empirical question. Claims about autonomous behavior also depend on access to the operational choices made during the run. LegalITA v2 therefore retains both the work product and the trace, with correctness assessed primarily from the work product. Process measures remain diagnostic until evidence connects a particular action to successful completion.

## 3. Measurement construct

The central construct is the **ability to complete a verifiable legal assignment within a declared informational and operational boundary**. It is observed through dimensions that answer different questions.

| Dimension | Observable question | Primary evidence |
|---|---|---|
| Matter-file coverage | Did the system identify and use the necessary sources? | Deliverable and file-access log |
| Factual fidelity | Do parties, dates, values, clauses, and attributions match the record? | Comparison with evidence anchors |
| Legal qualification | Is the admitted rule applied to the relevant fact without an unsupported leap? | Substantive criterion and response span |
| Cross-document reasoning | Are distributed facts connected without erasing conflicts or document hierarchy? | Relations expressed in the deliverable |
| Procedural computation | Do trigger, dies a quo, type of time limit, suspensions, and consequences form the correct chain? | Values and legally material intermediate steps |
| Uncertainty discipline | Are missing facts, assumptions, and alternatives kept visible? | Conditioned conclusions and requests for missing information |
| False-positive control | Does the system avoid turning noise, unproven facts, or controlled non-issues into findings? | Absence criteria and negative space |
| Completeness | Are all decidable and material issues addressed? | Coverage of the challenge map |
| Scope discipline | Does the work respect client position, date, admitted sources, and mandate? | Deliverable and run manifest |
| Document transformation | Are edits usable, internally consistent, and propagated across dependent clauses? | Native artifact and structural checks |
| Product conformity | Do format, files, sections, and tables comply with the assignment? | Deterministic checks |
| Operational robustness | Does the system finish, leave the required outputs, and stay within limits? | Trace, failure record, cost, and latency |

The measured construct has defined boundaries. Free recall of law beyond the admitted sources falls outside it, as do stylistic similarity and private chain of thought. A single score offers too little resolution for an undifferentiated notion of “lawyering ability.” LegalITA v2 measures conformity to a corpus and to rubrics that require professional validation. The score carries no independent legal authority.

## 4. Unit of evaluation and task anatomy

The principal statistical unit is the **task**. Each task represents a bounded professional mandate. It identifies the instructing role and the represented side, fixes an as-of date, and supplies a delimited collection of documents. The assignment states its constraints and names the expected deliverables. Criteria provide the smallest units of judgment. Their shared inputs and shared generation make them statistically dependent.

The as-of date prevents later law or later facts from entering the answer retrospectively. The represented side matters because contract review has no neutral ideal form. The deliverable carries equal weight in defining the assignment. A request for a redline makes a memorandum incomplete. A mandate for a procedural timeline also requires the system to expose dependencies and consequences.

Every task is divided into two envelopes. The **public envelope** contains everything the system may know during the run: mandate, documents, admitted sources, and any public instructions governing the work product. The **private envelope**, opened only after the submission has been frozen, contains the issue map, evidentiary anchors, reference solution, distractor, and rubric. This separation is a validity condition. Once evaluation criteria or expected solutions enter the model's context, the benchmark ceases to measure completion of the assignment and begins to measure recognition of the expected answer.

## 5. Corpus design

The current snapshot contains 100 tasks and 5,032 atomic criteria. The portfolio follows a matrix of professional operations and legal areas. This design determines which cases enter the corpus.

### 5.1 Workflow families

| Family | Tasks | Dominant operation | Typical products |
|---|---:|---|---|
| Dossier analysis | 34 | Reconstruct and prioritize issues from distributed evidence | Due-diligence memorandum, risk matrix, evidence matrix |
| Document review and revision | 33 | Identify defects and transform a draft in the represented party's interest | Issue list, review note, tracked-changes DOCX |
| Procedural computation | 33 | Derive a sequence of deadlines, procedural acts, and remedies | Deadline memorandum, calendar, timeline, checklist |

Workflow families are defined by the operation performed. Doctrinal field remains a separate attribute. A privacy matter centered on a deadline belongs to procedural computation. Revision of a banking clause belongs to document review. Ten subtypes refine the expected product. The review family includes `review_only`, `targeted_redline`, and `review_and_redline`. Dossier analysis includes four subtypes, while procedural computation includes three.

### 5.2 Legal coverage

The corpus spans sixteen legal areas. They range from Corporate/M&A and Commercial Contracts to Litigation, Data Protection, Employment, Tax, and Antitrust. Banking, Insolvency, Insurance, Public Procurement, Intellectual Property, Real Estate, Compliance, Financial Crime, and Environmental matters complete the matrix. Each area appears at least twice in every workflow family. Four additional matters provide capstones or designed variation.

This arrangement supports separate analysis by operation and by domain. It offers no estimate of how frequently these matters arise in Italian practice. The distribution reflects benchmark design and should be reported as such.

### 5.3 Difficulty

Page count is a poor proxy for difficulty. The benchmark instead considers how many legal steps the assignment requires and where the relevant evidence appears. Document hierarchies, alternative branches, and chained calculations increase difficulty. So does a record that requires the system to withhold a conclusion. Matter-file size and estimated expert effort are recorded separately. A long linear file may therefore sit below a short matter in which one ambiguity changes the legal characterization.

## 6. Three representative examples

### 6.1 Dossier analysis: M&A due diligence

In task WF2-003, the system acts for the purchaser of an industrial company. It receives a disorderly data room and must isolate red flags with an estimated individual impact above EUR 250,000. Matters below EUR 50,000 should be omitted. Each finding needs a document reference and precise locator. Where the record permits, the system must also quantify the exposure and propose an appropriate contractual response.

Issue spotting is the first step. The system must distinguish a change-of-control clause held by a customer responsible for 34% of revenue from a similar clause held by a replaceable supplier. A separate group of documents establishes a remediation liability estimated at EUR 1.2 to 1.6 million, with no matching provision or insurance. Employment records create a different problem: they show a descriptive ratio of fixed-term to permanent employees, yet omit data required by the legal test. Treating that ratio as an established violation would be an overclaim.

This matter exposes prioritization and cross-document synthesis. It also tests quantification, remedy selection, and control of false positives. A response that lists every anomaly performs poorly because the mandate requires a materiality judgment. Completeness here depends on selection.

### 6.2 Document revision: data processing agreement

In task WF2-001, the system acts for the controller and receives a draft data processing agreement still under negotiation. It must return a complete DOCX with tracked changes and notes linked to the edits. A separate section identifies the points on which the client should hold its position and those open to compromise. The file covers role allocation, the vendor's own use of data, and sub-processors. Other clauses concern metadata retention, international transfers, and breach handling.

The edit must exist in the document and operate on the right clause. It must preserve the remainder of the agreement and match the accompanying explanation. These requirements measure the movement from legal analysis to controlled modification of a professional artifact.

### 6.3 Procedural computation: challenge to the schedule of liabilities

In task WF2-002, a lawyer inherits a disorderly insolvency file. The system must determine whether an already-filed challenge was timely. It must then identify the remedy against the later decree and calculate the next deadline as of 1 February 2027. The mandate also asks which procedural irregularities carry consequences. Several events look like plausible triggers, including the insolvency practitioner's communication and filing of the decree. A registry notice, a repeated transmission, and informal knowledge add noise. The legally operative event changes between the first and second stage of review.

The task requires both the correct date and the correct trigger. A coincidentally accurate calculation still rests on faulty procedural reasoning. Outcome and derivation therefore receive separate criteria.

## 7. Task construction

Authoring proceeds from the intended evidence toward the narrative. Before the matter file is written, a **challenge map** identifies the material issues and controlled non-issues. It records missing facts and dependencies among documents, then specifies any calculation or target error. It also gives each attachment a function. The mandate and public documents are produced from that map. Every item in the file should prove a fact, alter a conclusion, expose a gap, or create a plausible false positive.

For each issue, the author identifies the operative fact and its source. The author then states the governing rule and the proposition required in the deliverable. Professionally equivalent formulations are recorded alongside assertions that would constitute overclaiming. These prohibited assertions define the **negative space**. In legal evaluation, noticing that a clause exists is often easier than controlling the legal effect assigned to it. Rubrics built entirely around presence requirements would reward verbosity and alarmism.

The reference answer defines one admissible solution. Textual similarity carries no value. The distractor is an intentionally defective submission whose expected failures are declared before testing. Together, the two artifacts test whether the rubric accepts substantively equivalent solutions and rejects known failure modes. When the record leaves a conclusion unresolved, the task should reward an actionable reservation. The answer should identify the missing fact and explain how it would affect the analysis.

The underlying facts are synthetic. This permits design control and protects personal data. The corpus description must still follow its provenance. Until legal rules and documentary exemplars are fully traced and professionally validated, the appropriate label is “synthetic cases with controlled legal sources.” Claims of empirical realism require separate evidence.

## 8. Execution protocol

The primary configuration places each system in a temporary workspace. Source documents are read-only. The system receives a separate area for notes and an output directory. Generic file tools and a sandboxed command interface remain available throughout the run. The user message is the public mandate itself. Private fields and evaluation criteria stay outside the conversation. Expected filenames appear only when the simulated practitioner has been given them.

The system chooses its sequence of actions and finishes when it stops invoking tools. Time limits and cost ceilings operate outside the conversation. Turn limits are enforced in the same way, so they carry no strategic signal. Network access is disabled in the closed-world condition. Writes are confined to the permitted directories, and the private envelope is never mounted. An empty output directory is recorded as an operational failure.

At termination, the protocol freezes the deliverables and normalized transcript. It also preserves the tool trace, environment manifest, and stopping reason. Timing, token use, and cost are stored as run metadata. Private reasoning is neither requested nor recorded. For native formats, the benchmark preserves the binary artifact together with a representation that can be judged. File-structure checks can then be evaluated independently from substantive content.

Three experimental conditions should be reported separately:

| Condition | Object of comparison | Purpose |
|---|---|---|
| Common harness, bare profile | Model plus the same minimal environment | Model comparison |
| Common harness, standardized document support | Model plus the same technical instructions | Operational capability on native artifacts |
| External system | Model plus proprietary orchestration and tools | Full-system comparison |

A one-shot condition serializes the entire matter into a prompt and provides a non-agentic control. The workspace run remains the primary condition. The difference between them estimates the contribution of active document handling to observed performance.

## 9. Evaluation

### 9.1 Atomic rubric

Each criterion states an observable proposition and receives `PASS`, `FAIL`, or `unresolved`. Every official criterion is required. Atomicity concerns the interpretability of failure. Keyword matching is one possible verification method, though many criteria require a semantic decision. A requirement such as “identify the trigger, calculate the date, and recommend the remedy” contains several legal operations. Each operation needs its own judgment.

Criteria distinguish several kinds of observable claims. Some require a proposition to appear. Others require its absence. Attribution and exact value form separate classes, as do legal characterization and structural compliance. Conditional criteria apply only when their stated trigger occurs. This logic preserves the difference between an omission and a prohibited assertion. Severity and category support diagnosis. The official verdict remains binary.

### 9.2 Deterministic checks and semantic judgment

Evaluation begins with properties that require no interpretive judgment. The evaluator checks whether files exist and can be opened. It then inspects format, required sections, tables, and tracked changes. Length limits and materialized exact values can also be verified directly. A missing or unreadable deliverable ends the task as an operational failure. Other deterministic findings feed the corresponding criterion.

Semantic requirements are assessed one at a time. The judge receives the submission and the relevant public mandate. It also receives the private formulation of the assigned criterion, which defines the conditions for each verdict and records accepted variants. The formulation includes the relevant negative space. The judge must identify the exact passage supporting its decision. The evaluator verifies that this passage exists in the permitted deliverable and section. For absence and omission criteria, the evidence consists of the scope actually inspected.

An adaptive panel can reduce random judgment error. Two independent judges evaluate the same criterion. A third is called when they disagree or one fails technically. The criterion remains `unresolved` unless two valid votes concur. Majority agreement supports interjudge reliability. Legal validity requires a different test because correlated mistakes on Italian law can produce apparent consensus. Calibration against blind human annotations is therefore a publication gate.

### 9.3 Official metrics

For a task whose required criteria are resolved:

```text
criterion_rate = number of required criteria marked PASS
                 / number of required criteria evaluated

all_pass = 1   if every required criterion is PASS
all_pass = 0   if at least one required criterion is FAIL
all_pass = NA  if at least one required criterion remains unresolved
```

`all_pass` asks whether the work product is deliverable under the task contract. The `criterion_rate` shows the extent and location of any shortfall. Task success has no percentage threshold. This avoids equating a minor formatting error with a dispositive deadline, even when both reduce the rate by one criterion. The diagnostic breakdown exposes the difference.

Aggregation proceeds in two stages. A result is first computed within each task. The second stage gives every task equal weight. A flat average across 5,032 criteria would over-weight matters with longer rubrics. The overall result should be accompanied by macro-averages for workflow family and legal area. Difficulty and matter-file size require separate breakdowns, together with the distribution of criterion counts. Because `all_pass` is conjunctive, the probability of success declines mechanically as a rubric grows. Every comparison must make that effect visible.

### 9.4 Diagnostic measures

The headline score leaves much of system behavior unexplained. Reporting should first separate omission, wrong fact, faulty reasoning, unsupported invention, and format failure. Errors in the rubric, routing, or judge belong to a different layer and must remain distinct from system failures.

Where a task requires evidence, the report should measure its coverage and correctness. The operational record adds documents opened, tool calls, files produced, failed actions, and stopping reason. Latency and cost complete the run-level account. Human reviewers assign `review_burden` using four ordered outcomes: usable as is, minor edits, substantial revision, and redo required.

One distinction deserves particular attention. Omission and false assertion may yield the same `criterion_rate`, yet their risk profiles differ sharply. A visible gap invites review. A plausible but incorrect date may survive precisely because the work appears complete.

## 10. Stability and experimental design

Each combination of task, system, and configuration should be run three times. Replicates measure generation variance. The judge panel measures judgment variance on a frozen submission. Keeping the two estimates separate reveals whether instability originates in the evaluated system or in the evaluator.

For each combination, the report should include `all_pass_rate` and the distribution of `criterion_rate`. It should also report per-criterion failure frequency and the unresolved rate. Latency, cost, and tool use describe the operational burden. Confidence intervals and system comparisons should cluster at task level, using a bootstrap stratified by workflow family or an equivalent hierarchical model. Criteria within one task share the same generation and require clustered treatment.

The main experiment should place every model in the same harness. Submissions from external systems form a second experiment because their tools and orchestration are part of the treatment. A mixed comparison may be commercially informative. Any observed difference in that setting belongs to the full system.

## 11. Human validation

An executable task may still fall short of gold status. Promotion first requires review of matter-file integrity and evidentiary anchors. A legal professional must then complete or review the task under blind conditions. Automated judges are calibrated against human verdicts that were frozen before any adjustment to judge prompts.

The calibration sample must cover criteria with different levels of difficulty. Presence and absence conditions both need representation. It should include calibrated caution, overclaiming, and answers that are prudent yet unusable. The report should publish percentage agreement and a suitable chance-corrected statistic. Disagreement by category and use of the third judge should also be visible. Cases excluded because the rubric was ambiguous remain part of the methodological record. Repairing the measuring instrument is itself a result.

Practitioners annotate reliability and usefulness separately. Reliability uses the same binary criteria. Usefulness records review time and the extent of intervention required. Pairwise comparison among deliverables may enrich this second analysis. Substantive evaluation continues to rest on the criterion-based rubric.

## 12. Validity, limitations, and threats to interpretation

**Closed-world design.** A closed file improves reproducibility and experimental control. Everyday legal research operates under looser informational boundaries. The present benchmark makes no claim about locating current law online, requesting missing documents from a client, or negotiating an information gap.

**Bounded agency.** Traces show how the system worked. In many current tasks, the same substantive information can be supplied as serialized text. The causal value of tool use can be tested through a one-shot ablation. A stronger test would place selected information behind an action.

**Syntheticity.** Synthetic matters provide control and confidentiality. They may simplify the distributions and language found in real files, including the way genuine contradictions appear. A transparent provenance policy is therefore necessary. An authorized sample of realistic or transformed matters would support a later external-validity study.

**Judge validity.** Two judges can agree on the same mistake. Until blind calibration is complete, semantic scores should be presented as pilot results. Unresolved cases and disagreement between human annotators and judges belong in the same report.

**Criterion dependence.** Several criteria may fail because of the same initial omission. The `criterion_rate` is diagnostic. The task remains the inferential unit because its criteria share the same generation.

**Rubric length.** `all_pass` mechanically penalizes tasks with more criteria. A longer assignment creates more opportunities to fail, which is part of the construct. Interpretation still requires comparisons within similar bands of scope.

**Versioning and contamination.** Every experimental component must be frozen and identified by hash. This includes the prompts and documents, as well as parsers, criteria, judges, and harnesses. Public tasks support development. Definitive comparative evaluation requires a sealed split because evaluated models may already have encountered public material.

**Generalizability.** The corpus uses Italian language, sources, professional conventions, and file formats. Applying the method to another jurisdiction requires new authoring and legal validation. Results remain specific to the Italian corpus.

## 13. Results plan

Once runs are frozen, the empirical section should begin with coverage: how many tasks were completed, how many ended in technical failure, and how many criteria remained unresolved. Performance results should follow only after those denominators are clear.

The main table should report task success rate for each system, followed by the task-macro average of `criterion_rate` and its confidence interval. Stability across three runs belongs beside these measures. Review burden, cost, and latency describe practical performance. Subsequent tables should separate workflow families, difficulty bands, and error categories. One figure should show how the probability of `all_pass` changes with criterion count. A second should place reliability and cost on separate axes.

Three analyses are especially informative:

1. An ablation between workspace and one-shot execution on the same matters.
2. A comparison between the bare profile and standardized technical support for native artifacts.
3. A qualitative audit of cases in which similar `criterion_rate` values conceal different risks, particularly omission versus false assertion.

## 14. Expected contributions

LegalITA v2 takes the mandate as its unit of evaluation. Matter files, professional artifacts, and anchored rubrics make that choice measurable. Corpus scale supports the analysis, although the methodological change carries the main claim. The method formalizes negative space and can therefore penalize alarmism. It records system failures separately from defects in criteria or judges. Operational failure enters the performance record. Model comparison and full-system comparison remain separate experiments.

If the protocol survives human validation, its most useful result will be a map of where legal work breaks. Failure may occur when a document is converted into a factual proposition, or when that proposition receives its legal characterization. A later error can arise in selecting the remedy. Sometimes the analysis survives all these stages and still fails during the deceptively ordinary act of producing the deliverable file.

---

## Editorial notes for the next iteration

This section is for drafting use and will be removed before submission.

### Decisions to freeze

1. Target venue and page limit.
2. Corpus snapshot, attachment count, and updated difficulty distribution.
3. Official judge configuration and human-calibration protocol.
4. Included systems, number of replicates, and budget.
5. Benchmark split used for publishable results.
6. Title terminology: “agentic legal benchmark” or the more cautious “tool-mediated legal workflow benchmark.”

### Tables and figures to produce

1. The 3 workflow families × 16 legal areas matrix.
2. Conceptual task anatomy, from mandate and public workspace to deliverable and scoring.
3. An example showing how a challenge map becomes presence, absence, and attribution criteria.
4. Distributions of criteria, documents, and difficulty.
5. Headline results with confidence intervals.
6. Failure taxonomy by workflow family.
7. Reliability against review burden.
8. Stability, cost, and latency across replicates.

### Facts already verified in the current snapshot

1. The common validator loads 100 tasks successfully.
2. The corpus contains 5,032 atomic criteria.
3. The workflow families contain 34, 33, and 33 tasks respectively.
4. The corpus covers sixteen legal areas.
5. The primary harness uses an isolated workspace and generic tools.
6. Public and private material remain separate, and evaluation begins after submission freeze.

### Claims to withhold until the corresponding gate is met

1. “Gold benchmark” before blind legal sign-off.
2. “Human-level” before a human baseline has been collected under the same protocol.
3. “Real-world” before the representativeness of the matters has been tested.
4. “Agentic reasoning” when the observable evidence consists of tool calls and artifacts.
5. “Judge-validated” before calibration against human annotators.
6. Superiority of one model when the harness also changes.
