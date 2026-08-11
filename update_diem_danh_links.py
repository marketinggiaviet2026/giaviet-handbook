import glob
import re
import os

def insert_diem_danh_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Header link using robust regex:
    pattern = re.compile(r'<a\s+([^>]*?)href="([^"]*)"([^>]*?)>([^<]*Quy\s*định\s*Điểm\s*danh[^<]*)</a>', re.IGNORECASE | re.DOTALL)
    def header_replacer(match):
        attr1 = match.group(1)
        current_href = match.group(2)
        attr2 = match.group(3)
        inner_text = match.group(4)
        
        if current_href == '#' or 'quy-dinh-diem-danh.html' not in current_href:
            return f'<a {attr1}href="quy-dinh-diem-danh.html"{attr2}>{inner_text}</a>'
        return match.group(0)

    content = pattern.sub(header_replacer, content)

    # 2. Inject into Sidebar
    basename = os.path.basename(filepath)
    is_active = (basename == 'quy-dinh-diem-danh.html')
    
    active_class = "text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-primary before:mr-2"
    inactive_class = "hover:text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-gray-300 before:mr-2 hover:before:bg-primary"
    
    new_sidebar_link = f'\n                                        <li><a href="quy-dinh-diem-danh.html" class="{active_class if is_active else inactive_class}">Quy định Điểm danh</a></li>'
    
    sidebar_idx = content.find('Danh mục bài')
    if sidebar_idx != -1:
        # Check if already inserted in sidebar
        has_in_sidebar = content.find('Quy định Điểm danh', sidebar_idx) != -1
        if not has_in_sidebar:
            giao_trinh_idx = content.find('Giáo trình & Tài liệu giảng dạy</a></li>', sidebar_idx)
            if giao_trinh_idx != -1:
                insert_pos = giao_trinh_idx + len('Giáo trình & Tài liệu giảng dạy</a></li>')
                content = content[:insert_pos] + new_sidebar_link + content[insert_pos:]
    
    # 3. Deactivate competing sidebar links if in new page
    if is_active:
        wrong_active = 'href="giao-trinh-tai-lieu.html" class="' + active_class + '"'
        correct_inactive = 'href="giao-trinh-tai-lieu.html" class="' + inactive_class + '"'
        content = content.replace(wrong_active, correct_inactive)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated links in {basename}")

if __name__ == '__main__':
    for f in glob.glob('/Users/vobac/Downloads/gia-viet-handbook/*.html'):
        insert_diem_danh_links(f)
