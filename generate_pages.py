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

def generate_page(title, nav_names, content_html, filename):
    content, start_idx, end_idx = get_template()
    # Replace title
    content = content.replace(
        '<title>Giáo trình & Tài liệu giảng dạy - Handbook</title>',
        f'<title>{title} - Handbook</title>'
    )
    
    breadcrumbs_list = []
    for n in nav_names[:-1]:
        href = "#"
        if n in ["Đào tạo & Đảm bảo chất lượng", "Chương trình Đào tạo", "Đảm bảo chất lượng"]:
            href = "dao-tao-dam-bao-chat-luong.html"
        elif n in ["Tổ chức & Nhân sự", "Tổ chức và Nhân sự"]:
            href = "to-chuc-nhan-su.html"
        elif n in ["Chính sách & Phúc lợi"]:
            href = "chinh-sach-phuc-loi.html"
        breadcrumbs_list.append(f'<a href="{href}" class="hover:text-primary transition-colors whitespace-nowrap">{n}</a>')
    
    breadcrumbs = ' <span class="material-symbols-outlined text-sm">chevron_right</span> '.join(breadcrumbs_list)
    if not breadcrumbs:
        breadcrumbs_full = f'<span class="text-[#0d121c] whitespace-nowrap">{nav_names[-1]}</span>'
    else:
        breadcrumbs_full = breadcrumbs + f' <span class="material-symbols-outlined text-sm">chevron_right</span> <span class="text-[#0d121c] whitespace-nowrap">{nav_names[-1]}</span>'
    
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
                            {content_html}
                        </div>
                    </div>

                    <!-- Right Column: Sidebar -->"""

    final_content = content[:start_idx] + new_section + content[end_idx:]
    with open(f'/Users/vobac/Downloads/gia-viet-handbook/{filename}', 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"Created {filename}")

html_phu_dao = """
<div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">
    <span class="text-primary font-bold tracking-wider uppercase text-sm font-body bg-blue-50 w-max px-3 py-1 rounded-full border border-blue-100">KIDS & TEENS</span>
    <h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display mt-2 mb-2">HƯỚNG DẪN & QUY TRÌNH ĐĂNG KÝ LỚP PHỤ ĐẠO</h2>
</div>

<!-- Intro -->
<div class="bg-gradient-to-r from-blue-50/80 to-indigo-50/50 rounded-2xl p-6 md:p-8 mb-10 border border-blue-100/60 shadow-sm relative overflow-hidden">
    <div class="absolute right-0 top-0 opacity-[0.03] translate-x-1/4 -translate-y-1/4">
        <span class="material-symbols-outlined text-[150px]">school</span>
    </div>
    <p class="mb-4 font-bold text-blue-900 relative z-10">Các lớp Phụ đạo (Extra classes) được mở nhằm hỗ trợ học viên cần củng cố kiến thức và cải thiện kỹ năng, bao gồm các trường hợp:</p>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 relative z-10 mb-5">
        <div class="bg-white p-4 rounded-xl border border-blue-100/80 flex items-start gap-3 shadow-sm">
            <span class="material-symbols-outlined text-orange-500">sentiment_dissatisfied</span>
            <span class="text-[14px] text-gray-700">Tiếp thu chậm, ghi nhớ bài chưa tốt.</span>
        </div>
        <div class="bg-white p-4 rounded-xl border border-blue-100/80 flex items-start gap-3 shadow-sm">
            <span class="material-symbols-outlined text-orange-500">record_voice_over</span>
            <span class="text-[14px] text-gray-700">Làm bài chậm, phản xạ – phát âm chưa đạt yêu cầu.</span>
        </div>
        <div class="bg-white p-4 rounded-xl border border-blue-100/80 flex items-start gap-3 shadow-sm">
            <span class="material-symbols-outlined text-red-500">emergency</span>
            <span class="text-[14px] text-gray-700">Có nội dung cấp bách cần cải thiện.</span>
        </div>
        <div class="bg-white p-4 rounded-xl border border-blue-100/80 flex items-start gap-3 shadow-sm">
            <span class="material-symbols-outlined text-purple-500">event_busy</span>
            <span class="text-[14px] text-gray-700">Học viên có năng lực khá nhưng vắng học nhiều buổi (từ 2–3 buổi trở lên).</span>
        </div>
    </div>
    <div class="bg-orange-50 border-l-4 border-l-orange-500 p-3 rounded-r-lg text-[13px] text-orange-800 relative z-10 font-medium">
        Lưu ý đối với học viên vắng học nhiều: Giáo viên cần ghi chú rõ tình trạng để Trợ giảng phụ trách có định hướng ôn tập phù hợp.
    </div>
</div>

<!-- 1. Thời điểm & Điều kiện -->
<h3 class="text-[#00174f] text-xl font-bold font-display mb-6 flex items-center gap-2 border-b border-gray-100 pb-2">
    <span class="w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center text-sm">1</span> 
    Thời điểm & điều kiện gửi học viên phụ đạo
