# Pi Practical Test

A CLI tool for managing customer follow-ups stored in JSON. Built with Python standard library only.

## Goal

Build a CLI that manages customer follow-ups stored in JSON.

## Execution order

Run the specs one at a time, in order:

1. `specs/01_core.md`
2. `specs/02_cli.md`
3. `specs/03_tests.md`
4. `specs/04_finish.md`

Do not execute all specs in one prompt. Each spec is intentionally small to keep local-model context and generation cost bounded.

## Python Requirement

Python 3.8 or higher

## CLI Commands

### Add a new follow-up
```bash
python3 -m followup --db sample/followups.json add --customer "John Doe" --channel email --due 2024-02-15 --note "Follow up on invoice"
```

### List follow-ups (with optional status filter)
```bash
python3 -m followup --db sample/followups.json list
python3 -m followup --db sample/followups.json list --status pending
```

### Mark a follow-up as done
```bash
python3 -m followup --db sample/followups.json done abc123def456
```

### Show statistics
```bash
python3 -m followup --db sample/followups.json stats
```

## Running Tests

```bash
python3 -m unittest -v
```

## Project Layout

```
projects/aider-practical-test/
├── README.md
├── followup/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── core.py
│   └── storage.py
├── sample/
│   └── followups.json
├── tests/
│   ├── __init__.py
│   ├── test_cli.py
│   └── test_core.py
└── specs/
    ├── 01_core.md
    ├── 02_cli.md
    ├── 03_tests.md
    └── 04_finish.md
```

## Constraints

- Python standard library only.
- No sudo.
- No package installation.
- Work only inside `projects/aider-practical-test`.
- Prefer small edits.
- Run the verification command at the end of each spec.
