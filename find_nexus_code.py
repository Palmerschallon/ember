import os

# Check the nexus directory
nexus_path = 'nexus'
if os.path.exists(nexus_path) and os.path.isdir(nexus_path):
    nexus_contents = os.listdir(nexus_path)
    print(f"Contents of {nexus_path}/ directory:")
    for item in sorted(nexus_contents):
        full_path = os.path.join(nexus_path, item)
        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            print(f"FILE: {item} ({size} bytes)")
        else:
            print(f"DIR:  {item}/")
else:
    print(f"Directory {nexus_path} not found")

# Let's also check if there's any file that looks like nexus code in the main directory
# by looking for files with "nexus" content or similar structure
print("\nSearching for files that might contain Nexus code...")
for filename in os.listdir('.'):
    if filename.endswith('.py') and os.path.isfile(filename):
        try:
            with open(filename, 'r') as f:
                content = f.read()
                if 'nexus' in content.lower() or 'synthesis' in content.lower():
                    print(f"{filename}: {len(content)} chars - likely contains nexus-related code")
        except:
            pass