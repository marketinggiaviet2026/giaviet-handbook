import os

html_content = """<div class="flex flex-col gap-2 mb-8">
    <span class="text-primary font-bold tracking-wider uppercase text-sm font-body">Đào tạo & Đảm bảo chất lượng</span>
    <h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display">Flexi-time English Program</h2>
</div>

<!-- 1. FLEXI-TIME LÀ GÌ? -->
<div class="mb-10">
    <h3 class="text-[#00174f] text-2xl font-bold font-display mb-4 border-b border-gray-100 pb-2">1. FLEXI-TIME LÀ GÌ?</h3>
    <p class="text-gray-600 leading-relaxed font-body text-[16px]">
        Chương trình Flexi 1-1 được thiết kế cho học viên có nhu cầu học cá nhân hóa, cần lịch học linh hoạt, hỗ trợ chuyên sâu hoặc muốn tăng band điểm trong thời gian ngắn. Vì vậy, học viên sẽ đóng học phí cao hơn và kỳ vọng chất lượng giảng dạy, theo sát và tư vấn tốt hơn từ giáo viên và điều phối viên.
    </p>
</div>

<!-- 2. ĐIỂM NỔI BẬT CỦA CHƯƠNG TRÌNH -->
<div class="mb-10">
    <h3 class="text-[#00174f] text-2xl font-bold font-display mb-4 border-b border-gray-100 pb-2">2. ĐIỂM NỔI BẬT CỦA CHƯƠNG TRÌNH</h3>
    <ul class="space-y-3 text-gray-600 font-body text-[16px]">
        <li class="flex items-start gap-2">
            <span class="material-symbols-outlined text-primary text-xl flex-shrink-0">check_circle</span>
            <span>Lộ trình học được cá nhân hóa dựa trên trình độ đầu vào và mục tiêu cụ thể của từng học viên.</span>
        </li>
        <li class="flex items-start gap-2">
            <span class="material-symbols-outlined text-primary text-xl flex-shrink-0">check_circle</span>
            <span>Tốc độ học tập linh hoạt theo năng lực từng học viên.</span>
        </li>
        <li class="flex items-start gap-2">
            <span class="material-symbols-outlined text-primary text-xl flex-shrink-0">check_circle</span>
            <span>Nội dung, tài liệu, kỹ năng được điều chỉnh liên tục theo tiến độ.</span>
        </li>
        <li class="flex items-start gap-2">
            <span class="material-symbols-outlined text-primary text-xl flex-shrink-0">check_circle</span>
            <span>Học viên được theo dõi và báo cáo tiến độ thường xuyên.</span>
        </li>
        <li class="flex items-start gap-2">
            <span class="material-symbols-outlined text-primary text-xl flex-shrink-0">check_circle</span>
            <span>Giao tiếp định kỳ giữa học viên – giáo viên – điều phối viên.</span>
        </li>
        <li class="flex items-start gap-2">
            <span class="material-symbols-outlined text-primary text-xl flex-shrink-0">check_circle</span>
            <span>Tư vấn học tập trực tiếp và thường xuyên từ giáo viên.</span>
        </li>
    </ul>
</div>

<!-- 3. QUY TRÌNH TRIỂN KHAI -->
<div class="mb-12">
    <h3 class="text-[#00174f] text-2xl font-bold font-display mb-6 border-b border-gray-100 pb-2">3. QUY TRÌNH TRIỂN KHAI</h3>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="flex items-center gap-4 bg-blue-50/50 p-4 rounded-xl border border-blue-100 p-4 rounded-xl items-stretch">
            <div class="w-10 h-10 rounded-full bg-primary text-white flex items-center justify-center font-bold text-lg flex-shrink-0">1</div>
            <div>
                <h4 class="font-bold text-[#00174f]">Tư vấn nhu cầu ban đầu (SRM).</h4>
            </div>
        </div>
        <div class="flex items-center gap-4 bg-blue-50/50 p-4 rounded-xl border border-blue-100 p-4 rounded-xl items-stretch">
            <div class="w-10 h-10 rounded-full bg-primary text-white flex items-center justify-center font-bold text-lg flex-shrink-0">2</div>
            <div>
                <h4 class="font-bold text-[#00174f]">Kiểm tra trình độ đầu vào & đề xuất lộ trình học phù hợp</h4>
                <p class="text-sm text-gray-500">(Placement Team + Coordinators)</p>
            </div>
        </div>
        <div class="flex items-center gap-4 bg-blue-50/50 p-4 rounded-xl border border-blue-100 p-4 rounded-xl items-stretch">
            <div class="w-10 h-10 rounded-full bg-primary text-white flex items-center justify-center font-bold text-lg flex-shrink-0">3</div>
            <div>
                <h4 class="font-bold text-[#00174f]">Ký hợp đồng & sắp xếp lịch học linh hoạt</h4>
                <p class="text-sm text-gray-500">(Coordinators + SRM)</p>
            </div>
        </div>
        <div class="flex items-center gap-4 bg-blue-50/50 p-4 rounded-xl border border-blue-100 p-4 rounded-xl items-stretch">
            <div class="w-10 h-10 rounded-full bg-primary text-white flex items-center justify-center font-bold text-lg flex-shrink-0">4</div>
            <div>
                <h4 class="font-bold text-[#00174f]">Khai giảng & giảng dạy</h4>
                <p class="text-sm text-gray-500">(Teachers + Coordinators)</p>
            </div>
        </div>
        <div class="flex items-center gap-4 bg-blue-50/50 p-4 rounded-xl border border-blue-100 p-4 rounded-xl items-stretch">
            <div class="w-10 h-10 rounded-full bg-primary text-white flex items-center justify-center font-bold text-lg flex-shrink-0">5</div>
            <div>
                <h4 class="font-bold text-[#00174f]">Theo dõi và thu thập phản hồi học tập</h4>
                <p class="text-sm text-gray-500">sau 2 tuần đầu, sau đó định kỳ mỗi 3 tuần.</p>
            </div>
        </div>
        <div class="flex items-center gap-4 bg-blue-50/50 p-4 rounded-xl border border-blue-100 p-4 rounded-xl items-stretch">
            <div class="w-10 h-10 rounded-full bg-primary text-white flex items-center justify-center font-bold text-lg flex-shrink-0">6</div>
            <div>
                <h4 class="font-bold text-[#00174f]">Quyết định ngày thi & đăng ký thi.</h4>
            </div>
        </div>
        <div class="flex items-center gap-4 bg-blue-50/50 p-4 rounded-xl border border-blue-100 p-4 rounded-xl items-stretch">
            <div class="w-10 h-10 rounded-full bg-primary text-white flex items-center justify-center font-bold text-lg flex-shrink-0">7</div>
            <div>
                <h4 class="font-bold text-[#00174f]">Đánh giá kết quả sau kỳ thi & quyết định tiếp tục</h4>
            </div>
        </div>
        <div class="flex items-center gap-4 bg-blue-50/50 p-4 rounded-xl border border-blue-100 p-4 rounded-xl items-stretch">
            <div class="w-10 h-10 rounded-full bg-primary text-white flex items-center justify-center font-bold text-lg flex-shrink-0">8</div>
            <div>
                <h4 class="font-bold text-[#00174f]">Kết thúc hợp đồng.</h4>
            </div>
        </div>
    </div>
</div>

<!-- 4. TÓM TẮT CHƯƠNG TRÌNH THEO TRÌNH ĐỘ -->
<div class="mb-10">
    <h3 class="text-[#00174f] text-2xl font-bold font-display mb-6 border-b border-gray-100 pb-2">4. TÓM TẮT CHƯƠNG TRÌNH THEO TRÌNH ĐỘ</h3>
    
    <div class="flex flex-col gap-6">
        <!-- Card 1: 6.5 -> 7.0+ -->
        <div class="flex flex-col md:flex-row bg-white rounded-xl shadow-[0_4px_20px_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden group hover:border-primary transition-colors cursor-pointer">
            <div class="bg-gradient-to-br from-[#0d59f2] to-[#0a46c2] p-6 md:w-1/3 flex flex-col justify-center items-center text-white relative overflow-hidden">
                <div class="absolute -right-4 -bottom-4 opacity-10">
                    <span class="material-symbols-outlined text-9xl">workspace_premium</span>
                </div>
                <h4 class="text-3xl font-bold font-display mb-1 relative z-10">6.5 → 7.0+</h4>
                <span class="bg-white/20 px-3 py-1 rounded-full text-sm font-medium relative z-10 backdrop-blur-sm">(C1+)</span>
                <div class="mt-4 flex items-center gap-1 text-blue-100 relative z-10">
                    <span class="material-symbols-outlined text-sm">schedule</span>
                    <span class="text-sm">60h (10 tuần) + 120h tự học</span>
                </div>
            </div>
            <div class="p-6 md:w-2/3 flex flex-col justify-center">
                <h5 class="text-[#00174f] font-bold text-lg mb-2">Mục tiêu: Nâng cao toàn diện, tối ưu hiệu suất</h5>
                <p class="text-sm text-gray-500 mb-3"><strong>Tập trung:</strong> Chiến lược làm bài, mock test, ngôn ngữ học thuật nâng cao</p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-sm text-gray-600">
                    <div class="flex items-start gap-1.5"><span class="text-primary font-bold">●</span><span><strong>S:</strong> Phản xạ nhanh, dài, logic</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-primary font-bold">●</span><span><strong>L:</strong> Mạnh Section 3–4</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-primary font-bold">●</span><span><strong>W:</strong> Task 1, 2 nâng cao, từ vựng phức</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-primary font-bold">●</span><span><strong>R:</strong> Quản lý thời gian, Passage 3</span></div>
                </div>
            </div>
        </div>

        <!-- Card 2: 6.0 -> 6.5 -->
        <div class="flex flex-col md:flex-row bg-white rounded-xl shadow-[0_4px_20px_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden group hover:border-blue-400 transition-colors cursor-pointer">
            <div class="bg-gradient-to-br from-blue-500 to-blue-600 p-6 md:w-1/3 flex flex-col justify-center items-center text-white relative overflow-hidden">
                <div class="absolute -right-4 -bottom-4 opacity-10">
                    <span class="material-symbols-outlined text-9xl">analytics</span>
                </div>
                <h4 class="text-3xl font-bold font-display mb-1 relative z-10">6.0 → 6.5</h4>
                <span class="bg-white/20 px-3 py-1 rounded-full text-sm font-medium relative z-10 backdrop-blur-sm">(B2–C1)</span>
                <div class="mt-4 flex items-center gap-1 text-blue-100 relative z-10">
                    <span class="material-symbols-outlined text-sm">schedule</span>
                    <span class="text-sm">60h (10 tuần)</span>
                </div>
            </div>
            <div class="p-6 md:w-2/3 flex flex-col justify-center">
                <h5 class="text-[#00174f] font-bold text-lg mb-3">Mục tiêu: Củng cố kỹ năng + tăng band điểm</h5>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-sm text-gray-600">
                    <div class="flex items-start gap-1.5"><span class="text-blue-500 font-bold">●</span><span><strong>S:</strong> Trả lời mạch lạc, thay đổi độ logic</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-blue-500 font-bold">●</span><span><strong>L:</strong> Tập trung Section 3–4</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-blue-500 font-bold">●</span><span><strong>W:</strong> Thành thạo Task 1 & 2</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-blue-500 font-bold">●</span><span><strong>R:</strong> Chiến lược skim-scan</span></div>
                </div>
            </div>
        </div>

        <!-- Card 3: 5.5 -> 6.0 -->
        <div class="flex flex-col md:flex-row bg-white rounded-xl shadow-[0_4px_20px_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden group hover:border-[#10b981] transition-colors cursor-pointer">
            <div class="bg-gradient-to-br from-[#10b981] to-[#0d9488] p-6 md:w-1/3 flex flex-col justify-center items-center text-white relative overflow-hidden">
                <div class="absolute -right-4 -bottom-4 opacity-10">
                    <span class="material-symbols-outlined text-9xl">trending_up</span>
                </div>
                <h4 class="text-3xl font-bold font-display mb-1 relative z-10">5.5 → 6.0</h4>
                <span class="bg-white/20 px-3 py-1 rounded-full text-sm font-medium relative z-10 backdrop-blur-sm">(B2+)</span>
                <div class="mt-4 flex items-center gap-1 text-green-100 relative z-10">
                    <span class="material-symbols-outlined text-sm">schedule</span>
                    <span class="text-sm">60h</span>
                </div>
            </div>
            <div class="p-6 md:w-2/3 flex flex-col justify-center">
                <h5 class="text-[#00174f] font-bold text-lg mb-3">Mục tiêu: Nâng nền tảng + làm quen chiến lược</h5>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-sm text-gray-600">
                    <div class="flex items-start gap-1.5"><span class="text-emerald-500 font-bold">●</span><span><strong>S:</strong> Mở rộng ý, luyện phản xạ</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-emerald-500 font-bold">●</span><span><strong>L:</strong> Section 1, 2, 4</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-emerald-500 font-bold">●</span><span><strong>W:</strong> Nắm vững cấu trúc bài rõ</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-emerald-500 font-bold">●</span><span><strong>R:</strong> Tập trung Passage 1–2</span></div>
                </div>
            </div>
        </div>

        <!-- Card 4: 5.0 -> 5.5 -->
        <div class="flex flex-col md:flex-row bg-white rounded-xl shadow-[0_4px_20px_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden group hover:border-[#f59e0b] transition-colors cursor-pointer">
            <div class="bg-gradient-to-br from-[#f59e0b] to-[#d97706] p-6 md:w-1/3 flex flex-col justify-center items-center text-white relative overflow-hidden">
                <div class="absolute -right-4 -bottom-4 opacity-10">
                    <span class="material-symbols-outlined text-9xl">lightbulb</span>
                </div>
                <h4 class="text-3xl font-bold font-display mb-1 relative z-10">5.0 → 5.5</h4>
                <span class="bg-white/20 px-3 py-1 rounded-full text-sm font-medium relative z-10 backdrop-blur-sm">(B2)</span>
                <div class="mt-4 flex items-center gap-1 text-orange-100 relative z-10">
                    <span class="material-symbols-outlined text-sm">schedule</span>
                    <span class="text-sm">48h</span>
                </div>
            </div>
            <div class="p-6 md:w-2/3 flex flex-col justify-center">
                <h5 class="text-[#00174f] font-bold text-lg mb-3">Mục tiêu: Làm quen format IELTS</h5>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-sm text-gray-600">
                    <div class="flex items-start gap-1.5"><span class="text-amber-500 font-bold">●</span><span><strong>S:</strong> Câu trả lời mạch lạc</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-amber-500 font-bold">●</span><span><strong>L:</strong> Chủ yếu dạng gap-fill</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-amber-500 font-bold">●</span><span><strong>W:</strong> Nắm cấu trúc cơ bản</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-amber-500 font-bold">●</span><span><strong>R:</strong> Skimming – scanning</span></div>
                </div>
            </div>
        </div>

        <!-- Card 5: 4.5 -> 5.0 -->
        <div class="flex flex-col md:flex-row bg-white rounded-xl shadow-[0_4px_20px_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden group hover:border-[#6366f1] transition-colors cursor-pointer">
            <div class="bg-gradient-to-br from-[#6366f1] to-[#4f46e5] p-6 md:w-1/3 flex flex-col justify-center items-center text-white relative overflow-hidden">
                <div class="absolute -right-4 -bottom-4 opacity-10">
                    <span class="material-symbols-outlined text-9xl">school</span>
                </div>
                <h4 class="text-3xl font-bold font-display mb-1 relative z-10">4.5 → 5.0</h4>
                <span class="bg-white/20 px-3 py-1 rounded-full text-sm font-medium relative z-10 backdrop-blur-sm">(B1+)</span>
                <div class="mt-4 flex items-center gap-1 text-indigo-100 relative z-10">
                    <span class="material-symbols-outlined text-sm">schedule</span>
                    <span class="text-sm">48h</span>
                </div>
            </div>
            <div class="p-6 md:w-2/3 flex flex-col justify-center">
                <h5 class="text-[#00174f] font-bold text-lg mb-3">Mục tiêu: Xây nền IELTS</h5>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-sm text-gray-600">
                    <div class="flex items-start gap-1.5"><span class="text-indigo-500 font-bold">●</span><span><strong>S:</strong> Part 1–2</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-indigo-500 font-bold">●</span><span><strong>L:</strong> Section 1–2</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-indigo-500 font-bold">●</span><span><strong>W:</strong> Task 1 đơn giản, Task 2 cơ bản</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-indigo-500 font-bold">●</span><span><strong>R:</strong> Kỹ năng đọc nền</span></div>
                </div>
            </div>
        </div>

        <!-- Card 6: 4.0 -> 4.5 -->
        <div class="flex flex-col md:flex-row bg-white rounded-xl shadow-[0_4px_20px_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden group hover:border-[#8b5cf6] transition-colors cursor-pointer">
            <div class="bg-gradient-to-br from-[#8b5cf6] to-[#7c3aed] p-6 md:w-1/3 flex flex-col justify-center items-center text-white relative overflow-hidden">
                <div class="absolute -right-4 -bottom-4 opacity-10">
                    <span class="material-symbols-outlined text-9xl">menu_book</span>
                </div>
                <h4 class="text-3xl font-bold font-display mb-1 relative z-10">4.0 → 4.5</h4>
                <span class="bg-white/20 px-3 py-1 rounded-full text-sm font-medium relative z-10 backdrop-blur-sm">(B1)</span>
                <div class="mt-4 flex items-center gap-1 text-purple-100 relative z-10">
                    <span class="material-symbols-outlined text-sm">schedule</span>
                    <span class="text-sm">48h</span>
                </div>
            </div>
            <div class="p-6 md:w-2/3 flex flex-col justify-center">
                <h5 class="text-[#00174f] font-bold text-lg mb-3">Mục tiêu: Làm quen bài thi IELTS</h5>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-sm text-gray-600">
                    <div class="flex items-start gap-1.5"><span class="text-purple-500 font-bold">●</span><span><strong>S:</strong> Part 1–2</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-purple-500 font-bold">●</span><span><strong>L:</strong> Section 1–2</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-purple-500 font-bold">●</span><span><strong>W:</strong> Đoạn văn & bài luận đơn giản</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-purple-500 font-bold">●</span><span><strong>R:</strong> Kỹ năng cơ bản</span></div>
                </div>
            </div>
        </div>

        <!-- Card 7: 3.5 -> 4.0 -->
        <div class="flex flex-col md:flex-row bg-white rounded-xl shadow-[0_4px_20px_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden group hover:border-[#ec4899] transition-colors cursor-pointer">
            <div class="bg-gradient-to-br from-[#ec4899] to-[#db2777] p-6 md:w-1/3 flex flex-col justify-center items-center text-white relative overflow-hidden">
                <div class="absolute -right-4 -bottom-4 opacity-10">
                    <span class="material-symbols-outlined text-9xl">draw</span>
                </div>
                <h4 class="text-3xl font-bold font-display mb-1 relative z-10">3.5 → 4.0</h4>
                <span class="bg-white/20 px-3 py-1 rounded-full text-sm font-medium relative z-10 backdrop-blur-sm">(A2–B1-)</span>
                <div class="mt-4 flex items-center gap-1 text-pink-100 relative z-10">
                    <span class="material-symbols-outlined text-sm">schedule</span>
                    <span class="text-sm">48h</span>
                </div>
            </div>
            <div class="p-6 md:w-2/3 flex flex-col justify-center">
                <h5 class="text-[#00174f] font-bold text-lg mb-3">Mục tiêu: Xây nền ngôn ngữ + làm quen IELTS</h5>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-sm text-gray-600">
                    <div class="flex items-start gap-1.5"><span class="text-pink-500 font-bold">●</span><span><strong>S:</strong> Chủ đề quen thuộc</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-pink-500 font-bold">●</span><span><strong>L:</strong> Nghe cơ bản</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-pink-500 font-bold">●</span><span><strong>W:</strong> Câu, đoạn, làm quen Task 1</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-pink-500 font-bold">●</span><span><strong>R:</strong> Dạng bài đơn giản</span></div>
                </div>
            </div>
        </div>

        <!-- Card 8: FOUNDATION -->
        <div class="flex flex-col md:flex-row bg-white rounded-xl shadow-[0_4px_20px_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden group hover:border-[#64748b] transition-colors cursor-pointer">
            <div class="bg-gradient-to-br from-[#64748b] to-[#475569] p-6 md:w-1/3 flex flex-col justify-center items-center text-white relative overflow-hidden">
                <div class="absolute -right-4 -bottom-4 opacity-10">
                    <span class="material-symbols-outlined text-9xl">foundation</span>
                </div>
                <h4 class="text-2xl md:text-3xl font-bold font-display mb-1 relative z-10 text-center">FOUNDATION</h4>
                <span class="bg-white/20 px-3 py-1 rounded-full text-sm font-medium relative z-10 backdrop-blur-sm mt-1">(A1–A2)</span>
                <div class="mt-4 flex items-center gap-1 text-slate-200 relative z-10">
                    <span class="material-symbols-outlined text-sm">schedule</span>
                    <span class="text-sm">48h</span>
                </div>
            </div>
            <div class="p-6 md:w-2/3 flex flex-col justify-center">
                <h5 class="text-[#00174f] font-bold text-lg mb-2">Mục tiêu: Xây dựng nền tảng từ vựng, ngữ pháp và phản xạ</h5>
                <p class="text-sm text-gray-500 mb-3"><strong>Nội dung:</strong> Giao tiếp hàng ngày</p>
                <div class="grid grid-cols-1 gap-3 text-sm text-gray-600">
                    <div class="flex items-start gap-1.5"><span class="text-slate-500 font-bold">●</span><span><strong>Listening – Speaking:</strong> Giao tiếp trong các tình huống thực tế</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-slate-500 font-bold">●</span><span><strong>Reading:</strong> Văn bản ngắn</span></div>
                    <div class="flex items-start gap-1.5"><span class="text-slate-500 font-bold">●</span><span><strong>Writing:</strong> Câu, email, mô tả.</span></div>
                </div>
            </div>
        </div>
    </div>
</div>"""

