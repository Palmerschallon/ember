from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt

from .config import get_db_path
from .ledger import Ledger

console = Console()


INTRO_TEXT = """[bold]Welcome to Anchor.[/]

This is a local ledger for your ideas.

• Everything you write is stored on [bold]this machine[/].  
• The file lives at:  
  [dim]{db_path}[/]
• Entries are linked together so the history can't be quietly rewritten.
• Anchor does [bold]not[/] use the network, cloud, or any token system.
"""


def maybe_run_first_run_flow(ledger: Ledger) -> None:
    if not ledger.is_empty():
        return

    db_path = get_db_path()
    panel = Panel(
        INTRO_TEXT.format(db_path=db_path),
        title="[bold red]ANCHOR[/]",
        border_style="white",
    )
    console.print(panel)

    if Confirm.ask("Anchor your first entry now?", default=True):
        text = Prompt.ask("First entry")
        if text.strip():
            ledger.add(text, meta={"origin": "first-run"})
            console.print("[green]Anchored.[/] You can see it with [bold]anchor list[/].")
        else:
            console.print("[dim]Skipped first entry.[/]")
