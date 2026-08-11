import os
import re

html_files = [
    '/Users/vobac/Downloads/gia-viet-handbook/index.html',
    '/Users/vobac/Downloads/gia-viet-handbook/ve-gia-viet.html',
    '/Users/vobac/Downloads/gia-viet-handbook/quy-dinh-tac-phong.html',
    '/Users/vobac/Downloads/gia-viet-handbook/che-do-luong-thuong.html',
    '/Users/vobac/Downloads/gia-viet-handbook/dai-ngo-giao-vien.html',
    '/Users/vobac/Downloads/gia-viet-handbook/cac-chinh-sach-ho-tro.html'
]

for file_path in html_files:
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        
        # fix Logo.png
        content = content.replace('src="picture/logo.png"', 'src="picture/Logo.png"')
        
        # fix ve gia viet banner
        content = content.replace("url('picture/banner-ve-gia-viet.png')", "url('picture/banner-ve-gia-viet.jpg')")
        
        with open(file_path, 'w') as f:
            f.write(content)
        
print("Updated HTML files with exact image filenames from picture folder.")
