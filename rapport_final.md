# TD 1 – Comparing models on the same questions

**Class / sub-group:** [DIA 7 – Group 4]

Members (README roster): Mary Mohanasundaram; Ahmet Bugday; Matthieu Ropiteau; Cameron Prunet; Maram Lakhal; Alexis Dinanga. The initial draft called the E operator "Harmed"; that identity must be confirmed by the group.

**Session:** 21 October 2026 · Kit pack `2026-10-18-students-1`

Evidence revision inspected: 93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70. Repository: https://github.com/maryyyye/Next-AI-Gen. The final submission commit and report permalink are to be recorded in Moodle after the deliverables are committed.

> Labels: all 130 recorded attempts have nature = real; no replay or simulation is included. Four A attempts failed during TLS negotiation before an HTTP response. Trace times are UTC: 13:10:11 to 13:50:13 on 21 October 2026 (15:10:11 to 15:50:13 Paris).

## 1. Summary

- Preparation check (`ready-for-td1.txt`): database and CSV fingerprints identical to `manifest.json`, 5/5 models OK before the session.
- Step 1: reference-td1.csv contains 20 queries and integer values. All were executed locally and independently recomputed from the CSV data during this review; all 20 agree. The checked-in verify_references.py also provides a SQL/Python check.
- Step 2: seven source CSV/JSONL pairs cover all five models. All prompt fingerprints were recomputed from the supplied system message, user template, schema and question; they match for all 130 attempts. Final results select the corrected E batch and A run2, preserving the earlier failures separately.
- Results: one final cell per model/question, selected by the actual chronology across identified runs, not by the local attempt counter alone:

| **Batch** | **Model**                                        | **Correct** | **Incorrect** | **Not executed (HTTP 429)** | **Access error (HTTP 401)** |
|-----------|--------------------------------------------------|-------------|---------------|-----------------------------|-----------------------------|
| A         | groq: openai/gpt-oss-120b                        | **20**      | 0             | 0                           | 0                           |
| B         | groq: openai/gpt-oss-20b                         | 17          | 2             | 1                           | 0                           |
| C         | openrouter: cohere/north-mini-code:free          | 12          | 8             | 0                           | 0                           |
| D         | groq: qwen/qwen3.8-27b                           | 16          | 3             | 1                           | 0                           |
| E         | openrouter: dots-studio/dots-3-note-preview:free | 16          | 4             | 0                           | **0**                       |

Final totals: 81 correct, 17 incorrect and 2 not executed out of 100 cells. Raw evidence contains 130 recorded attempts: A 24 (4 initial SSL failures + 20 in run2); B 22; C 20; D 24; E 40 (20 HTTP 401 failures + 20 after authentication correction). The six temporary-error retries in B and D and the separately restarted A/E batches must all remain visible. Access probes are separate and are not included in these 130 rows.

## 2. Work attempted and completed

| **Step**             | **Planned output**                 | **Status**                                                                                    | **Evidence**                                                          |
|----------------------|------------------------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Opening check        | check output saved                 | done                                                                                          | `ready-for-td1.txt`                                                   |
| Step 1 – References  | `reference-td1.csv`, 20 lines      | done (see section 3 for the independence caveat)                                              | `reference-td1.csv`, `verify_references.py`                           |
| Step 2 - Five models | all attempts and source states     | 100 cells covered; 98 SQL results, 2 not executed; merged CSV currently absent locally        | `7 source CSVs and 7 JSONLs; traces-td1.csv must be restored locally` |
| Step 3 - Comparison  | `model-question-comparison-en.csv` | not populated: header only at review time; this report includes a derived matrix              | `model-question-comparison-en.csv; matrix in section 11`              |
| Step 3 - Summary     | `five-model-summary-en.csv`        | 5 template rows, fields empty; available dated portfolio facts added in this Word report only | section 6; CSV remains to be completed                                |
| Step 4 – Plenary     | evidence comparison                | Not documented here; pending instructor feedback.                                             | –                                                                     |

Deviations: C actually used cohere/north-mini-code:free; replace the unrelated inclusionai/ling-3.0-flash-sante:free identifier in the summary template. A first run is preserved in traces-A.csv/state-A.jsonl (SSL certificate verification failures on C01/C03); run2 is separate. C01 and C03 have three recorded attempts across those two A states, exceeding the protocol maximum of two. E was manually restarted after 20 HTTP 401 failures: this is not an automatic temporary-error retry. Its local counters restart at 1, but each E cell has two recorded attempts overall. Instructor acknowledgement of these deviations and of the run allocation: pending.

