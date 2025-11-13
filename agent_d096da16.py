import os

ember5_dir = "/media/palmerschallon/ThePod1/ember5"
if not os.path.exists(ember5_dir):
    os.makedirs(ember5_dir)
    print(f"Created directory: {ember5_dir}")
else:
    print(f"Directory already exists: {ember5_dir}")