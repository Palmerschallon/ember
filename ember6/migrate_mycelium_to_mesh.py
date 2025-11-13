#!/usr/bin/env python3
"""
Migrate conversations from mycelium database to mesh database
"""

import sqlite3
import hashlib
from pathlib import Path
from datetime import datetime

THEPOD_PATH = Path("/media/palmerschallon/ThePod1")
MYCELIUM_DB = THEPOD_PATH / "ember6/mycelium/conversations.db"
MESH_DB = THEPOD_PATH / "_mesh/conversations.db"

def migrate():
    print("🔥 Migrating mycelium conversations to mesh...")
    print()
    
    # Connect to both databases
    mycelium = sqlite3.connect(MYCELIUM_DB)
    mesh = sqlite3.connect(MESH_DB)
    
    mycelium_cursor = mycelium.cursor()
    mesh_cursor = mesh.cursor()
    
    # Get conversations from mycelium
    mycelium_cursor.execute("SELECT * FROM conversations")
    conversations = mycelium_cursor.fetchall()
    
    print(f"Found {len(conversations)} conversations in mycelium")
    
    migrated = 0
    
    for conv in conversations:
        conv_id, title, created_at, updated_at = conv
        
        # Get messages for this conversation
        mycelium_cursor.execute("SELECT * FROM messages WHERE conversation_id = ?", (conv_id,))
        messages = mycelium_cursor.fetchall()
        
        # Convert datetime strings to timestamps
        try:
            created_ts = datetime.fromisoformat(created_at.replace('Z', '+00:00')).timestamp()
            updated_ts = datetime.fromisoformat(updated_at.replace('Z', '+00:00')).timestamp()
        except:
            created_ts = datetime.now().timestamp()
            updated_ts = created_ts
        
        # Insert into mesh
        try:
            mesh_cursor.execute("""
                INSERT OR REPLACE INTO conversation_threads 
                (id, title, created_at, updated_at, folder, model, message_count)
                VALUES (?, ?, ?, ?, 'recent', 'gpt-4', ?)
            """, (conv_id, title, created_ts, updated_ts, len(messages)))
            
            # Insert messages
            for msg in messages:
                msg_id, _, role, content, model, msg_created = msg
                
                try:
                    msg_ts = datetime.fromisoformat(msg_created.replace('Z', '+00:00')).timestamp()
                except:
                    msg_ts = created_ts
                
                msg_hash = hashlib.md5(f"{conv_id}_{msg_id}".encode()).hexdigest()
                
                mesh_cursor.execute("""
                    INSERT OR REPLACE INTO conversation_messages
                    (id, thread_id, role, content, timestamp)
                    VALUES (?, ?, ?, ?, ?)
                """, (msg_hash, conv_id, role, content, msg_ts))
            
            migrated += 1
            print(f"  ✅ {title} ({len(messages)} messages)")
            
        except Exception as e:
            print(f"  ❌ Failed to migrate {title}: {e}")
    
    mesh.commit()
    
    mycelium.close()
    mesh.close()
    
    print()
    print(f"✅ Migrated {migrated}/{len(conversations)} conversations!")
    print()

if __name__ == '__main__':
    migrate()