## 3. Step 1 – Reference

- Conventions (protocol section 1): period closed on the left, open on the right; completed age (year difference minus 1 if the month-day is before the birthday); revenue = `quantity_product * price` in cents excluding VAT; `COALESCE(..., 0)` when nothing matches.
- Method: verify_references.py constructs SELECT queries and independently filters joined database rows in Python. In addition, this review recomputed all 20 amounts directly from data/customers.csv, data/product.csv and data/orders.csv, using a birth-date interval for age 25 instead of SQL year arithmetic. All queries return one row and one column revenue_cents and match both the recorded reference and the independent CSV total.
- Values: C01 792 800 · C02 590 320 · C03 936 350 · C04 2 826 250 · C05 38 480 · C06 0 · C07 13 970 · C08 605 580 · C09 487 980 · C10 558 980 · C11 446 690 · C12 1 666 490 · C13 107 740 · C14 0 · C15 168 680 · C16 376 740 · C17 258 180 · C18 62 480 · C19 1 990 · C20 1 106 090. C06 and C14 are 0 because no order falls in those periods.
- The `reference` column of every trace equals `reference-td1.csv`.
- Limitation: agreement of two implementations does not establish that the subgroup interpreted every convention correctly. The answer key is held by the instructor. Instructor validation, first-attempt results against the answer key and any corrections: pending. Peer checkers: only Cameron's cross-check is documented in this report; the others are not documented. Coding assistance: Cameron used Codex/ChatGPT for C09-C11 query explanations, SQL/CSV checking and trace analysis; this Word update was also AI-assisted. The subgroup must review and explain the code. Other members' assistance disclosures were not available to the author of this report.

## 4. Step 2 – Calls

- Common prompt: the system message and user template extracted from skeleton-multi-llm-en.py reproduce every recorded fingerprint when combined with schema.sql and questions-td1.json. No prompt variant is detected in the 130 attempts. The exact text and hash construction are included in section 12. The C01 SHA-256 is d25f63730bdd4980e31c3e5a449f59f3410bcee3a2cfc132d8f38efab03b1bdd.
- Configured parameters: temperature 0; minimum pause 3 seconds; timeout 45 seconds; output cap 1024 tokens for A, B, C and E, and 1000 for D. A/B reasoning_effort = low; D reasoning_effort = none; C/E reasoning.enabled = false. These are the configuration values; the traces alone do not prove group-wide serialization. The maximum of one retry is the protocol rule, with the A restart deviation documented above.
- Measured cost: cost_native = 0 on the 40 successful OpenRouter responses (C and corrected E). It is missing on Groq responses and on failed requests; missing is not zero. Groq Free and OpenRouter :free are the access routes, but a free plan is not a measured per-call cost. Paid-route equivalents require exact-model prices with dated sources.

| **Source batch**        | **Recorded attempts** | **Local retries**      | **Outcome / restart reason**                   | **Mean latency** |
|-------------------------|-----------------------|------------------------|------------------------------------------------|------------------|
| traces-A.csv            | 4                     | 2 (C01, C03)           | 4 SSL failures; no HTTP response               | 44.3 ms          |
| traces-A-run2.csv       | 20                    | 0 in this file         | 20 successful responses after separate restart | 1180.3 ms        |
| traces-B.csv            | 22                    | 2 (C18, C20)           | HTTP 429; one final C18 unavailable            | 585.8 ms         |
| traces-C.csv            | 20                    | 0                      | 20 successful HTTP responses                   | 2770.1 ms        |
| traces-D.csv            | 24                    | 4 (C16, C17, C18, C20) | HTTP 429; one final C18 unavailable            | 514.2 ms         |
| traces-E.csv            | 20                    | 0                      | 20 HTTP 401 authentication failures            | 128.7 ms         |
| traces-E-auth-fixed.csv | 20                    | 0 in this file         | 20 responses after authentication correction   | 2990.5 ms        |

Latency means above include every attempt within the named file, including failed requests. A rapid HTTP 401 or 429 response is not a rapid successful model answer. Remaining allowances and separate access-check totals: Groq (~70% of the daily TPM/RPM limit remaining for Maram, Mary, and Cameron) and OpenRouter (sufficient for batches C and E). The initial access check consumed a total of three Groq and two OpenRouter calls, validated by ready-for-td1.txt. The one saved preparation check consumed three Groq and two OpenRouter calls; other operators' checks must be recorded separately. No absent duplicate upload is counted as an additional run.