</h3>
<div class="flex flex-col md:flex-row gap-4 mb-10">
    <div class="flex-1 bg-white border border-gray-200 rounded-xl p-5 shadow-sm text-center relative">
        <div class="text-primary font-bold mb-2">Lần gửi thứ nhất</div>
        <div class="w-16 h-16 bg-blue-50 rounded-full flex items-center justify-center mx-auto mb-3 text-blue-600 font-display text-xl font-bold">T4-5</div>
        <p class="text-[13px] text-gray-600">Thường rơi vào Tuần 4–5 của khóa (Sau 3-4 tuần cân nhắc).</p>
    </div>
    <div class="hidden md:flex items-center justify-center text-gray-300">
        <span class="material-symbols-outlined text-3xl">arrow_forward</span>
    </div>
    <div class="flex-1 bg-white border border-gray-200 rounded-xl p-5 shadow-sm text-center relative">
        <div class="text-primary font-bold mb-2">Lần gửi thứ hai</div>
        <div class="w-16 h-16 bg-indigo-50 rounded-full flex items-center justify-center mx-auto mb-3 text-indigo-600 font-display text-xl font-bold">+3-4W</div>
        <p class="text-[13px] text-gray-600">Sau đó 3-4 tuần, rà soát lại và quyết định gửi lần 2 nếu chưa cải thiện.</p>
    </div>
    <div class="hidden md:flex items-center justify-center text-gray-300">
        <span class="material-symbols-outlined text-3xl">arrow_forward</span>
    </div>
    <div class="flex-1 bg-gray-50 border border-gray-200 rounded-xl p-5 shadow-sm text-center relative">
        <div class="text-gray-700 font-bold mb-2">Phát sinh</div>
        <div class="w-16 h-16 bg-white rounded-full border border-gray-200 flex items-center justify-center mx-auto mb-3 text-gray-600 font-display text-xl"><span class="material-symbols-outlined">support_agent</span></div>
        <p class="text-[13px] text-gray-600">Trung bình 2 lần/khóa. Nếu lớp đông cần thêm, báo Co-ordinator hỗ trợ.</p>
    </div>
</div>

<!-- 2. Thời gian đăng ký -->
<h3 class="text-[#00174f] text-xl font-bold font-display mb-6 flex items-center gap-2 border-b border-gray-100 pb-2">
    <span class="w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center text-sm">2</span> 
    Thời gian & cách thức đăng ký
</h3>
<div class="bg-red-50/30 border border-red-100 rounded-xl p-6 mb-10">
    <div class="flex items-center gap-3 mb-4">
        <span class="material-symbols-outlined text-red-500 text-3xl">pending_actions</span>
        <div>
            <div class="font-bold text-red-800 text-lg">Khung giờ vàng đăng ký hằng tuần</div>
            <div class="text-[14px] text-red-600">Bắt đầu từ <strong class="text-red-700 px-1 bg-red-100 rounded">13:00 Thứ Sáu</strong> đến <strong class="text-red-700 px-1 bg-red-100 rounded">23:59 Chủ Nhật</strong></div>
        </div>
    </div>
    <ul class="text-[14px] text-gray-700 space-y-3 p-4 bg-white rounded-lg border border-red-100/50">
        <li class="flex items-start gap-2"><span class="material-symbols-outlined text-[18px] text-red-400">cancel</span> <strong>Hủy Slot:</strong> Sau thời hạn trên, nếu chưa nhập đủ thông tin, Team Phụ đạo xin phép hủy slot để kịp gọi điện cho Phụ huynh.</li>
        <li class="flex items-start gap-2"><span class="material-symbols-outlined text-[18px] text-orange-400">warning</span> <strong>Giới hạn:</strong> Số lượng lớp giới hạn (phụ thuộc phòng & TA), ưu tiên đăng ký sớm.</li>
        <li class="flex items-start gap-2"><span class="material-symbols-outlined text-[18px] text-blue-400">info</span> <strong>Khẩn cấp:</strong> KHÔNG TỰ Ý xóa/sửa lịch lớp khác. Nếu cận thi cần gấp, liên hệ Lý Gia Linh (0939386227).</li>
    </ul>
</div>

<!-- 3. Quy mô & Hình thức -->
<h3 class="text-[#00174f] text-xl font-bold font-display mb-6 flex items-center gap-2 border-b border-gray-100 pb-2">
    <span class="w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center text-sm">3</span> 
    Quy mô lớp & hình thức dạy
</h3>
<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
    <div class="bg-white border border-gray-200 rounded-xl p-5 shadow-[0_2px_10px_rgba(0,0,0,0.02)] flex flex-col items-center text-center gap-2">
        <span class="material-symbols-outlined text-4xl text-blue-400">groups</span>
        <h4 class="font-bold text-gray-800">Sĩ số tối đa</h4>
        <p class="text-[14px] text-gray-600">5 – 7 học viên/lớp nhằm đảm bảo chất lượng sát sao.</p>
    </div>
    <div class="bg-white border border-gray-200 rounded-xl p-5 shadow-[0_2px_10px_rgba(0,0,0,0.02)] flex flex-col items-center text-center gap-2">
        <span class="material-symbols-outlined text-4xl text-purple-400">dark_mode</span>
        <h4 class="font-bold text-gray-800">Thời gian & Địa điểm</h4>
        <p class="text-[14px] text-gray-600">Khung giờ Tối (18:00–20:00). T2 - CN. Tại phòng học riêng do Trợ giảng (TA) đứng lớp.</p>
    </div>
    <div class="bg-white border border-gray-200 rounded-xl p-5 shadow-[0_2px_10px_rgba(0,0,0,0.02)] flex flex-col items-center text-center gap-2">
        <span class="material-symbols-outlined text-4xl text-green-400">done_all</span>
        <h4 class="font-bold text-gray-800">Cam kết tham gia</h4>
        <p class="text-[14px] text-gray-600">Học viên chỉ tham gia khi Trung tâm đã chốt lịch và thông báo thành công cho Phụ huynh.</p>
    </div>
</div>

<!-- 4. Yêu cầu nhập nội dung -->
<h3 class="text-[#00174f] text-xl font-bold font-display mb-6 flex items-center gap-2 border-b border-gray-100 pb-2">
    <span class="w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center text-sm">4</span> 
    Yêu cầu nhập nội dung trực tuyến
