#!/usr/bin/env python3
"""
ChromaDB Semantic Mesh - Modern vector database
Replaces custom SQLite with proper semantic search
"""

import chromadb
from chromadb.config import Settings
from pathlib import Path
import json

THEPOD_PATH = Path("/media/palmerschallon/ThePod1")
CHROMA_PATH = THEPOD_PATH / "_mesh" / "chromadb"

# Initialize ChromaDB client
client = chromadb.PersistentClient(
    path=str(CHROMA_PATH),
    settings=Settings(anonymized_telemetry=False)
)

# Get or create collections
files_collection = client.get_or_create_collection(
    name="files",
    metadata={"description": "All files on ThePod"}
)

conversations_collection = client.get_or_create_collection(
    name="conversations",
    metadata={"description": "Chat history with Ember"}
)

concepts_collection = client.get_or_create_collection(
    name="concepts",
    metadata={"description": "Extracted concepts and knowledge"}
)

def store_file(filepath, content, metadata=None):
    """Store a file in the mesh"""
    if metadata is None:
        metadata = {}
    
    metadata["filepath"] = str(filepath)
    metadata["type"] = "file"
    
    files_collection.add(
        documents=[content],
        metadatas=[metadata],
        ids=[str(filepath)]
    )

def store_conversation(message, role, metadata=None):
    """Store a conversation turn"""
    if metadata is None:
        metadata = {}
    
    metadata["role"] = role
    metadata["type"] = "conversation"
    
    import hashlib
    import time
    msg_id = hashlib.md5(f"{message}{time.time()}".encode()).hexdigest()
    
    conversations_collection.add(
        documents=[message],
        metadatas=[metadata],
        ids=[msg_id]
    )

def recall_from_mesh(query, limit=5):
    """
    Semantic search across the mesh
    Returns most relevant content based on meaning, not keywords
    """
    results = []
    
    # Search files
    file_results = files_collection.query(
        query_texts=[query],
        n_results=limit
    )
    
    for i, doc in enumerate(file_results["documents"][0]):
        results.append({
            "type": "file",
            "name": file_results["metadatas"][0][i].get("filepath", "Unknown"),
            "content": doc,
            "distance": file_results["distances"][0][i]
        })
    
    # Search conversations
    conv_results = conversations_collection.query(
        query_texts=[query],
        n_results=limit
    )
    
    for i, doc in enumerate(conv_results["documents"][0]):
        results.append({
            "type": "conversation",
            "name": f"Conversation ({conv_results['metadatas'][0][i].get('role', 'unknown')})",
            "content": doc,
            "distance": conv_results["distances"][0][i]
        })
    
    # Sort by distance (lower = more similar)
    results.sort(key=lambda x: x["distance"])
    
    return results[:limit]

def get_mesh_stats():
    """Get statistics about the mesh"""
    return {
        "files": files_collection.count(),
        "conversations": conversations_collection.count(),
        "concepts": concepts_collection.count(),
        "total": files_collection.count() + conversations_collection.count() + concepts_collection.count()
    }

def migrate_from_sqlite():
    """
    Migrate data from old SQLite mesh to ChromaDB
    Run this once to transfer existing data
    """
    import sqlite3
    
    old_db = THEPOD_PATH / "_mesh" / "content.db"
    if not old_db.exists():
        print("No old database to migrate")
        return
    
    print("🔄 Migrating from SQLite to ChromaDB...")
    
    conn = sqlite3.connect(old_db)
    cursor = conn.cursor()
    
    # Migrate files
    cursor.execute("SELECT current_path, full_content, content_preview FROM files")
    files = cursor.fetchall()
    print(f"  Migrating {len(files)} files...")
    
    for path, full_content, preview in files:
        try:
            content = full_content or preview or ""
            store_file(path, content, {"migrated": True})
        except Exception as e:
            print(f"  Failed to migrate {path}: {e}")
    
    # Migrate conversations
    cursor.execute("SELECT content, role FROM conversations")
    convs = cursor.fetchall()
    print(f"  Migrating {len(convs)} conversations...")
    
    for content, role in convs:
        try:
            store_conversation(content or "", role or "unknown", {"migrated": True})
        except Exception as e:
            print(f"  Failed to migrate conversation: {e}")
    
    conn.close()
    print("✅ Migration complete!")
    print(f"📊 New mesh stats: {get_mesh_stats()}")

if __name__ == "__main__":
    print("🧠 ChromaDB Semantic Mesh")
    print(f"📍 Location: {CHROMA_PATH}")
    print(f"📊 Stats: {get_mesh_stats()}")
    print("\nRun migrate_from_sqlite() to transfer old data")