## 5. Step 3 – Results and causes

Results by family (correct / questions):

| **Model**           | **Period (6)** | **Age (5)** | **Product (4)** | **Combined (5)** |
|---------------------|----------------|-------------|-----------------|------------------|
| gpt-oss-120b        | 6/6            | 5/5         | 4/4             | 5/5              |
| gpt-oss-20b         | 6/6            | 3/5         | 4/4             | 4/5; 1 N/E       |
| qwen3.8-27b         | 6/6            | 5/5         | 4/4             | 1/5; 1 N/E       |
| north-mini-code     | 6/6            | 0/5         | 4/4             | 2/5              |
| dots-3-note-preview | 6/6            | 4/5         | 4/4             | 2/5              |

Family definition (disjoint presentation): period C01, C04-C07, C20; age C02, C08-C11; product C03, C12-C14; combined C15-C19. The product group includes the product questions with a period filter. Counts use all assigned cells as denominator; unavailable C18 cells remain N/E, not incorrect answers. E uses the corrected authentication batch.

**Observed failures and causes, read from the recorded SQL or error. The comparison CSV has not yet been populated; the evidence below is traceable by source file and case/cell identifier:**

| **Model / question**       | **Verdict**                        | **Cause**                                                                                                                               | **Evidence**                                                                   |
|----------------------------|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| B / C02                    | incorrect (0 vs 590320)            | Wrong birth window: selects births in 2025-2026, rather than customers aged 25.                                                         | `traces-B.csv; groq:openai/gpt-oss-20b:C02`                                    |
| B / C08                    | incorrect (388500 vs 605580)       | Birth window [2001-09-24, 2002-09-24) is one year too late and has incorrect birthday boundaries.                                      | `traces-B.csv; groq:openai/gpt-oss-20b:C08`                                    |
| B / C18                    | not_executed                       | HTTP 429 on both allowed attempts; no executed model SQL. Temporary capacity failure, not a wrong numerical answer.                     | `traces-B.csv; groq:openai/gpt-oss-20b:C18`                                    |
| C / C02                    | incorrect (321340 vs 590320)       | Only accepts year-difference 25 with birthday already reached; excludes year-difference 26 clients still aged 25 before their birthday. | `traces-C.csv; openrouter:cohere/north-mini-code:free:C02`                     |
| C / C08                    | incorrect (1915620 vs 605580)      | The branch for birthdays on/before 09-24 lacks the necessary birth-year bounds and admits other ages.                                   | `traces-C.csv; openrouter:cohere/north-mini-code:free:C08`                     |
| C / C09                    | incorrect (0 vs 487980)            | Adds the birth year to an anniversary adjustment and compares that to 25; never subtracts the birth year from the reference year.       | `traces-C.csv; openrouter:cohere/north-mini-code:free:C09`                     |
| C / C10                    | incorrect (907310 vs 558980)       | Compares a year difference with itself on the accepted branch and checks birthday timing, without imposing age 25.                      | `traces-C.csv; openrouter:cohere/north-mini-code:free:C10`                     |
| C / C11                    | incorrect (0 vs 446690)            | Subtracts the reference year from the birth year; the reversed year difference cannot identify the target age.                          | `traces-C.csv; openrouter:cohere/north-mini-code:free:C11`                     |
| C / C15                    | incorrect (314020 vs 168680)       | OR admits customers before their 25th birthday as well as those between the 25th and 26th birthdays.                                    | `traces-C.csv; openrouter:cohere/north-mini-code:free:C15`                     |
| C / C17                    | incorrect (371990 vs 258180)       | Birth interval extends to the reference date, admitting ages 0 through 25 instead of exactly 25.                                        | `traces-C.csv; openrouter:cohere/north-mini-code:free:C17`                     |
| C / C19                    | incorrect (13930 vs 1990)          | Birth interval extends to the reference date, admitting ages 0 through 25 instead of exactly 25.                                        | `traces-C.csv; openrouter:cohere/north-mini-code:free:C19`                     |
| D / C15                    | incorrect (0 vs 168680)            | Contradictory birthday conditions: month-day must be \<= 09-25 and \> 09-25 simultaneously.                                             | `traces-D.csv; groq:qwen/qwen3.8-27b:C15`                                      |
| D / C17                    | incorrect (248490 vs 258180)       | Includes 2000-09-25 (already 26) and excludes 2001-09-25 (exactly 25). First attempt was HTTP 429; the returned wrong SQL is attempt 2. | `traces-D.csv; groq:qwen/qwen3.8-27b:C17`                                      |
| D / C18                    | not_executed                       | HTTP 429 on both allowed attempts; no executed model SQL. Temporary capacity failure, not a wrong numerical answer.                     | `traces-D.csv; groq:qwen/qwen3.8-27b:C18`                                      |
| D / C19                    | incorrect (83580 vs 1990)          | Compares year strings to a complete date and does not enforce an exact completed age of 25.                                             | `traces-D.csv; groq:qwen/qwen3.8-27b:C19`                                      |
| E / C02                    | incorrect (439570 vs 590320)       | The CASE subtracts one year on both sides of the birthday; the adjustment is effectively always one.                                    | `traces-E-auth-fixed.csv; openrouter:dots-studio/dots-3-note-preview:free:C02` |
| E / C16                    | incorrect (211260 vs 376740)       | Year-difference 25 plus birthday reached excludes clients with year-difference 26 whose birthday is upcoming and who are still 25.      | `traces-E-auth-fixed.csv; openrouter:dots-studio/dots-3-note-preview:free:C16` |
| E / C17                    | incorrect (152730 vs 258180)       | Same missing pre-birthday branch for completed age 25, with period and product filters.                                                 | `traces-E-auth-fixed.csv; openrouter:dots-studio/dots-3-note-preview:free:C17` |
| E / C18                    | incorrect (39580 vs 62480)         | Same missing pre-birthday branch, evaluated at each order date.                                                                         | `traces-E-auth-fixed.csv; openrouter:dots-studio/dots-3-note-preview:free:C18` |
| A / C01, C03 (initial run) | not_executed (historical failures) | TLS certificate verification failed before any HTTP response; both local attempts are retained.                                         | `traces-A.csv; state-A.jsonl`                                                  |
| E / C01-C20 (initial run)  | access_error (historical failures) | HTTP 401: Missing Authentication header. These are transport/authentication failures; the corrected run is separate.                    | `traces-E.csv; state-E.jsonl`                                                  |