</h3>
<div class="bg-gray-50 rounded-2xl p-6 md:p-8 border border-gray-200 mb-10">
    <div class="space-y-6">
        <div class="bg-white p-5 rounded-xl border border-blue-100 shadow-sm">
            <h4 class="font-bold text-blue-800 mb-2 flex items-center gap-2"><span class="material-symbols-outlined">menu_book</span> Lesson Content</h4>
            <p class="text-[14px] text-gray-700 pl-8">Ghi rõ nội dung trọng tâm cần ôn tập (ngữ pháp, từ vựng, kỹ năng cụ thể). <strong>Tránh chung chung hoặc quá tải.</strong> Đính kèm link tài liệu/handouts nếu có.</p>
        </div>
        <div class="bg-white p-5 rounded-xl border border-green-100 shadow-sm relative">
            <h4 class="font-bold text-green-800 mb-2 flex items-center gap-2"><span class="material-symbols-outlined">chat</span> Teacher's Comment / Note</h4>
            <p class="text-[14px] text-gray-700 pl-8 mb-3">Nhận xét theo hướng <strong>mô tả – hỗ trợ</strong> phục vụ tư vấn Phụ huynh.<br> <span class="text-gray-500 italic">Ví dụ: "cần thêm gợi ý khi làm bài", "chưa thành thạo", "cần luyện tập".</span></p>
            <div class="pl-8 text-[13px] text-red-600 font-bold flex items-center gap-1"><span class="material-symbols-outlined text-[16px]">cancel</span> Cấm sử dụng từ tiêu cực hoặc so sánh với bạn khác!</div>
        </div>
        <div class="bg-white p-5 rounded-xl border border-orange-100 shadow-sm">
            <h4 class="font-bold text-orange-800 mb-2 flex items-center gap-2"><span class="material-symbols-outlined">badge</span> Thông tin học viên (Họ tên - SĐT)</h4>
            <p class="text-[14px] text-gray-700 pl-8">Sao chép trực tiếp từ hệ thống Web (Previous Lessons Diary &rarr; Student List). Nhập đầy đủ <strong>NGAY KHI ĐĂNG KÝ</strong>, không được giữ chỗ trống.</p>
        </div>
    </div>
</div>

<!-- 5. Theo dõi sau Phụ đạo -->
<div class="bg-[#00174f] text-white rounded-xl p-6 md:p-8 flex flex-col md:flex-row items-center gap-6 shadow-lg">
    <div class="w-16 h-16 rounded-full bg-white/10 flex items-center justify-center shrink-0">
        <span class="material-symbols-outlined text-4xl text-blue-300">find_in_page</span>
    </div>
    <div>
        <h4 class="font-bold text-xl mb-2 font-display">5. Theo dõi sau buổi phụ đạo</h4>
        <p class="text-[15px] text-blue-100 leading-relaxed">Sau buổi học 1–2 ngày, Giáo viên có trách nhiệm truy cập lại File đăng ký để xem nhận xét của TA ở cột <strong>FEEDBACK</strong>, từ đó đánh giá mức độ cải thiện và lập kế hoạch hỗ trợ tiếp theo cho học viên.</p>
    </div>
</div>
"""

html_hoc_bong = """
<div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">
    <span class="text-primary font-bold tracking-wider uppercase text-sm font-body bg-blue-50 w-max px-3 py-1 rounded-full border border-blue-100">KIDS & TEENS</span>
    <h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display mt-2 mb-2">QUY ĐỊNH MỨC HỌC BỔNG</h2>
</div>

<!-- 1. Bảng quy định -->
<h3 class="text-[#00174f] text-xl font-bold font-display mb-6 flex items-center gap-2">
    <span class="material-symbols-outlined text-primary text-[28px]">workspace_premium</span>
    1. Các mức học bổng áp dụng
</h3>

