import os
import re

DIR_PATH = '/Users/vobac/Downloads/gia-viet-handbook'

# Banner template to inject
BANNER_TEMPLATE = """<!-- Redesigned High-End Banner -->
                        <div
                            class="w-full h-[240px] bg-gradient-to-br {gradient} relative flex items-center justify-center p-8 overflow-hidden z-0 rounded-2xl shadow-md border border-{border_color}/10">
                            <!-- Premium Radial Light Overlay -->
                            <div
                                class="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(255,255,255,0.15),transparent_60%)]">
                            </div>

                            <!-- Pure CSS Elegant Geometric Glassmorphic Shapes -->
                            <div class="absolute -top-12 -left-12 w-48 h-48 rounded-full bg-white/5 blur-2xl"></div>
                            <div class="absolute -bottom-16 -right-16 w-64 h-64 rounded-full bg-white/10 blur-3xl">
                            </div>

                            <div class="relative z-10 flex flex-col items-center text-center">
                                <h2
                                    class="text-white text-2xl md:text-3xl font-black font-display tracking-tight leading-tight px-4 max-w-3xl uppercase">
                                    {title}
                                </h2>
                                <p class="{text_color} text-xs md:text-sm font-body mt-2 max-w-xl opacity-90">{category}</p>
                            </div>
                        </div>"""

