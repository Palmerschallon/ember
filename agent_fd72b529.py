import os

ember5_dir = "/media/palmerschallon/ThePod1/ember5"
os.system(f"sudo chown -R $USER:$USER {ember5_dir}")
os.system(f"sudo chmod -R 777 {ember5_dir}")
print("Updated ownership and permissions on ember5 directory")