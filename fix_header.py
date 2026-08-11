import glob
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The string to replace:
    # <div class="hidden md:flex flex-1 items-center justify-center gap-6 whitespace-nowrap mx-4">
    # Replace justify-center with justify-start, adjust gap to gap-4 lg:gap-6, and increase left margin slightly so it's not glued to the logo
    
    pattern = r'<div class="hidden md:flex flex-1 items-center justify-center gap-6 whitespace-nowrap mx-4">'
    replacement = r'<div class="hidden md:flex flex-1 items-center justify-start gap-4 xl:gap-6 whitespace-nowrap ml-8 mr-4">'
    
    if pattern in content:
        content = content.replace(pattern, replacement)
        
        # Also, let's make sure the search and login button don't overflow on small screens by adding some flex-wrap or just keeping it compact.
        # But for now, justify-start and gap-4 xl:gap-6 should easily fit.
        
        # We also need to fix if the pattern was slightly different, e.g. already modified. Use regex to be safe:
    else:
        # Regex replacement in case of slight variations
        content, count = re.subn(
            r'class="hidden md:flex flex-1 items-center justify-center gap-6 whitespace-nowrap mx-4"',
            r'class="hidden md:flex flex-1 items-center justify-start gap-4 xl:gap-6 whitespace-nowrap ml-4 lg:ml-8 mr-4"',
            content
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

html_files = glob.glob('/Users/vobac/Downloads/gia-viet-handbook/*.html')
for f in html_files:
    process_file(f)
print("All files processed!")
