# Spec 03 — tests

Work only inside `projects/aider-practical-test`.

Assume specs 01 and 02 are complete.

Create exactly:
- `tests/__init__.py`
- `tests/test_core.py`
- `tests/test_cli.py`

Use `unittest` only.

Cover at minimum:

Core:
- valid record creation
- invalid channel
- invalid date format
- mark_done does not mutate input
- missing storage file returns []
- save/load round trip

CLI:
- add creates a persisted record
- list filters by status
- done changes status
- done with unknown id exits 2
- stats counts pending/done/total

Use temporary directories/files; do not write test data into the project tree.

Run:
`python3 -m unittest -v`

If anything fails, fix the implementation or tests and rerun until green.

At the end respond only:
STATUS: PASS or FAIL
TESTS: number passing
FILES: list changed files