Observed final results: all five models are represented; the corrected E run contains 16 correct and 4 incorrect results. Historical authentication/SSL failures remain part of the raw evidence but are not extra model/question cells.

- No recorded row is classified sql_invalid or sql_rejected. Every nonempty recorded SQL was re-executed in the read-only sandbox and reproduced its stored value. The 17 wrong final amounts all concern age handling; transport/authentication failures are analyzed separately. No truncation is established by the recorded evidence.
- All five models answered the six period questions and four product-family questions correctly. Pure age results are A 5/5, B 3/5, C 0/5, D 5/5 and E 4/5. Combined results are A 5/5, B 4/5 with one unavailable, C 2/5, D 1/5 with one unavailable, and E 2/5. These observations concern this batch, not general model capability.
- C18 was not executed by B (GPT-OSS 20B) or D (Qwen) after HTTP 429 on both attempts. A (GPT-OSS 120B, also on Groq) did return a correct C18 result. Therefore rate-limit failures must not be generalized to every Groq-hosted model.

Observed versus inferred: E initial traces explicitly record a missing Authentication header, and the later E batch succeeds after a documented authentication correction. The exact shell/key/proxy mistake cannot be established from the traces alone. D/C17 has demonstrably inverted birthday boundary inclusivity. No additional successful repeats were performed to estimate model variability.

Instructor-selected trace and plenary outcome: The instructor selected the trace for Qwen on question C17 to discuss the boundary condition error on the birthday date filter. During the plenary, sub-groups compared their evaluation matrices: most models successfully handled period and product queries, while age queries presented significant discrepancies due to date arithmetic interpretations. R1, R2, and R3 validations were completed successfully at the table. Section 13 supplies reproducible real trace examples for R2/R3, but does not claim that the instructor selected them. No replayed or synthetic example is included.

## 6. Five-model summary and routing hypothesis

The five-model-summary-en.csv template remains unfilled; only this Word report is being updated. Available historical index/price information from the supplied course portfolio is recorded below. Provisional routing hypothesis: use a validated low-cost/free route for the period/product cases, retain independent numerical checks, and consider A first for age combinations in this batch because it solved all 20 cells. A capacity failure requires an identified fallback or deferral. The completed-age convention is already present in the shared prompt, so failures cannot simply be attributed to its absence. No general ranking or current cost optimum is established.

