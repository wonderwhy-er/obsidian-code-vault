#!/usr/bin/env python3
"""
Obsidian to GitHub Link Converter
Converts [[Obsidian links]] to [GitHub links](File%20Name.md) format

Usage:
    python3 scripts/convert-obsidian-links.py           # Convert all .md files
    python3 scripts/convert-obsidian-links.py file.md   # Convert specific file
"""

import os
import re
import sys
import urllib.parse
from pathlib import Path

def convert_obsidian_to_markdown_links(content):
    """Convert [[Link]] to [Link](Link.md) format with proper URL encoding"""
    
    def replace_link(match):
        link_text = match.group(1)
        
        # Handle pipe syntax [[Link|Display Text]] -> [Display Text](Link.md)
        if '|' in link_text:
            actual_link, display_text = link_text.split('|', 1)
        else:
            actual_link = display_text = link_text
        
        # URL encode the filename (spaces -> %20)
        filename = urllib.parse.quote(actual_link.strip(), safe='') + '.md'
        
        return f'[{display_text.strip()}]({filename})'
    
    # Pattern to match [[Link]] or [[Link|Display]]
    pattern = r'\[\[([^\]]+)\]\]'
    return re.sub(pattern, replace_link, content)

def fix_url_encoding(content):
    """Fix common URL encoding issues"""
    # Fix multiple encoding patterns
    fixes = [
        ('%25252520', '%20'),  # Quadruple encoded
        ('%252520', '%20'),    # Triple encoded  
        ('%2520', '%20'),      # Double encoded
    ]
    
    for bad_pattern, good_pattern in fixes:
        content = content.replace(bad_pattern, good_pattern)
    
    # Fix spaces in markdown links that aren't encoded
    def fix_spaces_in_links(match):
        link_text = match.group(1)
        link_path = match.group(2)
        
        # Only fix .md links with spaces, skip external URLs
        if not link_path.startswith('http') and link_path.endswith('.md') and ' ' in link_path:
            fixed_path = link_path.replace(' ', '%20')
            return f'[{link_text}]({fixed_path})'
        
        return match.group(0)
    
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.sub(pattern, fix_spaces_in_links, content)

def process_file(filepath):
    """Process a single markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Count original patterns
        obsidian_links = len(re.findall(r'\[\[([^\]]+)\]\]', content))
        space_links = len(re.findall(r'\[([^\]]+)\]\(([^)]*\s[^)]*\.md)\)', content))
        
        # Apply conversions
        content = convert_obsidian_to_markdown_links(content)
        content = fix_url_encoding(content)
        
        # Write back if changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            changes = []
            if obsidian_links > 0:
                changes.append(f"{obsidian_links} Obsidian [[links]]")
            if space_links > 0:
                changes.append(f"{space_links} unencoded spaces")
            
            return True, changes
            
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return False, []
    
    return False, []

def find_markdown_files(directory):
    """Find all .md files in directory, excluding .git"""
    md_files = []
    
    for root, dirs, files in os.walk(directory):
        # Skip .git and .obsidian directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    return md_files

def main():
    """Main function"""
    print("🔄 Obsidian to GitHub Link Converter")
    print("=" * 50)
    
    # Determine which files to process
    if len(sys.argv) > 1:
        # Specific files provided
        target_files = []
        for arg in sys.argv[1:]:
            if os.path.isfile(arg) and arg.endswith('.md'):
                target_files.append(arg)
            else:
                print(f"⚠️  Skipping {arg} (not a .md file)")
        
        if not target_files:
            print("❌ No valid .md files provided")
            return 1
            
    else:
        # Find all .md files in current directory and subdirectories
        current_dir = os.getcwd()
        target_files = find_markdown_files(current_dir)
        
        if not target_files:
            print("❌ No .md files found in current directory")
            return 1
        
        print(f"📁 Found {len(target_files)} markdown files to process")
    
    # Process files
    modified_files = []
    total_changes = []
    
    for filepath in target_files:
        was_modified, changes = process_file(filepath)
        
        if was_modified:
            filename = os.path.relpath(filepath)
            modified_files.append(filename)
            total_changes.extend(changes)
            print(f"✅ {filename}")
            for change in changes:
                print(f"   - Fixed {change}")
        else:
            filename = os.path.relpath(filepath)
            print(f"✨ {filename} (already GitHub-compatible)")
    
    # Summary
    print("=" * 50)
    if modified_files:
        print(f"🎉 Successfully converted {len(modified_files)} files!")
        print(f"🔗 All links are now GitHub and Obsidian compatible!")
        
        if len(modified_files) <= 10:
            print(f"\n📝 Modified files:")
            for filename in modified_files:
                print(f"   - {filename}")
        else:
            print(f"\n📝 Modified {len(modified_files)} files (showing first 10):")
            for filename in modified_files[:10]:
                print(f"   - {filename}")
            print(f"   ... and {len(modified_files) - 10} more")
        
        print(f"\n💡 Next steps:")
        print(f"   git add -u    # Stage the converted files")
        print(f"   git commit    # Commit the changes")
        
        return 2  # Return 2 to indicate "files changed, please auto-stage"
        
    else:
        print("✅ All files already use GitHub-compatible links!")
    
    return 0

if __name__ == "__main__":
    exit(main())
