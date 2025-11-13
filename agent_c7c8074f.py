import sqlite3

conn = sqlite3.connect("/media/palmerschallon/ThePod1/_mesh/content.db")
c = conn.cursor()

c.execute("PRAGMA table_info(files)")
print("Files table columns:")
for col in c.fetchall():
    print(col[1])
    
conn.close()