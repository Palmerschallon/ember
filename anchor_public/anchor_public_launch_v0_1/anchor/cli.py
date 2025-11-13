from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Dict, Optional

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

import uvicorn

from .ledger import Ledger
from .onboarding import maybe_run_first_run_flow

console = Console()


def _parse_meta(meta_str: Optional[str]) -> Dict[str, Any]:
    if not meta_str:
        return {}
    try:
        return json.loads(meta_str)
    except Exception as e:
        raise SystemExit(f"Could not parse --meta as JSON: {e}")


def cmd_add(args: argparse.Namespace) -> None:
    ledger = Ledger()
    maybe_run_first_run_flow(ledger)
    text = args.text or Prompt.ask("Entry")
    meta = _parse_meta(args.meta)
    entry = ledger.add(text, meta)
    console.print("[bold green]Anchored[/] entry:")
    console.print(f"[dim]{entry.ts_utc}[/]  #{entry.id}")
    console.print(entry.text)
    console.print(f"[dim]hash  {entry.hash_hex}[/]")


def cmd_list(args: argparse.Namespace) -> None:
    ledger = Ledger()
    maybe_run_first_run_flow(ledger)
    entries = ledger.list(limit=args.limit)
    table = Table(show_header=True, header_style="bold")
    table.add_column("id", style="dim", width=5)
    table.add_column("timestamp (UTC)", style="dim", width=20)
    table.add_column("preview")
    table.add_column("hash", style="dim", width=18)

    for e in entries:
        preview = e.text.replace("\n", " ")
        if len(preview) > 60:
            preview = preview[:57] + "..."
        table.add_row(
            str(e.id),
            e.ts_utc,
            preview,
            e.hash_hex[:16] + "…",
        )
    console.print(table)


def cmd_verify(args: argparse.Namespace) -> None:
    ledger = Ledger()
    text = args.text or Prompt.ask("Text to verify")
    results = ledger.verify_text(text, at_ts=args.at)
    if not results:
        console.print("[red]No matching anchored entries found.[/]")
        raise SystemExit(1)

    console.print("[green]Verified entries:[/]")
    for e in results:
        console.print(f"- [dim]{e.ts_utc}[/]  id={e.id}  hash={e.hash_hex}")


def cmd_export(args: argparse.Namespace) -> None:
    ledger = Ledger()
    data = ledger.export_jsonl()
    if args.output and args.output != "-":
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(data + "\n")
        console.print(f"[green]Exported to[/] {args.output}")
    else:
        sys.stdout.write(data + "\n")


def cmd_serve(args: argparse.Namespace) -> None:
    from . import server  # noqa: F401
    uvicorn.run(
        "anchor.server:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
        log_level="info",
    )


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="anchor",
        description="Anchor – a local, immutable ledger for your ideas.",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    add_p = sub.add_parser("add", help="Add a new anchored entry")
    add_p.add_argument("text", nargs="?", help="Text to anchor (optional)")
    add_p.add_argument("--meta", help="Optional JSON metadata", default=None)
    add_p.set_defaults(func=cmd_add)

    list_p = sub.add_parser("list", help="List recent entries")
    list_p.add_argument("--limit", type=int, default=20, help="How many to show")
    list_p.set_defaults(func=cmd_list)

    ver_p = sub.add_parser("verify", help="Verify that text exists in the ledger")
    ver_p.add_argument("text", nargs="?", help="Exact text to verify")
    ver_p.add_argument(
        "--at",
        help="Only consider entries at or before this ISO8601 UTC timestamp",
        default=None,
    )
    ver_p.set_defaults(func=cmd_verify)

    exp_p = sub.add_parser("export", help="Export all entries as JSONL")
    exp_p.add_argument(
        "-o",
        "--output",
        help='Output file (or "-" for stdout)',
        default="-",
    )
    exp_p.set_defaults(func=cmd_export)

    srv_p = sub.add_parser("serve", help="Run the local Anchor HTTP API")
    srv_p.add_argument("--host", default="127.0.0.1", help="Bind host")
    srv_p.add_argument("--port", type=int, default=7171, help="Bind port")
    srv_p.add_argument(
        "--reload",
        action="store_true",
        help="Enable auto-reload (dev only)",
    )
    srv_p.set_defaults(func=cmd_serve)

    return p


def main(argv: Optional[list[str]] = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
