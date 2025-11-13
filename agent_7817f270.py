import os

ui_dirs = []
for dirpath, dirnames, filenames in os.walk("/media/palmerschallon/ThePod1"):
    if "ui" in dirpath.lower():
        ui_dirs.append(dirpath)

print(f"Potential UI directories: {ui_dirs}")