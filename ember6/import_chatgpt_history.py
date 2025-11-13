#!/usr/bin/env python3
"""
Import ChatGPT conversation history into Ember's database
"""

import json
import sqlite3
import hashlib
from pathlib import Path
from datetime import datetime

THEPOD_PATH = Path("/media/palmerschallon/ThePod1")
CONVERSATIONS_DB = THEPOD_PATH / "_mesh" / "conversations.db"
CHATGPT_EXPORT = THEPOD_PATH / "ember6/memory/bookshelves/palmers_book/conversations.json"

def init_db():
    """Ensure database schema exists"""
    conn = sqlite3.connect(CONVERSATIONS_DB)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversation_threads (
            id TEXT PRIMARY KEY,
            title TEXT,
            created_at REAL,
            updated_at REAL,
            folder TEXT DEFAULT 'chatgpt_import',
            archived BOOLEAN DEFAULT 0,
            model TEXT,
            message_count INTEGER DEFAULT 0
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversation_messages (
            id TEXT PRIMARY KEY,
            thread_id TEXT,
            role TEXT,
            content TEXT,
            timestamp REAL,
            tool_calls TEXT,
            created_files TEXT,
            FOREIGN KEY (thread_id) REFERENCES conversation_threads(id)
        )
    """)
    
    conn.commit()
    conn.close()

def extract_messages_from_mapping(mapping):
    """Extract messages from ChatGPT's mapping structure"""
    messages = []
    
    # Find root node (has no parent or parent is None)
    roots = [node for node_id, node in mapping.items() 
             if node.get('parent') is None or node.get('parent') == '']
    
    if not roots:
        return messages
    
    # Traverse from root following children
    def traverse(node_id, depth=0):
        if node_id not in mapping or depth > 100:  # Prevent infinite loops
            return
        
        node = mapping[node_id]
        msg = node.get('message')
        
        if msg and msg.get('content'):
            role = msg['content'].get('role', 'user')
            parts = msg['content'].get('parts', [])
            
            if parts and len(parts) > 0:
                # Join all parts into content
                content = '\n'.join(str(part) for part in parts if part)
                
                if content.strip():
                    messages.append({
                        'role': role,
                        'content': content,
                        'timestamp': msg.get('create_time', 0)
                    })
        
        # Follow the first child (main conversation thread)
        children = node.get('children', [])
        if children:
            traverse(children[0], depth + 1)
    
    traverse(roots[0]['id'])
    return messages

def import_conversations():
    """Import ChatGPT conversations into Ember database"""
    print("🔥 Importing ChatGPT history into Ember...")
    print()
    
    # Load ChatGPT export
    print(f"📖 Reading {CHATGPT_EXPORT}...")
    with open(CHATGPT_EXPORT, 'r') as f:
        chatgpt_data = json.load(f)
    
    print(f"   Found {len(chatgpt_data)} conversations")
    print()
    
    # Initialize database
    init_db()
    conn = sqlite3.connect(CONVERSATIONS_DB)
    cursor = conn.cursor()
    
    imported = 0
    skipped = 0
    
    for i, conv in enumerate(chatgpt_data):
        if (i + 1) % 100 == 0:
            print(f"   Processing {i + 1}/{len(chatgpt_data)}...")
        
        conv_id = conv.get('conversation_id', conv.get('id'))
        title = conv.get('title', 'Untitled')
        created_at = conv.get('create_time', 0)
        updated_at = conv.get('update_time', 0)
        model = conv.get('default_model_slug', 'gpt-3.5')
        mapping = conv.get('mapping', {})
        
        # Skip if no messages
        if not mapping:
            skipped += 1
            continue
        
        # Check if already imported
        cursor.execute("SELECT id FROM conversation_threads WHERE id = ?", (conv_id,))
        if cursor.fetchone():
            skipped += 1
            continue
        
        # Extract messages
        messages = extract_messages_from_mapping(mapping)
        
        if not messages:
            skipped += 1
            continue
        
        # Insert conversation thread
        cursor.execute("""
            INSERT INTO conversation_threads 
            (id, title, created_at, updated_at, folder, model, message_count)
            VALUES (?, ?, ?, ?, 'chatgpt_import', ?, ?)
        """, (conv_id, title, created_at, updated_at, model, len(messages)))
        
        # Insert messages
        for msg in messages:
            msg_id = hashlib.md5(f"{conv_id}_{msg['timestamp']}_{msg['content'][:100]}".encode()).hexdigest()
            cursor.execute("""
                INSERT INTO conversation_messages
                (id, thread_id, role, content, timestamp)
                VALUES (?, ?, ?, ?, ?)
            """, (msg_id, conv_id, msg['role'], msg['content'], msg['timestamp']))
        
        imported += 1
    
    conn.commit()
    conn.close()
    
    print()
    print("✅ IMPORT COMPLETE!")
    print()
    print(f"   Imported: {imported} conversations")
    print(f"   Skipped: {skipped} (empty or duplicate)")
    print()
    print(f"💾 Database: {CONVERSATIONS_DB}")
    print()

if __name__ == '__main__':
    import_conversations()

