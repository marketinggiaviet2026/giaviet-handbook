import re
import glob

html_code = """
<div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">
    <span class="text-primary font-bold tracking-wider uppercase text-sm font-body bg-blue-50 w-max px-3 py-1 rounded-full border border-blue-100">CHẤT LƯỢNG ĐÀO TẠO</span>
    <h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display mt-2 mb-2">HOẠT ĐỘNG MENTORING 1-1</h2>
    <h3 class="text-gray-500 text-md font-medium font-body mb-4">(Hỗ trợ chuyên môn cho giáo viên mới & giáo viên tham gia giảng dạy chương trình mới)</h3>
</div>

<!-- 1. Mục đích -->
<h3 class="text-[#00174f] text-xl font-bold font-display mb-6 flex items-center gap-2">
    <span class="material-symbols-outlined text-primary">target</span> 1. Mục đích
</h3>
<div class="bg-gradient-to-br from-indigo-50 to-blue-50 border border-blue-100 rounded-2xl p-6 md:p-8 mb-10 relative overflow-hidden shadow-sm hover:shadow-md transition-all duration-300 group">
    <div class="absolute right-0 top-0 opacity-[0.03] translate-x-1/4 -translate-y-1/4 group-hover:scale-110 transition-transform duration-500">
        <span class="material-symbols-outlined text-[150px]">hub</span>
    </div>
    <p class="relative z-10 text-[15px] font-medium text-[#00174f] mb-4">Hoạt động Mentoring 1-1 là một phần quan trọng trong công tác đảm bảo chất lượng giảng dạy tại Anh ngữ Gia Việt, nhằm:</p>
    <ul class="relative z-10 space-y-3 mt-4">
        <li class="flex gap-3"><span class="material-symbols-outlined text-blue-500 shrink-0">check_circle</span> <span class="text-sm text-gray-700">Hỗ trợ giáo viên mới nhanh chóng thích nghi với chương trình, phương pháp và tiêu chuẩn giảng dạy của trung tâm.</span></li>
        <li class="flex gap-3"><span class="material-symbols-outlined text-blue-500 shrink-0">check_circle</span> <span class="text-sm text-gray-700">Giúp giáo viên tự tin và sẵn sàng khi tham gia giảng dạy một chương trình mới.</span></li>
        <li class="flex gap-3"><span class="material-symbols-outlined text-blue-500 shrink-0">check_circle</span> <span class="text-sm text-gray-700">Nâng cao chất lượng bài dạy thông qua trao đổi chuyên môn sâu, phản hồi mang tính xây dựng và định hướng phát triển.</span></li>
        <li class="flex gap-3"><span class="material-symbols-outlined text-blue-500 shrink-0">check_circle</span> <span class="text-sm text-gray-700">Xây dựng văn hóa học tập – chia sẻ – cải tiến liên tục trong đội ngũ giáo viên YLE.</span></li>
    </ul>
</div>

<!-- 2. Đối tượng -->
<h3 class="text-[#00174f] text-xl font-bold font-display mb-6 flex items-center gap-2">
    <span class="material-symbols-outlined text-primary">group</span> 2. Đối tượng được hỗ trợ (Mentee)
</h3>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
    <div class="bg-white border border-gray-200 rounded-xl p-6 shadow-sm hover:border-blue-400 hover:shadow-md hover:-translate-y-1 transition-all">
        <div class="w-10 h-10 bg-blue-50 rounded-full flex items-center justify-center mb-4 text-blue-600">
            <span class="material-symbols-outlined">person_add</span>
        </div>
        <h4 class="font-bold text-[#00174f] mb-2">Giáo viên mới</h4>
        <p class="text-sm text-gray-600">Những giáo viên cần được hỗ trợ chuyên sâu thêm về kiến thức chuyên môn, phương pháp giảng dạy, quản lý lớp học và kỹ năng triển khai lesson plan theo chuẩn YLE.</p>
    </div>
    <div class="bg-white border border-gray-200 rounded-xl p-6 shadow-sm hover:border-emerald-400 hover:shadow-md hover:-translate-y-1 transition-all">
        <div class="w-10 h-10 bg-emerald-50 rounded-full flex items-center justify-center mb-4 text-emerald-600">
            <span class="material-symbols-outlined">switch_account</span>
        </div>
        <h4 class="font-bold text-[#00174f] mb-2">Giáo viên dạy hệ mới</h4>
        <p class="text-sm text-gray-600">Những giáo viên đổi hệ. <strong class="text-gray-800">Ví dụ:</strong> Giáo viên đang dạy chương trình Kids đăng ký chuyển sang giảng dạy thêm chương trình EFT – Global Teens hoặc ngược lại.</p>
    </div>
</div>

<!-- 3. Hình thức -->
<h3 class="text-[#00174f] text-xl font-bold font-display mb-6 flex items-center gap-2">
    <span class="material-symbols-outlined text-primary">tune</span> 3. Hình thức &amp; Thời gian
</h3>
<div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-12">
    <div class="bg-blue-50/50 border border-blue-100 p-5 rounded-xl transition-all hover:-translate-y-1 hover:shadow-md cursor-pointer">
        <span class="material-symbols-outlined text-blue-500 mb-2">meeting_room</span>
        <h5 class="text-[11px] font-bold text-gray-500 uppercase tracking-widest mb-1">Hình thức</h5>
        <div class="font-bold text-sm text-[#00174f]">Trực tiếp / Online (Ưu tiên gặp trực tiếp)</div>
    </div>
    <div class="bg-blue-50/50 border border-blue-100 p-5 rounded-xl transition-all hover:-translate-y-1 hover:shadow-md cursor-pointer">
        <span class="material-symbols-outlined text-blue-500 mb-2">co_present</span>
        <h5 class="text-[11px] font-bold text-gray-500 uppercase tracking-widest mb-1">Nhân sự hỗ trợ</h5>
        <div class="font-bold text-sm text-[#00174f]">Điều phối viên / GV giàu kinh nghiệm</div>
    </div>
    <div class="bg-blue-50/50 border border-blue-100 p-5 rounded-xl transition-all hover:-translate-y-1 hover:shadow-md cursor-pointer">
        <span class="material-symbols-outlined text-blue-500 mb-2">event</span>
        <h5 class="text-[11px] font-bold text-gray-500 uppercase tracking-widest mb-1">Thời gian khóa</h5>
        <div class="font-bold text-sm text-[#00174f]">3 - 6 tuần (Có thể gia hạn)</div>
    </div>
    <div class="bg-blue-50/50 border border-blue-100 p-5 rounded-xl transition-all hover:-translate-y-1 hover:shadow-md cursor-pointer">
        <span class="material-symbols-outlined text-blue-500 mb-2">schedule</span>
        <h5 class="text-[11px] font-bold text-gray-500 uppercase tracking-widest mb-1">Thời lượng</h5>
        <div class="font-bold text-sm text-[#00174f]">1-2 buổi/tuần (1.5 - 2h/buổi)</div>
    </div>
</div>

<!-- 4. Quy trình -->
<h3 class="text-[#00174f] text-2xl font-bold font-display mb-8 flex items-center gap-2">
    <span class="material-symbols-outlined text-primary text-[28px]">timeline</span> 4. Nội dung &amp; Quy trình Mentoring
</h3>
<div class="space-y-4 mb-14 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px before:md:mx-auto before:md:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-blue-300 before:to-transparent">
    
    <!-- Bước 1 -->
    <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active mb-8 transition-all duration-300 cursor-pointer">
        <div class="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white bg-blue-500 text-white shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 shadow flex-col absolute left-0 md:left-1/2 transform -translate-x-1/2 z-10 transition-transform duration-300 group-hover:scale-110">
            <span class="font-bold text-sm">4.1</span>
        </div>
        <div class="w-[calc(100%-4rem)] md:w-[calc(50%-3rem)] bg-white p-6 rounded-2xl shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07)] border border-blue-50 group-hover:-translate-y-1 group-hover:shadow-lg transition-all duration-300 ml-16 md:ml-0">
            <h4 class="font-bold text-lg text-[#00174f] mb-3">Chuẩn bị trước buổi</h4>
            <div class="text-[13px] text-gray-600 leading-relaxed bg-blue-50/30 p-4 rounded-xl">
                <strong>Giáo viên Mentee cần chuẩn bị lesson plan chi tiết, nêu rõ:</strong>
                <ul class="list-disc pl-5 mt-2 space-y-1 text-gray-600 marker:text-blue-400">
                    <li>Mục tiêu bài học</li>
                    <li>Các hoạt động chính</li>
                    <li>Ý tưởng triển khai, trò chơi, hoạt động tương tác</li>
                    <li>Nhấn mạnh các điểm còn băn khoăn hoặc cần được hỗ trợ.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- Bước 2 -->
    <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active mb-8 transition-all duration-300 cursor-pointer">
        <div class="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white bg-purple-500 text-white shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 shadow flex-col absolute left-0 md:left-1/2 transform -translate-x-1/2 z-10 transition-transform duration-300 group-hover:scale-110">
            <span class="font-bold text-sm">4.2</span>
        </div>
        <div class="w-[calc(100%-4rem)] md:w-[calc(50%-3rem)] bg-white p-6 rounded-2xl shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07)] border border-purple-50 group-hover:-translate-y-1 group-hover:shadow-lg transition-all duration-300 ml-16 md:ml-0">
            <h4 class="font-bold text-lg text-[#00174f] mb-3">Trao đổi &amp; Góp ý</h4>
            <div class="text-[13px] text-gray-600 leading-relaxed bg-purple-50/30 p-4 rounded-xl">
                Mentor và Mentee gặp gỡ để trao đổi ý tưởng cho bài dạy. Phân tích cụ thể tính phù hợp của hoạt động đối với: <strong class="text-purple-600">Độ tuổi học viên; Mục tiêu chương trình; Thời lượng tiết học.</strong><br><br>
                <span class="font-semibold text-gray-800">Mentor sẽ góp ý và điều chỉnh:</span> Cấu trúc lesson plan, cách dẫn dắt hoạt động, ngôn ngữ sử dụng, kỹ thuật quản lý lớp và tạo tương tác.
            </div>
        </div>
    </div>

    <!-- Bước 3 -->
    <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active mb-8 transition-all duration-300 cursor-pointer">
        <div class="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white bg-amber-500 text-white shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 shadow flex-col absolute left-0 md:left-1/2 transform -translate-x-1/2 z-10 transition-transform duration-300 group-hover:scale-110">
            <span class="font-bold text-sm">4.3</span>
        </div>
        <div class="w-[calc(100%-4rem)] md:w-[calc(50%-3rem)] bg-white p-6 rounded-2xl shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07)] border border-amber-50 group-hover:-translate-y-1 group-hover:shadow-lg transition-all duration-300 ml-16 md:ml-0">
            <h4 class="font-bold text-lg text-[#00174f] mb-3">Dạy Demo &amp; Quan sát</h4>
            <div class="text-[13px] text-gray-600 leading-relaxed bg-amber-50/30 p-4 rounded-xl">
                Giáo viên Mentee được khuyến khích mô phỏng cách triển khai hoạt động trên lớp (Demo teaching) đối với một số kỹ thuật chính.<br><br>
                <span class="font-semibold text-gray-800">Mentor sẽ:</span> Quan sát trực tiếp thao tác hướng dẫn học viên, tương tác, xử lý tình huống và cuối cùng đưa ra các lời khuyên mang tính thực tiễn cao nhất.
            </div>
        </div>
    </div>

    <!-- Bước 4 -->
    <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active transition-all duration-300 cursor-pointer">
        <div class="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white bg-emerald-500 text-white shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 shadow flex-col absolute left-0 md:left-1/2 transform -translate-x-1/2 z-10 transition-transform duration-300 group-hover:scale-110">
            <span class="font-bold text-sm">4.4</span>
        </div>
        <div class="w-[calc(100%-4rem)] md:w-[calc(50%-3rem)] bg-white p-6 rounded-2xl shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07)] border border-emerald-50 group-hover:-translate-y-1 group-hover:shadow-lg transition-all duration-300 ml-16 md:ml-0">
            <h4 class="font-bold text-lg text-[#00174f] mb-3">Reflection &amp; Cải thiện</h4>
            <div class="text-[13px] text-gray-600 leading-relaxed bg-emerald-50/30 p-4 rounded-xl">
                Ở buổi gặp tiếp theo, Mentee tiến hành tự đánh giá bài dạy (Reflection) trên lớp thực tế: Chia sẻ các vướng mắc, điểm mạnh, cực hạn gặp phải.<br><br>
                <span class="font-semibold text-emerald-800">Mentor sẽ:</span> Lắng nghe, định hướng, đưa ra giải pháp cải thiện và gợi ý chiến lược phù hợp hoàn hảo hơn cho các buổi kế tiếp.
            </div>
        </div>
    </div>
</div>

<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
    <div class="bg-gray-50 border border-gray-200 p-8 rounded-2xl hover:bg-white hover:border-blue-300 transition-all hover:shadow-lg">
        <h4 class="font-bold text-lg text-[#00174f] mb-4 flex gap-2 items-center"><span class="material-symbols-outlined text-gray-500">checklist</span> 5. Vai trò của Mentee</h4>
        <ul class="space-y-3 text-[13.5px] text-gray-700 list-disc pl-5 marker:text-gray-400">
            <li>Chuẩn bị nghiêm túc lesson plan và nội dung muốn trao đổi tham vấn.</li>
            <li>Luôn chủ động, không ngại chia sẻ khó khăn thắc mắc trong quá trình giảng dạy.</li>
            <li>Sẵn sàng tâm thế mở: Tiếp nhận phản hồi và mạnh dạn thử nghiệm các chiến lược do Mentor đề xuất.</li>
            <li>Thực hiện Reflection trung thực, tích cực với tinh thần cải tiến liên tục.</li>
        </ul>
    </div>
    
    <div class="bg-blue-50 border border-blue-200 p-8 rounded-2xl hover:bg-white hover:border-blue-400 transition-all hover:shadow-lg relative overflow-hidden group">
        <div class="absolute -right-5 -bottom-5 opacity-10 scale-150 group-hover:scale-110 transition-transform duration-700">
            <span class="material-symbols-outlined text-[120px] text-blue-800">workspace_premium</span>
        </div>
        <h4 class="font-bold text-lg text-blue-800 mb-4 flex gap-2 items-center relative z-10"><span class="material-symbols-outlined">stars</span> 6. Kết quả mong đợi</h4>
        <ul class="space-y-3 text-[13.5px] text-gray-800 list-disc pl-5 marker:text-blue-500 font-medium relative z-10">
            <li>Nắm vững được yêu cầu chuyên môn của chương trình đang giảng dạy.</li>
            <li>Đạt tới mức độ tự tin tối đa khi xây dựng và triển khai lesson plan tại lớp.</li>
            <li>Hoàn thiện toàn vẹn kỹ năng giảng dạy, quản trị học viên và tương tác xử lý tình huống.</li>
            <li>100% Sẵn sàng đứng lớp độc lập theo tiêu chuẩn chất lượng khắt khe của Gia Việt!</li>
        </ul>
    </div>
</div>
"""

