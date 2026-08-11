import os
import re

files_to_update = [
    '/Users/vobac/Downloads/gia-viet-handbook/ve-gia-viet.html',
    '/Users/vobac/Downloads/gia-viet-handbook/quy-dinh-tac-phong.html',
    '/Users/vobac/Downloads/gia-viet-handbook/che-do-luong-thuong.html',
    '/Users/vobac/Downloads/gia-viet-handbook/dai-ngo-giao-vien.html',
    '/Users/vobac/Downloads/gia-viet-handbook/cac-chinh-sach-ho-tro.html'
]

index_file = '/Users/vobac/Downloads/gia-viet-handbook/index.html'

with open(index_file, 'r') as f:
    index_content = f.read()

# Extract footer
match = re.search(r'(<footer\b[^>]*>.*?</footer>)', index_content, re.DOTALL)
if match:
    footer_content = match.group(1)
    
    for file_path in files_to_update:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
            
            # If footer already exists, skip or replace. Let's assume it doesn't exist.
            if '<footer' not in content:
                # Insert before </main>
                content = content.replace('</main>', f'{footer_content}\n</main>')
                with open(file_path, 'w') as f:
                    f.write(content)
                print(f"Added footer to {os.path.basename(file_path)}")
else:
    print("Could not find footer in index.html")
