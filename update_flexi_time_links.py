import os
import glob

html_files = glob.glob('/Users/vobac/Downloads/gia-viet-handbook/*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    old_menu_link = '<a href="#" class="text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-primary transition-colors">Flexi-time</a>'
    new_menu_link = '<a href="flexi-time.html" class="text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-primary transition-colors">Flexi-time</a>'
    
    old_footer_link = '<li><a class="hover:text-white transition-colors" href="#">Flexi-time English Program</a></li>'
    new_footer_link = '<li><a class="hover:text-white transition-colors" href="flexi-time.html">Flexi-time English Program</a></li>'
    
    content = content.replace(old_menu_link, new_menu_link)
    content = content.replace(old_footer_link, new_footer_link)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
        
print(f"Updated Flexi-time links in {len(html_files)} HTML files.")
