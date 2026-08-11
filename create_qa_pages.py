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

def generate_page(filename, title, breadcrumb_label, html_content):
    content, start_idx, end_idx = get_template()
    # Replace the <title> tag properly
    import re
    title_pattern = re.compile(r'<title>.*?</title>')
    content = title_pattern.sub(f'<title>{title} - Handbook</title>', content)
    
    breadcrumbs_full = f'<a href="dao-tao-dam-bao-chat-luong.html" class="hover:text-primary transition-colors whitespace-nowrap">Đào tạo & Đảm bảo chất lượng</a> <span class="material-symbols-outlined text-sm">chevron_right</span> <span class="text-[#0d121c] whitespace-nowrap">{breadcrumb_label}</span>'
    
    new_section = f"""<!-- Breadcrumb & Title Area -->
            <div class="w-full bg-white py-12 px-4 md:px-10 border-b border-gray-100 shadow-sm relative overflow-hidden">
                <div class="absolute right-0 top-0 w-64 h-64 bg-blue-50/50 rounded-full translate-x-1/2 -translate-y-1/2 opacity-50"></div>
                <div class="absolute right-0 top-0 w-32 h-32 text-blue-100 translate-x-1/4 -translate-y-1/4 opacity-30" style="background-image: radial-gradient(#0d59f2 2px, transparent 2px); background-size: 16px 16px;"></div>

                <div class="w-full max-w-[1280px] mx-auto relative z-10 font-body">
                    <h1 class="text-3xl md:text-4xl font-bold text-[#00174f] mb-6 font-display tracking-wide">{title}</h1>
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
                    <div class="w-full md:w-[70%] lg:w-[75%] font-body text-gray-800 leading-relaxed space-y-8">
                        <div class="bg-white rounded-2xl shadow-sm border border-gray-100/50 p-6 md:p-10 lg:p-12">
                            {html_content}
                        </div>
                    </div>

                    <!-- Right Column: Sidebar -->"""

    final_content = content[:start_idx] + new_section + content[end_idx:]
    
    # Update sidebar Link active state!
    # By default, template has giao-trinh-tai-lieu active. Must deactivate it.
    inactive_class = "hover:text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-gray-300 before:mr-2 hover:before:bg-primary"
    active_class = "text-primary transition-colors flex items-center before:content-[''] before:w-1.5 before:h-1.5 before:rounded-full before:bg-primary before:mr-2"
    
    wrong_link = f'href="giao-trinh-tai-lieu.html" class="{active_class}"'
    fixed_link = f'href="giao-trinh-tai-lieu.html" class="{inactive_class}"'
    final_content = final_content.replace(wrong_link, fixed_link)

    # NOW we must activate the CURRENT filename in the sidebar! Wait, the Sidebar template currently doesn't possess these links.
    # Ah! The sidebar hasn't been updated to include "Dự giờ đồng nghiệp", "Chương trình CoP", etc. in the template!!!
    # Let me check my previous update_he_thong_ho_tro.py. It updated "Hệ thống & Hỗ trợ", but the template in 'Đào tạo & ĐBgClượng' probably still doesn't have these 4 items in the sidebar.
    # We will let another python script handle the global sidebar replacement for the QA module. For now, generate the files!
    
    with open(f'/Users/vobac/Downloads/gia-viet-handbook/{filename}', 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"Created {filename}")