<div class="overflow-x-auto rounded-xl border border-gray-200 shadow-sm mb-12">
    <table class="w-full text-left border-collapse text-[14px] md:text-[15px] font-body bg-white">
        <thead>
            <tr class="bg-gradient-to-r from-[#00174f] to-blue-900 text-white">
                <th class="py-4 px-6 font-bold w-[10%] text-center border-r border-blue-800">STT</th>
                <th class="py-4 px-6 font-bold w-[40%] border-r border-blue-800">Tên học bổng & Tiêu chí</th>
                <th class="py-4 px-6 font-bold text-center border-r border-blue-800"><div class="text-[12px] font-normal text-blue-200 uppercase tracking-wider mb-1">Mức thưởng cho</div>Lớp từ 18+ HV</th>
                <th class="py-4 px-6 font-bold text-center"><div class="text-[12px] font-normal text-blue-200 uppercase tracking-wider mb-1">Mức thưởng cho</div>Lớp từ 09-17 HV</th>
            </tr>
        </thead>
        <tbody class="text-gray-700 divide-y divide-gray-100">
            <tr class="hover:bg-yellow-50/30 transition-colors">
                <td class="py-5 px-6 text-center font-bold text-xl text-yellow-500 border-r border-gray-100">1</td>
                <td class="py-5 px-6 border-r border-gray-100">
                    <div class="font-bold text-gray-800 text-[16px]">Học bổng 01</div>
                    <div class="text-[13px] text-gray-500 mt-1">Dành cho học viên đạt kết quả cao nhất trong suốt khóa học.</div>
                </td>
                <td class="py-5 px-6 text-center border-r border-gray-100">
                    <span class="inline-block bg-yellow-100 text-yellow-800 font-bold px-4 py-1.5 rounded-full text-lg shadow-sm">75%</span>
                </td>
                <td class="py-5 px-6 text-center">
                    <span class="inline-block bg-yellow-50 text-yellow-700 font-bold px-4 py-1.5 rounded-full text-lg shadow-sm border border-yellow-100">50%</span>
                </td>
            </tr>
            <tr class="hover:bg-gray-50 transition-colors">
                <td class="py-5 px-6 text-center font-bold text-xl text-gray-400 border-r border-gray-100">2</td>
                <td class="py-5 px-6 border-r border-gray-100">
                    <div class="font-bold text-gray-800 text-[16px]">Học bổng 02</div>
                    <div class="text-[13px] text-gray-500 mt-1">Dành cho học viên đạt kết quả thứ hai trong suốt khóa học.</div>
                </td>
                <td class="py-5 px-6 text-center border-r border-gray-100">
                    <span class="inline-block bg-gray-100 text-gray-700 font-bold px-4 py-1.5 rounded-full text-lg shadow-sm">50%</span>
                </td>
                <td class="py-5 px-6 text-center">
                    <span class="inline-block bg-gray-50 text-gray-600 font-bold px-4 py-1.5 rounded-full text-lg shadow-sm border border-gray-200">30%</span>
                </td>
            </tr>
            <tr class="hover:bg-orange-50/30 transition-colors">
                <td class="py-5 px-6 text-center font-bold text-xl text-orange-400 border-r border-gray-100">3</td>
                <td class="py-5 px-6 border-r border-gray-100">
                    <div class="font-bold text-gray-800 text-[16px]">Học bổng 03</div>
                    <div class="text-[13px] text-gray-500 mt-1">Dành cho học viên đạt kết quả thứ ba trong suốt khóa học.</div>
                </td>
                <td class="py-5 px-6 text-center border-r border-gray-100">
                    <span class="inline-block bg-orange-100 text-orange-800 font-bold px-4 py-1.5 rounded-full text-lg shadow-sm">25%</span>
                </td>
                <td class="py-5 px-6 text-center">
                    <span class="inline-block bg-orange-50 text-orange-700 font-bold px-4 py-1.5 rounded-full text-lg shadow-sm border border-orange-100">20%</span>
                </td>
            </tr>
        </tbody>
    </table>
</div>

<div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8 items-stretch">
    <!-- 2. Phạm vi áp dụng -->
    <div class="bg-gray-50 border border-gray-200 rounded-2xl p-6 md:p-8 flex flex-col justify-center">
        <h3 class="text-[#00174f] text-xl font-bold font-display mb-4 flex items-center gap-2">
            <span class="material-symbols-outlined text-primary">rule</span>
            2. Phạm vi áp dụng
        </h3>
        <p class="text-[15px] text-gray-700 mb-4">Chính sách học bổng này có <strong>cột mốc bắt buộc</strong> áp dụng dựa trên sĩ số thực tế của lớp.</p>
        <div class="flex flex-col gap-3">
            <div class="flex items-center gap-3 bg-white p-3 rounded-xl border border-green-200 text-green-800 font-medium">
                <span class="material-symbols-outlined text-green-500">check_circle</span> Áp dụng cho lớp có sĩ số ≥ 09 học viên.
            </div>
            <div class="flex items-center gap-3 bg-white p-3 rounded-xl border border-red-200 text-red-800 font-medium opacity-80">
                <span class="material-symbols-outlined text-red-500">cancel</span> KHÔNG áp dụng cho lớp có sĩ số < 09.
            </div>
        </div>
    </div>

    <!-- 3. Lưu ý trong công tác chấm điểm -->
    <div class="bg-blue-50/50 border border-blue-100 rounded-2xl p-6 md:p-8">
        <h3 class="text-[#00174f] text-xl font-bold font-display mb-4 flex items-center gap-2">
            <span class="material-symbols-outlined text-primary">edit_square</span>
            3. Lưu ý: Chấm điểm & Xếp hạng
        </h3>
        <ul class="space-y-4 text-[14px] text-gray-700">
            <li class="flex items-start gap-3">
                <span class="material-symbols-outlined text-blue-500 shrink-0">crisis_alert</span>
                <div><strong>Khách quan & Phân hóa:</strong> Cần chấm điểm cẩn trọng, có sự phân hóa rõ ràng giữa các mức kết quả.</div>
            </li>
            <li class="flex items-start gap-3">
                <span class="material-symbols-outlined text-red-400 shrink-0">warning</span>
                <div><strong>Tránh tình trạng đồng điểm:</strong> Hạn chế tuyệt đối việc nhiều học viên có tổng điểm bằng nhau trong Top 3 cao nhất lớp.</div>
            </li>
            <li class="flex items-start gap-3">
                <span class="material-symbols-outlined text-purple-500 shrink-0">manage_search</span>
                <div>
                    <strong>Phân xử sát điểm:</strong> Khi điểm số quá sát nhau, phải xem xét tổng thể toàn khóa bao gồm:
                    <ul class="list-disc pl-5 mt-1 text-[13px] text-gray-600 space-y-0.5">
                        <li>Quá trình học tập & Mức độ tiến bộ.</li>
                        <li>Thái độ và sự tham gia.</li>
                        <li>Độ khó bài kiểm tra.</li>
                    </ul>
                </div>
            </li>
        </ul>
    </div>
</div>
"""

html_khao_thi = """
<div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">
    <h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display mt-2 mb-2">QUY ĐỊNH & HƯỚNG DẪN TỔ CHỨC THI CUỐI KHÓA</h2>
</div>