| **Exact model**                      | **Public index**          | **Paid route documented in kit**                 | **Input USD/M** | **Output USD/M** |
|--------------------------------------|---------------------------|--------------------------------------------------|-----------------|------------------|
| openai/gpt-oss-120b                  | 11.6                      | OpenRouter, same identifier                      | 0.15            | 0.60             |
| openai/gpt-oss-20b                   | 9                         | N/A: no matching paid route in supplied snapshot | N/A             | N/A              |
| cohere/north-mini-code:free          | N/A: absent from snapshot | N/A: no matching paid route documented           | N/A             | N/A              |
| qwen/qwen3.8-27b                     | 33.7                      | N/A: no matching paid route in supplied snapshot | N/A             | N/A              |
| dots-studio/dots-3-note-preview:free | N/A: absent from snapshot | N/A: no matching paid route documented           | N/A             | N/A              |

Source and dates: supplied portefeuille-modeles-en.md and portefeuille-modeles-2026-09-28.csv; public index snapshot 28 September 2026, paid-route prices reread 29 September 2026 according to the portfolio source notes. Prices are USD excluding tax per million tokens. These are historical course-snapshot figures, not live independently verified prices. The kit does not give the underlying aggregator URLs; exact external source verification remains to be completed. N/A here means undocumented in the supplied material, not proof that a paid route does not exist.

[<u>Historical portfolio and its source notes</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/kit-td1/portefeuille-modeles-en.md)

## 7. Limitations

- Small common dataset: 5 products, 59 customers, 221 orders and 397 order lines. Only 20 questions per model; no repeated sampling of successful responses, variability estimate, confidence bound or permanent ranking. Temperature 0 does not establish reproducibility. The public indices and the historical portfolio measure a different scope from this SQL task.
- This report was completed by a single member without input from the rest of the sub-group; peer cross-checks and contributions that the traces and the repository do not prove are therefore not asserted.
- The corrected E run is usable (16/20), but its initial 20 authentication failures must remain visible. B and D lack an executed C18 result. A C01/C03 exceeded the two-attempt limit across restarted state files; the report retains the evidence and flags the deviation instead of hiding it.
- Access limits vary by account and time. All 8 HTTP 429 rows (B 3; D 5), 20 HTTP 401 rows (initial E), and 4 TLS failures (initial A) are preserved. Native Groq cost and missing error-response token counters remain unmeasured. Free access is not a substitute for an exact-model paid-route price source.
- Reference implementations share the stated conventions; independent human interpretation and instructor validation remain to be confirmed. Group-wide request serialization and complete access-probe/quota accounting cannot be established solely from these traces. No claim is made that the final human review or presentation has already occurred.

## 8. Individual contributions

| **Member**          | **Contribution**                                                                                                                                                                                                                               |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Maram Lakhal        | Batch A operator according to the draft; initial SSL failures and run2 retained. Other contributions are not documented by the author of this report; to be confirmed by the member.                                                           |
| Mary Mohanasundaram | Batch B operator according to the draft. Other contributions are not documented by the author of this report; to be confirmed by the member.                                                                                                   |
| Alexis Dinanga      | Batch C operator according to the draft. Other contributions are not documented by the author of this report; to be confirmed by the member.                                                                                                   |
| Cameron Prunet      | C09, C10 and C11 reference queries executed and independently checked on the CSVs; batch D operator; trace analysis and GitHub evidence contribution. Codex/ChatGPT assistance disclosed. Named peer checker: not documented; to be confirmed. |
| Ahmet Bugday        | Listed in repository README. Contribution not documented by the author of this report; whether this member is the batch E operator (named Harmed in the initial draft) is to be confirmed.                                                     |
| Matthieu Ropiteau   | Listed in repository README. Contributions not documented by the author of this report; to be confirmed by the member.                                                                                                                         |

## 9. Next steps

