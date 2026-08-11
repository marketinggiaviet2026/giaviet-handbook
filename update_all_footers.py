import os
import re

footer_html = """<footer class="w-full bg-[#0d59f2] text-white py-12">
<div class="w-full flex justify-center">
<div class="w-full max-w-[1280px] px-4 md:px-10">
<div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 mb-8 w-full">
<div class="lg:col-span-4">
<div class="flex items-center gap-2 mb-4">
<h3 class="text-xl font-bold font-display whitespace-nowrap">Gia Viet English Language Center</h3>
</div>
<p class="text-blue-100 text-sm leading-relaxed font-body">
                                    Tiếng Anh và sự tự tin vươn ra thế giới.
                                </p>
</div>
<div class="lg:col-span-2">
<h4 class="font-bold text-lg mb-4 font-display">Về chúng tôi</h4>
<ul class="space-y-2 text-blue-100 text-sm font-body">
<li><a class="hover:text-white transition-colors" href="ve-gia-viet.html">Về Gia Việt</a></li>
<li><a class="hover:text-white transition-colors" href="quy-dinh-tac-phong.html">Quy định tác phong</a></li>
<li><a class="hover:text-white transition-colors" href="che-do-luong-thuong.html">Chế độ lương - Thưởng</a></li>
<li><a class="hover:text-white transition-colors" href="dai-ngo-giao-vien.html">Đãi ngộ giáo viên</a></li>
</ul>
</div>
<div class="lg:col-span-3">
                                <h4 class="font-bold text-lg mb-4 font-display">Chương trình đào tạo</h4>
<ul class="space-y-2 text-blue-100 text-sm font-body">
<li><a class="hover:text-white transition-colors" href="tieng-anh-thieu-nhi-thieu-nien.html">Tiếng Anh Thiếu nhi - Thiếu niên</a></li>
<li><a class="hover:text-white transition-colors" href="#">Tiếng Anh Người lớn</a></li>
<li><a class="hover:text-white transition-colors" href="#">Flexi-time English Program</a></li>
<li><a class="hover:text-white transition-colors" href="#">Elite Kids Program</a></li>
<li><a class="hover:text-white transition-colors" href="#">Liên kết đào tạo</a></li>
</ul>
</div>
<div class="lg:col-span-3">
                                <h4 class="font-bold text-lg mb-4 font-display">Liên hệ</h4>
<ul class="space-y-2 text-blue-100 text-sm font-body">
<li class="flex items-start gap-2">
<span class="material-symbols-outlined text-sm mt-0.5">location_on</span>
<span>Trụ sở chính: Số 39, Đường Mậu Thân, Phường Ninh Kiều, Thành phố Cần Thơ</span>
</li>
<li class="flex items-center gap-2">
<span class="material-symbols-outlined text-sm">call</span>
<span>0292 383 1000</span>
</li>
<li class="flex items-center gap-2">
<span class="material-symbols-outlined text-sm">mail</span>
<span>info@giaviet.edu.vn</span>
</li>
</ul>
</div>
</div>
<div class="border-t border-blue-400/30 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
<p class="text-blue-200 text-sm font-body">© 2026 Gia Viet English Center. All rights reserved.</p>
<div class="flex gap-4 font-body">
<a class="text-blue-200 hover:text-white transition-colors" href="https://www.facebook.com/giavietcenter" target="_blank">Facebook</a>
<a class="text-blue-200 hover:text-white transition-colors" href="https://youtube.com/@trungtamanhngugiaviet?si=iZlHr2h5nTGlV0TS" target="_blank">Youtube</a>
<a class="text-blue-200 hover:text-white transition-colors" href="https://giaviet.edu.vn/" target="_blank">Website</a>
</div>
</div>
</div>
</div>
</footer>"""

directory = '/Users/vobac/Downloads/gia-viet-handbook'

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Replace the existing footer
        # We find everything from <footer to </footer>
        new_content = re.sub(r'<footer\b[^>]*>.*?</footer>', footer_html, content, flags=re.DOTALL)
        
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filename}")
