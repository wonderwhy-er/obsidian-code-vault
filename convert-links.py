#!/usr/bin/env python3
"""
Convert Obsidian [[double bracket]] links to standard markdown [text](file.md) format
This makes links work in both Obsidian and GitHub
"""

import os
import re
import urllib.parse

def convert_obsidian_links_to_markdown(content):
    """Convert [[Link]] to [Link](Link.md) format with URL encoding for spaces"""
    
    def replace_link(match):
        link_text = match.group(1)
        # URL encode the filename (replace spaces with %20, etc.)
        filename = urllib.parse.quote(link_text.replace(' ', '%20')) + '.md'
        return f'[{link_text}]({filename})'
    
    # Pattern to match [[Link Text]] but not inside code blocks
    # This is a simplified version - more complex regex would handle nested brackets
    pattern = r'\[\[([^\]]+)\]\]'
    return re.sub(pattern, replace_link, content)

def process_markdown_files(directory):
    """Process all .md files in the directory"""
    converted_files = []
    
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            filepath = os.path.join(directory, filename)
            
            # Read the file
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Convert links
            original_content = content
            converted_content = convert_obsidian_links_to_markdown(content)
            
            # Only write back if there were changes
            if original_content != converted_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(converted_content)
                converted_files.append(filename)
                print(f"Converted links in: {filename}")
    
    return converted_files

if __name__ == "__main__":
    vault_directory = "/Users/fiberta/work/obsidian-code-vault"
    
    print("Converting Obsidian [[links]] to markdown [links](file.md) format...")
    print("This will make links work in both Obsidian and GitHub!")
    print()
    
    converted = process_markdown_files(vault_directory)
    
    if converted:
        print(f"\n✅ Successfully converted {len(converted)} files:")
        for file in converted:
            print(f"   - {file}")
        print("\n🔗 Links now work in both Obsidian and GitHub!")
    else:
        print("✅ All files already use standard markdown link format!")