# ------------------ PAGE 1: DỰ GIỜ ĐỒNG NGHIỆP ------------------
du_gio_html = """
<div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">
    <span class="text-primary font-bold tracking-wider uppercase text-sm font-body bg-blue-50 w-max px-3 py-1 rounded-full border border-blue-100">CHẤT LƯỢNG ĐÀO TẠO</span>
    <h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display mt-2 mb-2">QUY ĐỊNH DỰ GIỜ ĐỒNG NGHIỆP</h2>
    <h3 class="text-primary text-xl font-medium font-body mb-4">(Peer-Observation)</h3>
</div>

<div class="bg-gradient-to-br from-indigo-50 to-blue-50 border border-blue-100 rounded-2xl p-6 md:p-8 mb-10 relative overflow-hidden text-[#00174f] text-[15px] leading-relaxed shadow-sm hover:shadow-md transition-all duration-300">
    <div class="absolute right-0 top-0 opacity-[0.03] translate-x-1/4 -translate-y-1/4">
        <span class="material-symbols-outlined text-[150px]">record_voice_over</span>
    </div>
    <p class="relative z-10"><strong class="text-primary text-lg">Hoạt động Peer Observation</strong> (Dự giờ đồng nghiệp) là cơ hội để giáo viên quan sát và học hỏi lẫn nhau thông qua việc tham gia dự giờ các tiết học do đồng nghiệp giảng dạy.</p>
    <p class="relative z-10 mt-3">Mỗi tuần, các giáo viên sẽ tự nguyện đăng ký dự giờ một hoặc nhiều tiết dạy của đồng nghiệp. Trong buổi dự giờ, giáo viên quan sát các kỹ thuật giảng dạy, phương pháp truyền đạt, cách xử lý tình huống, quản lý lớp học và cách xây dựng tương tác. Sau mỗi buổi, các giáo viên sẽ cùng trao đổi ý kiến, chia sẻ quan điểm để rút kinh nghiệm.</p>
</div>

<!-- Mục tiêu -->
<h3 class="text-[#00174f] text-2xl font-bold font-display mb-6 flex items-center gap-2">
    <span class="material-symbols-outlined text-primary text-[28px]">flag</span> Mục Tiêu
</h3>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5 mb-12">
    <div class="bg-white rounded-xl p-6 border border-gray-200 shadow-sm hover:-translate-y-1 hover:shadow-md transition-all duration-300 group cursor-pointer">
        <div class="w-12 h-12 rounded-full bg-blue-50 text-blue-600 flex items-center justify-center mb-4 group-hover:bg-blue-600 group-hover:text-white transition-colors duration-300">
            <span class="material-symbols-outlined">school</span>
        </div>
        <h4 class="font-bold text-gray-800 text-base mb-2">Học hỏi kinh nghiệm</h4>
        <p class="text-sm text-gray-500">Tiếp thu những kỹ thuật, phương pháp và ý tưởng mới trong giảng dạy từ đồng nghiệp.</p>
    </div>
    <div class="bg-white rounded-xl p-6 border border-gray-200 shadow-sm hover:-translate-y-1 hover:shadow-md transition-all duration-300 group cursor-pointer">
        <div class="w-12 h-12 rounded-full bg-amber-50 text-amber-600 flex items-center justify-center mb-4 group-hover:bg-amber-500 group-hover:text-white transition-colors duration-300">
            <span class="material-symbols-outlined">trending_up</span>
        </div>
        <h4 class="font-bold text-gray-800 text-base mb-2">Phát triển chuyên môn</h4>
        <p class="text-sm text-gray-500">Nhận diện điểm mạnh và các khía cạnh cần cải thiện trong phong cách giảng dạy.</p>
    </div>
    <div class="bg-white rounded-xl p-6 border border-gray-200 shadow-sm hover:-translate-y-1 hover:shadow-md transition-all duration-300 group cursor-pointer">
        <div class="w-12 h-12 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center mb-4 group-hover:bg-emerald-500 group-hover:text-white transition-colors duration-300">
            <span class="material-symbols-outlined">star</span>
        </div>
        <h4 class="font-bold text-gray-800 text-base mb-2">Nâng cao chất lượng</h4>
        <p class="text-sm text-gray-500">Áp dụng những phương pháp, kỹ thuật hiệu quả hơn vào lớp học thực tế.</p>
    </div>
    <div class="bg-white rounded-xl p-6 border border-gray-200 shadow-sm hover:-translate-y-1 hover:shadow-md transition-all duration-300 group cursor-pointer">
        <div class="w-12 h-12 rounded-full bg-purple-50 text-purple-600 flex items-center justify-center mb-4 group-hover:bg-purple-500 group-hover:text-white transition-colors duration-300">
            <span class="material-symbols-outlined">psychology</span>
        </div>
        <h4 class="font-bold text-gray-800 text-base mb-2">Tư duy phản biện & sáng tạo</h4>
        <p class="text-sm text-gray-500">Quan sát, phân tích và áp dụng linh hoạt các phương pháp vào lớp mình.</p>
    </div>
    <div class="bg-white rounded-xl p-6 border border-gray-200 shadow-sm hover:-translate-y-1 hover:shadow-md transition-all duration-300 group cursor-pointer lg:col-span-2">
        <div class="w-12 h-12 rounded-full bg-rose-50 text-rose-600 flex items-center justify-center mb-4 group-hover:bg-rose-500 group-hover:text-white transition-colors duration-300">
            <span class="material-symbols-outlined">diversity_3</span>
        </div>
        <h4 class="font-bold text-gray-800 text-base mb-2">Xây dựng tinh thần đồng đội</h4>
        <p class="text-sm text-gray-500">Tạo không gian kết nối, hỗ trợ và thúc đẩy sự gắn kết giữa các giáo viên trong trung tâm.</p>
    </div>
</div>

<!-- Đối tượng -->
<div class="flex items-center gap-4 bg-gray-50 border border-gray-200 rounded-xl p-5 mb-12 shadow-sm">
    <div class="w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-sm border border-gray-100 flex-shrink-0">
        <span class="material-symbols-outlined text-gray-600">group</span>
    </div>
    <div>
        <h4 class="font-bold text-sm text-gray-500 uppercase tracking-wider">ĐỐI TƯỢNG THAM GIA</h4>
        <p class="font-semibold text-[#00174f] text-lg">Tất cả giáo viên tiếng Anh đang giảng dạy tại Anh Ngữ Gia Việt.</p>
    </div>
</div>

<!-- Quy trình -->
<h3 class="text-[#00174f] text-2xl font-bold font-display mb-8 flex items-center gap-2">
    <span class="material-symbols-outlined text-primary text-[28px]">timeline</span> Quy Trình Dự Giờ (3 Bước)
</h3>
<div class="max-w-4xl mx-auto mb-16 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-blue-300 before:to-transparent">
    
    <!-- Bước 1 -->
    <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active mb-12">
        <!-- Icon -->
        <div class="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white bg-blue-500 text-white shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 shadow flex-col absolute left-0 md:left-1/2 transform -translate-x-1/2 z-10 transition-transform duration-300 group-hover:scale-110">
            <span class="material-symbols-outlined text-xl">event_upcoming</span>
        </div>
        <!-- Card -->
        <div class="w-[calc(100%-4rem)] md:w-[calc(50%-3rem)] bg-white p-6 rounded-2xl shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] border border-gray-100 group-hover:-translate-y-1 group-hover:shadow-lg transition-all duration-300 ml-16 md:ml-0 cursor-pointer">
            <div class="flex items-center justify-between mb-2">
                <h4 class="font-bold text-lg text-[#00174f]">1. TRƯỚC khi dự giờ</h4>
            </div>
            <ul class="text-sm text-gray-600 space-y-2.5 mt-4 list-disc pl-4 marker:text-blue-500">
                <li>Giáo viên dự giờ cần <strong class="text-gray-800">trao đổi với giáo viên dạy</strong> để tìm hiểu về chủ đề bài học, hoạt động giảng dạy và mục tiêu lớp học.</li>
                <li>Nên chuẩn bị sổ tay hoặc thiết bị điện tử (tablet, laptop) để ghi chép.</li>
            </ul>
        </div>
    </div>

    <!-- Bước 2 -->
    <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active mb-12">
        <div class="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white bg-amber-500 text-white shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 shadow flex-col absolute left-0 md:left-1/2 transform -translate-x-1/2 z-10 transition-transform duration-300 group-hover:scale-110">
            <span class="material-symbols-outlined text-xl">visibility</span>
        </div>
        <div class="w-[calc(100%-4rem)] md:w-[calc(50%-3rem)] bg-white p-6 rounded-2xl shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] border border-gray-100 group-hover:-translate-y-1 group-hover:shadow-lg transition-all duration-300 ml-16 md:ml-0 cursor-pointer">
            <div class="flex items-center justify-between mb-2">
                <h4 class="font-bold text-lg text-[#00174f]">2. TRONG khi dự giờ</h4>
            </div>
            <ul class="text-sm text-gray-600 space-y-2.5 mt-4 list-disc pl-4 marker:text-amber-500">
                <li>Đến lớp đúng giờ, giới thiệu bản thân trước khi vào lớp. Tập trung quan sát chuyên môn lớp học.</li>
                <li>Chỉ tham gia hoạt động khi <strong class="text-gray-800">được giáo viên nhờ hỗ trợ</strong>.</li>
                <li>Ghi chép theo biểu mẫu dự giờ của TCM.</li>
                <li><strong class="text-red-500">Tuyệt đối Không:</strong> Dùng điện thoại làm việc riêng. Chỉ chụp ảnh/Ghi hình khi có sự đồng ý của GV đứng lớp!</li>
            </ul>
        </div>
    </div>

     <!-- Bước 3 -->
    <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
        <div class="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white bg-emerald-500 text-white shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 shadow flex-col absolute left-0 md:left-1/2 transform -translate-x-1/2 z-10 transition-transform duration-300 group-hover:scale-110">
            <span class="material-symbols-outlined text-xl">forum</span>
        </div>
        <div class="w-[calc(100%-4rem)] md:w-[calc(50%-3rem)] bg-white p-6 rounded-2xl shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] border border-gray-100 group-hover:-translate-y-1 group-hover:shadow-lg transition-all duration-300 ml-16 md:ml-0 cursor-pointer">
            <div class="flex items-center justify-between mb-2">
                <h4 class="font-bold text-lg text-[#00174f]">3. SAU khi dự giờ</h4>
            </div>
            <ul class="text-sm text-gray-600 space-y-2.5 mt-4 list-disc pl-4 marker:text-emerald-500">
                <li>Trao đổi ngắn với GV lớp học về điểm mạnh / cần cải thiện.</li>
                <li>Dành thời gian suy nghĩ, đúc rút bài học kinh nghiệm riêng.</li>
                <li>Chia sẻ các kinh nghiệm học hỏi được trong các buổi sinh hoạt chuyên môn.</li>
            </ul>
        </div>
    </div>
</div>

<!-- LƯU Ý -->
<div class="bg-gray-800 text-white rounded-2xl p-8 mb-10 border border-gray-700 shadow-lg relative overflow-hidden group hover:shadow-2xl hover:-translate-y-1 transition-all duration-300">
    <div class="absolute right-0 top-0 opacity-10 translate-x-1/4 -translate-y-1/4">
        <span class="material-symbols-outlined text-[150px]">warning</span>
    </div>
    <div class="relative z-10">
        <h3 class="text-xl font-bold font-display mb-6 border-b border-gray-600 pb-4 text-rose-400">IV. Quy Định Bắt Buộc Chung</h3>
        <div class="space-y-4 text-sm font-medium">
            <div class="flex gap-3 items-start"><span class="material-symbols-outlined text-green-400">check_circle</span> <span><strong>Trang phục & Thái độ:</strong> Lịch sự, tích cực, cởi mở, tôn trọng tuyệt đối. Chào hỏi học viên đàng hoàng. Cảm ơn GV trước khi về.</span></div>
            <div class="flex gap-3 items-start"><span class="material-symbols-outlined text-amber-400">lock</span> <span><strong>Bảo mật:</strong> Tuyệt đối giữ bí mật thông tin nhạy cảm của GV/HS thu thập được trong giờ quan sát.</span></div>
            <div class="flex gap-3 items-start"><span class="material-symbols-outlined text-blue-400">calendar_clock</span> <span><strong>Tuân thủ lịch trình:</strong> Dự đúng lịch. Nếu vắng mặt đột xuất, phải báo cáo Tổ trưởng chuyên môn và xin phép đường hoàng.</span></div>
            <div class="flex gap-3 items-start mt-6 p-4 bg-gray-900/50 rounded-xl border border-gray-700/50"><span class="material-symbols-outlined text-red-500">gavel</span> <span class="text-gray-300">Việc dự giờ chỉ mang tính chất tham khảo học hỏi kinh nghiệm. <strong class="text-white">Giáo viên dự giờ KHÔNG ĐƯỢC PHÉP ĐÁNH GIÁ HAY PHÊ BÌNH</strong> giáo viên đang giảng dạy!</span></div>
        </div>
    </div>
</div>
"""

