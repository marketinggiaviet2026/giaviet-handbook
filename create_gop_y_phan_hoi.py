import os
import re

def create_gop_y_page():
    source_file = '/Users/vobac/Downloads/gia-viet-handbook/giao-trinh-tai-lieu.html'
    target_file = '/Users/vobac/Downloads/gia-viet-handbook/gop-y-phan-hoi.html'
    
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Title tag
    content = content.replace(
        '<title>Giáo trình & Tài liệu giảng dạy - Handbook</title>',
        '<title>Kênh nhận góp ý & phản hồi - Handbook</title>'
    )
    
    start_str = '<!-- Breadcrumb & Title Area -->'
    end_str = '<!-- Right Column: Sidebar -->'
    
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    
    if start_idx == -1 or end_idx == -1:
        print("Could not find boundaries in template!")
        return

    new_section = """<!-- Breadcrumb & Title Area -->
            <div class="w-full bg-white py-12 px-4 md:px-10 border-b border-gray-100 shadow-sm relative overflow-hidden">
                <div class="absolute right-0 top-0 w-64 h-64 bg-blue-50/50 rounded-full translate-x-1/2 -translate-y-1/2 opacity-50"></div>
                
                <div class="w-full max-w-[1280px] mx-auto relative z-10 font-body">
                    <h1 class="text-3xl md:text-4xl font-bold text-[#00174f] mb-6 font-display tracking-wide">Kênh nhận góp ý & phản hồi</h1>
                    <div class="flex items-center gap-2 text-[15px] text-gray-500 font-body flex-wrap">
                        <a href="index.html" class="flex items-center hover:text-primary transition-colors">
                            <span class="material-symbols-outlined text-[18px]">home</span>
                            <span class="ml-1">Trang chủ</span>
                        </a>
                        <span class="material-symbols-outlined text-sm">chevron_right</span>
                        <a href="#" class="hover:text-primary transition-colors whitespace-nowrap">Hệ thống & Hỗ trợ</a> 
                        <span class="material-symbols-outlined text-sm">chevron_right</span> 
                        <span class="text-[#0d121c] whitespace-nowrap">Kênh nhận góp ý & phản hồi</span>
                    </div>
                </div>
            </div>

            <!-- 2 Column Layout -->
            <div class="w-full max-w-[1440px] px-4 md:px-10 py-16 mx-auto">
                <div class="flex flex-col md:flex-row gap-8 lg:gap-16 items-start">
                    <!-- Left Column: Content -->
                    <div class="w-full md:w-[70%] lg:w-[75%] bg-white rounded-xl shadow-sm border border-gray-100/50 overflow-hidden">
                        <div class="p-6 md:p-10 lg:p-12 space-y-8">
                            
                            <!-- Introduction Alert -->
                            <div class="text-justify font-medium text-gray-700 bg-blue-50/60 border-l-4 border-primary p-6 rounded-r-xl shadow-sm">
                                Trung tâm Anh ngữ Gia Việt luôn trân trọng mọi ý kiến đóng góp, phản hồi từ Quý Thầy/Cô để không ngừng cải thiện chất lượng đào tạo, môi trường làm việc và dịch vụ hỗ trợ. Mọi thông tin phản hồi sẽ được tiếp nhận và xử lý bảo mật bởi các bộ phận chuyên trách.
                            </div>

                            <!-- Contact Methods Grid -->
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                                
                                <!-- Zalo Card -->
                                <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-6 md:p-8 space-y-6 hover:shadow-md hover:border-green-500/20 hover:-translate-y-1 transition-all duration-300">
                                    <div class="flex items-center gap-3.5 border-b border-gray-100 pb-4">
                                        <div class="w-12 h-12 rounded-xl bg-green-50 text-green-600 flex items-center justify-center shrink-0">
                                            <span class="material-symbols-outlined text-2xl font-bold">chat</span>
                                        </div>
                                        <div>
                                            <h3 class="text-xl font-bold font-display text-[#00174f] tracking-tight">KÊNH CHÁT / ZALO</h3>
                                            <p class="text-xs text-gray-400 mt-0.5">Hỗ trợ phản hồi nhanh chóng qua Zalo</p>
                                        </div>
                                    </div>
                                    
                                    <div class="space-y-4">
                                        <p class="text-sm text-gray-600">Quý Thầy/Cô có thể liên hệ trực tiếp với nhân sự phụ trách qua Zalo:</p>
                                        <div class="p-4 bg-green-50/30 rounded-xl border border-green-100/50 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
                                            <div class="flex flex-col">
                                                <span class="text-sm font-bold text-gray-800">Ms. Lê Kim Thoa</span>
                                                <span class="text-xs text-gray-400 font-medium">Bộ phận Nhân sự</span>
                                            </div>
                                            <a href="https://zalo.me/0775897997" target="_blank" class="px-4 py-2 bg-green-600 hover:bg-green-700 text-white text-xs font-bold rounded-lg shadow-sm transition-colors flex items-center justify-center gap-1.5 whitespace-nowrap">
                                                <span class="material-symbols-outlined text-sm font-bold">send</span> 0775 897 997
                                            </a>
                                        </div>
                                    </div>
                                </div>

                                <!-- Email Card -->
                                <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-6 md:p-8 space-y-6 hover:shadow-md hover:border-primary/20 hover:-translate-y-1 transition-all duration-300">
                                    <div class="flex items-center gap-3.5 border-b border-gray-100 pb-4">
                                        <div class="w-12 h-12 rounded-xl bg-blue-50 text-primary flex items-center justify-center shrink-0">
                                            <span class="material-symbols-outlined text-2xl font-bold">mail</span>
                                        </div>
                                        <div>
                                            <h3 class="text-xl font-bold font-display text-[#00174f] tracking-tight">HÒM THƯ ĐIỆN TỬ</h3>
                                            <p class="text-xs text-gray-400 mt-0.5">Gửi góp ý chính thức qua Email</p>
                                        </div>
                                    </div>
                                    
                                    <div class="space-y-4">
                                        <p class="text-sm text-gray-600">Quý Thầy/Cô gửi thư góp ý hoặc phản hồi chi tiết về các địa chỉ:</p>
                                        <div class="flex flex-col gap-3">
                                            <div class="p-4 bg-blue-50/30 rounded-xl border border-blue-100/50 flex flex-col gap-1 hover:border-primary/30 transition-colors">
                                                <span class="text-xs font-bold text-gray-400 uppercase tracking-wider">Hòm thư Nhân sự (HR)</span>
                                                <a href="mailto:givihumanresources@gmail.com" class="text-sm font-bold text-primary hover:underline break-all">givihumanresources@gmail.com</a>
                                            </div>
                                            <div class="p-4 bg-blue-50/30 rounded-xl border border-blue-100/50 flex flex-col gap-1 hover:border-primary/30 transition-colors">
                                                <span class="text-xs font-bold text-gray-400 uppercase tracking-wider">Hòm thư chung Trung tâm</span>
                                                <a href="mailto:info@giaviet.edu.vn" class="text-sm font-bold text-primary hover:underline break-all">info@giaviet.edu.vn</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                            </div>

                            <!-- Feedback Guidelines -->
                            <div class="bg-gray-50 border border-gray-200 rounded-2xl p-6 md:p-8 space-y-6">
                                <h3 class="text-lg font-bold font-display text-[#00174f] border-b border-gray-200 pb-2 flex items-center gap-2">
                                    <span class="material-symbols-outlined text-primary text-[22px]">info</span>
                                    Lưu ý khi gửi thông tin góp ý & phản hồi
                                </h3>
                                
                                <ul class="space-y-4 text-sm text-gray-600 pl-2">
                                    <li class="flex items-start gap-3">
                                        <span class="material-symbols-outlined text-primary text-[18px] mt-0.5">check_circle</span>
                                        <span><strong>Nội dung rõ ràng:</strong> Mô tả cụ thể sự việc, tình huống hoặc đề xuất để bộ phận phụ trách có đầy đủ thông tin xử lý.</span>
                                    </li>
                                    <li class="flex items-start gap-3">
                                        <span class="material-symbols-outlined text-primary text-[18px] mt-0.5">check_circle</span>
                                        <span><strong>Đính kèm minh chứng (nếu có):</strong> Khuyến khích đính kèm hình ảnh, ảnh chụp màn hình hoặc tài liệu liên quan để làm rõ phản hồi.</span>
                                    </li>
                                    <li class="flex items-start gap-3">
                                        <span class="material-symbols-outlined text-primary text-[18px] mt-0.5">check_circle</span>
                                        <span><strong>Bảo mật thông tin:</strong> Gia Việt cam kết bảo mật danh tính của người góp ý/phản hồi theo quy định của Trung tâm.</span>
                                    </li>
                                </ul>
                            </div>
                            
                        </div>
                    </div>

                    <!-- Right Column: Sidebar -->"""

    final_content = content[:start_idx] + new_section + content[end_idx:]

    # Sidebar active highlight classes swap
    inactive_class = "hover:text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-gray-300 before:mr-2 hover:before:bg-primary"
    active_class = "text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-primary before:mr-2"
    
    # Deactivate the active class in sidebar (which belongs to quy-dinh-tac-phong.html in template)
    final_content = re.sub(
        r'(<li>\s*<a[^>]*href="quy-dinh-tac-phong.html"[^>]*)\s+class="[^"]*"',
        rf'\1 class="{inactive_class}"',
        final_content
    )
    
    # Replace the sidebar Hệ thống & Hỗ trợ menu list completely to have correct links & active highlight
    sidebar_pattern = re.compile(
        r'(<a[^>]*href="[^"]*"[^>]*>Hệ\s*thống\s*&\s*Hỗ\s*trợ</a>\s*<ul[^>]*>).*?(</ul>)',
        re.DOTALL
    )
    
    sidebar_replacement = r"""\1
                                        <li><a href="app-gia-viet.html" class="hover:text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-gray-300 before:mr-2 hover:before:bg-primary">App Gia Việt</a></li>
                                        <li><a href="quy-dinh-in-an.html" class="hover:text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-gray-300 before:mr-2 hover:before:bg-primary">Quy định in ấn & Hỗ trợ khác</a></li>
                                        <li><a href="gop-y-phan-hoi.html" class="text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-primary before:mr-2">Kênh nhận góp ý & phản hồi</a></li>
                                    \2"""
    final_content = sidebar_pattern.sub(sidebar_replacement, final_content)

    # Header navigation active highlighting swap:
    # 1) Make nav-to-chuc normal (inactive)
    final_content = re.sub(
        r'id="nav-to-chuc"\s+class="[^"]*"',
        'id="nav-to-chuc" class="text-[#0d121c] dark:text-gray-300 text-sm font-medium hover:text-primary transition-colors whitespace-nowrap flex items-center gap-1 cursor-pointer"',
        final_content
    )
    # 2) Make nav-he-thong highlighted (active)
    final_content = re.sub(
        r'id="nav-he-thong"\s+class="[^"]*"',
        'id="nav-he-thong" class="text-primary text-sm font-bold border-b-2 border-primary pb-0.5 whitespace-nowrap flex items-center gap-1 cursor-pointer"',
        final_content
    )

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    print("Successfully generated gop-y-phan-hoi.html")

if __name__ == '__main__':
    create_gop_y_page()
