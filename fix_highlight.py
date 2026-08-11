import re

files_to_fix = [
    ('to-chuc-nhan-su.html', 'nav-to-chuc'),
    ('chinh-sach-phuc-loi.html', 'nav-chinh-sach')
]

for filename, active_id in files_to_fix:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Make nav-he-thong normal
    content = content.replace(
        '''<a id="nav-he-thong" class="text-primary text-sm font-bold border-b-2 border-primary pb-0.5 whitespace-nowrap flex items-center gap-1 cursor-pointer"''',
        '''<a id="nav-he-thong" class="text-[#0d121c] dark:text-gray-300 text-sm font-medium hover:text-primary transition-colors whitespace-nowrap flex items-center gap-1 cursor-pointer"'''
    )
    
    # Make active_id highlighted
    content = re.sub(
        rf'<a id="{active_id}" class="text-\[#0d121c\] dark:text-gray-300 text-sm font-medium hover:text-primary transition-colors whitespace-nowrap flex items-center gap-1 cursor-pointer"',
        f'<a id="{active_id}" class="text-primary text-sm font-bold border-b-2 border-primary pb-0.5 whitespace-nowrap flex items-center gap-1 cursor-pointer"',
        content
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed header highlights text.")
