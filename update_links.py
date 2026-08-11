import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update top navigation
    # <a id="nav-to-chuc" class="..." href="#">
    content = re.sub(
        r'(<a id="nav-to-chuc"[^>]*?href=")(#)(")',
        r'\g<1>to-chuc-nhan-su.html\3',
        content
    )
    content = re.sub(
        r'(<a id="nav-chinh-sach"[^>]*?href=")(#)(")',
        r'\g<1>chinh-sach-phuc-loi.html\3',
        content
    )

    # Update sidebar links if they exist
    # <a href="#" class="hover:text-primary transition-colors flex items-center group">Tổ chức & Nhân sự</a>
    content = re.sub(
        r'<a href="#"([^>]*>)\s*Tổ chức & Nhân sự\s*</a>',
        r'<a href="to-chuc-nhan-su.html"\1Tổ chức & Nhân sự</a>',
        content
    )
    # <a href="#" class="hover:text-primary transition-colors flex items-center group">Chính sách & Phúc lợi</a>
    content = re.sub(
        r'<a href="#"([^>]*>)\s*Chính sách & Phúc lợi\s*</a>',
        r'<a href="chinh-sach-phuc-loi.html"\1Chính sách & Phúc lợi</a>',
        content
    )

    # Another possible format with \n inside the tag text
    content = re.sub(
        r'<a href="#"([^>]*>)\s*Tổ\s*chức & Nhân sự\s*</a>',
        r'<a href="to-chuc-nhan-su.html"\1Tổ chức & Nhân sự</a>',
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated links in all HTML files.")
