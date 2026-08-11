import glob
import os

def update_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Header Link Update
    header_target = '<a href="#" class="text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-primary transition-colors">Giáo trình & Tài liệu giảng dạy</a>'
    header_repl = '<a href="giao-trinh-tai-lieu.html" class="text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-primary transition-colors">Giáo trình & Tài liệu giảng dạy</a>'
    content = content.replace(header_target, header_repl)
    
    # 2. Sidebar Link Update
    # Find: <li><a href="#" class="hover:text-primary transition-colors flex items-center group">Đào tạo & Đảm bảo chất lượng</a></li>
    is_active = os.path.basename(filepath) == 'giao-trinh-tai-lieu.html'
    active_class = "text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-primary before:mr-2"
    inactive_class = "hover:text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-gray-300 before:mr-2 hover:before:bg-primary"
    
    item_class = active_class if is_active else inactive_class
    
    sidebar_target = '<li><a href="#" class="hover:text-primary transition-colors flex items-center group">Đào tạo & Đảm bảo chất lượng</a></li>'
    if sidebar_target in content:
        sidebar_repl = f"""<li class="flex flex-col gap-3">
                            <a href="#" class="hover:text-primary transition-colors flex items-center group">Đào tạo & Đảm bảo chất lượng</a>
                            <ul class="flex flex-col gap-3 pl-4 border-l-2 border-gray-100 font-normal text-sm text-gray-500">
                                <li><a href="giao-trinh-tai-lieu.html" class="{item_class}">Giáo trình & Tài liệu giảng dạy</a></li>
                            </ul>
                        </li>"""
        content = content.replace(sidebar_target, sidebar_repl)
    else:
        # Maybe it's already expanded?
        pass

    # Additionally, on giao-trinh-tai-lieu.html, the "Quy định tác phong" might still be marked active from the copy-paste
    if is_active:
        wrong_active = 'href="quy-dinh-tac-phong.html" class="text-primary transition-colors flex items-center before:content-[\'\'] before:w-1.5 before:h-1.5 before:rounded-full before:bg-primary before:mr-2"'
        correct_inactive = 'href="quy-dinh-tac-phong.html" class="hover:text-primary transition-colors flex items-center before:content-[\'\'] before:w-1.5 before:h-1.5 before:rounded-full before:bg-gray-300 before:mr-2 hover:before:bg-primary"'
        content = content.replace(wrong_active, correct_inactive)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated links in {filepath}")

if __name__ == '__main__':
    html_files = glob.glob('/Users/vobac/Downloads/gia-viet-handbook/*.html')
    for file in html_files:
        if 'index.html' not in file:
            update_links(file)
    
    update_links('/Users/vobac/Downloads/gia-viet-handbook/index.html')
