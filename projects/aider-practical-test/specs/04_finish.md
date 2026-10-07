# Spec 04 — sample, docs and final validation

Work only inside `projects/aider-practical-test`.

Assume specs 01–03 are complete.

Create:
- `sample/followups.json`

The sample must contain 4 valid records:
- at least 2 pending
- at least 1 done
- at least 2 different channels

Update `README.md` with:
- what the project does
- Python requirement
- four CLI examples: add, list, done, stats
- test command
- project layout

Then run all of these:

1. `python3 -m unittest -v`
2. `python3 -m followup --db sample/followups.json stats`
3. `python3 -m followup --db sample/followups.json list`

Fix any error and rerun until all commands succeed.

Do not install packages.

At the end respond only:
STATUS: PASS or FAIL
TESTS: number passing
FILES: list changed files
