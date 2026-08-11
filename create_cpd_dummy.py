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

def generate_placeholder_page(title, filename):
    content, start_idx, end_idx = get_template()
    content = content.replace('<title>Giáo trình & Tài liệu giảng dạy - Handbook</title>', f'<title>{title} - Handbook</title>')
    breadcrumbs_full = f'<a href="#" class="hover:text-primary transition-colors whitespace-nowrap">Đào tạo & Đảm bảo chất lượng</a> <span class="material-symbols-outlined text-sm">chevron_right</span> <span class="text-[#0d121c] whitespace-nowrap">{title}</span>'
    empty_html = f"""
    <div class="flex flex-col items-center justify-center py-20 px-4 text-center">
        <div class="w-32 h-32 bg-blue-50 text-blue-300 rounded-full flex flex-col items-center justify-center mb-6 border-4 border-white shadow-lg animate-pulse">
            <span class="material-symbols-outlined text-[60px]">construction</span>
        </div>
        <h2 class="text-3xl font-bold font-display text-[#00174f] mb-4">Đang cập nhật nội dung</h2>
        <p class="text-gray-500 max-w-md text-base">Trang <strong class="text-primary">{title}</strong> hiện đang trong quá trình xây dựng và hoàn thiện. Vui lòng quay lại sau nhé!</p>
        <button onclick="window.location.href='index.html'" class="mt-8 px-6 py-3 bg-primary text-white font-medium rounded-full hover:bg-blue-700 transition-colors shadow-sm flex items-center gap-2">
            <span class="material-symbols-outlined">home</span> Về trang chủ
        </button>
    </div>
    """
    new_section = f"""<!-- Breadcrumb & Title Area -->
            <div class="w-full bg-white py-12 px-4 md:px-10 border-b border-gray-100 shadow-sm relative overflow-hidden">
                <div class="absolute right-0 top-0 w-64 h-64 bg-blue-50/50 rounded-full translate-x-1/2 -translate-y-1/2 opacity-50"></div>
                <div class="w-full max-w-[1280px] mx-auto relative z-10 font-body">
                    <h1 class="text-3xl md:text-4xl font-bold text-[#00174f] mb-6 font-display tracking-wide">{title}</h1>
                    <div class="flex items-center gap-2 text-[15px] text-gray-500 font-body flex-wrap">
                        <a href="index.html" class="flex items-center hover:text-primary transition-colors"><span class="material-symbols-outlined text-[18px]">home</span><span class="ml-1">Trang chủ</span></a>
                        <span class="material-symbols-outlined text-sm">chevron_right</span>{breadcrumbs_full}
                    </div>
                </div>
            </div>
            <!-- 2 Column Layout -->
            <div class="w-full max-w-[1440px] px-4 md:px-10 py-16 mx-auto">
                <div class="flex flex-col md:flex-row gap-8 lg:gap-16 items-start">
                    <!-- Left Column: Content -->
                    <div class="w-full md:w-[70%] lg:w-[75%] bg-white rounded-xl shadow-[0_2px_20px_rgba(0,0,0,0.03)] border border-gray-100/50 overflow-hidden min-h-[500px] flex items-center justify-center">
                        {empty_html}
                    </div>
                    <!-- Right Column: Sidebar -->"""
    final_content = content[:start_idx] + new_section + content[end_idx:]
    with open(f'/Users/vobac/Downloads/gia-viet-handbook/{filename}', 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"Created {filename}")

if __name__ == '__main__':
    generate_placeholder_page("Chương trình CPD", "cpd.html")
