"""CLI implementation for followup commands."""

import argparse
import sys
from typing import Optional

from .core import new_record, validate_record, mark_record_done
from .storage import load_records, save_records


VALID_CHANNELS = {"email", "whatsapp", "phone"}


def add(args: argparse.Namespace) -> int:
    """Add a new follow-up record."""
    try:
        validate_record({
            "customer": args.customer,
            "channel": args.channel,
            "due_date": args.due,
            "status": "pending",
            "note": args.note or "",
        })
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    records = load_records(args.db)
    new_record_obj = new_record(
        customer=args.customer,
        channel=args.channel,
        due_date=args.due,
        note=args.note or ""
    )
    records.append(new_record_obj)
    save_records(args.db, records)

    print(new_record_obj["id"])
    return 0


def list_records(args: argparse.Namespace) -> int:
    """List follow-up records."""
    records = load_records(args.db)

    # Filter by status if specified
    if args.status:
        records = [r for r in records if r.get("status") == args.status]

    # Sort by due_date, then customer
    sorted_records = sorted(records, key=lambda r: (r.get("due_date", ""), r.get("customer", "")))

    for record in sorted_records:
        print(f"{record['id']} | {record['status']} | {record['due_date']} | {record['channel']} | {record['customer']}")

    return 0


def done(args: argparse.Namespace) -> int:
    """Mark a follow-up record as done."""
    records = load_records(args.db)

    # Find the record by id
    for record in records:
        if record.get("id") == args.id:
            updated_record = mark_record_done(record)
            records.remove(record)
            records.append(updated_record)
            save_records(args.db, records)
            print(updated_record["id"])
            return 0

    print("Error: Record not found", file=sys.stderr)
    return 2


def stats(args: argparse.Namespace) -> int:
    """Print statistics."""
    records = load_records(args.db)

    pending_count = sum(1 for r in records if r.get("status") == "pending")
    done_count = sum(1 for r in records if r.get("status") == "done")
    total_count = len(records)

    print(f"pending={pending_count} done={done_count} total={total_count}")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Followup CLI")
    parser.add_argument("--db", required=True, help="Database file path")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new follow-up")
    add_parser.add_argument("--customer", required=True, help="Customer name")
    add_parser.add_argument("--channel", required=True, help="Contact channel (email, whatsapp, phone)")
    add_parser.add_argument("--due", required=True, help="Due date in YYYY-MM-DD format")
    add_parser.add_argument("--note", default="", help="Optional note")

    # list command
    list_parser = subparsers.add_parser("list", help="List follow-ups")
    list_parser.add_argument("--status", choices=["pending", "done"], help="Filter by status")

    # done command
    done_parser = subparsers.add_parser("done", help="Mark a follow-up as done")
    done_parser.add_argument("id", help="Record ID")

    # stats command
    stats_parser = subparsers.add_parser("stats", help="Show statistics")

    args = parser.parse_args()

    if args.command == "add":
        sys.exit(add(args))
    elif args.command == "list":
        sys.exit(list_records(args))
    elif args.command == "done":
        sys.exit(done(args))
    elif args.command == "stats":
        sys.exit(stats(args))


if __name__ == "__main__":
    main()
