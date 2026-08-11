import glob
import re

replacement_html = """<div class="relative group py-2 flex items-center">
    <a class="text-[#0d121c] dark:text-gray-300 text-sm font-medium hover:text-primary transition-colors whitespace-nowrap flex items-center gap-1 cursor-pointer" href="#">
        Hệ thống & Hỗ trợ
        <span class="material-symbols-outlined text-sm transition-transform duration-300 group-hover:rotate-180">expand_more</span>
    </a>
    <div class="absolute top-full right-0 pt-2 w-72 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 transform origin-top translate-y-2 group-hover:translate-y-0 z-[100]">
        <div class="bg-white dark:bg-[#1a202c] rounded-xl shadow-[0_10px_40px_-10px_rgba(0,0,0,0.1)] border border-gray-100 dark:border-gray-700 py-2 flex flex-col relative overflow-hidden text-left">
            <a href="app-gia-viet.html" class="px-5 py-3 text-sm text-gray-600 dark:text-gray-300 hover:text-primary hover:bg-[#f8fbff] dark:hover:bg-slate-800 transition-colors font-medium border-b border-gray-50 dark:border-gray-700/50 last:border-0">App Gia Việt</a>
            <a href="quy-dinh-in-an.html" class="px-5 py-3 text-sm text-gray-600 dark:text-gray-300 hover:text-primary hover:bg-[#f8fbff] dark:hover:bg-slate-800 transition-colors font-medium border-b border-gray-50 dark:border-gray-700/50 last:border-0">Quy định in ấn & Hỗ trợ khác</a>
            <a href="gop-y-phan-hoi.html" class="px-5 py-3 text-sm text-gray-600 dark:text-gray-300 hover:text-primary hover:bg-[#f8fbff] dark:hover:bg-slate-800 transition-colors font-medium">Kênh nhận góp ý & phản hồi</a>
        </div>
    </div>
</div>"""

def inject(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The target string to replace
    target = '<a class="text-[#0d121c] dark:text-gray-300 text-sm font-medium hover:text-primary transition-colors whitespace-nowrap" href="#">Hệ thống & Hỗ trợ</a>'
    
    # Also another known variation (if missing classes or formatting differences)
    pattern = re.compile(r'<a[^>]*Hệ thống & Hỗ trợ[^<]*</a>')

    if target in content:
        content = content.replace(target, replacement_html)
    else:
        # Fallback if there was a slight difference
        content = pattern.sub(replacement_html, content)

    # I also want to make sure the right sidebar includes "Hệ thống & Hỗ trợ"
    # Actually wait! The UI sidebar doesn't have a "Hệ thống & Hỗ trợ" list! 
    # Let me check if `ve-gia-viet.html` had a sidebar entry...
    # Ah, in `ve-gia-viet.html` line 664: `<li><a href="#" class="hover:text-primary transition-colors flex items-center group">Hệ thống & Hỗ trợ</a></li>`
    
    sidebar_target = r'<li>\s*<a href="#" class="[^"]*">Hệ\s*thống\s*&\s*Hỗ\s*trợ</a>\s*</li>'
    sidebar_replacement = """<li class="flex flex-col gap-3">
                                    <a href="#" class="hover:text-primary transition-colors flex items-center group font-medium text-[#00174f]">Hệ thống & Hỗ trợ</a>
                                    <ul class="flex flex-col gap-3 pl-4 border-l-2 border-gray-100 font-normal text-sm text-gray-500">
                                        <li><a href="app-gia-viet.html" class="hover:text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-gray-300 before:mr-2 hover:before:bg-primary">App Gia Việt</a></li>
                                        <li><a href="quy-dinh-in-an.html" class="hover:text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-gray-300 before:mr-2 hover:before:bg-primary">Quy định in ấn & Hỗ trợ khác</a></li>
                                        <li><a href="gop-y-phan-hoi.html" class="hover:text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-gray-300 before:mr-2 hover:before:bg-primary">Kênh nhận góp ý & phản hồi</a></li>
                                    </ul>
                                </li>"""
    content = re.sub(sidebar_target, sidebar_replacement, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    for f in glob.glob('/Users/vobac/Downloads/gia-viet-handbook/*.html'):
        inject(f)
