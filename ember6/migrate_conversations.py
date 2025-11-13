#!/usr/bin/env python3
"""
Migrate conversations from old ember5 format to ember6 format
"""
import sqlite3
from pathlib import Path
from datetime import datetime

OLD_DB = "/media/palmerschallon/ThePod1/_mesh/conversations.db"
NEW_DB = "/media/palmerschallon/ThePod1/ember6/mycelium/conversations.db"

def migrate():
    print("🔄 Migrating conversations from ember5 to ember6...")
    print()
    
    # Connect to both databases
    old_conn = sqlite3.connect(OLD_DB)
    new_conn = sqlite3.connect(NEW_DB)
    
    old_cur = old_conn.cursor()
    new_cur = new_conn.cursor()
    
    # Get all old threads
    old_cur.execute("SELECT id, title, created_at, updated_at FROM conversation_threads ORDER BY created_at")
    threads = old_cur.fetchall()
    
    print(f"Found {len(threads)} conversations to migrate")
    print()
    
    migrated = 0
    for thread_id, title, created_at, updated_at in threads:
        # Check if already migrated
        new_cur.execute("SELECT id FROM conversations WHERE id = ?", (thread_id,))
        if new_cur.fetchone():
            print(f"⏭️  Skipping '{title}' (already migrated)")
            continue
        
        # Convert timestamp
        created_iso = datetime.fromtimestamp(created_at).isoformat() if created_at else datetime.now().isoformat()
        updated_iso = datetime.fromtimestamp(updated_at).isoformat() if updated_at else created_iso
        
        # Insert conversation
        new_cur.execute("""
            INSERT INTO conversations (id, title, created_at, updated_at)
            VALUES (?, ?, ?, ?)
        """, (thread_id, title, created_iso, updated_iso))
        
        # Get messages for this thread
        old_cur.execute("""
            SELECT id, role, content, timestamp 
            FROM conversation_messages 
            WHERE thread_id = ? 
            ORDER BY timestamp
        """, (thread_id,))
        messages = old_cur.fetchall()
        
        # Insert messages
        for msg_id, role, content, timestamp in messages:
            ts_iso = datetime.fromtimestamp(timestamp).isoformat() if timestamp else datetime.now().isoformat()
            new_cur.execute("""
                INSERT INTO messages (conversation_id, role, content, created_at, model)
                VALUES (?, ?, ?, ?, ?)
            """, (thread_id, role, content, ts_iso, 'unknown'))
        
        print(f"✅ Migrated '{title}' ({len(messages)} messages)")
        migrated += 1
    
    new_conn.commit()
    old_conn.close()
    new_conn.close()
    
    print()
    print(f"🎉 Migration complete! Migrated {migrated} conversations")

if __name__ == '__main__':
    migrate()