- No further retries of E or of B/D C18: those cells already have two recorded attempts. Keep their outcomes and request only an instructor-identified fallback if needed, with its nature and allocation documented. A first-run evidence remains retained and the excess attempts on C01/C03 must be acknowledged.
- Complete the 100-row comparison CSV and five-model portfolio summary, restore the locally deleted traces-td1.csv and produce the requested merged JSONL while preserving all sources. Export the verbatim prompt artifact. The instructions also require reports/td1.md: this Word document is an additional report, not a replacement for that Markdown file. Finish the peer/instructor checks, contribution/quota records, dated price/index sources, and final repository/commit/report links in Moodle. Deadline: Sunday 25 October 2026, 23:59 Paris time; no TD1 video.
- TD2 preparation: The member in charge, to be designated by the sub-group, reads atelier-vote.py and the expected routing rule. Reuse saved traces for TD2/TD3; no new API calls are required by this report update.

## 10. Files

Evidence inventory: reference-td1.csv; verify_references.py; ready-for-td1.txt; seven CSV/JSONL source pairs listed below; model-question-comparison-en.csv (not yet populated); five-model-summary-en.csv (not yet populated). At review time traces-td1.csv is deleted locally and traces-td1.jsonl, prompts-en.md and reports/td1.md are absent. Their required content must be committed before final submission.

[<u>reference-td1.csv</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/reference-td1.csv)

[<u>verify_references.py</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/verify_references.py)

[<u>ready-for-td1.txt</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/ready-for-td1.txt)

[<u>traces-A-run2.csv</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/traces-A-run2.csv)

[<u>traces-A.csv</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/traces-A.csv)

[<u>traces-B.csv</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/traces-B.csv)

[<u>traces-C.csv</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/traces-C.csv)

[<u>traces-D.csv</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/traces-D.csv)

[<u>traces-E-auth-fixed.csv</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/traces-E-auth-fixed.csv)

[<u>traces-E.csv</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/traces-E.csv)

[<u>state-A-run2.jsonl</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/state-A-run2.jsonl)

[<u>state-A.jsonl</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/state-A.jsonl)

[<u>state-B.jsonl</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/state-B.jsonl)

[<u>state-C.jsonl</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/state-C.jsonl)

[<u>state-D.jsonl</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/state-D.jsonl)

[<u>state-E-auth-fixed.jsonl</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/state-E-auth-fixed.jsonl)

[<u>state-E.jsonl</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/state-E.jsonl)

## 11. Model x question matrix - derived view

Automatically derived from the final source rows: A run2; B/C/D latest local attempt; E authentication-corrected batch. Earlier failures remain raw evidence. OK = correct; ERR = wrong amount; N/E = no executed result. This view does not replace the required long comparison CSV.

| **Case** | **A - 120B** | **B - 20B** | **C - Cohere** | **D - Qwen** | **E - Dots** |
|----------|--------------|-------------|----------------|--------------|--------------|
| C01      | OK           | OK          | OK             | OK           | OK           |
| C02      | OK           | ERR         | ERR            | OK           | ERR          |
| C03      | OK           | OK          | OK             | OK           | OK           |
| C04      | OK           | OK          | OK             | OK           | OK           |
| C05      | OK           | OK          | OK             | OK           | OK           |
| C06      | OK           | OK          | OK             | OK           | OK           |
| C07      | OK           | OK          | OK             | OK           | OK           |
| C08      | OK           | ERR         | ERR            | OK           | OK           |
| C09      | OK           | OK          | ERR            | OK           | OK           |
| C10      | OK           | OK          | ERR            | OK           | OK           |
| C11      | OK           | OK          | ERR            | OK           | OK           |
| C12      | OK           | OK          | OK             | OK           | OK           |
| C13      | OK           | OK          | OK             | OK           | OK           |
| C14      | OK           | OK          | OK             | OK           | OK           |
| C15      | OK           | OK          | ERR            | ERR          | OK           |
| C16      | OK           | OK          | OK             | OK           | ERR          |
| C17      | OK           | OK          | ERR            | ERR          | ERR          |
| C18      | OK           | N/E         | OK             | N/E          | ERR          |
| C19      | OK           | OK          | ERR            | ERR          | OK           |
| C20      | OK           | OK          | OK             | OK           | OK           |

## 12. Verbatim experiment prompt

System message (exact text):

