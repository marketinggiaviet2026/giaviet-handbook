import sys

def main():
    filepath = '/Users/vobac/Downloads/gia-viet-handbook/ve-gia-viet.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The block to replace
    start_str = '<div class="p-6 md:p-8 text-[#49659c] text-lg leading-relaxed space-y-6 text-justify font-body">'
    end_str = '</div>\n            </div>\n\n            <!-- Right Column: Sidebar -->'
    
    if start_str not in content or end_str not in content:
        print("Could not find the target block.")
        return

    # Construct the new HTML
    cards_data = [
        {
            "title": "Thành lập",
            "icon": "event",
            "body": "<p class='font-medium text-gray-700'>29/12/2009</p>"
        },
        {
            "title": "Sứ mệnh",
            "icon": "my_location",
            "body": "<p class='font-medium text-gray-700'>Xây dựng môi trường giáo dục tiếng Anh chất lượng, nhân văn & bền vững.</p>"
        },
        {
            "title": "Hành trình phát triển",
            "icon": "timeline",
            "body": "<ul class='list-disc pl-5 mt-2 space-y-1.5 text-gray-600'><li>Hơn 16 năm hoạt động</li><li>Kiên định định hướng lấy con người làm trung tâm</li><li>Xây dựng uy tín từ chất lượng & giá trị giáo dục</li></ul>"
        },
        {
            "title": "Hệ thống cơ sở",
            "icon": "domain",
            "body": "<ul class='list-disc pl-5 mt-2 space-y-1.5 text-gray-600'><li>Trụ sở chính: 39 Mậu Thân</li><li>Chi nhánh: 30/4, Bình Minh, Ô Môn (từ 09/2025)</li><li>Nhà học Đinh Công Tráng</li></ul>"
        },
        {
            "title": "Hệ sinh thái giáo dục",
            "icon": "hub",
            "body": "<ul class='list-disc pl-5 mt-2 space-y-1.5 text-gray-600'><li>4Cs Café</li><li>Văn phòng Tư vấn Du học & Visa</li></ul><p class='mt-3 text-primary font-medium flex items-center gap-1'><span class='material-symbols-outlined text-[18px]'>arrow_right_alt</span> Mở rộng trải nghiệm & kết nối cộng đồng</p>"
        },
        {
            "title": "Quy mô đào tạo",
            "icon": "school",
            "body": "<ul class='list-disc pl-5 mt-2 space-y-1.5 text-gray-600'><li>Hàng ngàn học viên mỗi năm</li><li>Đa dạng độ tuổi: Mầm non – Thiếu nhi – Thiếu niên – Người lớn</li></ul>"
        },
        {
            "title": "Đội ngũ",
            "icon": "diversity_3",
            "body": "<ul class='list-disc pl-5 mt-2 space-y-1.5 text-gray-600'><li>~30 nhân sự vận hành & chuyên môn</li><li>~60 giáo viên trong & ngoài nước</li><li>Tuyển chọn & đào tạo theo tiêu chuẩn rõ ràng</li></ul>"
        },
        {
            "title": "Văn hoá nội bộ",
            "icon": "auto_awesome",
            "body": "<ul class='list-disc pl-5 mt-2 space-y-1.5 text-gray-600'><li>Môi trường làm việc nhân văn, tôn trọng & phát triển lâu dài</li><li>Giá trị tích cực lan tỏa từ giáo viên đến học viên</li></ul>"
        },
        {
            "title": "Cam kết",
            "icon": "verified",
            "body": "<ul class='list-disc pl-5 mt-2 space-y-1.5 text-gray-600'><li>Mang đến môi trường học tập thân thiện, an toàn</li><li>Lan tỏa yêu thương & hạnh phúc trong hành trình học tập</li></ul>"
        }
    ]

    html_cards = '<div class="p-6 md:p-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-4 lg:gap-6 font-body">\n'
    # Wait, the column is 75% width. So lg:grid-cols-3 might be a bit tight, but md:grid-cols-2 or lg:grid-cols-2 is better.
    # Actually, lg:grid-cols-2 looks great since the container is 75%, allowing cards enough width for long titles/contents.
    
    for idx, card in enumerate(cards_data):
        html_cards += f"""
        <div class="bg-white rounded-xl border border-gray-100/80 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300 p-6 flex flex-col gap-2 cursor-pointer group" onclick="toggleGVCard(this)">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 rounded-full bg-blue-50 text-primary flex items-center justify-center flex-shrink-0 group-hover:scale-110 group-hover:bg-primary group-hover:text-white transition-all duration-300">
                        <span class="material-symbols-outlined text-2xl">{card['icon']}</span>
                    </div>
                    <h3 class="text-xl font-bold font-display text-[#00174f] group-hover:text-primary transition-colors">{card['title']}</h3>
                </div>
                <div class="w-8 h-8 rounded-full border border-gray-100 flex items-center justify-center text-gray-400 group-hover:border-primary group-hover:text-primary transition-colors">
                    <span class="material-symbols-outlined text-[20px] expand-icon transition-transform duration-300">add</span>
                </div>
            </div>
            
            <div class="gv-card-content overflow-hidden transition-all duration-500 max-h-0 opacity-0 pl-[4rem]">
                <div class="pt-2 pb-1">
                    {card['body']}
                </div>
            </div>
        </div>
        """

    html_cards += '</div>'

    # The javascript for toggle GV card
    script_to_add = """
    <script>
        function toggleGVCard(element) {
            // Check if this card is currently active
            const content = element.querySelector('.gv-card-content');
            const icon = element.querySelector('.expand-icon');
            const isActive = element.classList.contains('ring-1');
            
            // First, close all other cards
            document.querySelectorAll('.gv-card-content').forEach(el => {
                el.style.maxHeight = '0px';
                el.style.opacity = '0';
                el.parentElement.classList.remove('ring-1', 'ring-primary', 'shadow-md');
                el.parentElement.querySelector('.expand-icon').textContent = 'add';
                el.parentElement.querySelector('.expand-icon').style.transform = 'rotate(0deg)';
                el.parentElement.querySelector('h3').classList.remove('text-primary');
            });
            
            // If it wasn't active, activate it
            if (!isActive) {
                element.classList.add('ring-1', 'ring-primary', 'shadow-md');
                content.style.maxHeight = content.scrollHeight + 40 + 'px';
                content.style.opacity = '1';
                icon.textContent = 'remove';
                icon.style.transform = 'rotate(180deg)';
                element.querySelector('h3').classList.add('text-primary');
            }
        }
    </script>
    """

    # Add the script to the end of the content before </body>
    if "function toggleGVCard" not in content:
        content = content.replace("</body>", script_to_add + "\n</body>")

    # Replace the text block
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    
    new_content = content[:start_idx] + html_cards + "\n" + content[end_idx:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Updated successfully!")

if __name__ == '__main__':
    main()