# ------------------ PAGE 2: CHƯƠNG TRÌNH CoP ------------------
cop_html = """
<div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">
    <span class="text-primary font-bold tracking-wider uppercase text-sm font-body bg-blue-50 w-max px-3 py-1 rounded-full border border-blue-100">CHẤT LƯỢNG ĐÀO TẠO</span>
    <h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display mt-2 mb-2">CHƯƠNG TRÌNH CoP</h2>
    <h3 class="text-gray-500 text-md font-medium font-body mb-4">(Community of Practice)</h3>
</div>

<div class="relative w-full rounded-2xl bg-gradient-to-r from-teal-500 to-emerald-600 p-8 mb-12 shadow-md overflow-hidden hover:shadow-lg hover:-translate-y-1 transition-all duration-300 cursor-pointer">
    <div class="absolute right-0 top-0 opacity-10 translate-x-1/4 -translate-y-1/4">
        <span class="material-symbols-outlined text-[150px] text-white">diversity_1</span>
    </div>
    <div class="relative z-10 text-white">
        <h3 class="font-display font-bold text-2xl mb-3">1. CoP Là Gì?</h3>
        <p class="text-[15px] leading-relaxed opacity-90 font-medium">CoP là chương trình phát triển chuyên môn thường xuyên dành cho GV YLE tại Gia Việt. Đây là không gian học tập, chia sẻ chuyên môn để cùng nhau cải tiến chất lượng giảng dạy.<br><br>CoP không chỉ là buổi đào tạo, mà là <strong>một cộng đồng chuyên nghiệp</strong>, nơi mỗi giáo viên vừa là người học, vừa là người đóng góp giá trị.</p>
    </div>
</div>

<!-- Grid Objectives -->
<h3 class="text-[#00174f] text-xl font-bold font-display mb-6">2. Mục tiêu của chương trình CoP</h3>
<div class="grid grid-cols-1 md:grid-cols-2 gap-5 mb-12">
    <div class="flex items-start gap-4 bg-white border border-gray-200 p-5 rounded-xl shadow-sm hover:border-teal-400 hover:shadow-md active:scale-[0.98] transition-all duration-300 cursor-pointer">
        <div class="w-10 h-10 bg-teal-50 text-teal-600 rounded-full flex items-center justify-center shrink-0 mt-1"><span class="material-symbols-outlined">upgrade</span></div>
        <p class="text-sm text-gray-700 leading-relaxed"><strong class="text-gray-900 block mb-1">Cải tiến phương pháp:</strong> Nâng cao chất lượng dạy thông qua việc chia sẻ kỹ thuật giảng dạy mới, hiệu quả.</p>
    </div>
    <div class="flex items-start gap-4 bg-white border border-gray-200 p-5 rounded-xl shadow-sm hover:border-teal-400 hover:shadow-md active:scale-[0.98] transition-all duration-300 cursor-pointer">
        <div class="w-10 h-10 bg-teal-50 text-teal-600 rounded-full flex items-center justify-center shrink-0 mt-1"><span class="material-symbols-outlined">support_agent</span></div>
        <p class="text-sm text-gray-700 leading-relaxed"><strong class="text-gray-900 block mb-1">Gỡ rối khó khăn:</strong> Chia sẻ thách thức và cùng nhau thảo luận tìm ra giải pháp tối ưu cho bối cảnh lớp học thực tế.</p>
    </div>
    <div class="flex items-start gap-4 bg-white border border-gray-200 p-5 rounded-xl shadow-sm hover:border-teal-400 hover:shadow-md active:scale-[0.98] transition-all duration-300 cursor-pointer">
        <div class="w-10 h-10 bg-teal-50 text-teal-600 rounded-full flex items-center justify-center shrink-0 mt-1"><span class="material-symbols-outlined">group_add</span></div>
        <p class="text-sm text-gray-700 leading-relaxed"><strong class="text-gray-900 block mb-1">Xây dựng cộng đồng:</strong> Kết nối sự gắn kết hỗ trợ tạo một môi trường giáo dục chuyên nghiệp, tích cực đổi mới liên tục.</p>
    </div>
    <div class="flex items-start gap-4 bg-white border border-gray-200 p-5 rounded-xl shadow-sm hover:border-teal-400 hover:shadow-md active:scale-[0.98] transition-all duration-300 cursor-pointer">
        <div class="w-10 h-10 bg-teal-50 text-teal-600 rounded-full flex items-center justify-center shrink-0 mt-1"><span class="material-symbols-outlined">psychology</span></div>
        <p class="text-sm text-gray-700 leading-relaxed"><strong class="text-gray-900 block mb-1">Kích thích Feedback:</strong> Khuyến khích tinh thần phản tư (reflection) qua hoạt động quan sát, mô phỏng và thử nghiệm.</p>
    </div>
</div>

<div class="flex bg-gray-50 rounded-2xl p-6 mb-12 shadow-inner border border-gray-200 gap-6">
    <div class="w-1/3 text-center border-r border-gray-300 pr-6 hidden md:block">
        <span class="material-symbols-outlined text-[80px] text-gray-300">group</span>
    </div>
    <div>
        <h4 class="font-bold text-gray-800 text-lg mb-2">3. Đối tượng tham gia</h4>
        <p class="text-[14px] text-gray-600 leading-relaxed">Tất cả giáo viên đang giảng dạy chương trình YLE tại Anh ngữ Gia Việt. (Giáo viên mới và GV có kinh nghiệm đều được đặc biệt khuyến khích để chia sẻ giá trị chéo.)</p>
    </div>
</div>

<h3 class="text-[#00174f] text-xl font-bold font-display mb-6">4. Hình Thức Tổ Chức</h3>
<div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-12">
    <div class="bg-blue-50/50 border border-blue-100 p-4 rounded-xl text-center hover:scale-105 transition-transform">
        <span class="material-symbols-outlined text-blue-500 mb-2">meeting_room</span>
        <h5 class="text-xs font-bold text-gray-500 uppercase tracking-widest mb-1">Hình thức</h5>
        <div class="font-bold text-[#00174f]">Gặp trực tiếp</div>
    </div>
    <div class="bg-blue-50/50 border border-blue-100 p-4 rounded-xl text-center hover:scale-105 transition-transform">
        <span class="material-symbols-outlined text-blue-500 mb-2">calendar_month</span>
        <h5 class="text-xs font-bold text-gray-500 uppercase tracking-widest mb-1">Tần suất</h5>
        <div class="font-bold text-[#00174f]">1 buổi/tháng</div>
    </div>
    <div class="bg-blue-50/50 border border-blue-100 p-4 rounded-xl text-center hover:scale-105 transition-transform">
        <span class="material-symbols-outlined text-blue-500 mb-2">schedule</span>
        <h5 class="text-xs font-bold text-gray-500 uppercase tracking-widest mb-1">Thời lượng</h5>
        <div class="font-bold text-[#00174f]">2 - 2.5 giờ/buổi</div>
    </div>
    <div class="bg-blue-50/50 border border-blue-100 p-4 rounded-xl text-center hover:scale-105 transition-transform">
        <span class="material-symbols-outlined text-blue-500 mb-2">assignment_turned_in</span>
        <h5 class="text-xs font-bold text-gray-500 uppercase tracking-widest mb-1">Đăng ký</h5>
        <div class="font-bold text-[#00174f]">Qua Form online</div>
    </div>
    <div class="col-span-2 md:col-span-4 bg-blue-50 border border-blue-200 p-5 rounded-xl text-sm text-gray-700">
        <strong>Tổ chức & Chủ đề:</strong> TCM YLE phối hợp với các GV cứng chuyên môn để xây dựng mỗi tháng 1 chủ đề trọng điểm dựa trên: Nhu cầu thực tế, Các vấn đề nhức nhối trong tháng, và Định hướng chiến lược sắp tới của trung tâm.
    </div>
</div>

<div class="grid grid-cols-1 lg:grid-cols-2 gap-10">
    <div>
        <h3 class="text-[#00174f] text-xl font-bold font-display mb-6">5. Các Hoạt Động Cốt Lõi</h3>
        <ul class="space-y-4 text-sm text-gray-600">
            <li class="flex gap-3"><span class="shrink-0 material-symbols-outlined text-teal-500 font-bold">check</span> <span><strong>Chia sẻ lý thuyết:</strong> Lý luận phương pháp & Kỹ năng mới đã được chứng minh hiệu quả.</span></li>
            <li class="flex gap-3"><span class="shrink-0 material-symbols-outlined text-teal-500 font-bold">check</span> <span><strong>Demo Teaching:</strong> GV đứng lớp minh hoạ lồng ghép thao tác thật vào lớp học mẫu.</span></li>
            <li class="flex gap-3"><span class="shrink-0 material-symbols-outlined text-teal-500 font-bold">check</span> <span><strong>Ghi nhận Feedback:</strong> Tập thể cùng theo dõi, phân tích chéo và đưa ý kiến khen chê đa chiều.</span></li>
            <li class="flex gap-3"><span class="shrink-0 material-symbols-outlined text-teal-500 font-bold">check</span> <span><strong>Workshop Kịch Bản Lớp:</strong> Làm bài cá nhân/nhóm để xẻ thịt giáo án, áp dụng kỹ thuật mới tại chỗ.</span></li>
            <li class="flex gap-3"><span class="shrink-0 material-symbols-outlined text-teal-500 font-bold">check</span> <span><strong>"Shark Tank" Khó khăn:</strong> Vứt ra những case study lớp quậy, phụ huynh khó... để xin giải pháp.</span></li>
        </ul>
    </div>
    
    <div>
        <h3 class="text-[#00174f] text-xl font-bold font-display mb-6">6. Quyền Lợi & Sự Tham Gia</h3>
        <div class="bg-yellow-50 border border-yellow-200 p-6 rounded-2xl mb-6 shadow-sm">
            <h4 class="font-bold text-yellow-800 mb-3 flex items-center gap-2"><span class="material-symbols-outlined">stars</span> Đối với Cá nhân tham gia</h4>
            <p class="text-sm text-yellow-800/80 leading-relaxed mb-4">GV được đặc biệt khuyến khích giơ tay xung phong đứng lớp Demo Teaching! Đây là sân khấu vàng để rèn luyện bản lĩnh sân khấu, nhận phản hồi thực chiến 1-1 từ dàn hội đồng máu mặt, và chứng tỏ năng lực truyền lửa.</p>
        </div>
        <div class="bg-white border border-gray-200 p-6 rounded-2xl shadow-sm">
            <h4 class="font-bold text-gray-800 mb-4">Giá trị Thực Tế Nhận Được</h4>
            <ul class="space-y-3 text-[13px] text-gray-600 font-medium">
                <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-green-500 rounded-full"></span> Ngân hàng phương pháp Gv khổng lồ</li>
                <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-green-500 rounded-full"></span> Không còn lo khớp/run khi bị dự giờ đột xuất</li>
                <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-green-500 rounded-full"></span> Mối quan hệ thân thiết khăng khít toàn hệ thống</li>
                <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-green-500 rounded-full"></span> Được ghi danh vào profile Gv triển vọng</li>
            </ul>
        </div>
    </div>
</div>
"""

