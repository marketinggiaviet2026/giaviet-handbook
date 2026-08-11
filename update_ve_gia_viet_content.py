import sys

def main():
    filepath = '/Users/vobac/Downloads/gia-viet-handbook/ve-gia-viet.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 16 -> 17 years
    content = content.replace(
        "<li>Hơn 16 năm hoạt động</li>",
        "<li>Hơn 17 năm hoạt động</li>"
    )

    # 2. Hệ thống cơ sở
    content = content.replace(
        "<ul class='list-disc pl-5 mt-2 space-y-1.5 text-gray-600'><li>Trụ sở chính: 39 Mậu Thân</li><li>Chi nhánh: 30/4, Bình Minh, Ô Môn (từ 09/2025)</li><li>Nhà học Đinh Công Tráng</li></ul>",
        "<ul class='list-disc pl-5 mt-2 space-y-1.5 text-gray-600'><li>Trụ sở chính: Số 39, đường Mậu Thân, phường Ninh Kiều, TP. Cần Thơ</li><li>Chi nhánh 30/4: Số 545, đường 30 Tháng 4, phường Tân An, TP. Cần Thơ</li><li>Chi nhánh Bình Minh: Số 112-114, đường Lê Văn Vị, khóm 2, phường Cái Vồn, tỉnh Vĩnh Long</li><li>Chi nhánh Ô Môn: Số 21, đường Trần Nguyên Hãn, phường Ô Môn, TP. Cần Thơ</li><li>Nhà học Đinh Công Tráng: Số 9/9A, đường Đinh Công Tráng, phường Ninh Kiều, TP. Cần Thơ</li></ul>"
    )

    # 3. Hệ sinh thái giáo dục
    content = content.replace(
        "<ul class='list-disc pl-5 mt-2 space-y-1.5 text-gray-600'><li>4Cs Café</li><li>Văn phòng Tư vấn Du học & Visa</li></ul>",
        "<ul class='list-disc pl-5 mt-2 space-y-1.5 text-gray-600'><li>4Cs Café: Số 80, đường Mậu Thân, phường Ninh Kiều, TP. Cần Thơ</li><li>Văn phòng Tư vấn Du học & Visa: Tầng 2 - Toà nhà Trụ sở chính Gia Việt</li></ul>"
    )

    # 4. Đội ngũ
    content = content.replace(
        "<ul class='list-disc pl-5 mt-2 space-y-1.5 text-gray-600'><li>~30 nhân sự vận hành & chuyên môn</li><li>~60 giáo viên trong & ngoài nước</li><li>Tuyển chọn & đào tạo theo tiêu chuẩn rõ ràng</li></ul>",
        "<ul class='list-disc pl-5 mt-2 space-y-1.5 text-gray-600'><li>60+ nhân sự vận hành & chuyên môn</li><li>200+ giáo viên trong & ngoài nước</li><li>Tuyển chọn & đào tạo theo tiêu chuẩn rõ ràng</li></ul>"
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Updated successfully!")

if __name__ == '__main__':
    main()
