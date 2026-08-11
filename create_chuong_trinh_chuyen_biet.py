import os
import re

user_content = """
<div class="flex flex-col gap-2 mb-8">
    <span class="text-primary font-bold tracking-wider uppercase text-sm font-body">Đào tạo & Đảm bảo chất lượng</span>
    <h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display">Chương trình chuyên biệt</h2>
</div>

<div class="space-y-10">
    <!-- Learning Through Playing -->
    <section id="ltp" class="scroll-mt-24">
        <h3 class="text-[#00174f] text-2xl font-bold font-display mb-4">1. Learning Through Playing (LTP)</h3>
        <p class="mb-3"><strong class="text-[#0d59f2]">Độ tuổi:</strong> 4 – 11 tuổi</p>
        <p class="mb-3"><strong class="text-[#0d59f2]">Mục tiêu:</strong> Học tiếng Anh tự nhiên thông qua phương pháp Play-based Learning (học qua vui chơi)</p>
        
        <h4 class="font-bold text-lg mt-6 mb-2">Phương pháp học:</h4>
        <ul class="list-disc pl-5 mb-3 space-y-1">
            <li>Học qua trò chơi, bài hát, kể chuyện & dự án sáng tạo</li>
            <li>Môi trường học tập tích cực, phù hợp từng độ tuổi</li>
        </ul>

        <h4 class="font-bold text-lg mt-6 mb-2">Phát triển ngôn ngữ:</h4>
        <ul class="list-disc pl-5 mb-3 space-y-1">
            <li>Hình thành phản xạ tiếng Anh tự nhiên</li>
            <li>Tăng sự tự tin trong giao tiếp</li>
            <li>Ghi nhớ & vận dụng ngôn ngữ qua ngữ cảnh thực tế</li>
        </ul>

        <h4 class="font-bold text-lg mt-6 mb-2">Giáo dục cảm xúc – xã hội (SEL):</h4>
        <ul class="list-disc pl-5 mb-3 space-y-1">
            <li>Nhận diện & quản lý cảm xúc cá nhân</li>
            <li>Phát triển kỹ năng giao tiếp, hợp tác</li>
            <li>Nuôi dưỡng sự đồng cảm, chia sẻ & tôn trọng</li>
        </ul>

        <h4 class="font-bold text-lg mt-6 mb-2">Kỹ năng hình thành:</h4>
        <ul class="list-disc pl-5 mb-3 space-y-1">
            <li>Tự tin thể hiện bản thân</li>
            <li>Biết lắng nghe & phản hồi phù hợp</li>
        </ul>

        <h4 class="font-bold text-lg mt-6 mb-2">Môi trường học tập:</h4>
        <ul class="list-disc pl-5 mb-3 space-y-1">
            <li>An toàn, thân thiện, khuyến khích sự tham gia</li>
            <li>Tôn trọng sự khác biệt của mỗi học viên</li>
        </ul>

        <div class="bg-blue-50 border-l-4 border-[#0d59f2] p-4 mt-6 rounded-r-lg">
            <p class="font-bold text-[#00174f]">Nền tảng: Phát triển toàn diện về ngôn ngữ, cảm xúc và kỹ năng xã hội</p>
        </div>
    </section>

    <hr class="border-gray-200 dark:border-gray-700">

    <!-- Elite Kids -->
    <section id="elite-kids" class="scroll-mt-24">
        <h3 class="text-[#00174f] text-2xl font-bold font-display mb-4">2. Elite Kids</h3>
        <p class="mb-3"><strong class="text-[#0d59f2]">Đối tượng:</strong> Học viên từ Tiểu học (lớp 3+) đến hết THCS</p>
        <p class="mb-3"><strong class="text-[#0d59f2]">Quy mô lớp:</strong> Nhóm nhỏ tối đa 10 học viên</p>
        
        <h4 class="font-bold text-lg mt-6 mb-2">Mục tiêu:</h4>
        <ul class="list-disc pl-5 mb-3 space-y-1">
            <li>Lộ trình liên thông, đầu ra tối thiểu IELTS 6.5</li>
            <li>Định hướng du học từ bậc THPT</li>
        </ul>

        <h4 class="font-bold text-lg mt-6 mb-2">Phát triển học thuật:</h4>
        <ul class="list-disc pl-5 mb-3 space-y-1">
            <li>Đọc hiểu, phân tích & tư duy phản biện</li>
            <li>Kỹ năng tổng hợp thông tin</li>
            <li>Thuyết trình, tranh biện</li>
        </ul>

        <h4 class="font-bold text-lg mt-6 mb-2">Kỹ năng học tập:</h4>
        <ul class="list-disc pl-5 mb-3 space-y-1">
            <li>Làm việc nhóm & dự án</li>
            <li>Ứng dụng tiếng Anh trong môi trường học thuật</li>
        </ul>

        <h4 class="font-bold text-lg mt-6 mb-2">Phát triển cá nhân:</h4>
        <ul class="list-disc pl-5 mb-3 space-y-1">
            <li>Tinh thần độc lập</li>
            <li>Quản lý cảm xúc</li>
            <li>Giao tiếp trong môi trường đa văn hoá</li>
        </ul>

        <h4 class="font-bold text-lg mt-6 mb-2">Giá trị đạt được:</h4>
        <ul class="list-disc pl-5 mb-3 space-y-1">
            <li>Nền tảng tiếng Anh vững chắc, hệ thống</li>
            <li>Tự tin hội nhập và sẵn sàng cho hành trình du học</li>
        </ul>
    </section>
</div>
"""

