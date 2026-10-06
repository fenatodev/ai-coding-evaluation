# Code review and AI coding evaluation rubric

Score each dimension from **0 to 4**.

| Dimension | 0 | 2 | 4 |
| --- | --- | --- | --- |
| Correctness | Misses the defect or asserts incorrect behavior | Partially identifies the problem | Correctly identifies behavior and relevant edge cases |
| Localization | Cannot identify the responsible boundary | Finds the general area | Isolates the minimal responsible code/path |
| Evidence | Speculative claim only | Some supporting reasoning | Reproducible test or concrete execution evidence |
| Severity | No impact analysis | Generic severity statement | Impact is tied to reachable behavior and scope |
| Test quality | No useful test | Happy-path or weak assertion | Minimal deterministic proof plus regression coverage |
| Fix quality | Overbroad or unsafe change | Plausible fix with gaps | Small fix that addresses root cause without unrelated change |
| Regression awareness | Ignores adjacent behavior | Mentions possible regressions | Protects invariants and relevant neighboring behavior |
| Communication | Vague or confident without evidence | Understandable but incomplete | Precise, bounded, distinguishes fact from inference |

## Interpretation

- **28–32:** strong evaluation
- **22–27:** useful with minor gaps
- **16–21:** partial
- **0–15:** insufficient evidence or correctness

## Evaluation principles

1. A plausible explanation is not evidence.
2. Passing tests are not enough if the tests miss the reported invariant.
3. A large patch is not automatically a better fix.
4. Security review must distinguish data presence from authorization enforcement.
5. Agent and tool output is untrusted until validated against repository behavior.
6. Uncertainty should be stated when evidence is incomplete.