<!-- Section A: ADU -->
<div class="mb-14">
    <div class="bg-[#00174f] p-4 rounded-t-xl text-white font-bold font-display text-lg tracking-wide">
        PHẦN 1: CHƯƠNG TRÌNH ACADEMIC (ADU)
    </div>
    <div class="bg-white border border-t-0 border-gray-200 rounded-b-xl p-6 md:p-8 shadow-sm">
        <p class="text-[14px] text-gray-500 mb-6 italic">Áp dụng cho: Academic English, EFL, IELTS for Teens, IELTS.</p>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 relative">
            
            <div class="space-y-8">
                <!-- 1. Lịch thi & Cấu trúc -->
                <div class="relative pl-8">
                    <div class="absolute left-0 top-0 text-gray-200 material-symbols-outlined text-[40px] -ml-2 -mt-2">calendar_month</div>
                    <div class="relative z-10">
                        <h4 class="font-bold text-[#00174f] text-lg mb-2">1. Lịch thi & 2. Tham khảo Cấu trúc</h4>
                        <ul class="text-[14px] text-gray-600 space-y-2 list-disc ml-4">
                            <li>Xem trên Hệ thống quản lý: <code class="bg-gray-100 text-blue-700 px-1 rounded">Final Test - [Kỹ năng]</code>.</li>
                            <li>Nếu cần cấu trúc đề, liên hệ Nhân sự/Phòng ĐT.</li>
                        </ul>
                        <div class="mt-3 bg-red-50 text-red-700 font-medium text-[13px] p-3 rounded-lg border border-red-100 flex items-start gap-2">
                            <span class="material-symbols-outlined text-[16px]">gpp_bad</span> Đề thi không được cung cấp trước dưới mọi hình thức!
                        </div>
                    </div>
                </div>

                <!-- 3. Nhận đề -->
                <div class="relative pl-8">
                    <div class="absolute left-0 top-0 text-gray-200 material-symbols-outlined text-[40px] -ml-2 -mt-2">inventory</div>
                    <div class="relative z-10">
                        <h4 class="font-bold text-[#00174f] text-lg mb-2">3. Nhận đề thi (Trước 15 phút)</h4>
                        <div class="bg-blue-50/50 p-4 rounded-lg border border-blue-100 text-[14px]">
                            <ul class="space-y-2 text-gray-700">
                                <li><strong>CN 30/4, Bình Minh, Ô Môn:</strong> Nhận tại Quầy Tư vấn.</li>
                                <li><strong>CN 39 Mậu Thân & DCT:</strong> Nhận tại Phòng Giáo viên của cơ sở đó.</li>
                            </ul>
                            <p class="mt-3 font-medium text-orange-700 flex items-center gap-1"><span class="material-symbols-outlined text-[16px]">visibility</span> Bắt buộc kiểm tra số lượng & nội dung ngay khi nhận!</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="space-y-8">
                <!-- 4. Chấm bài -->
                <div class="relative pl-8">
                    <div class="absolute left-0 top-0 text-gray-200 material-symbols-outlined text-[40px] -ml-2 -mt-2">draw</div>
                    <div class="relative z-10">
                        <h4 class="font-bold text-[#00174f] text-lg mb-2">4. Thời hạn Chấm bài (<span class="text-primary">03 Ngày</span>)</h4>
                        <p class="text-[14px] text-gray-600 mb-2">Tính từ:</p>
                        <ul class="text-[14px] text-gray-600 space-y-2 list-disc ml-4">
                            <li><strong>Ngày thi:</strong> Nếu Giáo viên trực tiếp gác thi.</li>
                            <li><strong>Ngày P.ĐT thông báo:</strong> Nếu Giáo viên không gác thi lớp đó.</li>
                        </ul>
                    </div>
                </div>

                <!-- 5. Nhập điểm -->
                <div class="relative pl-8">
                    <div class="absolute left-0 top-0 text-gray-200 material-symbols-outlined text-[40px] -ml-2 -mt-2">cloud_upload</div>
                    <div class="relative z-10">
                        <h4 class="font-bold text-[#00174f] text-lg mb-2">5. Nhập điểm & Trả bài</h4>
                        <div class="bg-gray-50 border border-gray-200 p-4 rounded-lg text-[14px] text-gray-700">
                            <strong>Academic English:</strong> Nhập Hệ thống Quản lý ngay khi có điểm.<br><br>
                            Sau đó hoàn trả bài thi vật lý về Phòng Đào tạo đúng quy định.
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</div>