template_path = '/Users/vobac/Downloads/gia-viet-handbook/che-do-luong-thuong.html'
with open(template_path, 'r') as f:
    template_content = f.read()

# 1. Update Title
template_content = re.sub(r'<title>.*?</title>', '<title>Chương trình chuyên biệt - Handbook</title>', template_content)

# 2. Update Breadcrumbs (h1 and links)
template_content = re.sub(r'<h1.*?>.*?</h1>', '<h1 class="text-3xl md:text-4xl font-bold text-[#00174f] mb-6 font-display tracking-wide">Chương trình chuyên biệt</h1>', template_content)
template_content = re.sub(r'<a[^>]*>Chính sách & Phúc lợi</a>', '<a href="dao-tao-dam-bao-chat-luong.html" class="hover:text-primary transition-colors">Chương trình Đào tạo</a>', template_content)
template_content = re.sub(r'<span class="text-\[#0d121c\]">Chế độ lương - Thưởng</span>', '<span class="text-[#0d121c]">Chương trình chuyên biệt</span>', template_content)

# 3. Replace Main Content (Left Column)
# Replace the container div and everything inside up to the sidebar
main_content_pattern = r'<!-- Left Column: Content -->\s*<div[^>]*>.*?(</div>\s*<!-- Right Column: Sidebar -->)'
new_left_column = """<!-- Left Column: Content -->
                    <div class="w-full md:w-[70%] lg:w-[75%] font-body text-gray-800 leading-relaxed space-y-8">
                        <div class="bg-white rounded-2xl shadow-sm border border-gray-100/50 p-6 md:p-8">
                            """ + user_content.strip() + """
                        </div>
                    </div>"""
template_content = re.sub(main_content_pattern, new_left_column + r'\n                    \g<1>', template_content, flags=re.DOTALL)

# 4. Save to new file
new_file_path = '/Users/vobac/Downloads/gia-viet-handbook/chuong-trinh-chuyen-biet.html'
with open(new_file_path, 'w') as f:
    f.write(template_content)

print(f"Created {os.path.basename(new_file_path)}")

# Update all HTML files' mega menus to point to this new file
html_files = [f for f in os.listdir('/Users/vobac/Downloads/gia-viet-handbook') if f.endswith('.html')]

for f_name in html_files:
    file_path = os.path.join('/Users/vobac/Downloads/gia-viet-handbook', f_name)
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Check if links exist
    content = content.replace(
        '<a href="#" class="text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-primary transition-colors">Learning Through Playing (LTP)</a>',
        '<a href="chuong-trinh-chuyen-biet.html#ltp" class="text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-primary transition-colors">Learning Through Playing (LTP)</a>'
    )
    content = content.replace(
        '<a href="#" class="text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-primary transition-colors">Elite Kids</a>',
        '<a href="chuong-trinh-chuyen-biet.html#elite-kids" class="text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-primary transition-colors">Elite Kids</a>'
    )
    
    with open(file_path, 'w') as f:
        f.write(content)

print("Updated mega menu links.")
