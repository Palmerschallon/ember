#!/usr/bin/env python3
"""
Conversation History System - ChatGPT Style
Manages persistent conversation threads with titles, folders, and search
"""

import sqlite3
import json
import time
import hashlib
from pathlib import Path
from datetime import datetime

THEPOD_PATH = Path("/media/palmerschallon/ThePod1")
CONVERSATIONS_DB = THEPOD_PATH / "_mesh" / "conversations.db"

def init_conversation_db():
    """Initialize conversation database with schema"""
    conn = sqlite3.connect(CONVERSATIONS_DB)
    cursor = conn.cursor()
    
    # Conversation threads table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversation_threads (
            id TEXT PRIMARY KEY,
            title TEXT,
            created_at REAL,
            updated_at REAL,
            folder TEXT DEFAULT 'general',
            archived BOOLEAN DEFAULT 0,
            model TEXT,
            message_count INTEGER DEFAULT 0
        )
    """)
    
    # Messages table
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
    
    # Indexes
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_thread_updated 
        ON conversation_threads(updated_at DESC)
    """)
    
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_message_thread 
        ON conversation_messages(thread_id, timestamp)
    """)
    
    conn.commit()
    conn.close()
    print(f"✅ Conversation database initialized: {CONVERSATIONS_DB}")

def create_conversation(title=None, model="openai", folder="general"):
    """Create a new conversation thread"""
    conn = sqlite3.connect(CONVERSATIONS_DB)
    cursor = conn.cursor()
    
    conv_id = hashlib.md5(f"{time.time()}".encode()).hexdigest()
    now = time.time()
    
    cursor.execute("""
        INSERT INTO conversation_threads 
        (id, title, created_at, updated_at, folder, model, message_count)
        VALUES (?, ?, ?, ?, ?, ?, 0)
    """, (conv_id, title or "New conversation", now, now, folder, model))
    
    conn.commit()
    conn.close()
    
    return conv_id

def add_message(thread_id, role, content, tool_calls=None, created_files=None):
    """Add a message to a conversation"""
    conn = sqlite3.connect(CONVERSATIONS_DB)
    cursor = conn.cursor()
    
    msg_id = hashlib.md5(f"{thread_id}{time.time()}{role}".encode()).hexdigest()
    now = time.time()
    
    cursor.execute("""
        INSERT INTO conversation_messages 
        (id, thread_id, role, content, timestamp, tool_calls, created_files)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        msg_id,
        thread_id,
        role,
        content,
        now,
        json.dumps(tool_calls) if tool_calls else None,
        json.dumps(created_files) if created_files else None
    ))
    
    # Update thread
    cursor.execute("""
        UPDATE conversation_threads 
        SET updated_at = ?, message_count = message_count + 1
        WHERE id = ?
    """, (now, thread_id))
    
    conn.commit()
    conn.close()
    
    return msg_id

def get_conversation(thread_id):
    """Get a conversation with all messages"""
    conn = sqlite3.connect(CONVERSATIONS_DB)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Get thread info
    cursor.execute("""
        SELECT * FROM conversation_threads WHERE id = ?
    """, (thread_id,))
    thread = cursor.fetchone()
    
    if not thread:
        conn.close()
        return None
    
    # Get messages
    cursor.execute("""
        SELECT * FROM conversation_messages 
        WHERE thread_id = ? 
        ORDER BY timestamp ASC
    """, (thread_id,))
    messages = cursor.fetchall()
    
    conn.close()
    
    return {
        "thread": dict(thread),
        "messages": [dict(m) for m in messages]
    }

def list_conversations(folder=None, archived=False, limit=50):
    """List conversations (most recent first)"""
    conn = sqlite3.connect(CONVERSATIONS_DB)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    query = """
        SELECT * FROM conversation_threads 
        WHERE archived = ?
    """
    params = [1 if archived else 0]
    
    if folder:
        query += " AND folder = ?"
        params.append(folder)
    
    query += " ORDER BY updated_at DESC LIMIT ?"
    params.append(limit)
    
    cursor.execute(query, params)
    threads = cursor.fetchall()
    
    conn.close()
    
    return [dict(t) for t in threads]

def search_conversations(query):
    """Search conversations by content"""
    conn = sqlite3.connect(CONVERSATIONS_DB)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Search in thread titles and message content
    cursor.execute("""
        SELECT DISTINCT t.* 
        FROM conversation_threads t
        LEFT JOIN conversation_messages m ON t.id = m.thread_id
        WHERE t.title LIKE ? OR m.content LIKE ?
        ORDER BY t.updated_at DESC
        LIMIT 20
    """, (f"%{query}%", f"%{query}%"))
    
    threads = cursor.fetchall()
    conn.close()
    
    return [dict(t) for t in threads]

def update_conversation_title(thread_id, title):
    """Update conversation title"""
    conn = sqlite3.connect(CONVERSATIONS_DB)
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE conversation_threads 
        SET title = ?, updated_at = ?
        WHERE id = ?
    """, (title, time.time(), thread_id))
    
    conn.commit()
    conn.close()

def delete_conversation(thread_id):
    """Delete a conversation and all its messages"""
    conn = sqlite3.connect(CONVERSATIONS_DB)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM conversation_messages WHERE thread_id = ?", (thread_id,))
    cursor.execute("DELETE FROM conversation_threads WHERE id = ?", (thread_id,))
    
    conn.commit()
    conn.close()

def generate_title_from_message(first_message):
    """Generate a conversation title from the first message"""
    # Simple title generation (can be improved with GPT later)
    words = first_message.split()[:8]
    title = " ".join(words)
    if len(first_message.split()) > 8:
        title += "..."
    return title

if __name__ == "__main__":
    # Initialize database
    init_conversation_db()
    
    # Test
    print("\n🧪 Testing conversation system...")
    
    conv_id = create_conversation(title="Test Conversation", model="gpt-4")
    print(f"Created conversation: {conv_id}")
    
    add_message(conv_id, "user", "Hello, can you help me?")
    add_message(conv_id, "assistant", "Of course! What do you need help with?")
    
    conv = get_conversation(conv_id)
    print(f"\nConversation '{conv['thread']['title']}':")
    for msg in conv['messages']:
        print(f"  {msg['role']}: {msg['content'][:50]}...")
    
    conversations = list_conversations()
    print(f"\n📋 Total conversations: {len(conversations)}")
    
    print("\n✅ Conversation system working!")

