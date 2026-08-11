import glob
import re

def fix_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern matches <a ... href="..." ...> ... Giáo trình & Tài liệu giảng dạy ... </a>
    # Uses DOTALL to match across newlines inside the tag or its attributes
    pattern = re.compile(r'<a\s+([^>]*?)href="([^"]*)"([^>]*?)>([^<]*Giáo\s*trình\s*&\s*Tài\s*liệu\s*giảng\s*dạy[^<]*)</a>', re.IGNORECASE | re.DOTALL)
    
    def replacer(match):
        attr1 = match.group(1)
        current_href = match.group(2)
        attr2 = match.group(3)
        inner_text = match.group(4)
        
        if current_href == '#':
            return f'<a {attr1}href="giao-trinh-tai-lieu.html"{attr2}>{inner_text}</a>'
        return match.group(0)

    new_content = pattern.sub(replacer, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated header/sidebar links in {filepath}")
    else:
        print(f"No changes needed in {filepath}")

if __name__ == '__main__':
    for f in glob.glob('/Users/vobac/Downloads/gia-viet-handbook/*.html'):
        fix_links(f)
