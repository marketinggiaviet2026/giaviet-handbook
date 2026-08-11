import os

user_content = """<div class="grid grid-cols-1 gap-8">
    <!-- LTP Card -->
    <div class="card group cursor-pointer scroll-mt-24" onclick="toggleAccordion(this)" id="ltp">
        <div class="flex items-center justify-between gap-3 mb-4 border-b border-gray-100 pb-4 w-full">
            <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
                    <span class="material-symbols-outlined text-2xl">extension</span>
                </div>
                <h3 class="text-[#00174f] text-2xl font-bold font-display m-0">1. Learning Through Playing (LTP)</h3>
            </div>
            <span class="material-symbols-outlined text-gray-400 group-hover:text-primary transition-transform duration-300 transform rotate-0 toggle-icon">expand_more</span>
        </div>
        <div class="text-gray-600 text-[15px] space-y-3 leading-relaxed font-body card-content hidden">
            <ul class="space-y-3">
                <li class="flex items-start gap-2">
                    <span class="material-symbols-outlined text-primary text-lg mt-0.5 flex-shrink-0">check_circle</span>
                    <span><strong>Độ tuổi:</strong> 4 – 11 tuổi</span>
                </li>
                <li class="flex items-start gap-2">
                    <span class="material-symbols-outlined text-primary text-lg mt-0.5 flex-shrink-0">check_circle</span>
                    <span><strong>Mục tiêu:</strong> Học tiếng Anh tự nhiên thông qua phương pháp Play-based Learning (học qua vui chơi)</span>
                </li>
                <li class="flex items-start gap-2">
                    <span class="material-symbols-outlined text-primary text-lg mt-0.5 flex-shrink-0">check_circle</span>
                    <div>
                        <span><strong>Phương pháp học:</strong></span>
                        <ul class="list-disc pl-6 mt-1 space-y-1 text-gray-500">
                            <li>Học qua trò chơi, bài hát, kể chuyện & dự án sáng tạo</li>
                            <li>Môi trường học tập tích cực, phù hợp từng độ tuổi</li>
                        </ul>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <span class="material-symbols-outlined text-primary text-lg mt-0.5 flex-shrink-0">check_circle</span>
                    <div>
                        <span><strong>Phát triển ngôn ngữ:</strong></span>
                        <ul class="list-disc pl-6 mt-1 space-y-1 text-gray-500">
                            <li>Hình thành phản xạ tiếng Anh tự nhiên</li>
                            <li>Tăng sự tự tin trong giao tiếp</li>
                            <li>Ghi nhớ & vận dụng ngôn ngữ qua ngữ cảnh thực tế</li>
                        </ul>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <span class="material-symbols-outlined text-primary text-lg mt-0.5 flex-shrink-0">check_circle</span>
                    <div>
                        <span><strong>Giáo dục cảm xúc – xã hội (SEL):</strong></span>
                        <ul class="list-disc pl-6 mt-1 space-y-1 text-gray-500">
                            <li>Nhận diện & quản lý cảm xúc cá nhân</li>
                            <li>Phát triển kỹ năng giao tiếp, hợp tác</li>
                            <li>Nuôi dưỡng sự đồng cảm, chia sẻ & tôn trọng</li>
                        </ul>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <span class="material-symbols-outlined text-primary text-lg mt-0.5 flex-shrink-0">check_circle</span>
                    <div>
                        <span><strong>Kỹ năng hình thành:</strong></span>
                        <ul class="list-disc pl-6 mt-1 space-y-1 text-gray-500">
                            <li>Tự tin thể hiện bản thân</li>
                            <li>Biết lắng nghe & phản hồi phù hợp</li>
                        </ul>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <span class="material-symbols-outlined text-primary text-lg mt-0.5 flex-shrink-0">check_circle</span>
                    <div>
                        <span><strong>Môi trường học tập:</strong></span>
                        <ul class="list-disc pl-6 mt-1 space-y-1 text-gray-500">
                            <li>An toàn, thân thiện, khuyến khích sự tham gia</li>
                            <li>Tôn trọng sự khác biệt của mỗi học viên</li>
                        </ul>
                    </div>
                </li>
                <li class="flex items-start gap-2 mt-4 text-[#0d59f2] font-semibold bg-blue-50/50 p-3 rounded-lg border border-blue-100">
                    <span class="material-symbols-outlined text-primary text-lg mt-0.5 flex-shrink-0">tips_and_updates</span>
                    Nền tảng: Phát triển toàn diện về ngôn ngữ, cảm xúc và kỹ năng xã hội
                </li>
            </ul>
        </div>
    </div>

    <!-- Elite Kids Card -->
    <div class="card group cursor-pointer scroll-mt-24" onclick="toggleAccordion(this)" id="elite-kids">
        <div class="flex items-center justify-between gap-3 mb-4 border-b border-gray-100 pb-4 w-full">
            <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
                    <span class="material-symbols-outlined text-2xl">school</span>
                </div>
                <h3 class="text-[#00174f] text-2xl font-bold font-display m-0">2. Elite Kids</h3>
            </div>
            <span class="material-symbols-outlined text-gray-400 group-hover:text-primary transition-transform duration-300 transform rotate-0 toggle-icon">expand_more</span>
        </div>
        <div class="text-gray-600 text-[15px] space-y-3 leading-relaxed font-body card-content hidden">
            <ul class="space-y-3">
                <li class="flex items-start gap-2">
                    <span class="material-symbols-outlined text-primary text-lg mt-0.5 flex-shrink-0">check_circle</span>
                    <span><strong>Đối tượng:</strong> Học viên từ Tiểu học (lớp 3+) đến hết THCS</span>
                </li>
                <li class="flex items-start gap-2">
                    <span class="material-symbols-outlined text-primary text-lg mt-0.5 flex-shrink-0">check_circle</span>
                    <span><strong>Quy mô lớp:</strong> Nhóm nhỏ tối đa 10 học viên</span>
                </li>
                <li class="flex items-start gap-2">
                    <span class="material-symbols-outlined text-primary text-lg mt-0.5 flex-shrink-0">check_circle</span>
                    <div>
                        <span><strong>Mục tiêu:</strong></span>
                        <ul class="list-disc pl-6 mt-1 space-y-1 text-gray-500">
                            <li>Lộ trình liên thông, đầu ra tối thiểu IELTS 6.5</li>
                            <li>Định hướng du học từ bậc THPT</li>
                        </ul>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <span class="material-symbols-outlined text-primary text-lg mt-0.5 flex-shrink-0">check_circle</span>
                    <div>
                        <span><strong>Phát triển học thuật:</strong></span>
                        <ul class="list-disc pl-6 mt-1 space-y-1 text-gray-500">
                            <li>Đọc hiểu, phân tích & tư duy phản biện</li>
                            <li>Kỹ năng tổng hợp thông tin</li>
                            <li>Thuyết trình, tranh biện</li>
                        </ul>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <span class="material-symbols-outlined text-primary text-lg mt-0.5 flex-shrink-0">check_circle</span>
                    <div>
                        <span><strong>Kỹ năng học tập:</strong></span>
                        <ul class="list-disc pl-6 mt-1 space-y-1 text-gray-500">
                            <li>Làm việc nhóm & dự án</li>
                            <li>Ứng dụng tiếng Anh trong môi trường học thuật</li>
                        </ul>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <span class="material-symbols-outlined text-primary text-lg mt-0.5 flex-shrink-0">check_circle</span>
                    <div>
                        <span><strong>Phát triển cá nhân:</strong></span>
                        <ul class="list-disc pl-6 mt-1 space-y-1 text-gray-500">
                            <li>Tinh thần độc lập</li>
                            <li>Quản lý cảm xúc</li>
                            <li>Giao tiếp trong môi trường đa văn hoá</li>
                        </ul>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <span class="material-symbols-outlined text-primary text-lg mt-0.5 flex-shrink-0">check_circle</span>
                    <div>
                        <span><strong>Giá trị đạt được:</strong></span>
                        <ul class="list-disc pl-6 mt-1 space-y-1 text-gray-500">
                            <li>Nền tảng tiếng Anh vững chắc, hệ thống</li>
                            <li>Tự tin hội nhập và sẵn sàng cho hành trình du học</li>
                        </ul>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</div>"""

