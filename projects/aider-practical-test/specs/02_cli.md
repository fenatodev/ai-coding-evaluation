# Spec 02 — CLI

Work only inside `projects/aider-practical-test`.

Assume spec 01 is complete.

Create exactly:
- `followup/cli.py`
- `followup/__main__.py`

Implement an argparse CLI runnable as:

`python3 -m followup --db data/followups.json <command>`

Commands:

1. `add`
   - required: `--customer`, `--channel`, `--due`
   - optional: `--note`
   - append one validated pending record
   - print only the created id

2. `list`
   - optional `--status pending|done`
   - output one compact line per record:
     `<id> | <status> | <due_date> | <channel> | <customer>`
   - sort by due_date then customer

3. `done <id>`
   - mark the matching record done
   - unknown id must print an error to stderr and exit 2

4. `stats`
   - print exactly:
     `pending=<n> done=<n> total=<n>`

Use only standard library modules.

Do not create tests yet.

Verification:
`python3 -m followup --help`

At the end respond only:
STATUS: PASS or FAIL
FILES: list changed files
