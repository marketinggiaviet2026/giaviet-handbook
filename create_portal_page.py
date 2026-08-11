import os

TEMPLATE_PATH = '/Users/vobac/Downloads/gia-viet-handbook/giao-trinh-tai-lieu.html'

def get_template():
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    start_str = '<!-- Breadcrumb & Title Area -->'
    end_str = '<!-- Right Column: Sidebar -->'
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    return content, start_idx, end_idx

def generate_portal():
    content, start_idx, end_idx = get_template()
    # Replace title
    content = content.replace(
        '<title>Giáo trình & Tài liệu giảng dạy - Handbook</title>',
        f'<title>Hệ thống & Hỗ trợ - Handbook</title>'
    )
    
    breadcrumbs_full = f'<span class="text-[#0d121c] whitespace-nowrap">Hệ thống & Hỗ trợ</span>'
    
    # Let's create an elegant grid layout with 3 portal cards
    portal_html = """
    <div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">
        <span class="text-primary font-bold tracking-wider uppercase text-sm font-body bg-blue-50 w-max px-3 py-1 rounded-full border border-blue-100">TRUNG TÂM GIA VIỆT</span>
        <h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display mt-2 mb-2">HỆ THỐNG & CÔNG CỤ HỖ TRỢ</h2>
        <p class="text-[15px] text-gray-500 max-w-2xl">Trang tổng hợp toàn bộ các tiện ích, ứng dụng và kênh hỗ trợ chính thức dành cho Giáo viên trong quá trình công tác tại Gia Việt.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
        <!-- Card 1: App Gia Viet -->
        <a href="app-gia-viet.html" class="bg-gradient-to-br from-blue-500 to-blue-700 rounded-2xl p-6 relative overflow-hidden group hover:shadow-xl hover:-translate-y-2 transition-all duration-300 flex flex-col h-[200px]">
            <div class="absolute right-0 top-0 opacity-20 group-hover:opacity-30 transition-opacity translate-x-1/4 -translate-y-1/4 group-hover:scale-110 duration-500">
                <span class="material-symbols-outlined text-[150px] text-white">smartphone</span>
            </div>
            <div class="w-12 h-12 bg-white/20 rounded-xl backdrop-blur-sm flex items-center justify-center text-white mb-4 shadow-sm border border-white/30">
                <span class="material-symbols-outlined text-2xl">apps</span>
            </div>
            <h3 class="text-white font-bold text-xl font-display mb-2 relative z-10">App Gia Việt</h3>
            <p class="text-blue-100 text-[13px] relative z-10 mt-auto flex items-center gap-1 group-hover:gap-2 transition-all">Truy cập ứng dụng <span class="material-symbols-outlined text-[16px]">arrow_forward</span></p>
        </a>

        <!-- Card 2: In ấn -->
        <a href="quy-dinh-in-an.html" class="bg-gradient-to-br from-emerald-500 to-teal-600 rounded-2xl p-6 relative overflow-hidden group hover:shadow-xl hover:-translate-y-2 transition-all duration-300 flex flex-col h-[200px]">
            <div class="absolute right-0 top-0 opacity-20 group-hover:opacity-30 transition-opacity translate-x-1/4 -translate-y-1/4 group-hover:scale-110 duration-500">
                <span class="material-symbols-outlined text-[150px] text-white">print</span>
            </div>
            <div class="w-12 h-12 bg-white/20 rounded-xl backdrop-blur-sm flex items-center justify-center text-white mb-4 shadow-sm border border-white/30">
                <span class="material-symbols-outlined text-2xl">local_printshop</span>
            </div>
            <h3 class="text-white font-bold text-xl font-display mb-2 relative z-10">Quy định in ấn & Hỗ trợ</h3>
            <p class="text-emerald-100 text-[13px] relative z-10 mt-auto flex items-center gap-1 group-hover:gap-2 transition-all">Xem chính sách <span class="material-symbols-outlined text-[16px]">arrow_forward</span></p>
        </a>

        <!-- Card 3: Góp ý -->
        <a href="gop-y-phan-hoi.html" class="bg-gradient-to-br from-orange-400 to-red-500 rounded-2xl p-6 relative overflow-hidden group hover:shadow-xl hover:-translate-y-2 transition-all duration-300 flex flex-col h-[200px]">
            <div class="absolute right-0 top-0 opacity-20 group-hover:opacity-30 transition-opacity translate-x-1/4 -translate-y-1/4 group-hover:scale-110 duration-500">
                <span class="material-symbols-outlined text-[150px] text-white">forum</span>
            </div>
            <div class="w-12 h-12 bg-white/20 rounded-xl backdrop-blur-sm flex items-center justify-center text-white mb-4 shadow-sm border border-white/30">
                <span class="material-symbols-outlined text-2xl">rate_review</span>
            </div>
            <h3 class="text-white font-bold text-xl font-display mb-2 relative z-10">Kênh nhận góp ý & phản hồi</h3>
            <p class="text-orange-100 text-[13px] relative z-10 mt-auto flex items-center gap-1 group-hover:gap-2 transition-all">Gửi ý kiến đóng góp <span class="material-symbols-outlined text-[16px]">arrow_forward</span></p>
        </a>
    </div>
    """
    
    new_section = f"""<!-- Breadcrumb & Title Area -->
            <div class="w-full bg-white py-12 px-4 md:px-10 border-b border-gray-100 shadow-sm relative overflow-hidden">
                <div class="absolute right-0 top-0 w-64 h-64 bg-blue-50/50 rounded-full translate-x-1/2 -translate-y-1/2 opacity-50"></div>
                
                <div class="w-full max-w-[1280px] mx-auto relative z-10 font-body">
                    <h1 class="text-3xl md:text-4xl font-bold text-[#00174f] mb-6 font-display tracking-wide">Hệ thống & Hỗ trợ</h1>
                    <div class="flex items-center gap-2 text-[15px] text-gray-500 font-body flex-wrap">
                        <a href="index.html" class="flex items-center hover:text-primary transition-colors">
                            <span class="material-symbols-outlined text-[18px]">home</span>
                            <span class="ml-1">Trang chủ</span>
                        </a>
                        <span class="material-symbols-outlined text-sm">chevron_right</span>
                        {breadcrumbs_full}
                    </div>
                </div>
            </div>

            <!-- 2 Column Layout -->
            <div class="w-full max-w-[1440px] px-4 md:px-10 py-16 mx-auto">
                <div class="flex flex-col md:flex-row gap-8 lg:gap-16 items-start">
                    <!-- Left Column: Content -->
                    <div class="w-full md:w-[70%] lg:w-[75%] bg-white rounded-xl shadow-[0_2px_20px_rgba(0,0,0,0.03)] border border-gray-100/50 overflow-hidden">
                        <div class="p-6 md:p-10 lg:p-12">
                            {portal_html}
                        </div>
                    </div>

                    <!-- Right Column: Sidebar -->"""

    final_content = content[:start_idx] + new_section + content[end_idx:]
    
    # Active state swap for sidebar
    inactive_class = "hover:text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-gray-300 before:mr-2 hover:before:bg-primary"
    active_class = "text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-primary before:mr-2"
    
    # Also we need to DEACTIVATE the 'giao-trinh-tai-lieu.html' which might be active in the template!
    wrong_giao_trinh = f'href="giao-trinh-tai-lieu.html" class="{active_class}"'
    correct_giao_trinh = f'href="giao-trinh-tai-lieu.html" class="{inactive_class}"'
    final_content = final_content.replace(wrong_giao_trinh, correct_giao_trinh)
    
    # Note: we are currently the main index for this category, so the parent sidebar category should be active maybe?
    # Right now I'll just change the link URL of the parent:
    # `href="#" class="hover:text-primary transition-colors flex items-center group font-medium text-[#00174f]">Hệ thống & Hỗ trợ</a>`
    # We will let `update_portal_links.py` handle all linking.

    with open('/Users/vobac/Downloads/gia-viet-handbook/he-thong-ho-tro.html', 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Created he-thong-ho-tro.html")

if __name__ == '__main__':
    generate_portal()
