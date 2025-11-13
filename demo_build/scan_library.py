#!/usr/bin/env python3
"""
BOOKSHELF SCANNER
Scans all bookshelves and creates an interactive library
"""

from pathlib import Path
import json

ESSENTIAL = Path("/media/palmerschallon/ThePod1/essential/bookshelves")

print("📚 Scanning bookshelves...")

library = {
    "shelves": [],
    "total_books": 0,
    "total_authors": 0
}

# Scan each shelf
for shelf in sorted(ESSENTIAL.iterdir()):
    if not shelf.is_dir():
        continue
    
    books = []
    for book in shelf.rglob("*.md"):
        books.append({
            "title": book.name.replace('.md', '').replace('_', ' ').title(),
            "path": str(book.relative_to(Path("/media/palmerschallon/ThePod1"))),
            "size": book.stat().st_size,
            "modified": book.stat().st_mtime
        })
    
    if books:
        library["shelves"].append({
            "name": shelf.name.replace('_', ' ').title(),
            "slug": shelf.name,
            "book_count": len(books),
            "books": sorted(books, key=lambda x: x['modified'], reverse=True)
        })
        library["total_books"] += len(books)

library["total_authors"] = len(library["shelves"])

# Save
output = Path("/media/palmerschallon/ThePod1/demo_build/library_data.json")
output.write_text(json.dumps(library, indent=2))

print(f"\n✅ Library scanned!")
print(f"   Authors: {library['total_authors']}")
print(f"   Books: {library['total_books']}")
print(f"   Saved to: {output}")

# Print notable shelves
print("\n📖 Notable shelves:")
for shelf in library["shelves"][:10]:
    print(f"   - {shelf['name']}: {shelf['book_count']} books")

