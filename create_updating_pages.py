import re
import os

with open('app-gia-viet.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Pages to create
pages = [
    {
        'filename': 'to-chuc-nhan-su.html',
        'title': 'Tổ chức & Nhân sự',
        'nav_id': 'nav-to-chuc'
    },
    {
        'filename': 'chinh-sach-phuc-loi.html',
        'title': 'Chính sách & Phúc lợi',
        'nav_id': 'nav-chinh-sach'
    }
]

for page in pages:
    content = template
    # Replace title tag
    content = re.sub(r'<title>.*?</title>', f'<title>{page["title"]} - Handbook</title>', content)
    
    # Replace breadcrumbs and heading
    content = re.sub(
        r'<h1 class="text-3xl md:text-4xl font-bold text-\[#00174f\] mb-6 font-display tracking-wide">App Gia Việt</h1>',
        f'<h1 class="text-3xl md:text-4xl font-bold text-[#00174f] mb-6 font-display tracking-wide">{page["title"]}</h1>',
        content
    )
    # The breadcrumb in app-gia-viet.html:
    # <span class="material-symbols-outlined text-sm">chevron_right</span>
    # <a href="#" class="hover:text-primary transition-colors whitespace-nowrap">Hệ thống & Hỗ trợ</a> <span class="material-symbols-outlined text-sm">chevron_right</span> <span class="text-[#0d121c] whitespace-nowrap">App Gia Việt</span>
    
    # We want to replace it with just:
    # <span class="material-symbols-outlined text-sm">chevron_right</span>
    # <span class="text-[#0d121c] whitespace-nowrap">{page["title"]}</span>
    
    content = re.sub(
        r'<a href="#" class="hover:text-primary transition-colors whitespace-nowrap">Hệ thống & Hỗ trợ</a> <span class="material-symbols-outlined text-sm">chevron_right</span> <span class="text-\[#0d121c\] whitespace-nowrap">App Gia Việt</span>',
        f'<span class="text-[#0d121c] whitespace-nowrap">{page["title"]}</span>',
        content
    )
    
    # Replace main updating message
    content = re.sub(
        r'Trang <strong class="text-primary">App Gia Việt</strong> hiện đang trong quá trình xây dựng',
        f'Trang <strong class="text-primary">{page["title"]}</strong> hiện đang trong quá trình xây dựng',
        content
    )

    # Clean up the sidebar
    # First, make App Gia Viet not active anymore
    content = content.replace(
        '''<a href="app-gia-viet.html" class="text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-primary before:mr-2">App Gia Việt</a>''',
        '''<a href="app-gia-viet.html" class="hover:text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-gray-300 before:mr-2 hover:before:bg-primary">App Gia Việt</a>'''
    )
    content = content.replace(
        '''<a href="#" class="hover:text-primary transition-colors flex items-center group font-medium text-[#00174f]">Hệ thống & Hỗ trợ</a>''',
        '''<a href="he-thong-ho-tro.html" class="hover:text-primary transition-colors flex items-center group">Hệ thống & Hỗ trợ</a>'''
    )

    # Now make the correct section active
    if page['title'] == 'Tổ chức & Nhân sự':
        content = content.replace(
            '''<a href="#" class="hover:text-primary transition-colors flex items-center group">Tổ\n                                        chức & Nhân sự</a>''',
            '''<a href="to-chuc-nhan-su.html" class="text-primary transition-colors flex items-center group font-medium text-[#00174f]">Tổ chức & Nhân sự</a>'''
        )
        content = content.replace(
            '''<a href="#" class="hover:text-primary transition-colors flex items-center group">Tổ chức & Nhân sự</a>''',
             '''<a href="to-chuc-nhan-su.html" class="text-primary transition-colors flex items-center group font-medium text-[#00174f]">Tổ chức & Nhân sự</a>'''
        )
    elif page['title'] == 'Chính sách & Phúc lợi':
        content = content.replace(
            '''<a href="#" class="hover:text-primary transition-colors flex items-center group">Chính sách & Phúc lợi</a>''',
            '''<a href="chinh-sach-phuc-loi.html" class="text-primary transition-colors flex items-center group font-medium text-[#00174f]">Chính sách & Phúc lợi</a>'''
        )

    # Also update the navigation link for this page to point to the new html file! (In the active file itself)
    # But wait, we want to update all HTML files to have these links in the header anyway.
    
    with open(page['filename'], 'w', encoding='utf-8') as f:
        f.write(content)

print("Created pages.")