path = '/Users/vobac/Downloads/gia-viet-handbook/mentoring-1-1.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the content between <!-- Breadcrumb & Title Area --> and <!-- Right Column: Sidebar -->
start_idx = content.find('<div class="w-full md:w-[70%] lg:w-[75%] bg-white rounded-xl shadow-[0_2px_20px_rgba(0,0,0,0.03)] border border-gray-100/50 overflow-hidden">')
end_idx = content.find('<!-- Right Column: Sidebar -->')

if start_idx != -1 and end_idx != -1:
    # need to find the specific closing div right before Right Column Sidebar
    # We will replace from '<div class="p-6 md:p-10 lg:p-12">' to '                        </div>'
    match = re.search(r'(<div class="p-6 md:p-10 lg:p-12">).*?(</div>\s*</div>\s*<!-- Right Column: Sidebar -->)', content[start_idx:], re.DOTALL)
    if match:
        middle = match.group(0)
        # we will extract the exact chunk
        p_start = content.find('<div class="p-6 md:p-10 lg:p-12">')
        p_end = content.find('</div>\n                    </div>\n\n                    <!-- Right Column: Sidebar -->')
        
        if p_start != -1 and p_end != -1:
            new_content = content[:p_start+len('<div class="p-6 md:p-10 lg:p-12">')] + "\n                            " + html_code + "\n                        " + content[p_end:]
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Successfully patched Mentoring 1-1 HTML!")
else:
    print("Could not find start or end tags")

# Now strip all '<!-- Right Column: Sidebar -->' strings globally!
print("Stripping HTML Sidebar text remnants globally!")
for filepath in glob.glob('/Users/vobac/Downloads/gia-viet-handbook/*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_data = f.read()
    
    file_data = file_data.replace('<!-- Right Column: Sidebar -->', '')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(file_data)