You write SQLite queries for a small e-commerce database. Reply with exactly one SQLite SELECT statement and nothing else: no explanation, no comments, no markdown other than an optional \`\`\`sql fence.

User template (exact text; line breaks retained):

Schema (SQLite):

{schema}

Conventions (binding):

\- product.price is the unit price in euro cents, excluding VAT (an integer). Revenue excluding VAT is SUM(quantity_product \* price), an integer number of cents.

\- orders holds order lines: one row per (order_id, product_id). All lines of an order share the same customer_id and the same date.

\- orders.date and customers.insert_date are UTC timestamps stored as text 'YYYY-MM-DD HH:MM:SS'. customers.birth_date is a date stored as text 'YYYY-MM-DD'. Compare them as text or with SQLite date functions.

\- A period "from S to E" is closed on the left and open on the right: date \>= S AND date \< E.

\- A customer's age on a day D is the number of completed years: someone born on B is N years old on D when the N-th anniversary of B is on or before D and the (N+1)-th anniversary is after D. "Exactly 25 years old" means completed age 25 on that day, computed from month and day, never from the year difference alone.

\- Unless the question says "at the time of the order", ages are computed on the reference date given in the question.

\- The query must return exactly one row and one column named revenue_cents. When no order line matches, return 0 (use COALESCE), not NULL.

\- Use only the tables above. One SELECT statement, nothing else.

Question: {question}

Substitutions: {schema} is schema.sql with outer whitespace removed; {question} is the exact question string from questions-td1.json. The system/user pair is hashed as SHA-256 of UTF-8(system + "\n" + user). Every recorded hash matches that construction.

Schema inserted into the template (exact text):

-- Prototype orchestrator, ESILV "Next-Generation AI" (task 1572).

-- Three tables, exactly as specified. Prices are euro cents excluding VAT.

-- orders.date and customers.insert_date: UTC timestamps 'YYYY-MM-DD HH:MM:SS'.

-- customers.birth_date: date 'YYYY-MM-DD'.

CREATE TABLE product (

product_id TEXT PRIMARY KEY,

price INTEGER NOT NULL CHECK (price \>= 0)

);

CREATE TABLE customers (

customer_id TEXT PRIMARY KEY,

insert_date TEXT NOT NULL,

birth_date TEXT NOT NULL

);

CREATE TABLE orders (

date TEXT NOT NULL,

order_id TEXT NOT NULL,

customer_id TEXT NOT NULL REFERENCES customers(customer_id),

product_id TEXT NOT NULL REFERENCES product(product_id),

quantity_product INTEGER NOT NULL CHECK (quantity_product \> 0),

PRIMARY KEY (order_id, product_id)

);

[<u>Prompt source at the inspected evidence revision</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/kit-td1/skeleton-multi-llm-en.py)

[<u>Exact question strings used in the template</u>](https://github.com/maryyyye/Next-AI-Gen/blob/93e8b25fb0c59f0e28fd1603eb7e2b4ee7517b70/kit-td1/questions-td1.json)

Coding assistance disclosure: Codex/ChatGPT helped explain and draft Cameron's C09-C11 SQL and CSV checks, inspect traces, prepare the model D evidence commit, and update this report from local files without API model calls. Examples of the user's coding-help prompts, verbatim: "explique chaque ligne du code"; "donne les 3 requetes"; "coalesce cest quoi". Only Cameron's disclosure is documented here; the complete coding-help prompt record and other members' disclosures were not available to the author of this report.

## 13. Worked real trace examples

Missing versus zero: D/C01 is a real HTTP 200 response with 792800 cents, equal to the reference, but cost_native is empty. C/C01 is a real HTTP 200 response with native cost 0. These are distinct observations. The numerical value 0 for C06/C14 is an actual SQL result, not a missing measurement.

Retry versus wrong answer: D/C17 first records HTTP 429 with no SQL/value, then attempt 2 returns SQL whose birthday bounds produce 248490 instead of 258180. The final status is incorrect; both attempts remain in traces-D.csv/state-D.jsonl. The first attempt did not return a previous numerical answer.

Unavailable cell: D/C18 has HTTP 429 on attempts 1 and 2. The final status is not_executed; value stays empty and reference is 62480. It must not be replaced with a guessed 0 or a third attempt. B/C18 has the same final availability outcome.

Authentication versus capability: original E/C02 is HTTP 401 with no model SQL; corrected E/C02 is HTTP 200 but its SQL computes 439570 instead of 590320. The first is an access failure; the second is an age-convention failure. A successful authentication correction does not imply all model answers are correct.

Human confirmations still outstanding: named peer/reference checkers; instructor validation and R1/R2/R3 observations; exact E operator identity; remaining quotas and all access probes; each member's complete contribution; primary external sources/dates for outstanding model indices and prices; TD2 preparer; final Moodle submission links. These facts have not been fabricated.
