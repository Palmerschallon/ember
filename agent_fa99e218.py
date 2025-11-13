import os

ember5_files = os.listdir("/media/palmerschallon/ThePod1/ember5")
print(f"Found {len(ember5_files)} files in /ember5:")
print("\n".join(ember5_files))