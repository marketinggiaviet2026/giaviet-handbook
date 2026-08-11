import glob
import re
import os

def insert_so_lien_lac_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Header link using robust regex:
    pattern = re.compile(r'<a\s+([^>]*?)href="([^"]*)"([^>]*?)>([^<]*Quy\s*định\s*Sổ\s*liên\s*lạc[^<]*)</a>', re.IGNORECASE | re.DOTALL)
    def header_replacer(match):
        attr1 = match.group(1)
        current_href = match.group(2)
        attr2 = match.group(3)
        inner_text = match.group(4)
        
        if current_href == '#' or 'quy-dinh-so-lien-lac.html' not in current_href:
            return f'<a {attr1}href="quy-dinh-so-lien-lac.html"{attr2}>{inner_text}</a>'
        return match.group(0)

    content = pattern.sub(header_replacer, content)

    # 2. Inject into Sidebar
    basename = os.path.basename(filepath)
    is_active = (basename == 'quy-dinh-so-lien-lac.html')
    
    active_class = "text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-primary before:mr-2"
    inactive_class = "hover:text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-gray-300 before:mr-2 hover:before:bg-primary"
    
    new_sidebar_link = f'\n                                        <li><a href="quy-dinh-so-lien-lac.html" class="{active_class if is_active else inactive_class}">Quy định Sổ liên lạc</a></li>'
    
    sidebar_idx = content.find('Danh mục bài')
    if sidebar_idx != -1:
        # Check if already inserted in sidebar
        has_in_sidebar = content.find('Quy định Sổ liên lạc', sidebar_idx) != -1
        if not has_in_sidebar:
            quy_trinh_idx = content.find('Quy trình giảng dạy và khen thưởng</a></li>', sidebar_idx)
            if quy_trinh_idx != -1:
                insert_pos = quy_trinh_idx + len('Quy trình giảng dạy và khen thưởng</a></li>')
                content = content[:insert_pos] + new_sidebar_link + content[insert_pos:]
    
    # 3. Deactivate competing sidebar links if in new page
    if is_active:
        wrong_active = 'class="' + active_class + '"'
        correct_inactive = 'class="' + inactive_class + '"'
        content = content.replace('href="giao-trinh-tai-lieu.html" ' + wrong_active, 'href="giao-trinh-tai-lieu.html" ' + correct_inactive)
        content = content.replace('href="quy-dinh-diem-danh.html" ' + wrong_active, 'href="quy-dinh-diem-danh.html" ' + correct_inactive)
        content = content.replace('href="quy-trinh-giang-day.html" ' + wrong_active, 'href="quy-trinh-giang-day.html" ' + correct_inactive)
        content = content.replace('href="quy-dinh-tac-phong.html" ' + wrong_active, 'href="quy-dinh-tac-phong.html" ' + correct_inactive)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated links in {basename}")

if __name__ == '__main__':
    for f in glob.glob('/Users/vobac/Downloads/gia-viet-handbook/*.html'):
        insert_so_lien_lac_links(f)
