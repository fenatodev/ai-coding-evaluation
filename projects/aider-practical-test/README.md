# Aider Practical Test

Small stdlib-only Python project designed to test a local Qwen 9B + Aider workflow.

## Goal

Build a CLI that manages customer follow-ups stored in JSON.

## Execution order

Run the specs one at a time, in order:

1. `specs/01_core.md`
2. `specs/02_cli.md`
3. `specs/03_tests.md`
4. `specs/04_finish.md`

Do not execute all specs in one prompt. Each spec is intentionally small to keep local-model context and generation cost bounded.

## Constraints

- Python standard library only.
- No sudo.
- No package installation.
- Work only inside `projects/aider-practical-test`.
- Prefer small edits.
- Run the verification command at the end of each spec.
