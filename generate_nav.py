#!/usr/bin/env python3
import yaml
import re
from pathlib import Path
from typing import Dict, List, Any

def convert_filename_to_title(filename: str) -> str:
    # Handle CamelCase
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', filename)
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

def extract_title_from_file(file_path: Path) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Look for first # heading
            title_match = re.search(r'^#\s+(.+?)(?:\s*\{[^}]*\})?\s*$', content, re.MULTILINE)
            if title_match:
                title = title_match.group(1).strip('*').strip()
                if title:
                    return title
    except Exception:
        pass

    # Fall back to filename conversion
    return convert_filename_to_title(file_path.stem)

def generate_function_nav(docs_dir: Path) -> List[Dict[str, Any]]:
    functions_dir = docs_dir / "Functions"
    if not functions_dir.exists():
        return []

    nav_items = []

    # Add main Functions index
    nav_items.append({"Function Index": "Functions/index.md"})

    # Get all category directories
    categories = []
    for item in functions_dir.iterdir():
        if item.is_dir() and item.name not in ['.', '..', '__pycache__']:
            # Check if directory has .md files
            md_files = [f for f in item.glob("*.md") if f.name.lower() != 'index.md']
            if md_files:
                categories.append((item.name, md_files))

    # Sort categories alphabetically
    categories.sort(key=lambda x: x[0])

    # Generate navigation for each category
    for category_name, md_files in categories:
        category_title = convert_filename_to_title(category_name)

        # Sort files alphabetically
        md_files.sort(key=lambda x: x.name.lower())

        # Create category navigation
        category_nav = []
        for file_path in md_files:
            title = extract_title_from_file(file_path)
            relative_path = str(file_path.relative_to(docs_dir)).replace('\\', '/')
            category_nav.append({title: relative_path})

        nav_items.append({category_title: category_nav})

    return nav_items

def generate_directory_nav(docs_dir: Path, dir_name: str, include_index: bool = True) -> List[Dict[str, Any]]:
    target_dir = docs_dir / dir_name
    if not target_dir.exists():
        return []

    nav_items = []
    md_files = []

    for file_path in target_dir.glob("*.md"):
        if not include_index and file_path.name.lower() == 'index.md':
            continue
        md_files.append(file_path)

    # Sort files alphabetically
    md_files.sort(key=lambda x: x.name.lower())

    for file_path in md_files:
        title = extract_title_from_file(file_path)
        relative_path = str(file_path.relative_to(docs_dir)).replace('\\', '/')
        nav_items.append({title: relative_path})

    return nav_items

def generate_manual_nav(docs_dir: Path) -> List[Dict[str, Any]]:
    manual_dir = docs_dir / "Manual"
    if not manual_dir.exists():
        return []

    nav_items = []

    # Get all subdirectories
    subdirs = []
    for item in manual_dir.iterdir():
        if item.is_dir() and item.name not in ['.', '..', '__pycache__']:
            # Check if directory has .md files
            md_files = list(item.glob("*.md"))
            if md_files:
                subdirs.append((item.name, md_files))

    # Sort subdirectories alphabetically
    subdirs.sort(key=lambda x: x[0])

    # Generate navigation for each subdirectory
    for subdir_name, md_files in subdirs:
        subdir_title = convert_filename_to_title(subdir_name)

        # Create subdirectory navigation - put index first
        subdir_nav = []
        index_files = []
        other_files = []

        for file_path in md_files:
            if file_path.name.lower() == 'index.md':
                index_files.append(file_path)
            else:
                other_files.append(file_path)

        # Sort non-index files alphabetically
        other_files.sort(key=lambda x: x.name.lower())

        # Add index files first, then others
        for file_path in index_files + other_files:
            title = extract_title_from_file(file_path)
            relative_path = str(file_path.relative_to(docs_dir)).replace('\\', '/')
            subdir_nav.append({title: relative_path})

        nav_items.append({subdir_title: subdir_nav})

    return nav_items

