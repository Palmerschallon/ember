# Example of chunked writing for large content
content_chunks = [
    "# Large Document Example\n\n",
    "This demonstrates how I write large files using Python.\n",
    "Instead of write_file(), I use open() with chunked writing.\n\n",
    "## Benefits:\n",
    "- Handles large content without memory issues\n",
    "- More control over file operations\n",
    "- Can append, modify, or create files\n"
]

# Write chunks to file
output_path = "/media/palmerschallon/ThePod1/ember6/chunked_writing_demo.md"
with open(output_path, 'w') as f:
    for chunk in content_chunks:
        f.write(chunk)

print(f"✅ Wrote chunked content to {output_path}")
print(f"Total chunks written: {len(content_chunks)}")