# ------------------ PAGE 3: FAST TRACK TRAINING ------------------
fast_track_html = """
<div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">
    <span class="text-primary font-bold tracking-wider uppercase text-sm font-body bg-blue-50 w-max px-3 py-1 rounded-full border border-blue-100">CHẤT LƯỢNG ĐÀO TẠO</span>
    <h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display mt-2 mb-2">CHƯƠNG TRÌNH FAST-TRACK TRAINING</h2>
    <h3 class="text-gray-500 text-md font-medium font-body mb-4">(Đào tạo tập trung Ngắn Hạn dành cho GV Thực Tập / Mới)</h3>
</div>

<div class="grid grid-cols-1 lg:grid-cols-12 gap-8 mb-16">
    <div class="lg:col-span-7 bg-white p-8 rounded-2xl border border-blue-100 shadow-[0_4px_25px_-5px_rgba(0,0,0,0.05)] hover:shadow-lg hover:-translate-y-1 transition-all duration-300">
        <h3 class="text-xl font-bold font-display text-[#00174f] mb-6 flex items-center gap-2"><span class="material-symbols-outlined text-primary">target</span> 1. Mục đích Sứ mệnh</h3>
        <p class="text-[14.5px] text-gray-600 mb-6 leading-relaxed">Được thiết kế hỏa tốc dành riêng cho Tân Binh gia nhập lực lượng chuyên môn (YLE/ADU) để biến lý thuyết giáo án thành mũi nhọn thực chiến phòng học thực tế.</p>
        <ul class="space-y-3 text-sm text-gray-600">
            <li class="flex gap-3 items-center"><span class="w-8 h-8 rounded bg-blue-50 text-blue-600 flex items-center justify-center shrink-0 font-bold">1</span> Đảm bảo đánh giá công bằng chất lượng đứng lớp đồng đều toàn bộ hệ thống.</li>
            <li class="flex gap-3 items-center"><span class="w-8 h-8 rounded bg-blue-50 text-blue-600 flex items-center justify-center shrink-0 font-bold">2</span> Hỗ trợ cầm tay chỉ việc chống sốc văn hóa và sốc môi trường sư phạm Gv.</li>
            <li class="flex gap-3 items-center"><span class="w-8 h-8 rounded bg-blue-50 text-blue-600 flex items-center justify-center shrink-0 font-bold">3</span> Sàng lọc & Đánh giá năng lực độc lập trước khi giao khoán cấp lớp chính thức.</li>
        </ul>
    </div>
    
    <div class="lg:col-span-5 bg-[#00174f] text-white p-8 rounded-2xl shadow-lg relative overflow-hidden group hover:shadow-2xl hover:-translate-y-1 transition-all duration-300">
        <div class="absolute right-0 bottom-0 opacity-10 translate-x-1/4 translate-y-1/4">
            <span class="material-symbols-outlined text-[200px]">person_check</span>
        </div>
        <h3 class="text-xl font-bold font-display mb-6 border-b border-white/20 pb-3 relative z-10">2. Đối Tượng Tham Gia</h3>
        <ul class="space-y-4 text-sm font-medium text-blue-100 relative z-10 list-disc pl-5">
            <li>Giáo viên mới tuyển dụng gia nhập trung tâm.</li>
            <li>Thực tập sinh vừa tốt nghiệp chuỗi Gia Viet TESOL nhưng KPI chưa đạt ngưỡng độc lập.</li>
            <li>Giáo viên cũ bị "rớt phong độ" cần được tái tu bổ, theo dõi & đào tạo trước khi điều động lại.</li>
        </ul>
        <div class="mt-8 bg-white/10 p-3 text-center rounded-lg font-bold text-white relative z-10 backdrop-blur-sm shadow-inner">THỜI LƯỢNG HUẤN LUYỆN: 4 - 8 TUẦN</div>
    </div>
</div>

<h3 class="text-[#00174f] text-2xl font-bold font-display mb-8 flex items-center gap-2">
    <span class="material-symbols-outlined text-primary text-[28px]">timeline</span> 3. Cấu Trúc Huấn Luyện 3 Pha Thực Chiến
</h3>
<div class="flex flex-col md:flex-row gap-6 mb-16 relative">
    <!-- Nền Line ngang desktop -->
    <div class="hidden md:block absolute top-[45px] left-0 right-0 h-1 bg-gradient-to-r from-blue-300 via-emerald-300 to-amber-300 z-0 rounded-full"></div>
    
    <!-- Giai doan 1 -->
    <div class="flex-1 relative z-10 bg-white border border-gray-100 p-6 rounded-2xl pt-10 shadow-sm hover:border-blue-300 hover:shadow-lg hover:-translate-y-2 transition-all duration-300 group cursor-pointer">
        <div class="absolute -top-7 left-1/2 transform -translate-x-1/2 w-14 h-14 bg-white rounded-full border-[6px] border-blue-500 shadow-lg flex items-center justify-center font-bold text-xl text-blue-600">1</div>
        <h4 class="text-center font-bold text-lg mb-4 text-[#00174f]">Quan sát (Observation)</h4>
        <div class="text-[13px] text-gray-600 space-y-3 font-medium">
            <p><span class="material-symbols-outlined text-[15px] align-middle text-blue-500">visibility</span> Theo đuôi dự các lớp của GV cộm cán (Mentor).</p>
            <p><span class="material-symbols-outlined text-[15px] align-middle text-blue-500">search</span> Tập trung soi: Cách quản trị lớp trẻ em hung hãn nhí nhố, Bố trí Timeframe, Tiếng Anh mệnh lệnh...</p>
            <p><span class="material-symbols-outlined text-[15px] align-middle text-blue-500">edit_document</span> <strong>KPI Hành động:</strong> Khai nộp Báo cáo Nhật ký dự giờ & Tham vấn Sư phụ chuyên môn.</p>
        </div>
    </div>
    
    <!-- Giai doan 2 -->
    <div class="flex-1 relative z-10 bg-white border border-gray-100 p-6 rounded-2xl pt-10 shadow-sm hover:border-emerald-400 hover:shadow-lg hover:-translate-y-2 transition-all duration-300 group cursor-pointer">
        <div class="absolute -top-7 left-1/2 transform -translate-x-1/2 w-14 h-14 bg-white rounded-full border-[6px] border-emerald-500 shadow-lg flex items-center justify-center font-bold text-xl text-emerald-600">2</div>
        <h4 class="text-center font-bold text-lg mb-4 text-[#00174f]">Đồng giảng (Co-teaching)</h4>
        <div class="text-[13px] text-gray-600 space-y-3 font-medium">
            <p><span class="material-symbols-outlined text-[15px] align-middle text-emerald-500">handshake</span> Bắt tay vào làm thật chung với Mentor!</p>
            <p><span class="material-symbols-outlined text-[15px] align-middle text-emerald-500">directions_run</span> <strong>Nhiệm vụ:</strong> Soạn giáo án, làm giáo cụ, Xung phong dạy 1-3 Activity nhẹ nhàng (30-60p/tuần).</p>
            <p><span class="material-symbols-outlined text-[15px] align-middle text-emerald-500">psychology</span> Kịch bản: Sư phụ gạch xoá giáo án > Lên lớp > Sư phụ ngồi chấm > Cuối tuần Review nhược điểm.</p>
        </div>
    </div>
    
    <!-- Giai doan 3 -->
    <div class="flex-1 relative z-10 bg-white border border-gray-100 p-6 rounded-2xl pt-10 shadow-sm hover:border-amber-400 hover:shadow-lg hover:-translate-y-2 transition-all duration-300 group cursor-pointer">
        <div class="absolute -top-7 left-1/2 transform -translate-x-1/2 w-14 h-14 bg-white rounded-full border-[6px] border-amber-500 shadow-lg flex items-center justify-center font-bold text-xl text-amber-600">3</div>
        <h4 class="text-center font-bold text-lg mb-4 text-[#00174f]">Thi Tốt Nghiệp (Demo)</h4>
        <div class="text-[13px] text-gray-600 space-y-3 font-medium">
            <p><span class="material-symbols-outlined text-[15px] align-middle text-amber-500">flag</span> Áp dụng khi Giáo viên được công nhận đủ độ chín.</p>
            <p><span class="material-symbols-outlined text-[15px] align-middle text-amber-500">mic</span> Trình diễn một Session hoàn chỉnh 60 Phút độc lập.</p>
            <p><span class="material-symbols-outlined text-[15px] align-middle text-amber-500">verified</span> <strong>Hệ quả:</strong> Qua vòng này sẽ được phong Ấn chính thức, Rải lớp thật, Nâng lương x2. Rớt thì quay lại Phase 2 hoặc Out!</p>
        </div>
    </div>
</div>

<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
    <div class="bg-gray-50 border border-gray-200 p-8 rounded-2xl hover:bg-gray-100 transition-colors">
        <h4 class="font-bold text-lg text-[#00174f] mb-4 flex gap-2 items-center"><span class="material-symbols-outlined text-gray-500">rule</span> Quy Chế Của Thực Tập Sinh</h4>
        <ul class="space-y-2 text-sm text-gray-700 list-disc pl-5 marker:text-gray-400">
            <li>Tuyệt đối KHÔNG LATE CATCH (Đi muộn về sớm). Đi muộn Cắt Training.</li>
            <li>Giáo án, bài trình duyệt nộp đúng Deadline cho Mentor. Lệch format trả về.</li>
            <li>Tác phong, Đầu tóc, Giao tiếp trên bục giảng xài chuẩn Nhân sự Gia Việt. Lôm côm bị sút luôn.</li>
        </ul>
    </div>
    <div class="bg-blue-50 border border-blue-200 p-8 rounded-2xl hover:bg-blue-100 transition-colors">
        <h4 class="font-bold text-lg text-[#00174f] mb-4 flex gap-2 items-center"><span class="material-symbols-outlined text-blue-500">autorenew</span> Báo Cáo Reflection Cuối Tuần</h4>
        <ul class="space-y-2 text-sm text-gray-700 list-disc pl-5 marker:text-blue-500 font-medium">
            <li>Bắt buộc ngồi uống trà xáp lá cà với Mentor để nghe ăn mắng (hoặc khen).</li>
            <li>Nhận diện gót chân Asin cá nhân. Chép phạt Phiếu <strong class="text-blue-800">Teaching Reflection</strong>.</li>
            <li>Đề mô ngay lập tức kỹ thuật khắc phục để tuần tới sửa sai.</li>
        </ul>
    </div>
</div>
"""