PAGES_INFO = {
    # --- Đào tạo & Đảm bảo chất lượng (15 pages) ---
    "tieng-anh-thieu-nhi-thieu-nien.html": {
        "title": "Chương trình tiếng Anh Thiếu nhi - Thiếu niên",
        "category": "Đào tạo & Đảm bảo chất lượng",
        "gradient": "from-[#00174f] via-[#0537a1] to-[#0d59f2]",
        "border_color": "blue-900",
        "text_color": "text-blue-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-2 mb-8">.*?Chương trình tiếng Anh Thiếu nhi - Thiếu niên.*?</div>'
    },
    "flexi-time.html": {
        "title": "Flexi-time English Program",
        "category": "Đào tạo & Đảm bảo chất lượng",
        "gradient": "from-[#00174f] via-[#0537a1] to-[#0d59f2]",
        "border_color": "blue-900",
        "text_color": "text-blue-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-2 mb-8">.*?Flexi-time English Program.*?</div>'
    },
    "chuong-trinh-chuyen-biet.html": {
        "title": "Chương trình chuyên biệt",
        "category": "Đào tạo & Đảm bảo chất lượng",
        "gradient": "from-[#2e0854] via-[#4c1d95] to-[#7c3aed]",
        "border_color": "purple-900",
        "text_color": "text-purple-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-2 mb-8">.*?Chương trình chuyên biệt.*?</div>'
    },
    "du-gio-dong-nghiep.html": {
        "title": "QUY ĐỊNH DỰ GIỜ ĐỒNG NGHIỆP",
        "category": "CHẤT LƯỢNG ĐÀO TẠO / Đào tạo & Đảm bảo chất lượng",
        "gradient": "from-[#0f766e] via-[#0d9488] to-[#14b8a6]",
        "border_color": "teal-900",
        "text_color": "text-teal-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">.*?QUY ĐỊNH DỰ GIỜ ĐỒNG NGHIỆP.*?</div>'
    },
    "chuong-trinh-cop.html": {
        "title": "CHƯƠNG TRÌNH CoP",
        "category": "CHẤT LƯỢNG ĐÀO TẠO / Đào tạo & Đảm bảo chất lượng",
        "gradient": "from-[#0f766e] via-[#0d9488] to-[#14b8a6]",
        "border_color": "teal-900",
        "text_color": "text-teal-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">.*?CHƯƠNG TRÌNH CoP.*?</div>'
    },
    "fast-track-training.html": {
        "title": "CHƯƠNG TRÌNH FAST-TRACK TRAINING",
        "category": "CHẤT LƯỢNG ĐÀO TẠO / Đào tạo & Đảm bảo chất lượng",
        "gradient": "from-[#0f766e] via-[#0d9488] to-[#14b8a6]",
        "border_color": "teal-900",
        "text_color": "text-teal-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">.*?CHƯƠNG TRÌNH FAST-TRACK TRAINING.*?</div>'
    },
    "mentoring-1-1.html": {
        "title": "HOẠT ĐỘNG MENTORING 1-1",
        "category": "CHẤT LƯỢNG ĐÀO TẠO / Đào tạo & Đảm bảo chất lượng",
        "gradient": "from-[#0f766e] via-[#0d9488] to-[#14b8a6]",
        "border_color": "teal-900",
        "text_color": "text-teal-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">.*?HOẠT ĐỘNG MENTORING 1-1.*?</div>'
    },
    "giao-trinh-tai-lieu.html": {
        "title": "GIÁO TRÌNH CHƯƠNG TRÌNH YLE",
        "category": "Quy định & Quy trình giảng dạy / Đào tạo & Đảm bảo chất lượng",
        "gradient": "from-[#1e1b4b] via-[#312e81] to-[#4338ca]",
        "border_color": "indigo-900",
        "text_color": "text-indigo-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-2 mb-10">.*?GIÁO TRÌNH CHƯƠNG TRÌNH YLE.*?</div>'
    },
    "quy-dinh-diem-danh.html": {
        "title": "QUY ĐỊNH ĐIỂM DANH",
        "category": "Quy định & Quy trình giảng dạy / Đào tạo & Đảm bảo chất lượng",
        "gradient": "from-[#1e1b4b] via-[#312e81] to-[#4338ca]",
        "border_color": "indigo-900",
        "text_color": "text-indigo-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-2 mb-10">.*?QUY ĐỊNH ĐIỂM DANH.*?</div>'
    },
    "quy-trinh-giang-day.html": {
        "title": "KHEN THƯỞNG & QUY TRÌNH HỌC THỬ",
        "category": "Quy định & Quy trình giảng dạy / Đào tạo & Đảm bảo chất lượng",
        "gradient": "from-[#064e3b] via-[#047857] to-[#10b981]",
        "border_color": "emerald-900",
        "text_color": "text-emerald-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-2 mb-10">.*?KHEN THƯỞNG & QUY TRÌNH HỌC THỬ.*?</div>'
    },
    "quy-dinh-so-lien-lac.html": {
        "title": "HƯỚNG DẪN VIẾT SỔ LIÊN LẠC",
        "category": "Quy định & Quy trình giảng dạy / Đào tạo & Đảm bảo chất lượng",
        "gradient": "from-[#1e1b4b] via-[#312e81] to-[#4338ca]",
        "border_color": "indigo-900",
        "text_color": "text-indigo-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-3 mb-12 border-b border-gray-100 pb-8">.*?HƯỚNG DẪN VIẾT SỔ LIÊN LẠC.*?</div>'
    },
    "quy-dinh-phu-dao.html": {
        "title": "HƯỚNG DẪN & QUY TRÌNH ĐĂNG KÝ<br>LỚP PHỤ ĐẠO",
        "category": "KIDS & TEENS / Đào tạo & Đảm bảo chất lượng",
        "gradient": "from-[#1e1b4b] via-[#312e81] to-[#4338ca]",
        "border_color": "indigo-900",
        "text_color": "text-indigo-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">.*?HƯỚNG DẪN & QUY TRÌNH ĐĂNG KÝ.*?LỚP PHỤ ĐẠO.*?</div>'
    },
    "chinh-sach-hoc-bong.html": {
        "title": "QUY ĐỊNH MỨC HỌC BỔNG",
        "category": "KIDS & TEENS / Đào tạo & Đảm bảo chất lượng",
        "gradient": "from-[#064e3b] via-[#047857] to-[#10b981]",
        "border_color": "emerald-900",
        "text_color": "text-emerald-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">.*?QUY ĐỊNH MỨC HỌC BỔNG.*?</div>'
    },
    "quy-dinh-khao-thi.html": {
        "title": "QUY ĐỊNH & HƯỚNG DẪN TỔ CHỨC<br>THI CUỐI KHÓA",
        "category": "Quy định & Quy trình giảng dạy / Đào tạo & Đảm bảo chất lượng",
        "gradient": "from-[#1e1b4b] via-[#312e81] to-[#4338ca]",
        "border_color": "indigo-900",
        "text_color": "text-indigo-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">.*?QUY ĐỊNH & HƯỚNG DẪN TỔ CHỨC.*?THI CUỐI KHÓA.*?</div>'
    },
    "quy-dinh-nghi-phep.html": {
        "title": "QUY ĐỊNH XIN NGHỈ PHÉP",
        "category": "KIDS & TEENS (YLE) / Đào tạo & Đảm bảo chất lượng",
        "gradient": "from-[#4c0519] via-[#881337] to-[#be123c]",
        "border_color": "rose-900",
        "text_color": "text-rose-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-3 mb-10 border-b border-gray-100 pb-8">.*?QUY ĐỊNH XIN NGHỈ PHÉP.*?</div>'
    },
    
    # --- Tổ chức & Nhân sự (5 pages) ---
    "quy-dinh-tac-phong.html": {
        "title": "Quy định tác phong",
        "category": "Tổ chức & Nhân sự",
        "gradient": "from-[#00174f] via-[#0537a1] to-[#0d59f2]",
        "border_color": "blue-900",
        "text_color": "text-blue-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-2 mb-10">.*?Quy định tác phong.*?</div>'
    },
    "quy-trinh-tiep-nhan-giao-vien-moi.html": {
        "title": "Quy trình tiếp nhận giáo viên mới",
        "category": "Tổ chức & Nhân sự",
        "gradient": "from-[#00174f] via-[#0537a1] to-[#0d59f2]",
        "border_color": "blue-900",
        "text_color": "text-blue-100",
        "restructure": False,
        "old_header_pat": r'<!-- Redesigned High-End Banner -->.*?</div>\s*</div>'
    },
    "quy-trinh-xin-ngung-cong-tac.html": {
        "title": "Quy trình giáo viên xin ngưng công tác",
        "category": "Tổ chức & Nhân sự",
        "gradient": "from-[#4c0519] via-[#881337] to-[#be123c]",
        "border_color": "rose-900",
        "text_color": "text-rose-100",
        "restructure": False,
        "old_header_pat": r'<!-- Redesigned High-End Banner.*?-->.*?</div>\s*</div>'
    },
    "quy-trinh-cham-cong-tinh-luong.html": {
        "title": "Quy trình chấm công & tính lương giảng dạy",
        "category": "Tổ chức & Nhân sự",
        "gradient": "from-[#064e3b] via-[#047857] to-[#10b981]",
        "border_color": "emerald-900",
        "text_color": "text-emerald-100",
        "restructure": False,
        "old_header_pat": r'<!-- Redesigned High-End Banner.*?-->.*?</div>\s*</div>'
    },
    "nhan-su-phu-trach.html": {
        "title": "Nhân sự phụ trách & Liên hệ",
        "category": "Tổ chức & Nhân sự",
        "gradient": "from-[#00174f] via-[#0537a1] to-[#0d59f2]",
        "border_color": "blue-900",
        "text_color": "text-blue-100",
        "restructure": False,
        "old_header_pat": r'<!-- Redesigned High-End Banner -->.*?</div>\s*</div>'
    },

    # --- Chính sách & Phúc lợi (2 pages) ---
    "chinh-sach-ho-tro-khac.html": {
        "title": "Chính sách hỗ trợ khác",
        "category": "Chính sách & Phúc lợi",
        "gradient": "from-[#00174f] via-[#0537a1] to-[#0d59f2]",
        "border_color": "blue-900",
        "text_color": "text-blue-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-[23] mb-10">.*?Chính sách hỗ trợ khác.*?</div>'
    },
    "dai-ngo-giao-vien.html": {
        "title": "Đãi ngộ Giáo viên Gia Việt",
        "category": "Chính sách & Phúc lợi",
        "gradient": "from-[#00174f] via-[#0537a1] to-[#0d59f2]",
        "border_color": "blue-900",
        "text_color": "text-blue-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-2 mb-10">.*?Đãi ngộ Giáo viên Gia Việt.*?</div>'
    },
    "gop-y-phan-hoi.html": {
        "title": "Kênh nhận góp ý & phản hồi",
        "category": "Hệ thống & Hỗ trợ",
        "gradient": "from-[#1d4ed8] via-[#3b82f6] to-[#60a5fa]",
        "border_color": "blue-900",
        "text_color": "text-blue-100",
        "restructure": True,
        "old_header_pat": r'<div class="flex flex-col gap-2 mb-10">.*?Kênh nhận góp ý & phản hồi.*?</div>'
    }
}

