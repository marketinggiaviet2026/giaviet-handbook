import glob

def fix_breakpoints(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We find the 2 column layout definitions
    # <div class="flex flex-col lg:flex-row gap-16 items-start">
    # <div class="w-full lg:w-[75%] bg-white rounded-xl shadow-sm border border-gray-100/50 overflow-hidden">
    # <div class="w-full lg:w-[25%] flex flex-col gap-10 mt-4 lg:mt-0 sticky top-32 self-start">
    
    target1 = 'class="flex flex-col lg:flex-row gap-16 items-start"'
    repl1 = 'class="flex flex-col md:flex-row gap-8 lg:gap-16 items-start"'
    
    target2 = 'class="w-full lg:w-[75%] bg-white rounded-xl shadow-sm border border-gray-100/50 overflow-hidden"'
    repl2 = 'class="w-full md:w-[70%] lg:w-[75%] bg-white rounded-xl shadow-sm border border-gray-100/50 overflow-hidden"'
    
    target3 = 'class="w-full lg:w-[25%] flex flex-col gap-10 mt-4 lg:mt-0 sticky top-32 self-start"'
    repl3 = 'class="w-full md:w-[30%] lg:w-[25%] flex flex-col gap-10 mt-8 md:mt-0 sticky top-32 self-start"'
    
    # Without sticky (if the previous script missed it)
    target3_alt = 'class="w-full lg:w-[25%] flex flex-col gap-10 mt-4 lg:mt-0"'
    repl3_alt = 'class="w-full md:w-[30%] lg:w-[25%] flex flex-col gap-10 mt-8 md:mt-0 sticky top-32 self-start"'
    
    modified = False
    if target1 in content:
        content = content.replace(target1, repl1)
        modified = True
    if target2 in content:
        content = content.replace(target2, repl2)
        modified = True
    if target3 in content:
        content = content.replace(target3, repl3)
        modified = True
    elif target3_alt in content:
        content = content.replace(target3_alt, repl3_alt)
        modified = True
        
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Skipped {filepath}")

if __name__ == '__main__':
    html_files = glob.glob('/Users/vobac/Downloads/gia-viet-handbook/*.html')
    for file in html_files:
        if 'index.html' not in file:
            fix_breakpoints(file)
