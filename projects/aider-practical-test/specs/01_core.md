# Spec 01 — core domain and storage

Work only inside `projects/aider-practical-test`.

Create exactly:
- `followup/__init__.py`
- `followup/core.py`
- `followup/storage.py`

Requirements:

1. A follow-up record is a dict with:
   - id: non-empty string
   - customer: non-empty string
   - channel: one of email, whatsapp, phone
   - due_date: YYYY-MM-DD
   - status: pending or done
   - note: string

2. In `core.py`, implement:
   - `validate_record(record) -> None` raising ValueError for invalid input.
   - `new_record(customer, channel, due_date, note="") -> dict`.
   - `mark_done(record) -> dict` returning a new dict without mutating the input.
   - Generate ids with `uuid.uuid4().hex`.

3. In `storage.py`, implement:
   - `load_records(path) -> list[dict]`: missing file returns [].
   - `save_records(path, records) -> None`: validate every record and write UTF-8 JSON with indent=2.
   - Use pathlib.
   - Parent directory should be created if needed.

Use only the Python standard library.

Do not create tests or CLI yet.

Verification:
`python3 -m py_compile followup/__init__.py followup/core.py followup/storage.py`

At the end respond only:
STATUS: PASS or FAIL
FILES: list changed files