def process_file(filename, info):
    filepath = os.path.join(DIR_PATH, filename)
    if not os.path.exists(filepath):
        print(f"File {filename} does not exist. Skipping.")
        return False
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Remove old header if not restructured yet
    content_no_header = content
    if "<!-- Redesigned High-End Banner" not in content:
        content_no_header = re.sub(info["old_header_pat"], "", content, flags=re.DOTALL)
        if content == content_no_header:
            # Loose fallback search for old header
            match = re.search(r'<div class="flex flex-col gap-[23] mb-(?:8|10|12)(?: border-b border-gray-100 pb-8)?">.*?</h2>(.*?</h3>)?\s*</div>', content, flags=re.DOTALL)
            if match:
                content_no_header = content.replace(match.group(0), "")
                print(f"Loose match succeeded for {filename}!")

    # 2. Update existing banner block if already present
    banner_match = re.search(r'(<!-- Redesigned High-End Banner.*?-->\s*<div\s+class="w-full h-\[240px\].*?</div>\s*</div>)', content_no_header, re.DOTALL)
    if banner_match:
        # Construct updated banner HTML
        banner_html = BANNER_TEMPLATE.format(
            title=info["title"],
            category=info["category"],
            gradient=info["gradient"],
            text_color=info["text_color"],
            border_color=info["border_color"]
        )
        restructured = content_no_header.replace(banner_match.group(1), banner_html)
    else:
        restructured = content_no_header

    # 3. Restructure layout container if requested
    if info.get("restructure", False) and "<!-- Main Content Card -->" not in restructured:
        # Replace Left Column container opening tag
        container_pat = r'(<!-- Left Column: Content -->\s*<div\s+class="w-full md:w-\[70%\] lg:w-\[75%\])[^"]*overflow-hidden[^"]*">'
        new_container = r'\1 font-body text-gray-800 leading-relaxed space-y-8">'
        restructured_layout = re.sub(container_pat, new_container, restructured)
        
        if restructured_layout != restructured:
            restructured = restructured_layout
            
            # Wrap the padding div that follows immediately
            container_pattern = r'(<!-- Left Column: Content -->\s*<div[^>]*>)'
            match_container = re.search(container_pattern, restructured)
            if match_container:
                rest_of_content = restructured[match_container.end():]
                # Look for the padding div after the banner ends
                padding_pat = r'(</div>\s*</div>\s*)<div class="(p-6 md:p-[^"]*)">'
                match_padding = re.search(padding_pat, rest_of_content)
                if match_padding:
                    old_block = match_padding.group(0)
                    new_block = f"{match_padding.group(1)}<!-- Main Content Card -->\n                        <div class=\"bg-white rounded-2xl shadow-sm border border-gray-100/50 {match_padding.group(2)}\">"
                    rest_of_content = rest_of_content.replace(old_block, new_block, 1)
                    restructured = restructured[:match_container.end()] + rest_of_content
                else:
                    # Alternative search: find first padding div directly
                    padding_pat_direct = r'^(\s*)<div class="(p-6 md:p-[^"]*)">'
                    match_padding_direct = re.search(padding_pat_direct, rest_of_content, re.MULTILINE)
                    if match_padding_direct:
                        indent = match_padding_direct.group(1)
                        padding_class = match_padding_direct.group(2)
                        old_div = match_padding_direct.group(0)
                        new_div = f"{indent}<!-- Main Content Card -->\n{indent}<div class=\"bg-white rounded-2xl shadow-sm border border-gray-100/50 {padding_class}\">"
                        rest_of_content = rest_of_content.replace(old_div, new_div, 1)
                        restructured = restructured[:match_container.end()] + rest_of_content
                    else:
                        print(f"Warning: Could not find padding div to wrap in {filename}")

    # 4. Inject banner from scratch if not present at all
    if "<!-- Redesigned High-End Banner" not in content_no_header:
        # First restructure container if requested
        if info.get("restructure", False):
            container_pat = r'(<!-- Left Column: Content -->\s*<div\s+class="w-full md:w-\[70%\] lg:w-\[75%\])[^"]*overflow-hidden[^"]*">'
            new_container = r'\1 font-body text-gray-800 leading-relaxed space-y-8">'
            restructured = re.sub(container_pat, new_container, restructured)
            
        # Find container tag
        container_pattern = r'(<!-- Left Column: Content -->\s*<div[^>]*>)'
        match_container = re.search(container_pattern, restructured)
        if not match_container:
            print(f"Failed to find Left Column container div in {filename}!")
            return False
            
        container_tag = match_container.group(1)
        
        # Construct banner HTML
        banner_html = BANNER_TEMPLATE.format(
            title=info["title"],
            category=info["category"],
            gradient=info["gradient"],
            text_color=info["text_color"],
            border_color=info["border_color"]
        )
        
        # Wrap padding div
        rest_of_content = restructured[match_container.end():]
        if info.get("restructure", False):
            padding_pat = r'^(\s*)<div class="(p-6 md:p-[^"]*)">'
            match_padding = re.search(padding_pat, rest_of_content, re.MULTILINE)
            if match_padding:
                indent = match_padding.group(1)
                padding_class = match_padding.group(2)
                old_div = match_padding.group(0)
                new_div = f"{indent}<!-- Main Content Card -->\n{indent}<div class=\"bg-white rounded-2xl shadow-sm border border-gray-100/50 {padding_class}\">"
                rest_of_content = rest_of_content.replace(old_div, new_div, 1)
                
        restructured = restructured[:match_container.end()] + f"\n                        {banner_html}\n" + rest_of_content

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(restructured)
        
    print(f"Successfully processed {filename}")
    return True

if __name__ == "__main__":
    success_count = 0
    for filename, info in PAGES_INFO.items():
        if process_file(filename, info):
            success_count += 1
    print(f"\nCompleted: Added banners and restructured {success_count}/{len(PAGES_INFO)} files successfully.")
