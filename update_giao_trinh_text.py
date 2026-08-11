def update_giao_trinh():
    filepath = '/Users/vobac/Downloads/gia-viet-handbook/giao-trinh-tai-lieu.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Title replacements
    content = content.replace('GIÁO TRÌNH CHƯƠNG TRÌNH YLE', 'GIÁO TRÌNH CHƯƠNG TRÌNH TIẾNG ANH THIẾU NHI - THIẾU NIÊN')
    content = content.replace('1. Chương trình tiếng Anh trẻ em', '1. Tiếng Anh Thiếu nhi - Thiếu niên')
    content = content.replace('2. Chương trình luyện thi', '2. Chương trình Luyện thi')
    content = content.replace('3. Chương trình tiếng Anh chuyên biệt', '3. Chương trình Chuyên biệt')

    # Content replacements for Card 1
    content = content.replace('(Không sử dụng giáo trình)', 'Không sử dụng giáo trình')
    content = content.replace('Family and Friends Starter, 1-4', 'Family and Friends Starter, Family and Friends 1-4')
    content = content.replace('Harmonize Starter, 1-4', 'Harmonize Starter, Harmonize 1-4')

    # Content replacements for Card 2
    # The current card 2 already matches perfectly with the user's new request, except the title which was replaced above.

    # Content replacements for Card 3
    content = content.replace('Harmonize Starter, 1-5', 'Harmonize Starter, Harmonize 1-5')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated text in giao-trinh-tai-lieu.html")

if __name__ == '__main__':
    update_giao_trinh()
