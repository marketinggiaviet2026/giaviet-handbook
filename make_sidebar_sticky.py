import glob

def make_sidebar_sticky(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We find the Sidebar column definition
    # <div class="w-full lg:w-[25%] flex flex-col gap-10 mt-4 lg:mt-0">
    
    target = '<div class="w-full lg:w-[25%] flex flex-col gap-10 mt-4 lg:mt-0">'
    replacement = '<div class="w-full lg:w-[25%] flex flex-col gap-10 mt-4 lg:mt-0 sticky top-32 self-start">'
    
    if target in content:
        content = content.replace(target, replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        # Check if already updated
        if "sticky top-32" in content and "w-full lg:w-[25%]" in content:
            print(f"Already sticky in {filepath}")
        else:
            print(f"Could not find exact target in {filepath}")

if __name__ == '__main__':
    html_files = glob.glob('/Users/vobac/Downloads/gia-viet-handbook/*.html')
    for file in html_files:
        if 'index.html' not in file:
            make_sidebar_sticky(file)
