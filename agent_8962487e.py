import os

search_terms = ["omega", "map"]

for dirpath, dirnames, filenames in os.walk("/media/palmerschallon/ThePod1"):
    for filename in filenames:
        if all(term in filename.lower() for term in search_terms):
            print(f"Possible match: {os.path.join(dirpath, filename)}")