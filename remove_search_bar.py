import glob
import re

pattern = re.compile(r'<!-- From Uiverse\.io by vinodjangid07 -->\s*<div class="InputContainer ml-2 hidden md:flex">\s*<input placeholder="Tìm kiếm\.\.\." id="input" class="input" name="text" type="text" autocomplete="off">\s*</div>', re.DOTALL)

for filepath in glob.glob('/Users/vobac/Downloads/gia-viet-handbook/*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = pattern.sub('', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Search bar successfully removed from all pages.")
