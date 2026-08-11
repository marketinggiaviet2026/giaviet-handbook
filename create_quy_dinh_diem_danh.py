import os
import re

def create_quy_dinh():
    source_file = '/Users/vobac/Downloads/gia-viet-handbook/giao-trinh-tai-lieu.html'
    target_file = '/Users/vobac/Downloads/gia-viet-handbook/quy-dinh-diem-danh.html'
    
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Title tag
    content = content.replace(
        '<title>Giáo trình & Tài liệu giảng dạy - Handbook</title>',
        '<title>Quy định Điểm danh - Handbook</title>'
    )
    
    # 2. Update Breadcrumbs & Main Heading Box
    # We will slice from <!-- Breadcrumb & Title Area --> to <div class="grid grid-cols-1 gap-8">
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
                    <h1 class="text-3xl md:text-4xl font-bold text-[#00174f] mb-6 font-display tracking-wide">Quy định Điểm danh</h1>
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
                        <span class="text-[#0d121c] whitespace-nowrap">Quy định Điểm danh</span>
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
                                <h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display mt-2">QUY ĐỊNH ĐIỂM DANH</h2>
                            </div>

                            <!-- Section 1: Tài khoản ứng dụng -->
                            <div class="bg-blue-50/50 border border-blue-100 rounded-xl p-6 mb-10 flex flex-col md:flex-row items-center md:items-start gap-5 hover:shadow-md transition-shadow">
                                <div class="w-16 h-16 rounded-full bg-white text-primary flex items-center justify-center shrink-0 shadow-sm">
                                    <span class="material-symbols-outlined text-3xl">manage_accounts</span>
                                </div>
                                <div class="text-gray-700 font-body flex-1">
                                    <h3 class="text-lg font-bold text-[#00174f] mb-2 font-display">Tài khoản Ứng dụng dành cho Giáo viên</h3>
                                    <p class="mb-3 leading-relaxed">Khi tham gia giảng dạy, Phòng Nhân sự sẽ cấp tài khoản ứng dụng phục vụ công tác giảng dạy & quản lý lớp học.</p>
                                    <div class="text-sm bg-white p-4 rounded-lg border border-blue-100/80 shadow-[0_2px_10px_rgba(0,0,0,0.02)]">
                                        <div class="flex items-center gap-2 mb-1">
                                            <span class="material-symbols-outlined text-orange-500 text-sm">info</span>
                                            <strong class="text-orange-600">Lưu ý đối với TA chuyển lên Giáo viên:</strong>
                                        </div>
                                        <p class="text-gray-500 ml-6">Tài khoản Giáo viên sẽ được cấp mới hoặc cập nhật lại (do cơ chế quản lý & tính lương của Giáo viên khác với TA).</p>
                                    </div>
                                </div>
                            </div>

                            <!-- Section 2: Điều kiện hoàn tất điểm danh -->
                            <h3 class="text-[#00174f] text-2xl font-bold font-display mb-6 border-b border-gray-100 pb-3 flex items-center gap-2">
                                <span class="material-symbols-outlined text-primary">checklist</span>
                                2 Bước Hoàn Tất Điểm Danh
                            </h3>
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12 relative">
                                <!-- Connecting line on desktop -->
                                <div class="hidden md:block absolute top-[50%] left-[50%] w-12 h-0.5 bg-gray-200 -translate-y-1/2 -translate-x-1/2 z-0"></div>
                                
                                <!-- Step 1 -->
                                <div class="bg-white rounded-xl border border-gray-200 p-6 shadow-sm relative z-10 hover:border-primary transition-colors flex flex-col h-full">
                                    <div class="flex items-center gap-3 mb-4">
                                        <div class="w-8 h-8 rounded-full bg-primary text-white font-bold flex items-center justify-center font-display">1</div>
                                        <h4 class="font-bold text-[#00174f] font-body text-lg">Nhập nội dung bài giảng</h4>
                                    </div>
                                    <p class="text-gray-600 text-[15px] font-body mb-auto">Nhập chi tiết nội dung bài giảng của buổi học hiện tại.</p>
                                    <div class="mt-6">
                                        <div class="bg-gray-50 border border-gray-100 p-2.5 rounded-lg flex items-center justify-center">
                                            <span class="text-xs font-bold text-gray-500 uppercase tracking-widest text-center">Sau đó nhấn chọn</span>
                                        </div>
                                        <div class="bg-[#00174f] text-white p-3 rounded-lg flex items-center justify-center mt-2 shadow-md hover:bg-primary transition-colors cursor-pointer">
                                            <span class="text-sm font-bold tracking-wide">SAVE YOUR TEACHING CONTENT</span>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- Step 2 -->
                                <div class="bg-white rounded-xl border border-gray-200 p-6 shadow-sm relative z-10 hover:border-primary transition-colors flex flex-col h-full">
                                    <div class="flex items-center gap-3 mb-4">
                                        <div class="w-8 h-8 rounded-full bg-primary text-white font-bold flex items-center justify-center font-display">2</div>
                                        <h4 class="font-bold text-[#00174f] font-body text-lg">Cập nhật trạng thái</h4>
                                    </div>
                                    <p class="text-gray-600 text-[15px] font-body mb-auto">Cập nhật trạng thái điểm danh cho từng học viên.</p>
                                    <div class="mt-6">
                                        <div class="flex justify-center gap-4 mt-2">
                                            <div class="flex-1 bg-green-50 border border-green-200 text-green-700 py-2.5 px-3 rounded-lg text-center font-bold text-sm cursor-pointer shadow-sm hover:bg-green-100 transition-colors">Present</div>
                                            <div class="flex-1 bg-red-50 border border-red-200 text-red-700 py-2.5 px-3 rounded-lg text-center font-bold text-sm cursor-pointer shadow-sm hover:bg-red-100 transition-colors">Absent</div>
                                        </div>
                                        <div class="mt-5 text-center bg-gray-50 py-3 rounded-lg border border-gray-100">
                                            <span class="inline-flex items-center gap-1.5 text-[13px] text-green-600 font-bold bg-green-100/50 px-3 py-1.5 rounded-full border border-green-200">
                                                <span class="material-symbols-outlined text-[16px]">check_circle</span> Attendance checked
                                            </span>
                                            <p class="text-[12px] text-gray-500 mt-2 italic font-medium">Lớp học hiển thị nút màu xanh = Thành công</p>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Section 3: Quy định thời gian điểm danh (30 phút) -->
                            <h3 class="text-[#00174f] text-2xl font-bold font-display mb-6 border-b border-gray-100 pb-3 flex items-center gap-2">
                                <span class="material-symbols-outlined text-primary">timer</span>
                                Quy định Thời gian (Ranh giới 30 Phút)
                            </h3>
                            <div class="bg-white rounded-xl border border-orange-200 overflow-hidden shadow-sm mb-10 font-body hover:shadow-md transition-shadow">
                                <div class="bg-gradient-to-r from-orange-50 to-orange-100/50 p-5 md:p-6 border-b border-orange-200 flex items-center gap-3">
                                    <span class="material-symbols-outlined text-orange-500 text-[28px]">hourglass_top</span>
                                    <h4 class="font-bold text-orange-800 text-xl font-display">Trong 29 phút đầu tiên</h4>
                                </div>
                                <div class="p-6 md:p-8">
                                    <div class="grid grid-cols-1 gap-6">
                                        <div class="flex items-start gap-4 bg-white p-5 rounded-xl border border-gray-100 shadow-[0_2px_10px_rgba(0,0,0,0.02)]">
                                            <div class="w-10 h-10 rounded-full bg-blue-50 flex items-center justify-center shrink-0 text-blue-600">
                                                <span class="material-symbols-outlined">notifications_active</span>
                                            </div>
                                            <div>
                                                <h5 class="font-bold text-gray-800 text-[16px] mb-1">Khi đánh "Vắng" học viên</h5>
                                                <p class="text-[15px] text-gray-600 leading-relaxed">Hệ thống sẽ <strong>gửi thông báo trực tiếp</strong> đến ứng dụng của học viên & phụ huynh ngay lập tức.</p>
                                            </div>
                                        </div>
                                        <div class="flex items-start gap-4 bg-red-50/30 p-5 rounded-xl border border-red-100 shadow-[0_2px_10px_rgba(0,0,0,0.02)]">
                                            <div class="w-10 h-10 rounded-full bg-red-100 flex items-center justify-center shrink-0 text-red-600">
                                                <span class="material-symbols-outlined">warning</span>
                                            </div>
                                            <div>
                                                <h5 class="font-bold text-red-800 text-[16px] mb-1">Nếu QUÊN điểm danh?</h5>
                                                <p class="text-[15px] text-gray-600 leading-relaxed">Nếu không điểm danh trong 30 phút đầu, hệ thống sẽ tự động mặc định toàn bộ học viên của lớp là <strong>"Vắng"</strong> và gửi thông báo vắng đồng loạt!</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="bg-gray-50/80 p-6 md:p-8 border-t border-gray-200 flex flex-col md:flex-row items-center md:items-start gap-5">
                                    <div class="w-12 h-12 rounded-full bg-gray-200 flex items-center justify-center shrink-0 text-gray-500">
                                        <span class="material-symbols-outlined text-[24px]">timer_off</span>
                                    </div>
                                    <div class="text-center md:text-left">
                                        <h4 class="font-bold text-gray-700 text-lg mb-1 font-display">Từ phút 30 trở đi</h4>
                                        <p class="text-[15px] text-gray-600 leading-relaxed">Mọi thay đổi trạng thái điểm danh sẽ <strong>không phát sinh thông báo bổ sung</strong>. Đây là căn cứ thời gian quan trọng để phân định khi có phụ huynh phản hồi kết quả sai sót.</p>
                                    </div>
                                </div>
                            </div>

                            <!-- Section 4: Hỗ trợ -->
                            <div class="bg-gradient-to-r from-[#f8fbff] to-white rounded-xl p-6 md:p-8 border border-blue-100 flex flex-col md:flex-row items-center justify-between gap-6 font-body shadow-sm">
                                <div class="flex items-center gap-5">
                                    <div class="w-14 h-14 bg-blue-100 rounded-full flex items-center justify-center text-primary shadow-inner shrink-0">
                                        <span class="material-symbols-outlined text-3xl">support_agent</span>
                                    </div>
                                    <div>
                                        <h4 class="font-bold text-[#00174f] text-lg mb-1">Cần hỗ trợ kỹ thuật?</h4>
                                        <p class="text-[15px] text-gray-600">Trường hợp điểm danh bị trễ hoặc gặp sự cố lỗi, kính mong Thầy/Cô chủ động liên hệ <strong>Phòng Đào tạo</strong> để được xử lý kịp thời.</p>
                                    </div>
                                </div>
                                <button class="w-full md:w-auto bg-primary hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-xl text-sm transition-colors shadow-md whitespace-nowrap">
                                    Liên hệ Hỗ trợ
                                </button>
                            </div>

                        </div>
                    </div>

                    <!-- Right Column: Sidebar -->"""

    final_content = content[:start_idx] + new_section + content[end_idx:]
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"Successfully created {target_file}")
    
if __name__ == '__main__':
    create_quy_dinh()
