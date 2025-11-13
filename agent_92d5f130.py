import os

folders = [
 "Ember3",
 "bookshelves",
 "memory", 
 "ember_mind",
 "essential",
 "_history",
 "_intake",
 "_mesh",
 "_state", 
 "_legacy",
 ".Trash-1000",
 "dreams",
 "ember_drafts",
 "ember_minimal",
 "ember_data",
 ".mycelium_update",
 "templates",
 "models",
 "_patterns",
 "__pycache__",
 "medusa",
 "logs",
 "_archive_merged", 
 "ember5",
 "ember6_nested",
 "node_modules",
 "_archive_old",
 "examples"
]

for folder in folders:
    subfolder = os.path.join("/media/palmerschallon/ThePod1/", folder)
    print(f"Checking {subfolder}...")
    if os.path.exists(subfolder):
        subfolders = os.listdir(subfolder)
        if "omegas" in subfolders:
            print(f"Found omegas in {subfolder}")
            break
    else:
        print(f"{subfolder} does not exist")