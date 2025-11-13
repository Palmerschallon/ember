import os
# Check what files actually exist
files = os.listdir('.')
nexus_files = [f for f in files if 'nexus' in f.lower()]
print("Nexus files found:", nexus_files)

# Try to read the file
if 'nexus_gen3.py' in files:
    with open('nexus_gen3.py', 'r') as f:
        content = f.read()
    print(f"File size: {len(content)} characters")
    print("First 500 characters:")
    print(content[:500])
else:
    print("nexus_gen3.py not found in current directory")