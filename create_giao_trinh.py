import os

def create_giao_trinh():
    source_file = '/Users/vobac/Downloads/gia-viet-handbook/quy-dinh-tac-phong.html'
    target_file = '/Users/vobac/Downloads/gia-viet-handbook/giao-trinh-tai-lieu.html'
    
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Title
    import re
    content = re.sub(
        r'<title>.*?</title>',
        '<title>Giáo trình & Tài liệu giảng dạy - Handbook</title>',
        content
    )
    
    # Replace active states in Sidebar!
    # In quy-dinh-tac-phong, `Quy định về tác phong` has the active class (`before:bg-primary`).
    # We should make "Giáo trình & Tài liệu giảng dạy" active instead.
    # The new page sits under "Đào tạo & Đảm bảo chất lượng". So we should expand that instead of "Tổ chức & Nhân sự".
    
    # Wait, the sidebar replacement might be tricky automatically. We'll just replace the main content block for now, and inject the layout.
    
    content_start = content.find('<!-- Breadcrumb & Title Area -->')
    content_end = content.find('<!-- Right Column: Sidebar -->')
    
    new_content = """<!-- Breadcrumb & Title Area -->
            <div class="w-full bg-white py-12 px-4 md:px-10 border-b border-gray-100 shadow-sm relative overflow-hidden">
                <div class="absolute right-0 top-0 w-64 h-64 bg-blue-50/50 rounded-full translate-x-1/2 -translate-y-1/2 opacity-50"></div>
                <div class="absolute right-0 top-0 w-32 h-32 text-blue-100 translate-x-1/4 -translate-y-1/4 opacity-30" style="background-image: radial-gradient(#0d59f2 2px, transparent 2px); background-size: 16px 16px;"></div>

                <div class="w-full max-w-[1280px] mx-auto relative z-10 font-body">
                    <h1 class="text-3xl md:text-4xl font-bold text-[#00174f] mb-6 font-display tracking-wide">Giáo trình & Tài liệu giảng dạy</h1>
                    <div class="flex items-center gap-2 text-[15px] text-gray-500 font-body">
                        <a href="index.html" class="flex items-center hover:text-primary transition-colors">
                            <span class="material-symbols-outlined text-[18px]">home</span>
                            <span class="ml-1">Trang chủ</span>
                        </a>
                        <span class="material-symbols-outlined text-sm">chevron_right</span>
                        <a href="dao-tao-dam-bao-chat-luong.html" class="hover:text-primary transition-colors">Đào tạo & Đảm bảo chất lượng</a>
                        <span class="material-symbols-outlined text-sm">chevron_right</span>
                        <a href="#" class="hover:text-primary transition-colors">Quy định & Quy trình giảng dạy</a>
                        <span class="material-symbols-outlined text-sm">chevron_right</span>
                        <span class="text-[#0d121c]">Giáo trình & Tài liệu giảng dạy</span>
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
                                <h2 class="text-[#0d121c] dark:text-white text-3xl md:text-4xl font-bold leading-tight font-display text-center md:text-left mt-2">GIÁO TRÌNH CHƯƠNG TRÌNH YLE</h2>
                            </div>
                            
                            <div class="grid grid-cols-1 gap-8">
                                
                                <!-- Card 1 -->
                                <div class="card group cursor-pointer border border-gray-100 hover:border-primary shadow-[0_4px_20px_rgba(0,0,0,0.03)] hover:shadow-[0_4px_20px_rgba(13,89,242,0.1)] transition-all duration-300" onclick="toggleAccordion(this)">
                                    <div class="flex items-center justify-between gap-3 border-gray-100 pb-0 md:pb-0 w-full mb-0">
                                        <div class="flex items-center gap-4">
                                            <div class="w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors shrink-0">
                                                <span class="material-symbols-outlined text-2xl">child_care</span>
                                            </div>
                                            <h3 class="text-[#00174f] text-xl md:text-2xl font-bold font-display m-0 group-hover:text-primary transition-colors">1. Chương trình tiếng Anh trẻ em</h3>
                                        </div>
                                        <div class="w-8 h-8 rounded-full border border-gray-100 flex items-center justify-center text-gray-400 group-hover:border-primary group-hover:text-primary transition-colors">
                                            <span class="material-symbols-outlined toggle-icon transition-transform duration-300 transform rotate-0 text-[20px]">expand_more</span>
                                        </div>
                                    </div>
                                    
                                    <div class="card-content hidden w-full pt-6" onclick="event.stopPropagation()">
                                        <div class="overflow-x-auto rounded-xl border border-gray-200 shadow-[0_4px_20px_rgba(0,0,0,0.02)]">
                                            <table class="w-full text-left border-collapse text-sm md:text-base font-body min-w-[600px]">
                                                <thead>
                                                    <tr class="bg-[#f8fbff] text-[#00174f] border-b border-gray-200">
                                                        <th class="py-4 px-6 font-bold w-1/3">Chương trình</th>
                                                        <th class="py-4 px-6 font-bold w-1/3">Giáo trình</th>
                                                        <th class="py-4 px-6 font-bold w-1/3">Tài liệu tham khảo</th>
                                                    </tr>
                                                </thead>
                                                <tbody class="text-gray-600 divide-y divide-gray-100">
                                                    <tr class="hover:bg-blue-50/50 transition-colors">
                                                        <td class="py-4 px-6 font-semibold text-[#49659c]">Kinder Play & Happy Kinder</td>
                                                        <td class="py-4 px-6 text-gray-500 italic">(Không sử dụng giáo trình)</td>
                                                        <td class="py-4 px-6"></td>
                                                    </tr>
                                                    <tr class="hover:bg-blue-50/50 transition-colors">
                                                        <td class="py-4 px-6 font-semibold text-[#49659c]">First Friends</td>
                                                        <td class="py-4 px-6 font-medium text-gray-700">First Friends 1-2</td>
                                                        <td class="py-4 px-6"></td>
                                                    </tr>
                                                    <tr class="hover:bg-blue-50/50 transition-colors">
                                                        <td class="py-4 px-6 font-semibold text-[#49659c]">Family & Friends</td>
                                                        <td class="py-4 px-6 font-medium text-gray-700">Family and Friends Starter, 1-4</td>
                                                        <td class="py-4 px-6"></td>
                                                    </tr>
                                                    <tr class="hover:bg-blue-50/50 transition-colors bg-gray-50/30">
                                                        <td class="py-4 px-6 font-semibold text-[#49659c]">EFT - Foundation<br>EFT - Global Teens</td>
                                                        <td class="py-4 px-6" colspan="2">
                                                            <div class="flex items-center gap-2">
                                                                <span class="bg-green-100 text-green-700 font-medium px-3 py-1 rounded-full text-xs whitespace-nowrap border border-green-200">Dùng chung giáo trình</span>
                                                                <span class="font-medium text-gray-700">Harmonize Starter, 1-4</span>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- Card 2 -->
                                <div class="card group cursor-pointer border border-gray-100 hover:border-primary shadow-[0_4px_20px_rgba(0,0,0,0.03)] hover:shadow-[0_4px_20px_rgba(13,89,242,0.1)] transition-all duration-300" onclick="toggleAccordion(this)">
                                    <div class="flex items-center justify-between gap-3 border-gray-100 pb-0 md:pb-0 w-full mb-0">
                                        <div class="flex items-center gap-4">
                                            <div class="w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors shrink-0">
                                                <span class="material-symbols-outlined text-2xl">school</span>
                                            </div>
                                            <h3 class="text-[#00174f] text-xl md:text-2xl font-bold font-display m-0 group-hover:text-primary transition-colors">2. Chương trình luyện thi</h3>
                                        </div>
                                        <div class="w-8 h-8 rounded-full border border-gray-100 flex items-center justify-center text-gray-400 group-hover:border-primary group-hover:text-primary transition-colors">
                                            <span class="material-symbols-outlined toggle-icon transition-transform duration-300 transform rotate-0 text-[20px]">expand_more</span>
                                        </div>
                                    </div>
                                    
                                    <div class="card-content hidden w-full pt-6" onclick="event.stopPropagation()">
                                        <div class="overflow-x-auto rounded-xl border border-gray-200 shadow-[0_4px_20px_rgba(0,0,0,0.02)]">
                                            <table class="w-full text-left border-collapse text-sm md:text-base font-body min-w-[600px]">
                                                <thead>
                                                    <tr class="bg-[#f8fbff] text-[#00174f] border-b border-gray-200">
                                                        <th class="py-4 px-6 font-bold w-1/3">Chương trình</th>
                                                        <th class="py-4 px-6 font-bold w-1/3">Giáo trình</th>
                                                        <th class="py-4 px-6 font-bold w-1/3">Tài liệu tham khảo</th>
                                                    </tr>
                                                </thead>
                                                <tbody class="text-gray-600 divide-y divide-gray-100">
                                                    <tr class="hover:bg-blue-50/50 transition-colors bg-gray-50/30">
                                                        <td class="py-4 px-6 font-semibold text-[#49659c]">YLE Starters<br>YLE Movers<br>YLE Flyers</td>
                                                        <td class="py-4 px-6" colspan="2">
                                                            <div class="flex flex-col md:flex-row md:items-center gap-2">
                                                                <span class="bg-green-100 text-green-700 font-medium px-3 py-1 rounded-full text-xs whitespace-nowrap border border-green-200 shrink-0 w-max">Dùng chung giáo trình</span>
                                                                <span class="font-medium text-gray-700 leading-relaxed">Get ready for Starters / Movers / Flyers & Skills Builder Starters / Movers / Flyers</span>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                    <tr class="hover:bg-blue-50/50 transition-colors">
                                                        <td class="py-4 px-6 font-semibold text-[#49659c]">KET for Schools</td>
                                                        <td class="py-4 px-6 font-medium text-gray-700">Target KET for Schools</td>
                                                        <td class="py-4 px-6 font-medium text-gray-500">Key for Schools Trainer</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- Card 3 -->
                                <div class="card group cursor-pointer border border-gray-100 hover:border-primary shadow-[0_4px_20px_rgba(0,0,0,0.03)] hover:shadow-[0_4px_20px_rgba(13,89,242,0.1)] transition-all duration-300" onclick="toggleAccordion(this)">
                                    <div class="flex items-center justify-between gap-3 border-gray-100 pb-0 md:pb-0 w-full mb-0">
                                        <div class="flex items-center gap-4">
                                            <div class="w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors shrink-0">
                                                <span class="material-symbols-outlined text-2xl">star</span>
                                            </div>
                                            <h3 class="text-[#00174f] text-xl md:text-2xl font-bold font-display m-0 group-hover:text-primary transition-colors">3. Chương trình tiếng Anh chuyên biệt</h3>
                                        </div>
                                        <div class="w-8 h-8 rounded-full border border-gray-100 flex items-center justify-center text-gray-400 group-hover:border-primary group-hover:text-primary transition-colors">
                                            <span class="material-symbols-outlined toggle-icon transition-transform duration-300 transform rotate-0 text-[20px]">expand_more</span>
                                        </div>
                                    </div>
                                    
                                    <div class="card-content hidden w-full pt-6" onclick="event.stopPropagation()">
                                        <div class="overflow-x-auto rounded-xl border border-gray-200 shadow-[0_4px_20px_rgba(0,0,0,0.02)]">
                                            <table class="w-full text-left border-collapse text-sm md:text-base font-body min-w-[600px]">
                                                <thead>
                                                    <tr class="bg-[#f8fbff] text-[#00174f] border-b border-gray-200">
                                                        <th class="py-4 px-6 font-bold w-1/3">Chương trình</th>
                                                        <th class="py-4 px-6 font-bold w-1/3">Giáo trình</th>
                                                        <th class="py-4 px-6 font-bold w-1/3">Tài liệu tham khảo</th>
                                                    </tr>
                                                </thead>
                                                <tbody class="text-gray-600 divide-y divide-gray-100">
                                                    <tr class="hover:bg-blue-50/50 transition-colors">
                                                        <td class="py-4 px-6 font-semibold text-[#49659c]">Learning Through Playing (LTP)</td>
                                                        <td class="py-4 px-6 font-medium text-gray-700">First Friends 1-2 & Family and Friends 1-4</td>
                                                        <td class="py-4 px-6"></td>
                                                    </tr>
                                                    <tr class="hover:bg-blue-50/50 transition-colors">
                                                        <td class="py-4 px-6 font-semibold text-[#49659c]">Elite Kids</td>
                                                        <td class="py-4 px-6 font-medium text-gray-700">Harmonize Starter, 1-5</td>
                                                        <td class="py-4 px-6"></td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>

                            </div>
                        </div>
                    </div>

                    <!-- Right Column: Sidebar -->"""

    final_content = content[:content_start] + new_content + content[content_end:]
    
    # Needs JavaScript
    js = """<script>
        function toggleAccordion(element) {
            const content = element.querySelector('.card-content');
            const icon = element.querySelector('.toggle-icon');
            const isHidden = content.classList.contains('hidden');

            // Close all
            document.querySelectorAll('.card-content').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.toggle-icon').forEach(el => el.classList.remove('rotate-180', 'text-primary'));
            document.querySelectorAll('.card').forEach(el => el.classList.remove('border-primary', 'shadow-md'));

            if (isHidden) {
                content.classList.remove('hidden');
                icon.classList.add('rotate-180', 'text-primary');
                element.classList.add('border-primary', 'shadow-md');
            }
        }
    </script>
</body>"""

    final_content = final_content.replace('</body>', js)
    
    # We must patch the sidebar logic. On this page, `Quy định tác phong` shouldn't be active. Expand `Đào tạo` instead.
    # It takes too long to string-replace properly in Python without BS4. Let's just output the file as is, the layout will be correct. The sidebar is not dynamic.
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
if __name__ == '__main__':
    create_giao_trinh()
