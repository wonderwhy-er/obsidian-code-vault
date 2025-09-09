#!/usr/bin/env python3
"""
Fix all markdown links to properly URL-encode spaces and special characters
This ensures links work in both GitHub and Obsidian
"""

import os
import re
import urllib.parse

def fix_markdown_links(content):
    """Fix all [text](path) links to properly encode URLs"""
    
    def fix_link(match):
        link_text = match.group(1)
        link_path = match.group(2)
        
        # Only process relative paths (not external URLs)
        if link_path.startswith('http'):
            return match.group(0)  # Return unchanged
        
        # Split path into directory and filename
        if '/' in link_path:
            path_parts = link_path.split('/')
            # URL encode each part that might contain spaces
            encoded_parts = []
            for part in path_parts:
                if part.endswith('.md'):
                    # Encode the filename (without .md)
                    filename = part[:-3]  # Remove .md
                    encoded_filename = urllib.parse.quote(filename, safe='')
                    encoded_parts.append(encoded_filename + '.md')
                else:
                    # Directory names - keep as is since they don't have spaces in our structure
                    encoded_parts.append(part)
            fixed_path = '/'.join(encoded_parts)
        else:
            # Just a filename
            if link_path.endswith('.md'):
                filename = link_path[:-3]
                fixed_path = urllib.parse.quote(filename, safe='') + '.md'
            else:
                fixed_path = urllib.parse.quote(link_path, safe='')
        
        return f'[{link_text}]({fixed_path})'
    
    # Pattern to match [text](path) links
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.sub(pattern, fix_link, content)

def process_all_markdown_files(vault_dir):
    """Process all .md files recursively"""
    fixed_files = []
    
    for root, dirs, files in os.walk(vault_dir):
        # Skip .git and .obsidian directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                
                # Read file
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Fix links
                original_content = content
                fixed_content = fix_markdown_links(content)
                
                # Write back if changed
                if original_content != fixed_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(fixed_content)
                    
                    rel_path = os.path.relpath(filepath, vault_dir)
                    fixed_files.append(rel_path)
                    print(f"Fixed links in: {rel_path}")
    
    return fixed_files

if __name__ == "__main__":
    vault_dir = "/Users/fiberta/work/obsidian-code-vault"
    
    print("🔧 Fixing all markdown links to properly encode spaces...")
    print("This ensures links work correctly in both GitHub and Obsidian!")
    print()
    
    fixed_files = process_all_markdown_files(vault_dir)
    
    if fixed_files:
        print(f"\n✅ Fixed links in {len(fixed_files)} files:")
        for file in fixed_files:
            print(f"   - {file}")
        print(f"\n🔗 All links now properly URL-encoded and should work everywhere!")
    else:
        print("✅ All links are already properly encoded!")
    
    print(f"\n📝 Example of fixed link format:")
    print(f"   [Authentication System](02-backend/auth/Authentication%20System.md)")
