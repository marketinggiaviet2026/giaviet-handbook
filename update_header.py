import os
import re

files = [
    '/Users/vobac/Downloads/gia-viet-handbook/index.html',
    '/Users/vobac/Downloads/gia-viet-handbook/ve-gia-viet.html',
    '/Users/vobac/Downloads/gia-viet-handbook/quy-dinh-tac-phong.html',
    '/Users/vobac/Downloads/gia-viet-handbook/che-do-luong-thuong.html',
    '/Users/vobac/Downloads/gia-viet-handbook/dai-ngo-giao-vien.html',
    '/Users/vobac/Downloads/gia-viet-handbook/cac-chinh-sach-ho-tro.html'
]

for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r') as file:
        content = file.read()
    
    # 1. container
    content = re.sub(
        r'class="w-full max-w-\[1280px\] px-4 md:px-10 py-3 flex items-center"',
        r'class="w-full max-w-[1280px] px-4 md:px-10 py-3 flex items-center justify-between"',
        content
    )
    
    # 2. logo text -> image
    logo_pattern = r'<div class="flex items-center gap-2 text-\[#0d121c\] dark:text-white flex-shrink-0 mr-auto">\s*<h2.*?>\s*Gia Viet English Language Center\s*</h2>\s*</div>'
    new_logo = '<div class="flex items-center gap-2 flex-shrink-0 md:w-48">\n<img src="logo.png" alt="Gia Viet" class="h-10 w-auto object-contain">\n</div>'
    content = re.sub(logo_pattern, new_logo, content, flags=re.DOTALL)
    
    # 3. nav container
    content = re.sub(
        r'<div class="hidden md:flex items-center gap-6 whitespace-nowrap ml-8">',
        r'<div class="hidden md:flex flex-1 items-center justify-center gap-6 whitespace-nowrap mx-4">',
        content
    )
    
    # 4. the button at the end
    btn_pattern = r'(<a[^>]*Hệ thống & Hỗ trợ.*?</a>)\s*(<button[^>]*>.*?Đăng nhập.*?<\/button>)\s*<\/div>'
    def replace_btn(match):
        a_tag = match.group(1)
        btn_tag = match.group(2)
        # remove ml-4 from btn
        btn_tag = btn_tag.replace(' ml-4"', '"')
        return f'{a_tag}\n</div>\n<div class="flex-shrink-0 md:w-48 flex justify-end">\n{btn_tag}\n</div>'
    
    content, count = re.subn(btn_pattern, replace_btn, content, flags=re.DOTALL)
    if count == 0:
        # no button case
        no_btn_pattern = r'(<a[^>]*Hệ thống & Hỗ trợ.*?</a>)\s*<\/div>'
        content = re.sub(no_btn_pattern, r'\1\n</div>\n<div class="flex-shrink-0 md:w-48"></div>', content, flags=re.DOTALL)

    with open(f, 'w') as file:
        file.write(content)

print("Done")
