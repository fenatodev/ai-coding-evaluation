# AI Coding Evaluation

**Executable portfolio for AI coding evaluation, code review, debugging, test design, and agent assessment.**

This repository contains small, synthetic engineering cases built to demonstrate one workflow:

~~~text
inspect
→ reproduce
→ localize
→ explain impact
→ write a failing test
→ implement the smallest safe fix
→ verify regression coverage
→ score the result against a rubric
~~~

The goal is not to showcase toy algorithms. The goal is to show how I evaluate code and AI-generated changes when correctness depends on hidden edge cases, state, authorization, or semantics.

## What this repository demonstrates

- code review focused on behavior, not style alone;
- deterministic failure reproduction;
- security and authorization boundary review;
- concurrency and state reasoning;
- coding-agent trace and authority evaluation;
- multi-file PR review with failure-path and retry analysis;
- detection of subtle semantic regressions introduced by concise refactors;
- minimal corrective patches;
- explicit severity and evidence;
- evaluation rubrics suitable for human or coding-agent review.

## Cases

| Case | Failure class | Signal |
| --- | --- | --- |
| [01 — Authorization boundary](cases/case_01_authz_boundary/report.md) | Cross-tenant object access / IDOR-style bug | Security review, API authorization, adversarial testing |
| [02 — Concurrent reservation](cases/case_02_concurrent_reservation/report.md) | Lost update / double allocation | Concurrency reasoning, deterministic reproduction |
| [03 — Falsy config refactor](cases/case_03_falsy_config_refactor/report.md) | AI-style semantic regression | Code review, edge cases, regression testing |
| [04 — Agent authority trace](cases/case_04_agent_authority_trace/report.md) | Unauthorized tool attempt hidden by runtime denial | Coding-agent evaluation, trace analysis, authority boundaries |
| [05 — Transfer idempotency PR](cases/case_05_pr_review_transaction/report.md) | Partial mutation + broken retry semantics | Multi-file PR review, state reasoning, idempotency |

Cases 01–03 are compact evaluation probes. Cases 04–05 add broader context: execution traces, policy boundaries, multiple modules, state transitions, exception paths, and retry semantics.

The failing behavior in buggy implementations is retained intentionally. Pytest marks those proof tests as strict expected failures so CI stays green while preserving executable evidence of each defect.

## Evaluation rubric

See [rubrics/code_review_rubric.md](rubrics/code_review_rubric.md).

A reusable report skeleton is in [reports/evaluation_template.md](reports/evaluation_template.md).

## Run locally

- Python 3.11+
- pytest

~~~bash
python -m pip install pytest
python -m pytest -q
~~~

Expected result: fixed implementations pass; intentionally buggy implementations appear as expected failures.

## Design rules

1. Cases are synthetic and contain no customer or private code.
2. A finding should be demonstrable, not merely plausible.
3. Tests should prove the reported failure at the smallest useful boundary.
4. Fixes should be minimal enough to reason about.
5. Security claims should distinguish implementation evidence from assumptions.
6. AI-generated code is evaluated by behavior, not fluency or confidence.
7. Runtime prevention and agent-behavior evaluation are separate concerns.
8. Review should inspect failure paths, not only happy-path output.

## Related projects

- [lai-harness](https://github.com/fenatodev/lai-harness) — local-first coding harness with bounded tools, review/promotion, sandboxing and validation gates.
- [lai-gateway](https://github.com/fenatodev/lai-gateway) — local companion gateway and operator workbench.
- [business-automation](https://github.com/fenatodev/business-automation) — FastAPI backend and automation engineering case.

## Author

Fernando Nascimento — [GitHub](https://github.com/fenatodev) · [LinkedIn](https://www.linkedin.com/in/fenatodev/)