<!-- Section B: YLE -->
<div>
    <div class="bg-gradient-to-r from-orange-400 to-orange-500 p-4 rounded-t-xl text-white font-bold font-display text-lg tracking-wide">
        PHẦN 2: CHƯƠNG TRÌNH KIDS & TEENS (YLE)
    </div>
    <div class="bg-white border border-t-0 border-gray-200 rounded-b-xl p-6 md:p-8 shadow-sm">
        
        <div class="grid grid-cols-1 gap-10">
            
            <!-- Trình tự thời gian -->
            <div class="relative overflow-hidden">
                <div class="absolute left-[39px] top-6 bottom-6 w-0.5 bg-gray-200 z-0 hidden md:block"></div>
                
                <div class="flex flex-col md:flex-row gap-6 items-start mb-10 relative z-10">
                    <div class="w-20 h-20 rounded-full bg-orange-100 text-orange-600 flex flex-col items-center justify-center shrink-0 border-4 border-white shadow-sm font-bold leading-tight">
                        <span class="text-xl">- 7</span>
                        <span class="text-[10px] uppercase">Ngày</span>
                    </div>
                    <div class="flex-1 bg-gray-50 p-5 rounded-xl border border-gray-200">
                        <h4 class="font-bold text-gray-800 text-lg mb-2">1. Email Thông báo Lịch thi</h4>
                        <p class="text-[14px] text-gray-600">Kiểm tra Hệ thống (THI NÓI / THI NGHE - ĐỌC - VIẾT). Phòng Đào tạo sẽ gửi Email gồm Lịch thi & <strong>Link Audio</strong>. Bắt buộc xem, xác nhận và phản hồi nếu sai sót.</p>
                    </div>
                </div>

                <div class="flex flex-col md:flex-row gap-6 items-start mb-10 relative z-10">
                    <div class="w-20 h-20 rounded-full bg-orange-100 text-orange-600 flex flex-col items-center justify-center shrink-0 border-4 border-white shadow-sm font-bold leading-tight">
                        <span class="text-xl">- 1</span>
                        <span class="text-[10px] uppercase">Ngày</span>
                    </div>
                    <div class="flex-1 bg-gray-50 p-5 rounded-xl border border-gray-200">
                        <h4 class="font-bold text-gray-800 text-lg mb-2">2. Nhận đề thi trực tiếp</h4>
                        <p class="text-[14px] text-gray-600 mb-2"><strong>30/4, Bình Minh, Ô Môn:</strong> Quầy TV nhánh. | <strong>39 MT & DCT:</strong> Chỉ nhận tại Quầy TV 39 Mậu Thân.</p>
                        <div class="bg-yellow-50 text-yellow-800 text-[13px] px-3 py-2 rounded font-medium border border-yellow-200 inline-flex items-center gap-2">
                            <span class="material-symbols-outlined text-[16px]">headphones</span> Kiểm tra cẩn thận đề thi cứng đã khớp với Audio chưa!
                        </div>
                    </div>
                </div>

                <div class="flex flex-col md:flex-row gap-6 items-start mb-10 relative z-10">
                    <div class="w-20 h-20 rounded-full bg-blue-100 text-blue-600 flex flex-col items-center justify-center shrink-0 border-4 border-white shadow-sm font-bold leading-tight">
                        <span class="text-[13px] px-2 text-center">TRONG BUỔI THI</span>
                    </div>
                    <div class="flex-1 bg-white border border-blue-200 p-5 rounded-xl shadow-[0_4px_15px_rgba(0,0,0,0.03)] border-l-4 border-l-blue-500">
                        <h4 class="font-bold text-[#00174f] text-lg mb-3">3. Tổ chức trong buổi thi</h4>
                        <div class="text-[14px] text-gray-700 space-y-3">
                            <p>Tự sắp xếp thứ tự Speaking. SV chờ ôn tập (nhờ TA hỗ trợ).</p>
                            <div class="bg-blue-50/50 p-3 rounded-lg border border-blue-100">
                                <strong class="text-blue-800">Cơ chế thi bù tại chỗ:</strong> Vắng Speaking nhưng có thi Writing &rarr; Có thể gài chức năng thi bù Speaking luôn tại khu vực trống (nhờ TA trông lớp hộ).
                            </div>
                            <div class="bg-gray-50 p-3 rounded-lg border border-gray-100">
                                <strong class="text-gray-800">Danh sách thi lại:</strong> Lập danh sách cho HV vắng Writing HOẶC vắng cả 2. Gửi Nhân sự phụ trách theo y/c Email.
                            </div>
                        </div>
                        
                        <div class="mt-4 pt-4 border-t border-gray-100">
                            <h4 class="font-bold text-gray-800 mb-2">4. Trả đề thi Ngay Lập Tức:</h4>
                            <p class="text-[13px] text-gray-600">Ký xác nhận trả Flashcard & Đề dư tại Quầy Tư vấn <strong>ngay sau buổi thi cuối.</strong></p>
                        </div>
                    </div>
                </div>

                <div class="flex flex-col md:flex-row gap-6 items-start relative z-10">
                    <div class="w-20 h-20 rounded-full bg-green-100 text-green-600 flex flex-col items-center justify-center shrink-0 border-4 border-white shadow-sm font-bold leading-tight">
                        <span class="text-xl">+ 3</span>
                        <span class="text-[10px] uppercase">Ngày</span>
                    </div>
                    <div class="flex-1 bg-gray-50 p-5 rounded-xl border border-gray-200">
                        <h4 class="font-bold text-gray-800 text-lg mb-2">5. Nhập điểm, Sổ LL & Trả bài</h4>
                        <ul class="text-[14px] text-gray-700 space-y-2 list-disc ml-4 mb-4">
                            <li><strong>Trong 3 ngày:</strong> Nhập điểm Online & Hoàn thành Sổ Liên Lạc Đợt 3.</li>
                            <li><strong>Trong 7 ngày:</strong> Nộp lại bài thi đã chấm cho Phòng Đào tạo.</li>
                        </ul>
                        <div class="bg-green-50 text-green-800 text-[13px] px-4 py-3 rounded-lg border border-green-200">
                            <strong>Quy cách gói bài trả về:</strong> Xếp gọn &rarr; Ghi thông tin ngoài bìa (Lớp, Khóa, Lịch, Tên GV, SL bài). KHÔNG gộp chung các lớp khác nhau hoặc gộp vào túi để thi trống.
                        </div>
                    </div>
                </div>

            </div>
            
        </div>
    </div>
</div>
"""

html_nghi_phep = """
<div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">
    <span class="text-primary font-bold tracking-wider uppercase text-sm font-body bg-blue-50 w-max px-3 py-1 rounded-full border border-blue-100">KIDS & TEENS (YLE)</span>
    <h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display mt-2 mb-2">QUY ĐỊNH XIN NGHỈ PHÉP</h2>
</div>

<!-- Mục đích / Nguyên Tắc -->
<div class="bg-gray-50 border border-gray-200 rounded-2xl p-6 mb-10 text-[14px] text-gray-700">
    <p>Quy định nhằm đảm bảo hoạt động giảng dạy liên tục, phối hợp điều phối GV dạy thay hiệu quả. CB-GV có quyền hạn Nghỉ phép, tuy nhiên cần thông báo <strong>Đúng Hạn - Đúng Quy Trình - Đúng Kênh</strong>.</p>
