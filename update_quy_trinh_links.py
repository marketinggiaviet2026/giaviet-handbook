import glob
import re
import os

def insert_quy_trinh_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Header link using robust regex:
    pattern = re.compile(r'<a\s+([^>]*?)href="([^"]*)"([^>]*?)>([^<]*Quy\s*trình\s*giảng\s*dạy\s*và\s*khen\s*thưởng[^<]*)</a>', re.IGNORECASE | re.DOTALL)
    def header_replacer(match):
        attr1 = match.group(1)
        current_href = match.group(2)
        attr2 = match.group(3)
        inner_text = match.group(4)
        
        if current_href == '#' or 'quy-trinh-giang-day.html' not in current_href:
            return f'<a {attr1}href="quy-trinh-giang-day.html"{attr2}>{inner_text}</a>'
        return match.group(0)

    content = pattern.sub(header_replacer, content)

    # 2. Inject into Sidebar
    basename = os.path.basename(filepath)
    is_active = (basename == 'quy-trinh-giang-day.html')
    
    active_class = "text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-primary before:mr-2"
    inactive_class = "hover:text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-gray-300 before:mr-2 hover:before:bg-primary"
    
    new_sidebar_link = f'\n                                        <li><a href="quy-trinh-giang-day.html" class="{active_class if is_active else inactive_class}">Quy trình giảng dạy và khen thưởng</a></li>'
    
    sidebar_idx = content.find('Danh mục bài')
    if sidebar_idx != -1:
        # Check if already inserted in sidebar
        has_in_sidebar = content.find('Quy trình giảng dạy và khen thưởng', sidebar_idx) != -1
        if not has_in_sidebar:
            diem_danh_idx = content.find('Quy định Điểm danh</a></li>', sidebar_idx)
            if diem_danh_idx != -1:
                insert_pos = diem_danh_idx + len('Quy định Điểm danh</a></li>')
                content = content[:insert_pos] + new_sidebar_link + content[insert_pos:]
    
    # 3. Deactivate competing sidebar links if in new page
    if is_active:
        wrong_active = 'class="' + active_class + '"'
        correct_inactive = 'class="' + inactive_class + '"'
        # we know exactly two other active elements could be around here from copy-pasting
        content = content.replace('href="giao-trinh-tai-lieu.html" ' + wrong_active, 'href="giao-trinh-tai-lieu.html" ' + correct_inactive)
        content = content.replace('href="quy-dinh-diem-danh.html" ' + wrong_active, 'href="quy-dinh-diem-danh.html" ' + correct_inactive)
        content = content.replace('href="quy-dinh-tac-phong.html" ' + wrong_active, 'href="quy-dinh-tac-phong.html" ' + correct_inactive)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated links in {basename}")

if __name__ == '__main__':
    for f in glob.glob('/Users/vobac/Downloads/gia-viet-handbook/*.html'):
        insert_quy_trinh_links(f)
