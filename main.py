import os
import re
from pathlib import Path

def define_env(env):
    @env.macro
    def list_function_files(category_path):
        docs_path = Path(env.conf['docs_dir'])
        full_path = docs_path / category_path

        if not full_path.exists():
            return f"<!-- Directory {category_path} not found -->"

        md_files = []
        for file_path in full_path.glob("*.md"):
            if file_path.name.lower() != "index.md":
                md_files.append(file_path)

        if not md_files:
            return "<!-- No function files found -->"

        # Sort files alphabetically
        md_files.sort(key=lambda x: x.name.lower())

        # Generate markdown list
        result = []
        for file_path in md_files:
            # Extract title from filename (remove .md and convert CamelCase to readable)
            filename = file_path.stem
            title = convert_camel_case(filename)

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Look for first # heading
                    title_match = re.search(r'^#\s+(.+?)(?:\s*\{[^}]*\})?\s*$', content, re.MULTILINE)
                    if title_match:
                        actual_title = title_match.group(1).strip('*').strip()
                        if actual_title:
                            title = actual_title
            except Exception:
                pass  # Fall back to filename-based title

            # Create relative link
            if category_path.startswith("Functions/"):
                # For Functions subdirectories, include the subdirectory name
                subdirectory = category_path[10:]  # Remove "Functions/" prefix
                relative_path = f"{subdirectory}/{file_path.name}"
            else:
                relative_path = file_path.name

            # For the first entry, do not prepend the dash
            if not result:
                result.append(f"[{title}]({relative_path})")
            else:
                result.append(f" - [{title}]({relative_path})")

        return "\t \n".join(result)

    @env.macro
    def ctrl_f_tip():
        return """!!! tip
    Use `Ctrl + F` via your browser or the search bar on the left to quickly
    find the functions you're looking for. You can also utilize your text
    editor's ability to search across multiple files to find examples for
    each function listed."""

def convert_camel_case(name):
    # Handle CamelCase
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', name)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1)

    # Handle snake_case and kebab-case
    s3 = s2.replace('_', ' ').replace('-', ' ')

    # Capitalize words
    words = s3.split()
    capitalized = []
    for word in words:
        if word.upper() in ['API', 'JSON', 'HTML', 'CSS', 'JS', 'MGD']:
            capitalized.append(word.upper())
        else:
            capitalized.append(word.capitalize())

    return ' '.join(capitalized)
