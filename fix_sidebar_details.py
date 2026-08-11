import glob
import os

def fix_ve_gia_viet_title(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace Title
    content = content.replace(
        '<h1 class="text-3xl md:text-4xl font-bold text-[#00174f] mb-6 font-display tracking-wide">Sứ mệnh - Tầm nhìn</h1>',
        '<h1 class="text-3xl md:text-4xl font-bold text-[#00174f] mb-6 font-display tracking-wide">Về Gia Việt</h1>'
    )
    
    # 2. Replace Breadcrumb
    breadcrumb_old = """<a href="#" class="hover:text-primary transition-colors">Về Gia Việt</a>
                <span class="material-symbols-outlined text-sm">chevron_right</span>
                <span class="text-[#0d121c]">Sứ mệnh - Tầm nhìn</span>"""
    breadcrumb_new = """<span class="text-[#0d121c]">Về Gia Việt</span>"""
    content = content.replace(breadcrumb_old, breadcrumb_new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def add_to_sidebar(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if "Về Gia Việt" is already in the sidebar list (to avoid duplicates)
    # The sidebar starts with:
    # <h3 class="text-[#00174f] text-2xl font-bold font-display mb-6 tracking-tight">Danh mục bài viết</h3>
    # <ul class="flex flex-col gap-5 font-body text-[16px] font-bold text-[#00174f]">
    
    target_str = '<h3 class="text-[#00174f] text-2xl font-bold font-display mb-6 tracking-tight">Danh mục bài viết</h3>\n                    <ul class="flex flex-col gap-5 font-body text-[16px] font-bold text-[#00174f]">'
    
    # Some older files might lack the newline indentation exactly like this, use robust matching
    if target_str in content:
        # Determine if it's ve-gia-viet.html for active highlighting
        is_active = os.path.basename(filepath) == 've-gia-viet.html'
        
        if is_active:
            item_html = '<li><a href="ve-gia-viet.html" class="text-primary transition-colors flex items-center before:content-[\'\'] before:w-1.5 before:h-1.5 before:rounded-full before:bg-primary before:mr-2">Về Gia Việt</a></li>'
        else:
            item_html = '<li><a href="ve-gia-viet.html" class="hover:text-primary transition-colors flex items-center group">Về Gia Việt</a></li>'
            
        replacement = target_str + '\n                        ' + item_html
        
        if 'href="ve-gia-viet.html" class="' not in content[content.find(target_str):content.find(target_str)+500]:
            content = content.replace(target_str, replacement)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added sidebar item to {filepath}")
        else:
            print(f"Item already exists in {filepath}")
    else:
        # Try a more relaxed string match
        target_str2 = '<ul class="flex flex-col gap-5 font-body text-[16px] font-bold text-[#00174f]">'
        if target_str2 in content:
            idx = content.find(target_str2)
            
            if 'href="ve-gia-viet.html"' not in content[idx:idx+300]:
                is_active = os.path.basename(filepath) == 've-gia-viet.html'
                if is_active:
                    item_html = '<li><a href="ve-gia-viet.html" class="text-primary transition-colors flex items-center before:content-[\'\'] before:w-1.5 before:h-1.5 before:rounded-full before:bg-primary before:mr-2">Về Gia Việt</a></li>'
                else:
                    item_html = '<li><a href="ve-gia-viet.html" class="hover:text-primary transition-colors flex items-center group">Về Gia Việt</a></li>'
                
                content = content.replace(target_str2, target_str2 + '\n                        ' + item_html, 1) # replace only first occurrence
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Added sidebar item (relaxed) to {filepath}")
        else:
            print(f"Could not find sidebar target in {filepath}")


if __name__ == '__main__':
    ve_gia_viet_path = '/Users/vobac/Downloads/gia-viet-handbook/ve-gia-viet.html'
    fix_ve_gia_viet_title(ve_gia_viet_path)
    print("Fixed title and breadcrumbs for ve-gia-viet.html")
    
    html_files = glob.glob('/Users/vobac/Downloads/gia-viet-handbook/*.html')
    for file in html_files:
        if 'index.html' not in file:
            add_to_sidebar(file)
            
