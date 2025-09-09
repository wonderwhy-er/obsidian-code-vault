#!/usr/bin/env python3
"""
Update all markdown links to use the new folder structure
"""

import os
import re

def update_links_in_file(filepath, link_mapping):
    """Update links in a single file based on the mapping"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Update all markdown links [Text](File.md) to new paths
    for old_link, new_path in link_mapping.items():
        # Handle both with and without .md extension
        old_pattern = f'\\[([^\\]]+)\\]\\({re.escape(old_link)}\\.md\\)'
        old_pattern_no_ext = f'\\[([^\\]]+)\\]\\({re.escape(old_link)}\\)'
        
        # Calculate relative path from current file to target
        current_dir = os.path.dirname(filepath)
        target_path = os.path.relpath(new_path, current_dir)
        
        # Replace with proper relative path
        content = re.sub(old_pattern, f'[\\1]({target_path}.md)', content)
        content = re.sub(old_pattern_no_ext, f'[\\1]({target_path}.md)', content)
    
    # Write back if changed
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated links in: {os.path.relpath(filepath, '/Users/fiberta/work/obsidian-code-vault')}")
        return True
    return False

def find_all_md_files(directory):
    """Find all .md files recursively"""
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

if __name__ == "__main__":
    vault_dir = "/Users/fiberta/work/obsidian-code-vault"
    
    # Mapping of old file references to new paths (without .md extension)
    link_mapping = {
        "Authentication%20System": "02-backend/auth/Authentication System",
        "Authentication System": "02-backend/auth/Authentication System", 
        "JWT%20Token%20Manager": "02-backend/auth/JWT Token Manager",
        "JWT Token Manager": "02-backend/auth/JWT Token Manager",
        "Database%20Layer": "02-backend/database/Database Layer",
        "Database Layer": "02-backend/database/Database Layer",
        "API%20Design": "02-backend/api/API Design", 
        "API Design": "02-backend/api/API Design",
        "User%20Management": "02-backend/User Management",
        "User Management": "02-backend/User Management",
        "Error%20Handling": "02-backend/Error Handling",
        "Error Handling": "02-backend/Error Handling",
        "Frontend%20Components": "03-frontend/Frontend Components",
        "Frontend Components": "03-frontend/Frontend Components",
        "Testing%20Strategy": "04-testing/Testing Strategy", 
        "Testing Strategy": "04-testing/Testing Strategy",
        "Configuration": "05-operations/Configuration"
    }
    
    print("Updating all cross-references to use new folder structure...")
    
    # Find all markdown files
    md_files = find_all_md_files(vault_dir)
    
    updated_count = 0
    for md_file in md_files:
        if update_links_in_file(md_file, link_mapping):
            updated_count += 1
    
    print(f"\n✅ Updated {updated_count} files with new folder structure paths!")
    print("🗂️ Documentation now properly organized and cross-linked!")