</div>

<!-- THỜI GIAN & HÌNH THỨC SƠ ĐỒ -->
<h3 class="text-[#00174f] text-xl font-bold font-display mb-6 flex items-center gap-2">
    <span class="material-symbols-outlined text-primary text-[28px]">event_busy</span>
    I. Kịch bản Thời gian & Hình thức Xin Nghỉ
</h3>

<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12 items-stretch">
    <!-- Ngắn hạn -->
    <div class="bg-white rounded-2xl p-6 border border-blue-200 shadow-[0_4px_15px_-5px_rgba(13,89,242,0.1)] hover:border-blue-400 transition-colors flex flex-col">
        <div class="w-12 h-12 bg-blue-50 text-blue-600 rounded-full flex items-center justify-center mb-4"><span class="material-symbols-outlined">hourglass_empty</span></div>
        <h4 class="font-bold text-gray-800 text-lg">1. Nghỉ Ngắn Hạn</h4>
        <p class="text-[13px] text-gray-500 mb-4">(Tối đa vài ngày)</p>
        <div class="bg-blue-50/50 p-3 rounded-lg border border-blue-100 text-[13px] text-gray-700 mb-4">
            Gửi EMAIL trước ít nhất <strong>01 TUẦN</strong>.
        </div>
        <div class="mt-auto bg-gray-50 p-3 rounded-lg text-[13px] border border-gray-100">
            <strong>Nếu phát sinh việc gấp:</strong>
            <ul class="list-disc pl-4 mt-1 text-gray-600">
                <li>Báo ráo rút tối thiểu 48 tiếng.</li>
                <li>Lớp cuối tuần: Hạn chót 23h thứ Tư.</li>
                <li>Lúc này nhắn Zalo cho nhanh.</li>
            </ul>
        </div>
    </div>
    
    <!-- Dài hạn -->
    <div class="bg-white rounded-2xl p-6 border border-purple-200 shadow-[0_4px_15px_-5px_rgba(168,85,247,0.1)] hover:border-purple-400 transition-colors flex flex-col">
        <div class="w-12 h-12 bg-purple-50 text-purple-600 rounded-full flex items-center justify-center mb-4"><span class="material-symbols-outlined">date_range</span></div>
        <h4 class="font-bold text-gray-800 text-lg">2. Nghỉ Dài Hạn</h4>
        <p class="text-[13px] text-gray-500 mb-4">(Từ 1 tuần trở lên)</p>
        <div class="bg-purple-50/50 p-3 rounded-lg border border-purple-100 text-[13px] text-gray-700 mt-auto">
            Gửi EMAIL trước ít nhất <strong>02 TUẦN</strong>.<br><br>
            Bắt buộc trình bày kế hoạch sắp xếp công việc và phương án phối hợp hỗ trợ dạy thay vắng mặt.
        </div>
    </div>
    
    <!-- Đột xuất -->
    <div class="bg-white rounded-2xl p-6 border border-red-200 shadow-[0_4px_15px_-5px_rgba(239,68,68,0.1)] hover:border-red-400 transition-colors flex flex-col">
        <div class="w-12 h-12 bg-red-50 text-red-600 rounded-full flex items-center justify-center mb-4"><span class="material-symbols-outlined">running_with_errors</span></div>
        <h4 class="font-bold text-gray-800 text-lg">3. Nghỉ Đột Xuất Cấp Bách</h4>
        <p class="text-[13px] text-gray-500 mb-4">(Sát giờ không thể báo trước)</p>
        <div class="bg-red-50/50 p-3 rounded-lg border border-red-100 text-[13px] text-red-800 mt-auto font-medium text-center">
            <span class="material-symbols-outlined text-3xl mb-2 block">phone_in_talk</span>
            GỌI ĐIỆN THOẠI TRỰC TIẾP ngay cho nhân sự điều phối để phòng cháy chữa cháy!
        </div>
    </div>
</div>

<!-- KÊNH LIÊN HỆ -->
<div class="bg-[#00174f] text-white rounded-2xl p-8 mb-12 relative overflow-hidden">
    <div class="absolute right-0 top-0 opacity-10 translate-x-1/4 -translate-y-1/4">
        <span class="material-symbols-outlined text-[200px]">contact_phone</span>
    </div>
    <div class="relative z-10">
        <h3 class="text-xl font-bold font-display mb-6 border-b border-white/20 pb-3">II. Danh bạ Khẩn YLE & Quy ước Phương thức</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-6">
            <div class="bg-white/10 rounded-xl p-5 border border-white/20 backdrop-blur-sm">
                <div class="flex items-center gap-3 mb-2 font-bold text-lg text-blue-200"><span class="material-symbols-outlined">person</span> Nguyễn Hoàng Phúc</div>
                <div class="text-[14px]">Tổ trưởng Tổ YLE</div>
                <div class="mt-3 text-[13px] space-y-1">
                    <div class="flex items-center gap-2"><span>E:</span> <a href="mailto:phuc116634@gmail.com" class="underline">phuc116634@gmail.com</a></div>
                    <div class="flex items-center gap-2"><span>P:</span> <strong>0354 367 827</strong> (Zalo/Call)</div>
                </div>
            </div>
            <div class="bg-white/10 rounded-xl p-5 border border-white/20 backdrop-blur-sm">
                <div class="flex items-center gap-3 mb-2 font-bold text-lg text-blue-200"><span class="material-symbols-outlined">person_4</span> Trần Tố Quyên</div>
                <div class="text-[14px]">Chuyên viên Phòng Đào tạo</div>
                <div class="mt-3 text-[13px] space-y-1">
                    <div class="flex items-center gap-2"><span>E:</span> <a href="mailto:toquyentran637@gmail.com" class="underline">toquyentran637@gmail.com</a></div>
                    <div class="flex items-center gap-2"><span>P:</span> <strong>0945 855 308</strong> (Zalo/Call)</div>
                </div>
            </div>
        </div>
        <div class="bg-black/30 w-fit px-4 py-2 rounded-lg text-sm font-medium">
            <strong>Nguyên tắc:</strong> Mặc định quy trình chuẩn xài EMAIL. Cần phản hồi ngay/Đột xuất mở ZALO/CALL.
        </div>
    </div>