template_path = '/Users/vobac/Downloads/gia-viet-handbook/tieng-anh-thieu-nhi-thieu-nien.html'
with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

# Replace document title
template_content = template_content.replace('<title>Tiếng Anh Thiếu nhi - Thiếu niên - Handbook</title>', '<title>Flexi-time - Handbook</title>')

# Replace active breadcrumb and h1
template_content = template_content.replace(
    '<h1 class="text-3xl md:text-4xl font-bold text-[#00174f] mb-6 font-display tracking-wide">Tiếng Anh Thiếu nhi - Thiếu niên</h1>',
    '<h1 class="text-3xl md:text-4xl font-bold text-[#00174f] mb-6 font-display tracking-wide">Flexi-time English Program</h1>'
)

template_content = template_content.replace(
    '<span class="text-[#0d121c]">Tiếng Anh Thiếu nhi - Thiếu niên</span>',
    '<span class="text-[#0d121c]">Flexi-time</span>'
)

# Extract right sidebar and wrapper structure, injecting `html_content`
import re
main_content_pattern = r'<!-- Left Column: Content -->\s*<div[^>]*>.*?(</div>\s*<!-- Right Column: Sidebar -->)'
new_left_column = """<!-- Left Column: Content -->
                    <div class="w-full md:w-[70%] lg:w-[75%] font-body text-gray-800 leading-relaxed space-y-8">
                        <div class="bg-white rounded-2xl shadow-sm border border-gray-100/50 p-6 md:p-8">
                            """ + html_content.strip() + """
                        </div>
                    </div>"""

if re.search(main_content_pattern, template_content, flags=re.DOTALL):
    final_html = re.sub(main_content_pattern, new_left_column + r'\n                    \g<1>', template_content, flags=re.DOTALL)
    with open('/Users/vobac/Downloads/gia-viet-handbook/flexi-time.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Successfully created flexi-time.html!")
else:
    print("Replacements failed.")