# ------------------ PAGE 4: MENTORING 1-1 ------------------
mentoring_1_1_html = """
<div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">
    <span class="text-primary font-bold tracking-wider uppercase text-sm font-body bg-blue-50 w-max px-3 py-1 rounded-full border border-blue-100">CHẤT LƯỢNG ĐÀO TẠO</span>
    <h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display mt-2 mb-2">HOẠT ĐỘNG MENTORING 1-1</h2>
    <h3 class="text-gray-500 text-md font-medium font-body mb-4">(Đặc Quyền Cố Vấn Tối Thượng Dành Cho Giáo Viên Mới)</h3>
</div>

<div class="bg-cover bg-center rounded-2xl mb-12 shadow-md hover:shadow-lg hover:-translate-y-1 transition-all duration-300 relative overflow-hidden h-[400px] flex items-end p-8" style="background-image: url('picture/Slide2.JPG');">
    <div class="absolute inset-0 bg-gradient-to-t from-[#00174f]/95 via-[#00174f]/70 to-transparent"></div>
    <div class="relative z-10 text-white max-w-3xl">
        <h3 class="font-display font-bold text-3xl mb-4">Giá trị của Chương trình</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-[14.5px] font-medium opacity-90">
            <div class="flex gap-2"><span class="material-symbols-outlined text-blue-400">check_circle</span> Giúp GV mới hòa nhập siêu tốc vào văn hóa hệ thống.</div>
            <div class="flex gap-2"><span class="material-symbols-outlined text-blue-400">check_circle</span> Phá vỡ sự tự ti, chuẩn bị băng đạn trước khi ra trận thật.</div>
            <div class="flex gap-2"><span class="material-symbols-outlined text-blue-400">check_circle</span> Mài xẻo giũa lỗi, Feedback sát sườn xây dựng định hướng cá nhân.</div>
            <div class="flex gap-2"><span class="material-symbols-outlined text-blue-400">check_circle</span> Lan tỏa tín ngưỡng học tập - cải tiến bất diệt của toàn TCM.</div>
        </div>
    </div>
</div>

<div class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-16">
    <div class="lg:col-span-1 bg-white border border-gray-200 rounded-2xl p-6 shadow-sm hover:border-primary hover:shadow-md transition-all">
        <h4 class="font-bold text-gray-800 text-lg mb-4 pt-1 flex items-center gap-2"><span class="material-symbols-outlined text-amber-500">admin_panel_settings</span> Đối tượng thụ hưởng</h4>
        <p class="text-[13px] text-gray-600 mb-3 p-3 bg-gray-50 rounded-lg border border-gray-100"><strong>Giáo viên mới tinh:</strong> Đang lạc lõng trong rào cản hành chính/phương pháp. Yếu quản lý lớp và viết Lesson Plan.</p>
        <p class="text-[13px] text-gray-600 p-3 bg-gray-50 rounded-lg border border-gray-100"><strong>Giáo viên Cũ Dạy Hệ Mới:</strong> Đang VIP dạy Kids YLE 5 năm... bị quăng nhầm qua hệ Cấp 3 thanh niên Global Teens!</p>
    </div>
    <div class="lg:col-span-2 bg-gradient-to-br from-blue-50 to-indigo-50 border border-blue-100 rounded-2xl p-6 shadow-sm hover:border-blue-400 hover:shadow-md transition-all">
        <h4 class="font-bold text-gray-800 text-lg mb-4 flex items-center gap-2"><span class="material-symbols-outlined text-blue-600">tune</span> Setup Thông Số Mentoring</h4>
        <div class="grid grid-cols-2 gap-4 text-sm bg-white p-5 rounded-xl border border-blue-50 shadow-inner">
            <div class="flex items-center gap-3"><span class="w-10 h-10 rounded-full bg-indigo-100 flex items-center justify-center font-bold text-indigo-700">1</span> <strong>Hình thức:</strong> Cà phê 1-1 / Gặp mặt trung tâm.</div>
            <div class="flex items-center gap-3"><span class="w-10 h-10 rounded-full bg-indigo-100 flex items-center justify-center font-bold text-indigo-700">2</span> <strong>Nhân sự Mentor:</strong> Cốt cán TCM/ Điều phối viên.</div>
            <div class="flex items-center gap-3"><span class="w-10 h-10 rounded-full bg-indigo-100 flex items-center justify-center font-bold text-indigo-700">3</span> <strong>Tiến độ:</strong> Ròng rã 3 - 6 tuần lễ.</div>
            <div class="flex items-center gap-3"><span class="w-10 h-10 rounded-full bg-indigo-100 flex items-center justify-center font-bold text-indigo-700">4</span> <strong>Tần suất:</strong> 1-2 cữ/tuần (Mỗi cữ 1.5 - 2h).</div>
        </div>
    </div>
</div>

<h3 class="text-[#00174f] text-2xl font-bold font-display mb-8">Quy Trình Mentoring Tuần Hoàn (4 Pha)</h3>
<div class="space-y-4 mb-14">
    <div class="bg-white border-l-4 border-blue-500 rounded-r-xl p-5 shadow-sm hover:translate-x-2 transition-transform cursor-pointer">
        <div class="font-bold text-[#00174f] mb-1">Pha 1: Viết kịch bản Lesson & Tham Vấn</div>
        <div class="text-[13px] text-gray-600">Ông Mentee ở nhà tự biên tự diễn cái sườn giáo án, liệt kê Objective, Idea chém chuối, và list 1 danh sách CÂU HỎI gửi Sư phụ.</div>
    </div>
    <div class="bg-white border-l-4 border-purple-500 rounded-r-xl p-5 shadow-sm hover:translate-x-2 transition-transform cursor-pointer">
        <div class="font-bold text-[#00174f] mb-1">Pha 2: Gặp gỡ Phân Thây Giáo Án</div>
        <div class="text-[13px] text-gray-600">Gặp Sư Phụ để phân tích tuổi thọ trò chơi có dài k? Xoá bớt cái cồng kềnh. Học cách dẫn mồi (Tạo context), cách dằn mặt trẻ em bằng Tiếng Anh. Sư phụ chốt kịch bản.</div>
    </div>
    <div class="bg-white border-l-4 border-amber-500 rounded-r-xl p-5 shadow-sm hover:translate-x-2 transition-transform cursor-pointer">
        <div class="font-bold text-[#00174f] mb-1">Pha 3: Diễn Thử Demo Trên Ván Trượt</div>
        <div class="text-[13px] text-gray-600">Được quyền xin lên Đứng lớp diễn sâu múa lửa một đoạn nhỏ (Demo) hoặc Demo giả lập tại bàn cafe. Sư phụ soi khẩu hình, body language, cách đảo mắt... để nắn.</div>
    </div>
    <div class="bg-white border-l-4 border-emerald-500 rounded-r-xl p-5 shadow-sm hover:translate-x-2 transition-transform cursor-pointer">
        <div class="font-bold text-[#00174f] mb-1">Pha 4: Hậu Huấn Luyện (Reflection Tự Vả)</div>
        <div class="text-[13px] text-gray-600">Nghỉ xả hơi xong gặp lại. Tự bạch xem bữa đó mình dở ở đâu? Gặp ca học viên nào khoai sắn tắt điện chưa biết làm gì? Sư phụ chích thuốc bổ trợ. Cycle tiếp tục.</div>
    </div>
</div>

<div class="bg-[#00174f] text-white p-8 rounded-2xl relative inline-block w-full overflow-hidden mb-8 hover:shadow-lg transition-shadow">
    <div class="absolute -right-10 -bottom-10 opacity-30 origin-bottom scale-150">
        <span class="material-symbols-outlined text-[300px] text-blue-500">workspace_premium</span>
    </div>
    <h3 class="text-xl font-bold font-display mb-4 relative z-10 text-amber-400 border-b border-blue-800 pb-3">Kết quả Tốt Nghiệp Phải Có!</h3>
    <ul class="text-sm space-y-3 font-medium relative z-10 list-disc pl-5">
        <li>Cứng tay lèo lái Giáo án độc lập! Mọi kịch bản đều cân!</li>
        <li>Miệng chữ O mồm chữ A với mọi kỹ thuật múa lửa truyền đạt mới tinh cực xịn.</li>
        <li>Dằn mặt lớp, cai trị lũ nhóc học viên thành danh sách thú cưng ngoan ngoãn.</li>
        <li>Đầy đủ bản lĩnh cầm sổ Nam Tào vào nhận danh hiệu GV Cứng Cựa của hệ thống Gia Việt!</li>
    </ul>
</div>
"""

if __name__ == '__main__':
    generate_page('du-gio-dong-nghiep.html', 'Quy định Dự Giờ Đồng Nghiệp', 'Dự giờ - Peer Observation', du_gio_html)
    generate_page('chuong-trinh-cop.html', 'Chương trình CoP Community of Practice', 'Chương trình CoP', cop_html)
    generate_page('fast-track-training.html', 'Chương trình Fast-Track Training', 'Fast-Track Training', fast_track_html)
    generate_page('mentoring-1-1.html', 'Hoạt động Mentoring 1-1', 'Mentoring 1-1', mentoring_1_1_html)