</div>

<!-- QUY TRÌNH HẬU XIN NGHỈ & BÁO BÀI DẠY THẾ -->
<h3 class="text-[#00174f] text-xl font-bold font-display mb-6 flex items-center gap-2">
    <span class="material-symbols-outlined text-primary text-[28px]">assignment_add</span>
    III. Quy trình xử lý Bàn giao Bài Dạy Thế
</h3>

<div class="flex flex-col md:flex-row gap-8 items-start mb-10">
    <!-- Timeline left -->
    <div class="flex-1 space-y-6 relative border-l-2 border-dashed border-gray-300 pl-6 ml-3">
        <div class="relative">
            <div class="absolute -left-[30px] top-1 w-4 h-4 rounded-full bg-primary border-4 border-white"></div>
            <h5 class="font-bold text-gray-800 text-lg mb-1">Gửi Mẫu Báo Bài (Phụ Lục)</h5>
            <p class="text-[14px] text-gray-600">Trong 24h sau khi chốt nghỉ, điền và gửi [Mẫu báo bài dạy thế] cho nhân sự điều phối (Lưu ý lớp có GVNN phải ghi đúng timeframe cần dạy thế).</p>
        </div>
        <div class="relative">
            <div class="absolute -left-[30px] top-1 w-4 h-4 rounded-full bg-primary border-4 border-white"></div>
            <h5 class="font-bold text-gray-800 text-lg mb-1">Nhân sự P.ĐT xử lý</h5>
            <p class="text-[14px] text-gray-600">Sẽ chốt giáo viên thay thế, ban phát slide/nội dung qua GV mới, và cập nhật chỉnh sửa lịch trên HTQL online.</p>
        </div>
        <div class="relative">
            <div class="absolute -left-[30px] top-1 w-4 h-4 rounded-full bg-green-500 border-4 border-white shadow-[0_0_10px_rgba(34,197,94,0.5)]"></div>
            <h5 class="font-bold text-gray-800 text-lg mb-1">Kiểm tra chép bài đôi</h5>
            <div class="bg-gray-50 border border-gray-200 p-3 rounded-lg text-[13px] text-gray-700 mt-2">
                Nghĩa vụ của bạn là check lại xem (1) File hệ thống đã ghi tên GV mới chưa, (2) App cá nhân đã biến mất cục gạch lớp đó chưa. Nếu chưa báo ngay. (Vắng sinh tử cần nhắc nhân sự lại 1 bận).
            </div>
        </div>
    </div>
    
    <!-- Code block template -->
    <div class="w-full md:w-[50%] lg:w-[45%]">
        <div class="bg-gray-900 rounded-xl overflow-hidden shadow-lg border border-gray-800">
            <div class="bg-gray-800 px-4 py-3 border-b border-gray-700 flex justify-between items-center text-gray-300 text-sm font-mono">
                <div class="flex gap-2">
                    <span class="w-3 h-3 rounded-full bg-red-500"></span>
                    <span class="w-3 h-3 rounded-full bg-yellow-500"></span>
                    <span class="w-3 h-3 rounded-full bg-green-500"></span>
                </div>
                Form_Day_The.txt
            </div>
            <div class="p-5 text-[#a3b1c6] text-[13px] font-mono whitespace-pre-line leading-relaxed h-full overflow-y-auto max-h-[400px]">
                <span class="text-white font-bold block mb-2">MẪU THÔNG TIN BÀI DẠY THẾ</span>
Dạy thế (Ms./Mr.):
Ngày: 
Giờ dạy:
Lớp/Cấp độ:
Phòng:
Sĩ số:
Nội dung giảng dạy: <span class="text-green-400"># VD: Unit 9 - L.2 - p.65</span>
Lưu ý khác:
<span class="text-gray-500">(về học viên cá biệt, activities gợi ý..)</span>
            </div>
        </div>
    </div>
</div>
"""

def main():
    pages = [
        ("Quy định Phụ đạo", ["Đào tạo & Đảm bảo chất lượng", "Quy định & Quy trình giảng dạy", "Quy định Phụ đạo"], html_phu_dao, "quy-dinh-phu-dao.html"),
        ("Chính sách Học bổng", ["Đào tạo & Đảm bảo chất lượng", "Các chính sách cốt lõi", "Chính sách Học bổng"], html_hoc_bong, "chinh-sach-hoc-bong.html"),
        ("Quy định Khảo thí", ["Đào tạo & Đảm bảo chất lượng", "Quy định & Quy trình giảng dạy", "Quy định Khảo thí"], html_khao_thi, "quy-dinh-khao-thi.html"),
        ("Quy định Nghỉ phép", ["Đào tạo & Đảm bảo chất lượng", "Quy định & Quy trình giảng dạy", "Quy định Nghỉ phép"], html_nghi_phep, "quy-dinh-nghi-phep.html")
    ]
    for title, breadcrumbs, content_html, filename in pages:
        generate_page(title, breadcrumbs, content_html, filename)

if __name__ == '__main__':
    main()
