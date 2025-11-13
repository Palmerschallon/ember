import os

# Define the directory you want to search
search_directory = '/media/palmerschallon/ThePod1/'

# Define the keyword you want to search for
keyword = 'omega'

# Walk through all files and folders within directory
for dirpath, dirnames, files in os.walk(search_directory):
    # Look for the keyword in each file name
    for file_name in files:
        # If the keyword is found, print absolute path
        if keyword.lower() in file_name.lower():
            print(os.path.abspath(os.path.join(dirpath, file_name)))