template_path = '/Users/vobac/Downloads/gia-viet-handbook/tieng-anh-thieu-nhi-thieu-nien.html'
with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

# 1. Update Title
template_content = template_content.replace(
    '<title>Tiếng Anh Thiếu nhi - Thiếu niên - Handbook</title>',
    '<title>Chương trình chuyên biệt - Handbook</title>'
)

# 2. Update Breadcrumbs (h1 and links)
template_content = template_content.replace(
    '<h1 class="text-3xl md:text-4xl font-bold text-[#00174f] mb-6 font-display tracking-wide">Tiếng Anh Thiếu nhi - Thiếu niên</h1>',
    '<h1 class="text-3xl md:text-4xl font-bold text-[#00174f] mb-6 font-display tracking-wide">Chương trình chuyên biệt</h1>'
)

template_content = template_content.replace(
    '<span class="text-[#0d121c]">Tiếng Anh Thiếu nhi - Thiếu niên</span>',
    '<span class="text-[#0d121c]">Chương trình chuyên biệt</span>'
)

template_content = template_content.replace(
    '<h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display">Chương trình tiếng Anh Thiếu nhi - Thiếu niên</h2>',
    '<h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display">Chương trình chuyên biệt</h2>'
)

# 3. Replace the entire cards container
start_marker = '<div class="grid grid-cols-1 gap-8">'
end_marker = '<!-- Right Column: Sidebar -->'

start_idx = template_content.find(start_marker)
end_idx = template_content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_html = template_content[:start_idx] + user_content + '\n                            </div>\n                        </div>\n                    </div>\n\n                    ' + template_content[end_idx:]
    
    new_file_path = '/Users/vobac/Downloads/gia-viet-handbook/chuong-trinh-chuyen-biet.html'
    with open(new_file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Created/Updated {os.path.basename(new_file_path)} with accordion layout!")
else:
    print("Could not find the cards container to replace.")