def update_mkdocs_nav():
    """
    Update the navigation in mkdocs.yml with automatically generated structure.
    """
    mkdocs_path = Path("mkdocs.yml")
    docs_dir = Path("docs")

    print("Updating navigation structure...")

    if not mkdocs_path.exists():
        print("⚠ Error: mkdocs.yml not found")
        print("   Please run this script from the mkDocsMGD root directory")
        return False

    if not docs_dir.exists():
        print("⚠ Error: docs directory not found")
        return False

    try:
        # YAML file as text to preserve ENV tags and other formatting
        with open(mkdocs_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # Temporary version without special MkDocs tags for parsing
        temp_content = original_content
        temp_content = re.sub(r'!ENV\s+\[([^\]]+)\]', r'false', temp_content)
        temp_content = re.sub(r'!!python/name:[^\s\n]+', r'"python_placeholder"', temp_content)
        config = yaml.safe_load(temp_content)
        print("✓ Loaded mkdocs.yml")
    except Exception as e:
        print(f"❌ Error reading mkdocs.yml: {e}")
        return False

    # Generate new navigation
    new_nav = []

    new_nav.append({"Home": "index.md"})

    # Getting Started
    getting_started_nav = []
    getting_started_files = [
        ("Editors", "GettingStarted/Editors.md"),
        ("Making A Mod", "GettingStarted/MakingAMod.md"),
        ("Music And Art", "GettingStarted/MusicAndArt.md"),
        ("Meta Creation", "GettingStarted/MetaCreation.md"),
        ("Publishing Mods", "GettingStarted/PublishingMods.md")
    ]
    for title, path in getting_started_files:
        if (docs_dir / path).exists():
            getting_started_nav.append({title: path})

    if getting_started_nav:
        new_nav.append({"Getting Started": getting_started_nav})

    # Tutorials
    tutorials_nav = []
    if (docs_dir / "Tutorials" / "index.md").exists():
        tutorials_nav.append({"Tutorials Index": "Tutorials/index.md"})

    # Other tutorial files
    tutorial_files = generate_directory_nav(docs_dir, "Tutorials", include_index=False)
    tutorials_nav.extend(tutorial_files)

    if tutorials_nav:
        new_nav.append({"Tutorials": tutorials_nav})

    # JSON Manual
    manual_nav = generate_manual_nav(docs_dir)
    if manual_nav:
        new_nav.append({"JSON Manual": manual_nav})

    # Reference
    reference_nav = []
    reference_files = [
        ("Markup", "Reference/Markup.md"),
        ("Stance Reference", "Reference/StanceRef.md"),
        ("Status Effect Reference", "Reference/StatusEffectRef.md"),
        ("Stat Reference", "Reference/StatRef.md"),
        ("FAQ", "Reference/FAQ.md"),
        ("Breaking Changes", "Reference/BreakingChanges.md"),
        ("Gridmap", "Reference/Gridmap.md")
    ]
    for title, path in reference_files:
        if (docs_dir / path).exists():
            reference_nav.append({title: path})

    if reference_nav:
        new_nav.append({"Reference": reference_nav})

    # Function Reference
    print("Scanning Functions directory...")
    function_nav = generate_function_nav(docs_dir)
    if function_nav:
        new_nav.append({"Functions": function_nav})
        print(f"✓ Found {len(function_nav)} function categories")
    else:
        print("⚠ No function files found")

    # Update the config
    config['nav'] = new_nav

    try:
        # Generate new YAML content
        new_yaml = yaml.dump(config, default_flow_style=False, sort_keys=False, allow_unicode=True)

        # Restore ENV tags and python/name tags in the new content
        new_yaml = re.sub(r'- navigation\.instant: false', '- navigation.instant: !ENV [OFFLINE, false]', new_yaml)
        new_yaml = re.sub(r'navigation\.instant: false', 'navigation.instant: !ENV [OFFLINE, false]', new_yaml)
        new_yaml = re.sub(r'emoji_index: python_placeholder', 'emoji_index: !!python/name:material.extensions.emoji.twemoji', new_yaml)
        new_yaml = re.sub(r'emoji_generator: python_placeholder', 'emoji_generator: !!python/name:material.extensions.emoji.to_svg', new_yaml)

        # Write back to mkdocs.yml
        with open(mkdocs_path, 'w', encoding='utf-8') as f:
            f.write(new_yaml)

        print("✓ Navigation updated")

        # Count total function files for summary
        total_files = 0
        for item in function_nav[1:]:  # Skip the main Functions index
            if isinstance(item, dict):
                for category, files in item.items():
                    if isinstance(files, list):
                        total_files += len(files)

        print(f"✓ Generated navigation for {total_files} function files")
        return True

    except Exception as e:
        print(f"⚠ Error writing mkdocs.yml: {e}")
        return False

if __name__ == '__main__':
    import sys

    print("=" * 50)
    print("MGD Documentation Navigation Generator")
    print("=" * 50)

    success = update_mkdocs_nav()

    if success:
        print("\nNavigation generation complete")
        print("   Ready to build with: mkdocs build")
        sys.exit(0)
    else:
        print("\nNavigation generation failed")
        sys.exit(1)
