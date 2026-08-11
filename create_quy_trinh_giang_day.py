import os

def create_quy_trinh():
    source_file = '/Users/vobac/Downloads/gia-viet-handbook/giao-trinh-tai-lieu.html'
    target_file = '/Users/vobac/Downloads/gia-viet-handbook/quy-trinh-giang-day.html'
    
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Title tag
    content = content.replace(
        '<title>Giáo trình & Tài liệu giảng dạy - Handbook</title>',
        '<title>Quy trình giảng dạy & khen thưởng - Handbook</title>'
    )
    
    start_str = '<!-- Breadcrumb & Title Area -->'
    end_str = '<!-- Right Column: Sidebar -->'
    
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    
    if start_idx == -1 or end_idx == -1:
        print("Could not find boundaries!")
        return

    new_section = """<!-- Breadcrumb & Title Area -->
            <div class="w-full bg-white py-12 px-4 md:px-10 border-b border-gray-100 shadow-sm relative overflow-hidden">
                <div class="absolute right-0 top-0 w-64 h-64 bg-blue-50/50 rounded-full translate-x-1/2 -translate-y-1/2 opacity-50"></div>
                <div class="absolute right-0 top-0 w-32 h-32 text-blue-100 translate-x-1/4 -translate-y-1/4 opacity-30" style="background-image: radial-gradient(#0d59f2 2px, transparent 2px); background-size: 16px 16px;"></div>

                <div class="w-full max-w-[1280px] mx-auto relative z-10 font-body">
                    <h1 class="text-3xl md:text-4xl font-bold text-[#00174f] mb-6 font-display tracking-wide">Quy trình giảng dạy & khen thưởng</h1>
                    <div class="flex items-center gap-2 text-[15px] text-gray-500 font-body flex-wrap">
                        <a href="index.html" class="flex items-center hover:text-primary transition-colors">
                            <span class="material-symbols-outlined text-[18px]">home</span>
                            <span class="ml-1">Trang chủ</span>
                        </a>
                        <span class="material-symbols-outlined text-sm">chevron_right</span>
                        <a href="dao-tao-dam-bao-chat-luong.html" class="hover:text-primary transition-colors whitespace-nowrap">Đào tạo & Đảm bảo chất lượng</a>
                        <span class="material-symbols-outlined text-sm">chevron_right</span>
                        <a href="#" class="hover:text-primary transition-colors whitespace-nowrap">Quy định & Quy trình giảng dạy</a>
                        <span class="material-symbols-outlined text-sm">chevron_right</span>
                        <span class="text-[#0d121c] whitespace-nowrap">Quy trình giảng dạy & khen thưởng</span>
                    </div>
                </div>
            </div>

            <!-- 2 Column Layout -->
            <div class="w-full max-w-[1440px] px-4 md:px-10 py-16 mx-auto">
                <div class="flex flex-col md:flex-row gap-8 lg:gap-16 items-start">

                    <!-- Left Column: Content -->
                    <div class="w-full md:w-[70%] lg:w-[75%] font-body text-gray-800 leading-relaxed space-y-8">
                        <div class="bg-white rounded-2xl shadow-sm border border-gray-100/50 p-6 md:p-10">
                            
                            <div class="flex flex-col gap-2 mb-10">
                                <span class="text-primary font-bold tracking-wider uppercase text-sm font-body">Quy định & Quy trình giảng dạy</span>
                                <h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display mt-2">KHEN THƯỞNG & QUY TRÌNH HỌC THỬ</h2>
                            </div>

                            <!-- Section 1: Việc phát Logos -->
                            <div class="bg-gradient-to-r from-yellow-50/50 to-orange-50/30 border border-yellow-200 rounded-2xl p-6 md:p-8 mb-12 flex flex-col md:flex-row items-center md:items-start gap-8 shadow-sm hover:shadow-md transition-shadow">
                                <div class="w-20 h-20 rounded-full bg-white text-yellow-500 flex items-center justify-center shrink-0 shadow-[0_4px_15px_rgba(0,0,0,0.05)] border border-yellow-100">
                                    <span class="material-symbols-outlined text-4xl">star_rate</span>
                                </div>
                                <div class="text-gray-700 font-body flex-1">
                                    <h3 class="text-xl font-bold text-[#00174f] mb-3 font-display">1. Về việc phát Logos & Đổi quà</h3>
                                    <p class="mb-5 leading-relaxed text-[15px] text-gray-600">Việc phát Logos và đổi quà là hoạt động mang tính khuyến khích, tạo động lực học tập, nhằm tăng sự hứng thú và mức độ tham gia của học viên trong các buổi học (bên cạnh các yếu tố cốt lõi như nội dung giảng dạy, hoạt động lớp).</p>
                                    
                                    <div class="grid grid-cols-1 md:grid-cols-2 gap-5 mt-6">
                                        <div class="bg-white p-5 rounded-xl border border-yellow-100 shadow-[0_2px_15px_rgba(0,0,0,0.02)] flex items-center gap-4">
                                            <div class="w-12 h-12 bg-yellow-50/80 rounded-full text-yellow-600 flex items-center justify-center font-bold text-xl border border-yellow-100">3</div>
                                            <div>
                                                <h4 class="font-bold text-gray-800">Tờ Logos / Giáo viên</h4>
                                                <p class="text-[13px] text-gray-500 mt-0.5">(1 tờ = 127 Logos &rarr; Tương đương <strong>381 Logos</strong>)</p>
                                            </div>
                                        </div>
                                        <div class="bg-white p-5 rounded-xl border border-yellow-100 shadow-[0_2px_15px_rgba(0,0,0,0.02)] flex items-center gap-4">
                                            <div class="w-12 h-12 bg-blue-50/80 rounded-full text-blue-600 flex items-center justify-center border border-blue-100">
                                                <span class="material-symbols-outlined">inventory_2</span>
                                            </div>
                                            <div>
                                                <h4 class="font-bold text-gray-800">Cấp phát 1 lần duyệt</h4>
                                                <p class="text-[13px] text-gray-500 mt-0.5">Phòng Đào tạo gửi một lần vào <strong>đầu khóa học</strong>.</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="mt-6 bg-orange-50/50 p-4 rounded-xl border border-orange-200/50 text-[14px] text-gray-600 shadow-inner flex gap-3">
                                        <span class="material-symbols-outlined text-orange-500">info</span>
                                        <p>
                                            <strong class="text-orange-700 block mb-1">CẦN LƯU Ý:</strong> 
                                            Trong trường hợp Thầy/Cô được phân công dạy thêm lớp mới nhưng chưa được bổ sung Logos tương ứng, vui lòng báo lại <strong>Phòng Đào tạo</strong> để được hỗ trợ kịp thời.
                                        </p>
                                    </div>
                                </div>
                            </div>

                            <!-- Section 2: Về việc học thử / học chờ của học viên -->
                            <h3 class="text-[#00174f] text-2xl font-bold font-display mb-6 border-b border-gray-100 pb-3 flex items-center gap-2">
                                <span class="material-symbols-outlined text-primary">person_search</span>
                                2. Về việc học thử / Học chờ khóa mới
                            </h3>

                            <!-- Tabs / Sections grid -->
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                                
                                <!-- 2.1 Đối tượng & 2.2 Nhận diện -->
                                <div class="bg-white rounded-2xl border border-gray-200 p-6 md:p-8 shadow-[0_4px_15px_rgba(0,0,0,0.02)] flex flex-col h-full hover:border-blue-300 transition-colors">
                                    <h4 class="font-bold text-[#00174f] text-lg mb-5 flex items-center gap-3"><span class="w-7 h-7 rounded-full bg-blue-50 text-blue-700 flex items-center justify-center text-[13px] font-bold border border-blue-100">2.1</span> Đối tượng áp dụng</h4>
                                    <ul class="space-y-3 text-[15px] text-gray-600 mb-6">
                                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-green-500 text-[20px]">check_circle</span> <span>Học viên mới.</span></li>
                                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-green-500 text-[20px]">check_circle</span> <span>Học viên cũ (nhảy lớp, nghỉ học dài ngày quay lại).</span></li>
                                        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-green-500 text-[20px]">check_circle</span> <span>Phụ huynh có nhu cầu đánh giá mức độ phù hợp / level dự kiến.</span></li>
                                    </ul>
                                    <div class="bg-blue-50/50 p-4 rounded-xl border border-blue-100/50 text-[13px] text-blue-900 mb-8 border-l-4 border-l-blue-500 font-medium">
                                        Không phải tất cả học viên mới đều học thử. Trường hợp học viên đã có sách riêng và không ghi chú "học thử", học viên được xem là học viên chính thức.
                                    </div>
                                    
                                    <h4 class="font-bold text-[#00174f] text-lg mb-5 flex items-center gap-3 mt-auto border-t border-gray-100 pt-6"><span class="w-7 h-7 rounded-full bg-blue-50 text-blue-700 flex items-center justify-center text-[13px] font-bold border border-blue-100">2.2</span> Nhận diện</h4>
                                    <div class="flex flex-col gap-3 text-[14px]">
                                        <div class="flex items-center gap-3 bg-gray-50 border border-gray-100 p-3.5 rounded-xl">
                                            <span class="material-symbols-outlined text-gray-500 text-[22px]">description</span> <strong>Phiếu học thử:</strong> Gửi trực tiếp vào lớp.
                                        </div>
                                        <div class="flex items-center gap-3 bg-gray-50 border border-gray-100 p-3.5 rounded-xl">
                                            <span class="material-symbols-outlined text-gray-500 text-[22px]">phonelink</span> <strong>Hệ thống:</strong> Mục "Learner Profile" trên App/Web.
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- 2.3 Thời lượng & 2.5 Học chờ -->
                                <div class="flex flex-col gap-6 h-full">
                                    <!-- 2.3 -->
                                    <div class="bg-white rounded-2xl border border-gray-200 p-6 md:p-8 shadow-[0_4px_15px_rgba(0,0,0,0.02)] hover:border-blue-300 transition-colors">
                                        <h4 class="font-bold text-[#00174f] text-lg mb-5 flex items-center gap-3"><span class="w-7 h-7 rounded-full bg-blue-50 text-blue-700 flex items-center justify-center text-[13px] font-bold border border-blue-100">2.3</span> Thời lượng học thử</h4>
                                        <div class="flex justify-between items-center bg-indigo-50/40 border border-indigo-100/60 rounded-xl p-4 md:p-5 mb-3">
                                            <div class="flex items-center gap-2 text-indigo-900 font-medium">
                                                <span class="material-symbols-outlined text-indigo-400">calendar_month</span> Cuối tuần
                                            </div>
                                            <span class="bg-indigo-100 text-indigo-800 font-bold px-3 py-1 rounded-[8px] text-[14px] shadow-sm">02 buổi</span>
                                        </div>
                                        <div class="flex justify-between items-center bg-purple-50/40 border border-purple-100/60 rounded-xl p-4 md:p-5 mb-4">
                                            <div class="flex items-center gap-2 text-purple-900 font-medium">
                                                <span class="material-symbols-outlined text-purple-400">routine</span> Buổi tối
                                            </div>
                                            <span class="bg-purple-100 text-purple-800 font-bold px-3 py-1 rounded-[8px] text-[14px] shadow-sm">02-03 buổi</span>
                                        </div>
                                        <p class="text-[13px] text-gray-500 bg-gray-50 p-3 rounded-lg flex gap-2"><span class="material-symbols-outlined text-[16px]">info</span> <span class="leading-relaxed">Giáo trình hỗ trợ: Photo / sách gốc mượn tạm (không làm trực tiếp vào sách). Trả về Quầy tư vấn khi kết thúc. Trừ trường hợp đặc biệt sẽ ghi ở phiếu.</span></p>
                                    </div>
                                    
                                    <!-- 2.5 Học chờ -->
                                    <div class="bg-white rounded-2xl border border-gray-200 p-6 shadow-[0_4px_15px_rgba(0,0,0,0.02)] hover:border-blue-300 transition-colors flex-1 flex flex-col justify-center">
                                        <h4 class="font-bold text-[#00174f] text-lg mb-3 flex items-center gap-3"><span class="w-7 h-7 rounded-full bg-blue-50 text-blue-700 flex items-center justify-center text-[13px] font-bold border border-blue-100">2.5</span> Trường hợp học chờ lên khóa</h4>
                                        <p class="text-[14px] text-gray-600 mb-4 bg-gray-50 p-3 rounded-lg border border-gray-100">Một số học viên được xếp <strong>học tạm (free)</strong> để chờ khóa mới. VD: Lớp Family 1B còn 2 tuần, chuyển sửa soạn vào chờ sang khóa 1C.</p>
                                        <div class="bg-red-50/60 p-4 border border-red-200 rounded-xl">
                                            <ul class="text-[13px] text-red-800 font-medium space-y-2">
                                                <li class="flex items-center"><span class="w-1.5 h-1.5 rounded-full bg-red-400 mr-2 shrink-0"></span> Vẫn tham gia thi cuối khóa.</li>
                                                <li class="flex items-center"><span class="w-1.5 h-1.5 rounded-full bg-red-400 mr-2 shrink-0"></span> Không xét học bổng Top 3 (do chưa chính thức).</li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- 2.4 Info Workflow -->
                            <h4 class="font-bold text-[#00174f] text-xl mb-6 md:mt-10 flex items-center gap-3"><span class="w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center text-sm font-bold font-display shadow-sm shadow-blue-200">2.4</span> Nhận xét & Chốt kết quả học thử</h4>
                            <div class="bg-gradient-to-br from-white to-[#f5f9ff] rounded-3xl border border-blue-100/80 shadow-[0_10px_40px_-10px_rgba(0,0,0,0.05)] p-6 md:p-8 relative overflow-hidden mb-4">
                                <div class="absolute right-0 bottom-0 opacity-[0.03] w-64 h-64 translate-x-1/4 translate-y-1/4">
                                    <span class="material-symbols-outlined text-[250px]">rate_review</span>
                                </div>

                                <!-- Timeline/Steps -->
                                <div class="relative z-10 flex flex-col lg:flex-row gap-6 items-stretch">
                                    <!-- Step 1 Output -->
                                    <div class="flex-1 bg-white p-6 rounded-2xl border border-gray-200 shadow-sm flex flex-col">
                                        <div class="text-primary bg-blue-50 w-12 h-12 rounded-xl flex items-center justify-center mb-5 shrink-0 border border-blue-100">
                                            <span class="material-symbols-outlined text-2xl">edit_note</span>
                                        </div>
                                        <h5 class="font-bold text-gray-800 mb-2">Cách thức thực hiện</h5>
                                        <p class="text-[14.5px] text-gray-600 mb-6 leading-relaxed">Vào buổi học cuối cùng, nhập đánh giá tại mục <strong class="text-blue-600 font-display">"COMMENT ON STUDENT'S PERFORMANCE"</strong> trên hệ thống/ứng dụng.</p>
                                        <div class="mt-auto bg-orange-50/70 p-4 rounded-xl border border-orange-200 text-[13px] text-orange-800">
                                            <ul class="space-y-1.5 flex flex-col font-medium">
                                                <li>- Tự động lưu sau khi nhập.</li>
                                                <li>- <strong>Khóa chỉnh sửa sau 48h</strong>.</li>
                                                <li>- Nhập đúng hạn để phục vụ phản hồi Phụ huynh.</li>
                                            </ul>
                                        </div>
                                    </div>
                                    
                                    <!-- Step 2 Fields -->
                                    <div class="flex-1 bg-white p-6 rounded-2xl border border-blue-200 shadow-[0_4px_20px_-5px_rgba(13,89,242,0.1)] flex flex-col relative">
                                        <div class="absolute top-0 right-0 bg-blue-500 text-white text-[10px] font-bold px-3 py-1.5 rounded-bl-xl origin-top-right uppercase tracking-wider">Yêu cầu nội dung</div>
                                        <div class="text-blue-500 bg-[#f4f7fc] w-12 h-12 rounded-xl flex items-center justify-center mb-5 shrink-0 border border-blue-100">
                                            <span class="material-symbols-outlined text-2xl">format_list_bulleted</span>
                                        </div>
                                        <h5 class="font-bold text-gray-800 mb-4">Các yếu tố nhận xét</h5>
                                        <ul class="space-y-4">
                                            <li class="flex items-start gap-3 bg-gray-50 p-3 rounded-xl border border-gray-100">
                                                <span class="material-symbols-outlined text-[#10b981] text-[20px] bg-green-50 p-1.5 rounded-lg shrink-0 border border-green-100/50">psychology</span>
                                                <div>
                                                    <span class="text-[14px] font-bold text-gray-800 block mb-0.5">Khả năng tiếp thu:</span>
                                                    <p class="text-[13px] text-gray-600">Nắm bài, phản xạ, phát âm, tốc độ làm bài.</p>
                                                </div>
                                            </li>
                                            <li class="flex items-start gap-3 bg-gray-50 p-3 rounded-xl border border-gray-100">
                                                <span class="material-symbols-outlined text-[#3b82f6] text-[20px] bg-blue-50 p-1.5 rounded-lg shrink-0 border border-blue-100/50">group</span>
                                                <div>
                                                    <span class="text-[14px] font-bold text-gray-800 block mb-0.5">Mức độ hòa nhập:</span>
                                                    <p class="text-[13px] text-gray-600">Giao tiếp với bạn bè, mức độ tham gia hoạt động, và đặc điểm nổi bật khác.</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                    
                                    <!-- Step 3 Final -->
                                    <div class="flex-1 bg-white p-6 rounded-2xl border border-gray-200 shadow-sm flex flex-col">
                                        <div class="text-primary bg-blue-50 w-12 h-12 rounded-xl flex items-center justify-center mb-5 shrink-0 border border-blue-100">
                                            <span class="material-symbols-outlined text-2xl">grading</span>
                                        </div>
                                        <h5 class="font-bold text-gray-800 mb-4">Kết luận cuối cùng</h5>
                                        <div class="flex flex-col gap-3">
                                            <div class="bg-green-50/50 border border-green-200 rounded-xl p-3 flex items-center gap-3">
                                                <div class="w-8 h-8 rounded-full bg-white flex items-center justify-center shadow-[0_2px_5px_rgba(0,0,0,0.05)] border border-green-100 shrink-0">
                                                    <span class="w-2.5 h-2.5 rounded-full bg-green-500"></span>
                                                </div>
                                                <span class="text-[13.5px] font-bold text-gray-700">Phù hợp level hiện tại</span>
                                            </div>
                                            <div class="bg-orange-50/50 border border-orange-200 rounded-xl p-3 flex items-center gap-3">
                                                <div class="w-8 h-8 rounded-full bg-white flex items-center justify-center shadow-[0_2px_5px_rgba(0,0,0,0.05)] border border-orange-100 shrink-0">
                                                    <span class="w-2.5 h-2.5 rounded-full bg-orange-500"></span>
                                                </div>
                                                <span class="text-[13.5px] font-bold text-gray-700">Chưa phù hợp (level cao/thấp)</span>
                                            </div>
                                            <div class="bg-purple-50/50 border border-purple-200 rounded-xl p-3 flex items-center gap-3">
                                                <div class="w-8 h-8 rounded-full bg-white flex items-center justify-center shadow-[0_2px_5px_rgba(0,0,0,0.05)] border border-purple-100 shrink-0">
                                                    <span class="w-2.5 h-2.5 rounded-full bg-purple-500"></span>
                                                </div>
                                                <span class="text-[13.5px] font-bold text-gray-700">Vượt trội (chuyển đổi lớp)</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- ... End content ... -->

                        </div>
                    </div>

                    <!-- Right Column: Sidebar -->"""

    final_content = content[:start_idx] + new_section + content[end_idx:]
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"Successfully created {target_file}")
    
if __name__ == '__main__':
    create_quy_trinh()
