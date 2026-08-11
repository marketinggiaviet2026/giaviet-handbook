import re

src = '/Users/vobac/Downloads/gia-viet-handbook/du-gio-dong-nghiep.html'
dest = '/Users/vobac/Downloads/gia-viet-handbook/mentoring-1-1.html'

with open(src, 'r', encoding='utf-8') as f:
    src_content = f.read()

header_match = re.search(r'(<header.*?</header>)', src_content, re.DOTALL)
if header_match:
    good_header = header_match.group(1)
    
    with open(dest, 'r', encoding='utf-8') as f:
        dest_content = f.read()
    
    dest_content = re.sub(r'<header.*?</header>', good_header, dest_content, flags=re.DOTALL)
    
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(dest_content)
    print("Successfully replaced header in mentoring-1-1.html with correct active state.")
else:
    print("Could not find header in source.")
