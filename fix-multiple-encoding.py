#!/usr/bin/env python3
"""
Fix triple and quadruple encoded URLs back to single encoding
"""

import os
import re

def fix_multiple_encoding(content):
    """Fix multiple levels of URL encoding"""
    
    # Fix common multiple encoding patterns
    patterns_to_fix = [
        ('%252520', '%20'),  # Triple encoded space
        ('%25252520', '%20'), # Quadruple encoded space
        ('%2520', '%20'),    # Double encoded space  
        ('%252F', '/'),      # Triple encoded slash
        ('%253A', ':'),      # Triple encoded colon
    ]
    
    for bad_pattern, good_pattern in patterns_to_fix:
        content = content.replace(bad_pattern, good_pattern)
    
    return content

def fix_all_files(vault_dir):
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
                fixed_content = fix_multiple_encoding(content)
                
                if content != fixed_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(fixed_content)
                    
                    rel_path = os.path.relpath(filepath, vault_dir)
                    fixed_files.append(rel_path)
                    print(f"Fixed multiple encoding in: {rel_path}")
                    
                    # Show what was changed
                    if '%2525' in original_content:
                        print(f"   - Removed triple/quadruple encoding")
    
    return fixed_files

if __name__ == "__main__":
    vault_dir = "/Users/fiberta/work/obsidian-code-vault"
    
    print("🔧 Fixing multiple URL encoding issues...")
    print("Converting %252520 → %20, %2520 → %20, etc.")
    print()
    
    fixed = fix_all_files(vault_dir)
    
    if fixed:
        print(f"\n✅ Fixed multiple encoding in {len(fixed)} files")
        for file in fixed:
            print(f"   - {file}")
    else:
        print("✅ No multiple encoding issues found!")
    
    print(f"\n🔗 Links should now work correctly in GitHub!")
