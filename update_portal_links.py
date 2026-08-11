import glob
import re

def update_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Header link
    # Match: <a class="..." href="#">\s*Hệ thống & Hỗ trợ
    header_pattern = re.compile(r'(<a\s+class="[^"]*"\s+href=")("#)(">\s*Hệ thống & Hỗ trợ)')
    content = header_pattern.sub(r'\g<1>he-thong-ho-tro.html\g<3>', content)

    # 2. Update Sidebar link
    # Match: <a href="#" class="...">Hệ thống & Hỗ trợ</a>
    sidebar_pattern = re.compile(r'(<a\s+href=")("#)("\s+class="[^"]*">Hệ thống & Hỗ trợ</a>)')
    content = sidebar_pattern.sub(r'\g<1>he-thong-ho-tro.html\g<3>', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated portal links in {filepath.split('/')[-1]}")

if __name__ == '__main__':
    for f in glob.glob('/Users/vobac/Downloads/gia-viet-handbook/*.html'):
        update_links(f)
