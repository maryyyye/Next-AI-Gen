# TD1 — Lot E

Model: `openrouter:dots-studio/dots-3-note-preview:free`.

After correcting authentication, the batch returned 20 HTTP 200 responses: **16 correct, 4 incorrect (80%)**. All results are real calls, not simulations. SQL results were independently re-executed locally in read-only SQLite; CSV/JSONL agreement, reference values and unchanged prompt fingerprints were checked with coding assistance.

## Evidence and attempt accounting

- Initial batch: [state-E.jsonl](../state-E.jsonl), [traces-E.csv](../traces-E.csv): 20 HTTP 401 authentication failures.
- After authentication correction: [state-E-auth-fixed.jsonl](../state-E-auth-fixed.jsonl), [traces-E-auth-fixed.csv](../traces-E-auth-fixed.csv): 20 calls, one per question, no automatic retries in this batch.
- Total recorded question attempts: **40**, or two per cell across both files. The new state file restarts its local `attempts` counter at 1; this is the second attempt overall, not another set of initial calls. Preserve both sets when consolidating. Do not launch further retries of these cells.
- The operator reported a successful separate model-access probe before the corrected batch. Earlier access-test failures were reported in the working conversation; a complete access-check count and terminal evidence still need to be recorded by the operator. These checks are separate from the 40 recorded question attempts.

## Incorrect answers

| Question | Model value (cents) | Reference (cents) | Cause in generated SQL |
|---|---:|---:|---|
| C02 | 439570 | 590320 | The CASE subtracts one year both before and after the birthday, effectively always subtracting one. |
| C16 | 211260 | 376740 | Requires calendar-year difference 25 and birthday already reached; excludes people with year difference 26 whose birthday is still upcoming and who are still 25. |
| C17 | 152730 | 258180 | Same missing branch for completed age 25 before the birthday. |
| C18 | 39580 | 62480 | Same missing branch, evaluated at the order date. |

The generated SQL is preserved unchanged. These are model errors, not reference corrections. The result supports analysis of completed-age handling on this dataset, not a general model ranking. Human peer validation of references and operator identity remain to be documented separately.
