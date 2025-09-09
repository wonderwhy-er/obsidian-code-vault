#!/usr/bin/env python3
"""
Fix over-encoded URLs and ensure proper single encoding
"""

import os
import re

def fix_over_encoding(content):
    """Fix %2520 (double encoded) back to %20 (single encoded)"""
    
    # Fix double-encoded spaces
    content = content.replace('%2520', '%20')
    
    # Also fix any other double encoding patterns
    content = content.replace('%252F', '%2F')  # Forward slash
    content = content.replace('%253A', '%3A')  # Colon
    
    return content

def fix_markdown_links_simple(content):
    """Simple approach: just ensure spaces in .md links are %20"""
    
    def fix_link(match):
        full_match = match.group(0)
        link_text = match.group(1) 
        link_path = match.group(2)
        
        # Only fix relative paths ending in .md
        if not link_path.startswith('http') and link_path.endswith('.md'):
            # Simple replacement: space -> %20
            fixed_path = link_path.replace(' ', '%20')
            return f'[{link_text}]({fixed_path})'
        
        return full_match
    
    # Pattern to match [text](path.md) links
    pattern = r'\[([^\]]+)\]\(([^)]+\.md)\)'
    return re.sub(pattern, fix_link, content)

def process_files(vault_dir):
    """Process all markdown files"""
    fixed_files = []
    
    for root, dirs, files in os.walk(vault_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Fix over-encoding first
                content = fix_over_encoding(content)
                
                # Then fix remaining space issues
                content = fix_markdown_links_simple(content)
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    rel_path = os.path.relpath(filepath, vault_dir)
                    fixed_files.append(rel_path)
                    print(f"Fixed: {rel_path}")
    
    return fixed_files

if __name__ == "__main__":
    vault_dir = "/Users/fiberta/work/obsidian-code-vault"
    
    print("🔧 Fixing over-encoded links...")
    
    fixed = process_files(vault_dir)
    
    if fixed:
        print(f"\n✅ Fixed {len(fixed)} files")
        print("🔗 Links should now work correctly!")
    else:
        print("✅ No fixes needed!")
