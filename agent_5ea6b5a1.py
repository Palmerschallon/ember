with open("/media/palmerschallon/ThePod1/EMBER5_BOOTSTRAP.md", "r") as f:
    bootstrap = f.read()

files_table_schema = bootstrap.split("**Files Table:**")[1].split("**Concepts Table:**")[0].strip()
print(files_table_schema)