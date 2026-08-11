import glob
import re
import os

def insert_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Header links using robust regex
    # a. Quy định Phụ đạo
    p1 = re.compile(r'<a\s+([^>]*?)href="([^"]*)"([^>]*?)>([^<]*Quy\s*định\s*Phụ\s*đạo[^<]*)</a>', re.IGNORECASE | re.DOTALL)
    def r1(m):
        if m.group(2) == '#' or 'quy-dinh-phu-dao.html' not in m.group(2):
            return f'<a {m.group(1)}href="quy-dinh-phu-dao.html"{m.group(3)}>{m.group(4)}</a>'
        return m.group(0)
    content = p1.sub(r1, content)
    
    # b. Học bổng
    p2 = re.compile(r'<a\s+([^>]*?)href="([^"]*)"([^>]*?)>([^<]*Chính\s*sách\s*học\s*bổng[^<]*)</a>', re.IGNORECASE | re.DOTALL)
    def r2(m):
        if m.group(2) == '#' or 'chinh-sach-hoc-bong.html' not in m.group(2):
            return f'<a {m.group(1)}href="chinh-sach-hoc-bong.html"{m.group(3)}>{m.group(4)}</a>'
        return m.group(0)
    content = p2.sub(r2, content)
    
    # c. Khảo thí (Matches "Quy định Khảo thí" or "Quy trình Khảo thí")
    p3 = re.compile(r'<a\s+([^>]*?)href="([^"]*)"([^>]*?)>([^<]*Khảo\s*thí[^<]*)</a>', re.IGNORECASE | re.DOTALL)
    def r3(m):
        if m.group(2) == '#' or 'quy-dinh-khao-thi.html' not in m.group(2):
            return f'<a {m.group(1)}href="quy-dinh-khao-thi.html"{m.group(3)}>{m.group(4)}</a>'
        return m.group(0)
    content = p3.sub(r3, content)
    
    # d. Nghỉ phép
    p4 = re.compile(r'<a\s+([^>]*?)href="([^"]*)"([^>]*?)>([^<]*Nghỉ\s*phép[^<]*)</a>', re.IGNORECASE | re.DOTALL)
    def r4(m):
        if m.group(2) == '#' or 'quy-dinh-nghi-phep.html' not in m.group(2):
            return f'<a {m.group(1)}href="quy-dinh-nghi-phep.html"{m.group(3)}>{m.group(4)}</a>'
        return m.group(0)
    content = p4.sub(r4, content)

    # 2. Inject into Sidebar
    basename = os.path.basename(filepath)
    
    active_class = "text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-primary before:mr-2"
    inactive_class = "hover:text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-gray-300 before:mr-2 hover:before:bg-primary"
    
    items = [
        ("quy-dinh-phu-dao.html", "Quy định Phụ đạo"),
        ("chinh-sach-hoc-bong.html", "Chính sách Học bổng"),
        ("quy-dinh-khao-thi.html", "Quy định Khảo thí"),
        ("quy-dinh-nghi-phep.html", "Quy định Nghỉ phép")
    ]
    
    sidebar_idx = content.find('Danh mục bài')
    if sidebar_idx != -1:
        # We find the end of the previous list item constraint
        anchor_idx = content.find('Quy định Sổ liên lạc</a></li>', sidebar_idx)
        if anchor_idx != -1 and content.find('Quy định Phụ đạo', sidebar_idx) == -1:
            insert_pos = anchor_idx + len('Quy định Sổ liên lạc</a></li>')
            
            blocks = []
            for href, text in items:
                _class = active_class if basename == href else inactive_class
                blocks.append(f'\n                                        <li><a href="{href}" class="{_class}">{text}</a></li>')
                
            content = content[:insert_pos] + "".join(blocks) + content[insert_pos:]
            
    # 3. Deactivate competing sidebar links if in new page
    our_pages = [i[0] for i in items]
    if basename in our_pages:
        wrong_active = 'class="' + active_class + '"'
        correct_inactive = 'class="' + inactive_class + '"'
        content = content.replace('href="giao-trinh-tai-lieu.html" ' + wrong_active, 'href="giao-trinh-tai-lieu.html" ' + correct_inactive)
        content = content.replace('href="quy-dinh-diem-danh.html" ' + wrong_active, 'href="quy-dinh-diem-danh.html" ' + correct_inactive)
        content = content.replace('href="quy-trinh-giang-day.html" ' + wrong_active, 'href="quy-trinh-giang-day.html" ' + correct_inactive)
        content = content.replace('href="quy-dinh-so-lien-lac.html" ' + wrong_active, 'href="quy-dinh-so-lien-lac.html" ' + correct_inactive)
        content = content.replace('href="quy-dinh-tac-phong.html" ' + wrong_active, 'href="quy-dinh-tac-phong.html" ' + correct_inactive)

        # Deactivate each other
        for p in our_pages:
            if p != basename:
                content = content.replace(f'href="{p}" {wrong_active}', f'href="{p}" {correct_inactive}')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated links in {basename}")

if __name__ == '__main__':
    for f in glob.glob('/Users/vobac/Downloads/gia-viet-handbook/*.html'):
        insert_links(f)
