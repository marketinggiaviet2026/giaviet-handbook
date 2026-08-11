import os

files = [
    '/Users/vobac/Downloads/gia-viet-handbook/index.html',
    '/Users/vobac/Downloads/gia-viet-handbook/ve-gia-viet.html',
    '/Users/vobac/Downloads/gia-viet-handbook/quy-dinh-tac-phong.html',
    '/Users/vobac/Downloads/gia-viet-handbook/che-do-luong-thuong.html',
    '/Users/vobac/Downloads/gia-viet-handbook/dai-ngo-giao-vien.html',
    '/Users/vobac/Downloads/gia-viet-handbook/cac-chinh-sach-ho-tro.html'
]

for f in files:
    if os.path.exists(f):
        with open(f, 'r') as file:
            content = file.read()
            content = content.replace('src="logo.png"', 'src="picture/logo.png"')
        with open(f, 'w') as file:
            file.write(content)
print("Updated logo path")
