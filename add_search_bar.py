import os
import glob
import re

css_to_add = """
        /* From Uiverse.io by vinodjangid07 */ 
        .InputContainer {
          width: 210px;
          height: 40px;
          display: flex;
          align-items: center;
          justify-content: center;
          background: linear-gradient(to bottom,rgb(227, 213, 255),rgb(255, 231, 231));
          border-radius: 30px;
          overflow: hidden;
          cursor: text;
          box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.075);
        }

        .input {
          width: 200px;
          height: 36px;
          border: none;
          outline: none;
          caret-color: rgb(255, 81, 0);
          background-color: rgb(255, 255, 255);
          border-radius: 30px;
          padding-left: 15px;
          letter-spacing: 0.8px;
          color: rgb(19, 19, 19);
          font-size: 13.4px;
        }
"""

html_to_add = """
<!-- From Uiverse.io by vinodjangid07 --> 
<div class="InputContainer ml-2 hidden md:flex">
  <input placeholder="Tìm kiếm..." id="input" class="input" name="text" type="text" autocomplete="off">
</div>
"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    
    # Add CSS inside <style>
    if 'class="InputContainer"' not in content:
        if '</style>' in content:
            content = content.replace('</style>', css_to_add + '\n    </style>', 1)
        
        # Add HTML before the login button
        btn_pattern = re.compile(r'(<button class="flex cursor-pointer[^>]*>.*?Đăng nhập.*?<\/button>)', re.DOTALL)
        if btn_pattern.search(content):
            content = btn_pattern.sub(html_to_add + r'\n\1', content)
            modified = True
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

html_files = glob.glob('/Users/vobac/Downloads/gia-viet-handbook/*.html')
for f in html_files:
    process_file(f)
print("All files processed!")
