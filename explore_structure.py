import os

# Get all files and folders in current directory
items = os.listdir('.')
print("All items in current directory:")
for item in sorted(items):
    if os.path.isfile(item):
        size = os.path.getsize(item)
        print(f"FILE: {item} ({size} bytes)")
    else:
        print(f"DIR:  {item}/")

print("\n" + "="*50)

# Check if there are any files with nexus in the name
nexus_files = []
for item in items:
    if 'nexus' in item.lower() and os.path.isfile(item):
        nexus_files.append(item)
        
print("Found nexus files:", nexus_files)

# Let's also check for the largest Python file (likely our main code)
py_files = [(f, os.path.getsize(f)) for f in items if f.endswith('.py') and os.path.isfile(f)]
py_files.sort(key=lambda x: x[1], reverse=True)
print("\nLargest Python files:")
for name, size in py_files[:5]:
    print(f"{name}: {size} bytes")