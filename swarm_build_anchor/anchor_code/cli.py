#!/usr/bin/env python3
"""
Anchor CLI - Command line interface for the eternal ledger
"""

import click
import json
from pathlib import Path
from database import AnchorDB
from datetime import datetime

DEFAULT_DB = Path.home() / ".anchor" / "ledger.db"

@click.group()
@click.option('--db-path', default=DEFAULT_DB, type=Path, help='Path to Anchor database')
@click.pass_context
def cli(ctx, db_path):
    """Anchor - Where memories become eternal"""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    ctx.obj = AnchorDB(db_path)

@cli.command()
@click.argument('content')
@click.option('--agent', default='human', help='Agent ID making the anchor')
@click.option('--metadata', type=json.loads, help='Additional metadata as JSON')
def drop(content, agent, metadata):
    """Drop an anchor - preserve something forever"""
    db = click.get_current_context().obj
    anchor_hash = db.anchor(agent, content, metadata)
    click.echo(f"⚓ Anchored: {anchor_hash}")

@cli.command()
@click.argument('hash')
def retrieve(hash):
    """Retrieve an anchor by its hash"""
    db = click.get_current_context().obj
    anchor = db.retrieve(hash)
    if anchor:
        click.echo(json.dumps(anchor, indent=2))
    else:
        click.echo(f"No anchor found with hash: {hash}")

@cli.command()
@click.option('--limit', default=10, help='Number of recent anchors to show')
def chain(limit):
    """View the chain of anchors"""
    db = click.get_current_context().obj
    anchors = db.get_chain(limit)
    
    for anchor in anchors:
        timestamp = datetime.fromtimestamp(anchor['timestamp'])
        click.echo(f"⚓ {anchor['hash'][:8]}... by {anchor['agent_id']} at {timestamp}")
        click.echo(f"   {anchor['content'][:60]}...")
        click.echo()

if __name__ == '__main__':
    cli()
