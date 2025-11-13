import os

search_terms = ["dream", "dreaming", "dreams"]

def search_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") or file.endswith(".md") or file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.read()
                    for term in search_terms:
                        if term in content.lower():
                            print(f"Found '{term}' in {file_path}")
                            print(f"Context: ...{content[content.lower().find(term)-50:content.lower().find(term)+50]}...")
                            print()

search_files("/media/palmerschallon/ThePod1/ember5")