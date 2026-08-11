import os
import re

file_categories = {
    # Trang chủ
    'index.html': 'nav-trang-chu',
    
    # Về Gia Việt
    've-gia-viet.html': 'nav-ve-gia-viet',
    
    # Tổ chức & Nhân sự
    'to-chuc-nhan-su.html': 'nav-to-chuc',
    'quy-trinh-tiep-nhan-giao-vien-moi.html': 'nav-to-chuc',
    'quy-trinh-xin-ngung-cong-tac.html': 'nav-to-chuc',
    'quy-trinh-cham-cong-tinh-luong.html': 'nav-to-chuc',
    'nhan-su-phu-trach.html': 'nav-to-chuc',
    'quy-dinh-tac-phong.html': 'nav-to-chuc',
    
    # Chính sách & Phúc lợi
    'chinh-sach-phuc-loi.html': 'nav-chinh-sach',
    'che-do-luong-thuong.html': 'nav-chinh-sach',
    'dai-ngo-giao-vien.html': 'nav-chinh-sach',
    'chinh-sach-ho-tro-khac.html': 'nav-chinh-sach',
    
    # Đào tạo & Đảm bảo chất lượng
    'dao-tao-dam-bao-chat-luong.html': 'nav-dao-tao',
    'tieng-anh-thieu-nhi-thieu-nien.html': 'nav-dao-tao',
    'flexi-time.html': 'nav-dao-tao',
    'chuong-trinh-chuyen-biet.html': 'nav-dao-tao',
    'du-gio-dong-nghiep.html': 'nav-dao-tao',
    'cpd.html': 'nav-dao-tao',
    'chuong-trinh-cop.html': 'nav-dao-tao',
    'fast-track-training.html': 'nav-dao-tao',
    'mentoring-1-1.html': 'nav-dao-tao',
    'giao-trinh-tai-lieu.html': 'nav-dao-tao',
    'quy-dinh-diem-danh.html': 'nav-dao-tao',
    'quy-trinh-giang-day.html': 'nav-dao-tao',
    'quy-dinh-so-lien-lac.html': 'nav-dao-tao',
    'quy-dinh-phu-dao.html': 'nav-dao-tao',
    'chinh-sach-hoc-bong.html': 'nav-dao-tao',
    'quy-dinh-khao-thi.html': 'nav-dao-tao',
    'quy-dinh-nghi-phep.html': 'nav-dao-tao',
    
    # Hệ thống & Hỗ trợ
    'he-thong-ho-tro.html': 'nav-he-thong',
    'app-gia-viet.html': 'nav-he-thong',
    'quy-dinh-in-an.html': 'nav-he-thong',
    'gop-y-phan-hoi.html': 'nav-he-thong'
}

def update_nav_class(content, nav_id, is_active):
    pattern = rf'(<a\s+[^>]*id="{nav_id}"[^>]*>)'
    
    dropdowns = ['nav-to-chuc', 'nav-chinh-sach', 'nav-dao-tao', 'nav-he-thong']
    is_dropdown = nav_id in dropdowns
    
    if is_active:
        if is_dropdown:
            new_class = 'text-primary text-sm font-bold border-b-2 border-primary pb-0.5 whitespace-nowrap flex items-center gap-1 cursor-pointer'
        else:
            new_class = 'text-primary text-sm font-bold border-b-2 border-primary pb-0.5 whitespace-nowrap'
    else:
        if is_dropdown:
            new_class = 'text-[#0d121c] dark:text-gray-300 text-sm font-medium hover:text-primary transition-colors whitespace-nowrap flex items-center gap-1 cursor-pointer'
        else:
            new_class = 'text-[#0d121c] dark:text-gray-300 text-sm font-medium hover:text-primary transition-colors whitespace-nowrap'

    def repl(match):
        tag = match.group(1)
        # Replace class attribute inside tag (supporting newlines/spaces inside class attribute)
        tag = re.sub(r'class="[^"]*"', f'class="{new_class}"', tag, flags=re.DOTALL)
        tag = re.sub(r"class='[^']*'", f'class="{new_class}"', tag, flags=re.DOTALL)
        return tag

    return re.sub(pattern, repl, content, flags=re.DOTALL)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    nav_ids = ['nav-trang-chu', 'nav-ve-gia-viet', 'nav-to-chuc', 'nav-chinh-sach', 'nav-dao-tao', 'nav-he-thong']
    
    fixed_count = 0
    for filename, correct_active_id in file_categories.items():
        file_path = os.path.join(base_dir, filename)
        if not os.path.exists(file_path):
            print(f"Skipping {filename} (does not exist)")
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            continue
            
        new_content = content
        for nav_id in nav_ids:
            is_active = (nav_id == correct_active_id)
            new_content = update_nav_class(new_content, nav_id, is_active)
            
        if new_content != content:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed navigation highlight in {filename} (active: {correct_active_id})")
                fixed_count += 1
            except Exception as e:
                print(f"Error writing to {filename}: {e}")
        else:
            print(f"Highlights already correct in {filename}")
            
    print(f"\nCompleted. Fixed highlights in {fixed_count} files.")
