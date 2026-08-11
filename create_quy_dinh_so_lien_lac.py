import os

def create_so_lien_lac():
    source_file = '/Users/vobac/Downloads/gia-viet-handbook/giao-trinh-tai-lieu.html'
    target_file = '/Users/vobac/Downloads/gia-viet-handbook/quy-dinh-so-lien-lac.html'
    
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Title tag
    content = content.replace(
        '<title>Giáo trình & Tài liệu giảng dạy - Handbook</title>',
        '<title>Quy định Sổ liên lạc - Handbook</title>'
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
                    <h1 class="text-3xl md:text-4xl font-bold text-[#00174f] mb-6 font-display tracking-wide">Quy định Sổ liên lạc</h1>
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
                        <span class="text-[#0d121c] whitespace-nowrap">Quy định Sổ liên lạc</span>
                    </div>
                </div>
            </div>

            <!-- 2 Column Layout -->
            <div class="w-full max-w-[1440px] px-4 md:px-10 py-16 mx-auto">
                <div class="flex flex-col md:flex-row gap-8 lg:gap-16 items-start">

                    <!-- Left Column: Content -->
                    <div class="w-full md:w-[70%] lg:w-[75%] font-body text-gray-800 leading-relaxed space-y-8">
                        <div class="bg-white rounded-2xl shadow-sm border border-gray-100/50 p-6 md:p-10 lg:p-12">
                            
                            <div class="flex flex-col gap-3 mb-12 border-b border-gray-100 pb-8">
                                <span class="text-primary font-bold tracking-wider uppercase text-sm font-body bg-blue-50 w-max px-3 py-1 rounded-full border border-blue-100">Dành cho Giáo viên</span>
                                <h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display mt-2 mb-2">HƯỚNG DẪN VIẾT SỔ LIÊN LẠC</h2>
                                <p class="text-gray-500 font-medium">Lớp Tiếng Anh Thiếu nhi &ndash; Thiếu niên</p>
                            </div>

                            <!-- I. Mục đích -->
                            <div class="bg-gradient-to-r from-blue-50/80 to-indigo-50/50 rounded-2xl p-6 md:p-8 mb-12 border border-blue-100/60 shadow-[0_4px_15px_-5px_rgba(0,0,0,0.05)] relative overflow-hidden">
                                <div class="absolute right-0 top-0 opacity-[0.03] translate-x-1/4 -translate-y-1/4">
                                    <span class="material-symbols-outlined text-[150px]">target</span>
                                </div>
                                <h3 class="text-xl font-bold text-[#00174f] mb-5 font-display flex items-center gap-3 relative z-10">
                                    <span class="w-10 h-10 rounded-full bg-blue-600 text-white flex items-center justify-center shadow-md"><span class="material-symbols-outlined">flag</span></span>
                                    I. Mục đích của sổ liên lạc
                                </h3>
                                <p class="mb-4 font-bold text-blue-900 relative z-10">Sổ liên lạc là kênh trao đổi chính thức giữa Giáo viên và Phụ huynh nhằm:</p>
                                <ul class="space-y-3 text-[15px] text-gray-700 relative z-10 ml-2">
                                    <li class="flex items-start gap-3"><span class="material-symbols-outlined text-blue-500">task_alt</span> <span>Cập nhật tình hình học tập, thái độ và sự tiến bộ của học viên theo từng giai đoạn học tập.</span></li>
                                    <li class="flex items-start gap-3"><span class="material-symbols-outlined text-blue-500">task_alt</span> <span>Giúp Phụ huynh nắm rõ điểm mạnh, điểm cần cải thiện của học viên.</span></li>
                                    <li class="flex items-start gap-3"><span class="material-symbols-outlined text-blue-500">task_alt</span> <span>Tăng cường sự phối hợp hiệu quả giữa giáo viên và gia đình trong việc hỗ trợ học tập cho học viên.</span></li>
                                </ul>
                                <div class="mt-6 bg-white/80 backdrop-blur-sm p-4 rounded-xl border border-blue-100 text-[14px] text-gray-600 shadow-sm relative z-10 font-bold border-l-4 border-l-orange-500">
                                    <span class="text-orange-600">Yêu cầu thiết yếu:</span> Giáo viên cần thực hiện việc viết sổ liên lạc đúng thời hạn, đúng nội dung, đúng format và mang tính cá nhân hóa cho từng học viên.
                                </div>
                            </div>

                            <!-- II. Quy trình nhập SLL -->
                            <h3 class="text-[#00174f] text-2xl font-bold font-display mb-8 flex items-center gap-3">
                                <span class="material-symbols-outlined text-primary text-[28px]">schema</span>
                                II. Quy trình nhập hệ thống
                            </h3>
                            
                            <div class="relative mb-12 border-l-2 border-blue-100 pl-8 ml-4 space-y-10">
                                <!-- Step 1 -->
                                <div class="relative">
                                    <div class="absolute -left-[45px] top-0 w-8 h-8 rounded-full bg-blue-100 border-4 border-white flex items-center justify-center text-primary font-bold shadow-sm">1</div>
                                    <h4 class="font-bold text-gray-800 text-lg mb-2">Đăng nhập hệ thống</h4>
                                    <div class="bg-gray-50 rounded-xl p-5 border border-gray-200">
                                        <div class="flex items-center gap-2 mb-3">
                                            <span class="material-symbols-outlined text-gray-400">language</span>
                                            <a href="http://htql.giaviet.edu.vn/" target="_blank" class="text-primary hover:underline font-medium">http://htql.giaviet.edu.vn/</a>
                                        </div>
                                        <p class="text-[14px] text-gray-600 mb-2">&bull; Đăng nhập bằng tài khoản được cấp (theo file HDSD SLL).</p>
                                        <p class="text-[14px] text-orange-600 font-medium bg-orange-50 inline-block px-3 py-1 rounded-md border border-orange-100"><span class="material-symbols-outlined text-[14px] mr-1 align-middle">lock_reset</span> Cần đổi mật khẩu sau lần đăng nhập đầu tiên!</p>
                                    </div>
                                </div>
                                
                                <!-- Step 2 -->
                                <div class="relative">
                                    <div class="absolute -left-[45px] top-0 w-8 h-8 rounded-full bg-blue-100 border-4 border-white flex items-center justify-center text-primary font-bold shadow-sm">2</div>
                                    <h4 class="font-bold text-gray-800 text-lg mb-2">Chọn lớp và Đợt viết sổ</h4>
                                    <div class="bg-gray-50 rounded-xl p-5 border border-gray-200">
                                        <ul class="text-[14px] text-gray-600 space-y-2">
                                            <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-gray-400 shrink-0"></span> Chọn lớp cần viết (nhấp vào tên lớp để hiện dấu tick xanh).</li>
                                            <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-gray-400 shrink-0"></span> Click nút <strong class="text-gray-800">"Xem sổ liên lạc"</strong>.</li>
                                            <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-gray-400 shrink-0"></span> Trong mỗi lớp sẽ có các đợt (Đợt 1, 2, 3). Chọn đúng đợt & nhấp <strong class="text-gray-800">"Nhận xét"</strong>.</li>
                                        </ul>
                                    </div>
                                </div>
                                
                                <!-- Step 3 -->
                                <div class="relative">
                                    <div class="absolute -left-[45px] top-0 w-8 h-8 rounded-full bg-blue-100 border-4 border-white flex items-center justify-center text-primary font-bold shadow-sm">3</div>
                                    <h4 class="font-bold text-gray-800 text-lg mb-2">Nhập nhận xét</h4>
                                    <div class="bg-gray-50 rounded-xl p-5 border border-gray-200">
                                        <p class="text-[13px] text-red-600 font-bold mb-3 uppercase tracking-wider">Mỗi lần thao tác chỉ chọn 1 học viên!</p>
                                        <ul class="text-[14px] text-gray-600 space-y-2 mb-3 border-l-[3px] border-blue-300 pl-3">
                                            <li><span class="font-bold text-gray-700">Bước 1:</span> Nhấp chọn tên học viên &rarr; Chọn "Cập nhật".</li>
                                            <li><span class="font-bold text-gray-700">Bước 2:</span> Nhập nội dung vào ô "Ý kiến giáo viên".</li>
                                            <li><span class="font-bold text-gray-700">Bước 3:</span> Kiểm tra lỗi chính tả kỹ &rarr; Nhấn "Cập nhật" để lưu.</li>
                                        </ul>
                                    </div>
                                </div>
                                
                                <!-- Step 4 -->
                                <div class="relative">
                                    <div class="absolute -left-[45px] top-0 w-8 h-8 rounded-full bg-blue-100 border-4 border-white flex items-center justify-center text-primary font-bold shadow-sm">4</div>
                                    <h4 class="font-bold text-gray-800 text-lg mb-2">Chỉnh sửa nhận xét</h4>
                                    <div class="bg-gray-50 rounded-xl p-5 border border-gray-200">
                                        <p class="text-[14px] text-gray-600">Nếu cần sửa: Chọn lại đúng học viên &rarr; Sửa nội dung &rarr; Nhấn "Cập nhật" lưu lại bản mới.</p>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Warning Box -->
                            <div class="bg-red-50/50 border border-red-200 rounded-xl p-6 mb-12 flex items-start gap-4">
                                <span class="material-symbols-outlined text-red-600 text-3xl shrink-0 mt-1">warning</span>
                                <div>
                                    <h5 class="font-bold text-red-800 text-lg mb-2">Lưu ý khi thao tác hệ thống</h5>
                                    <ul class="text-[14px] text-red-700 space-y-2">
                                        <li>&bull; Do giao diện chưa tối ưu, Giáo viên cần chú ý chọn <strong>ĐÚNG TÊN HỌC VIÊN</strong> trước khi nhập.</li>
                                        <li>&bull; Nhớ kéo danh sách xuống để kiểm tra & nhập đầy đủ cho các bảng ghi ở cuối.</li>
                                        <li>&bull; Tuyệt đối tránh nhập nhầm nhận xét râu ông nọ cắm cằm bà kia.</li>
                                    </ul>
                                </div>
                            </div>

                            <!-- III. Thời gian Hạn chót -->
                            <h3 class="text-[#00174f] text-2xl font-bold font-display mb-6 flex items-center gap-3">
                                <span class="material-symbols-outlined text-primary text-[28px]">calendar_clock</span>
                                III. Số lần & Thời gian viết Sổ liên lạc
                            </h3>
                            
                            <div class="overflow-x-auto rounded-xl border border-gray-200 shadow-sm mb-6">
                                <table class="w-full text-left border-collapse text-[14px] md:text-[15px] font-body">
                                    <thead>
                                        <tr class="bg-[#f8fbff] text-[#00174f] border-b border-gray-200">
                                            <th class="py-4 px-6 font-bold w-[40%]">Phân loại Khóa học</th>
                                            <th class="py-4 px-6 font-bold text-center">Số lần viết</th>
                                            <th class="py-4 px-6 font-bold w-[40%]">Thời điểm thực hiện</th>
                                        </tr>
                                    </thead>
                                    <tbody class="text-gray-700 divide-y divide-gray-100">
                                        <tr class="hover:bg-blue-50/30 transition-colors">
                                            <td class="py-4 px-6 font-semibold">Khóa 9 tuần</td>
                                            <td class="py-4 px-6 text-center font-bold text-blue-600">3</td>
                                            <td class="py-4 px-6 text-gray-600">Sau tuần 3, 6 và 9</td>
                                        </tr>
                                        <tr class="hover:bg-blue-50/30 transition-colors">
                                            <td class="py-4 px-6 font-semibold">Khóa 10 tuần</td>
                                            <td class="py-4 px-6 text-center font-bold text-blue-600">3</td>
                                            <td class="py-4 px-6 text-gray-600">Sau tuần 4, 7 và 10</td>
                                        </tr>
                                        <tr class="hover:bg-blue-50/30 transition-colors">
                                            <td class="py-4 px-6 font-semibold">Khóa 11 tuần</td>
                                            <td class="py-4 px-6 text-center font-bold text-blue-600">3</td>
                                            <td class="py-4 px-6 text-gray-600">Sau tuần 4, 8 và 11</td>
                                        </tr>
                                        <tr class="hover:bg-blue-50/30 transition-colors">
                                            <td class="py-4 px-6 font-semibold">Khóa 12 tuần</td>
                                            <td class="py-4 px-6 text-center font-bold text-blue-600">3</td>
                                            <td class="py-4 px-6 text-gray-600">Sau tuần 4, 8 và 12</td>
                                        </tr>
                                        <tr class="bg-gray-50 border-t-2 border-gray-200">
                                            <td colspan="3" class="py-2 px-6 font-bold text-xs text-gray-400 uppercase tracking-widest text-center">Chương trình Luyện thi</td>
                                        </tr>
                                        <tr class="hover:bg-blue-50/30 transition-colors">
                                            <td class="py-4 px-6 font-semibold">Cambridge Starters (8 tuần)</td>
                                            <td class="py-4 px-6 text-center font-bold text-purple-600">2</td>
                                            <td class="py-4 px-6 text-gray-600">Sau tuần 4 và 8</td>
                                        </tr>
                                        <tr class="hover:bg-blue-50/30 transition-colors">
                                            <td class="py-4 px-6 font-semibold">Cambridge Movers (10 tuần)</td>
                                            <td class="py-4 px-6 text-center font-bold text-purple-600">2</td>
                                            <td class="py-4 px-6 text-gray-600">Sau tuần 5 và 10</td>
                                        </tr>
                                        <tr class="hover:bg-blue-50/30 transition-colors">
                                            <td class="py-4 px-6 font-semibold">Cambridge Flyers (15 tuần)</td>
                                            <td class="py-4 px-6 text-center font-bold text-purple-600">3</td>
                                            <td class="py-4 px-6 text-gray-600">Sau tuần 5, 10 và 15</td>
                                        </tr>
                                        <tr class="hover:bg-blue-50/30 transition-colors">
                                            <td class="py-4 px-6 font-semibold">KET for Schools (12 tuần)</td>
                                            <td class="py-4 px-6 text-center font-bold text-purple-600">3</td>
                                            <td class="py-4 px-6 text-gray-600">Sau tuần 4, 8 và 12</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            
                            <div class="bg-[#00174f] text-white rounded-xl p-6 flex flex-col md:flex-row justify-between items-center gap-4 mb-14 shadow-lg">
                                <div>
                                    <h4 class="font-bold text-lg mb-1 flex items-center gap-2"><span class="material-symbols-outlined text-orange-400">alarm_on</span> Thời hạn hoàn thành bắt buộc</h4>
                                    <p class="text-[14px] text-blue-100">Sau khi tuần học kết thúc, Giáo viên có tối đa <strong class="text-white text-base">03 NGÀY</strong> để hoàn thành.</p>
                                </div>
                                <div class="bg-white/10 px-4 py-2 rounded-lg text-sm text-center">
                                    Vui lòng chủ động sắp xếp thời gian!<br>Đảm bảo tiến độ chung của Trung tâm.
                                </div>
                            </div>

                            <!-- IV. Nội dung Form -->
                            <h3 class="text-[#00174f] text-2xl font-bold font-display mb-6 flex items-center gap-3">
                                <span class="material-symbols-outlined text-primary text-[28px]">format_align_justify</span>
                                IV. Hình thức & Nội dung Nhận xét
                            </h3>
                            
                            <div class="grid grid-cols-1 gap-6 mb-12">
                                
                                <!-- Card Đợt 1 -->
                                <div class="card group cursor-pointer border border-gray-200 hover:border-primary shadow-sm hover:shadow-md transition-all duration-300" onclick="toggleAccordion(this)">
                                    <div class="flex items-center justify-between gap-3 pb-0 w-full mb-0">
                                        <div class="flex items-center gap-4">
                                            <div class="w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors shrink-0 font-bold border border-blue-100">1</div>
                                            <h3 class="text-[#00174f] text-xl font-bold font-display m-0 group-hover:text-primary transition-colors">NHẬN XÉT ĐỢT 1</h3>
                                        </div>
                                        <div class="w-8 h-8 rounded-full border border-gray-100 flex items-center justify-center text-gray-400 group-hover:border-primary group-hover:text-primary transition-colors">
                                            <span class="material-symbols-outlined toggle-icon transition-transform duration-300 transform rotate-0">expand_more</span>
                                        </div>
                                    </div>
                                    <div class="card-content hidden w-full pt-6" onclick="event.stopPropagation()">
                                        <div class="bg-gray-50 rounded-xl p-6 border border-gray-100 relative text-[14px]">
                                            <div class="absolute -top-3 left-6 bg-white px-3 font-bold text-sm text-gray-600 border border-gray-200 rounded-full">Ví dụ: Tuần 1 – Tuần 4</div>
                                            <div class="space-y-6 mt-2">
                                                <div>
                                                    <h5 class="font-bold text-blue-800 mb-2 border-b border-blue-100 pb-1">NỘI DUNG BÀI HỌC</h5>
                                                    <ul class="text-gray-700 pl-4 list-disc space-y-1">
                                                        <li>Ghi theo đúng tiến độ chương trình đã học.</li>
                                                        <li>Bổ sung các chủ điểm từ vựng, mẫu câu, cấu trúc ngữ pháp và chuyên đề trọng tâm.</li>
                                                    </ul>
                                                </div>
                                                <div>
                                                    <h5 class="font-bold text-blue-800 mb-2 border-b border-blue-100 pb-1">NHẬN XÉT CỦA GIÁO VIÊN</h5>
                                                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                                        <div class="bg-white p-4 rounded-lg border border-gray-200">
                                                            <strong class="text-green-700 flex items-center gap-1 mb-2"><span class="material-symbols-outlined text-sm">mood</span> Tinh thần / Thái độ:</strong>
                                                            <ul class="text-gray-600 pl-4 list-disc space-y-1 text-[13px]">
                                                                <li>Chuyên cần (đầy đủ, đúng giờ).</li>
                                                                <li>Tính cách trên lớp, tập trung.</li>
                                                                <li>Tinh thần xung phong, phát biểu.</li>
                                                                <li>Hợp tác làm việc nhóm, hoàn thành BTVN.</li>
                                                            </ul>
                                                        </div>
                                                        <div class="bg-white p-4 rounded-lg border border-gray-200">
                                                            <strong class="text-purple-700 flex items-center gap-1 mb-2"><span class="material-symbols-outlined text-sm">school</span> Năng lực học tập:</strong>
                                                            <ul class="text-gray-600 pl-4 list-disc space-y-1 text-[13px]">
                                                                <li>Tiếp thu & hiểu bài, ghi nhớ ngữ pháp.</li>
                                                                <li>Kỹ năng vận dụng lý thuyết ra thực tiễn.</li>
                                                                <li><strong class="font-medium">Nói:</strong> phát âm, ngữ điệu, phản xạ, diễn đạt.</li>
                                                                <li><strong class="font-medium">Viết:</strong> chính tả, cấu trúc câu, liên kết ý.</li>
                                                            </ul>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div>
                                                    <h5 class="font-bold text-blue-800 mb-2 border-b border-blue-100 pb-1">ĐỀ XUẤT CỦA GIÁO VIÊN</h5>
                                                    <ul class="text-gray-700 pl-4 list-disc space-y-1">
                                                        <li>Đưa ra đề xuất giải pháp cụ thể để học viên nâng cao thành tích.</li>
                                                        <li>Gợi ý nội dung Phụ huynh có thể phối hợp hỗ trợ thêm tại nhà.</li>
                                                    </ul>
                                                </div>
                                                <div class="bg-gray-100 p-3 rounded-lg text-center font-medium italic text-gray-500">
                                                    “Cám ơn Quý Phụ huynh đã xem nhận xét!” <br> Thầy/Cô ………………
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- Card Đợt 2 -->
                                <div class="card group cursor-pointer border border-gray-200 hover:border-primary shadow-sm hover:shadow-md transition-all duration-300" onclick="toggleAccordion(this)">
                                    <div class="flex items-center justify-between gap-3 pb-0 w-full mb-0">
                                        <div class="flex items-center gap-4">
                                            <div class="w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors shrink-0 font-bold border border-blue-100">2</div>
                                            <h3 class="text-[#00174f] text-xl font-bold font-display m-0 group-hover:text-primary transition-colors">NHẬN XÉT ĐỢT 2</h3>
                                        </div>
                                        <div class="w-8 h-8 rounded-full border border-gray-100 flex items-center justify-center text-gray-400 group-hover:border-primary group-hover:text-primary transition-colors">
                                            <span class="material-symbols-outlined toggle-icon transition-transform duration-300 transform rotate-0">expand_more</span>
                                        </div>
                                    </div>
                                    <div class="card-content hidden w-full pt-6" onclick="event.stopPropagation()">
                                        <div class="bg-gray-50 rounded-xl p-6 border border-gray-100 text-[14px]">
                                            <div class="space-y-6">
                                                <div>
                                                    <h5 class="font-bold text-blue-800 mb-2 border-b border-blue-100 pb-1">NỘI DUNG BÀI HỌC</h5>
                                                    <p class="text-gray-700">Cập nhật nội dung đã học trong giai đoạn kế tiếp (không lặp lại Đợt 1).</p>
                                                </div>
                                                <div>
                                                    <h5 class="font-bold text-blue-800 mb-2 border-b border-blue-100 pb-1">NHẬN XÉT CỦA GIÁO VIÊN</h5>
                                                    <p class="text-gray-700 mb-2">Đánh giá theo các tiêu chí giống Đợt 1, tuy nhiên cần làm nổi bật trọng tâm:</p>
                                                    <div class="flex flex-col gap-2 pl-2">
                                                        <div class="bg-green-50 p-2 rounded border border-green-100 flex items-center gap-2"><span class="text-green-500 font-bold">+</span> Những điểm đang thể hiện tốtf.</div>
                                                        <div class="bg-orange-50 p-2 rounded border border-orange-100 flex items-center gap-2"><span class="text-orange-500 font-bold">-</span> Những khuyết điểm cần khắc phục và nỗ lực để học hiệu quả hơn.</div>
                                                    </div>
                                                </div>
                                                <div>
                                                    <h5 class="font-bold text-red-700 mb-2 border-b border-red-100 pb-1 flex items-center gap-2"><span class="material-symbols-outlined text-[18px]">event</span> NGÀY THI CUỐI KHÓA (Dự kiến)</h5>
                                                    <div class="bg-white p-3 border border-red-100 rounded-lg flex flex-col gap-1">
                                                        <div class="flex justify-between items-center"><span class="font-bold text-gray-700">Thi Nói:</span> <span class="text-gray-400">........................</span></div>
                                                        <div class="flex justify-between items-center"><span class="font-bold text-gray-700">Thi Nghe - Đọc - Viết:</span> <span class="text-gray-400">........................</span></div>
                                                    </div>
                                                </div>
                                                <div class="bg-gray-100 p-3 rounded-lg text-center font-medium italic text-gray-500">
                                                    “Cám ơn Quý Phụ huynh đã xem nhận xét!” <br> Thầy/Cô ………………
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- Card Đợt 3 -->
                                <div class="card group cursor-pointer border border-gray-200 hover:border-primary shadow-sm hover:shadow-md transition-all duration-300" onclick="toggleAccordion(this)">
                                    <div class="flex items-center justify-between gap-3 pb-0 w-full mb-0">
                                        <div class="flex items-center gap-4">
                                            <div class="w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors shrink-0 font-bold border border-blue-100">3</div>
                                            <h3 class="text-[#00174f] text-xl font-bold font-display m-0 group-hover:text-primary transition-colors">NHẬN XÉT ĐỢT 3 (TỔNG KẾT)</h3>
                                        </div>
                                        <div class="w-8 h-8 rounded-full border border-gray-100 flex items-center justify-center text-gray-400 group-hover:border-primary group-hover:text-primary transition-colors">
                                            <span class="material-symbols-outlined toggle-icon transition-transform duration-300 transform rotate-0">expand_more</span>
                                        </div>
                                    </div>
                                    <div class="card-content hidden w-full pt-6" onclick="event.stopPropagation()">
                                        <div class="bg-gray-50 rounded-xl p-6 border border-gray-100 text-[14px]">
                                            <div class="space-y-6">
                                                <div>
                                                    <h5 class="font-bold text-blue-800 mb-2 border-b border-blue-100 pb-1">NỘI DUNG BÀI HỌC</h5>
                                                    <p class="text-gray-700">Tổng hợp lại các nội dung cốt lõi của giai đoạn cuối khóa.</p>
                                                </div>
                                                <div>
                                                    <h5 class="font-bold text-blue-800 mb-2 border-b border-blue-100 pb-1">NHẬN XÉT TỔNG KẾT (TỪ BÀI THI)</h5>
                                                    <p class="text-gray-700 mb-2">Đưa ra nhận xét tổng quát về quá trình học tập xuyên suốt khóa, dựa trên kết quả thi thực tế để phân tích:</p>
                                                    <div class="flex flex-col gap-2 pl-2">
                                                        <div class="bg-green-50 p-2 rounded border border-green-100 flex items-center gap-2"><span class="text-green-500 font-bold">+</span> Thành quả đã làm tốt.</div>
                                                        <div class="bg-orange-50 p-2 rounded border border-orange-100 flex items-center gap-2"><span class="text-orange-500 font-bold">-</span> Giải pháp khắc phục các điểm hạn chế cho lộ trình tới.</div>
                                                    </div>
                                                </div>
                                                <div>
                                                    <h5 class="font-bold text-purple-700 mb-2 border-b border-purple-100 pb-1 flex items-center gap-2"><span class="material-symbols-outlined text-[18px]">forward</span> LỘ TRÌNH KHÓA HỌC THĂNG TIẾP</h5>
                                                    <div class="bg-white p-3 border border-purple-100 rounded-lg flex flex-col gap-1">
                                                        <div class="flex justify-between items-center"><span class="font-bold text-gray-700">Tên lớp:</span> <span class="text-gray-400">........................</span></div>
                                                        <div class="flex justify-between items-center"><span class="font-bold text-gray-700">Ngày khai giảng dự kiến:</span> <span class="text-gray-400">..../..../.......</span></div>
                                                    </div>
                                                </div>
                                                <div class="bg-gray-100 p-3 rounded-lg text-center font-medium italic text-gray-500">
                                                    “Cám ơn Quý Phụ huynh đã xem nhận xét!” <br> Thầy/Cô ………………
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                            </div>

                            <!-- V. Một số lưu ý quan trọng (End notes) -->
                            <div class="bg-gradient-to-b from-gray-50 to-white rounded-2xl p-6 border border-gray-200 shadow-sm mt-8">
                                <h4 class="font-bold text-red-600 text-lg mb-4 flex items-center gap-2 border-b border-red-100 pb-2"><span class="material-symbols-outlined text-[24px]">gpp_maybe</span> Những ĐIỀU CẤM KỴ & LƯU Ý trong Sổ Liên Lạc</h4>
                                <ul class="space-y-4 text-[14px]">
                                    <li class="flex items-start gap-3">
                                        <span class="material-symbols-outlined text-green-500 shrink-0">visibility</span>
                                        <div><strong class="text-gray-800">Theo dõi sát sao:</strong> Ghi chép và quan sát kỹ tình hình học viên suốt khóa để có căn cứ nhận xét xác thực và chi tiết nhất.</div>
                                    </li>
                                    <li class="flex items-start gap-3">
                                        <span class="material-symbols-outlined text-red-500 shrink-0">content_copy</span>
                                        <div><strong class="text-gray-800">Cấm sao chép (Copy-paste):</strong> Khước từ văn mẫu, không viết quá chung chung hoặc chép y đúc một nội dung cho hàng loạt học viên.</div>
                                    </li>
                                    <li class="flex items-start gap-3">
                                        <span class="material-symbols-outlined text-red-500 shrink-0">cancel</span>
                                        <div><strong class="text-gray-800">Tránh từ ngữ cảm tính, tiêu cực, đa nghĩa:</strong> Không dùng các từ địa phương dễ gây phật lòng như <span class="bg-red-50 text-red-600 px-1 rounded italic">"quậy", "lo ra", "thụ động", "rụt rè", "nhút nhát"...</span></div>
                                    </li>
                                    <li class="flex items-start gap-3">
                                        <span class="material-symbols-outlined text-green-500 shrink-0">balance</span>
                                        <div><strong class="text-gray-800">Cân bằng & Xây dựng:</strong> Hành văn chuyên nghiệp lịch sự. Công bằng giữa Khen (Điểm sáng) và Ý kiến xây dựng (Điểm cần cải thiện), chốt lại bằng định hướng hỗ trợ cụ thể.</div>
                                    </li>
                                </ul>
                            </div>

                        </div>
                    </div>

                    <!-- Right Column: Sidebar -->"""

    final_content = content[:start_idx] + new_section + content[end_idx:]
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"Successfully created {target_file}")
    
if __name__ == '__main__':
    create_so_lien_lac()
