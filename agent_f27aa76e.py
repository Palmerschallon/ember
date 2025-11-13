import sqlite3

conn = sqlite3.connect("/media/palmerschallon/ThePod1/_mesh/content.db")
c = conn.cursor()

def search_concepts(query):
    c.execute("SELECT * FROM concepts WHERE concept LIKE ?", [f"%{query}%"])
    return c.fetchall()

def search_files(query):
    c.execute("SELECT * FROM files WHERE file_name LIKE ? OR full_content LIKE ?", [f"%{query}%", f"%{query}%"])
    return c.fetchall()
    
concept_results = search_concepts("omega")
file_results = search_files("omega")

print(f"Found {len(concept_results)} matching concepts:")
for row in concept_results:
    print(f"- {row[1]} (from file hash {row[2]})")
    
print(f"\nFound {len(file_results)} matching files:")
for row in file_results:
    print(f"- {row[2]} ({row[3]} bytes)")
    
conn.close()