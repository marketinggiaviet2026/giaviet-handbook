import os
import re

html_to_insert = """                                        <div>
                                             <h4 class="text-[#00174f] dark:text-gray-100 text-base font-bold font-display mb-3 border-b border-gray-100 dark:border-gray-700 pb-2">Chương trình chuyên biệt</h4>
                                             <ul class="flex flex-col gap-2.5">
                                                 <li><a href="#" class="text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-primary transition-colors">Learning Through Playing (LTP)</a></li>
                                                 <li><a href="#" class="text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-primary transition-colors">Elite Kids</a></li>
                                             </ul>
                                        </div>"""

directory = '/Users/vobac/Downloads/gia-viet-handbook'

# Regex pattern to find the end of the "Chương trình Đào tạo" block
# We look for the </div> closing that block, and insert our new block after it.
# The block is:
# <div>
#   <h4 ...>Chương trình Đào tạo</h4>
#   <ul ...>...</ul>
# </div>
# Then comes:
# <div>
#   <h4 ...>Đảm bảo chất lượng</h4>

pattern = re.compile(
    r'(<h4[^>]*>Chương trình Đào tạo</h4>\s*<ul[^>]*>.*?</ul>\s*</div>)',
    re.DOTALL
)

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Check if already added
        if "Chương trình chuyên biệt" in content:
            continue
            
        def replacement(match):
            return match.group(1) + "\n" + html_to_insert
            
        new_content, count = pattern.subn(replacement, content)
        
        if count > 0:
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"Could not find target block in {filename}")
