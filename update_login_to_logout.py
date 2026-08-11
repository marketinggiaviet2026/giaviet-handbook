import os
import glob
import re

def update_button_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    # Look for the "Đăng nhập" button in the header
    # Match button tags with class containing bg-primary and containing "Đăng nhập"
    button_pattern = re.compile(
        r'(<button[^>]*class="[^"]*flex[^"]*bg-primary[^"]*"[^>]*>\s*<span class="truncate">)Đăng nhập(</span>\s*</button>)',
        re.DOTALL
    )

    def replace_button(match):
        button_start = match.group(1)
        button_end = match.group(2)
        
        # Check if onclick is already present (e.g. if script is re-run)
        if 'onclick' in button_start:
            return match.group(0)

        onclick_attr = (
            ' onclick="localStorage.removeItem(\'gv_auth_token\'); '
            'const currentUrl = encodeURIComponent(window.location.protocol === \'file:\' ? window.location.href : window.location.pathname + window.location.search); '
            'window.location.href = (window.location.protocol === \'file:\' ? \'login.html\' : \'/login.html\') + \'?redirect=\' + currentUrl;"'
        )
        
        if button_start.startswith('<button'):
            new_start = button_start.replace('<button', '<button' + onclick_attr, 1)
            return new_start + 'Đăng xuất' + button_end
        return match.group(0)

    new_content, count = button_pattern.subn(replace_button, content)

    if count > 0:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated header button in {os.path.basename(file_path)}: replaced {count} button(s) with 'Đăng xuất'.")
        except Exception as e:
            print(f"Error writing to {file_path}: {e}")
    else:
        # Check if already updated (for safety/logging)
        if 'Đăng xuất' in content and 'gv_auth_token' in content and 'onclick' in content:
            print(f"Skipping {os.path.basename(file_path)}, button already updated to 'Đăng xuất'.")
        else:
            print(f"No matching header button found in {os.path.basename(file_path)}.")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)
    
    count = 0
    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename in ["login.html"]:
            continue
        update_button_in_file(file_path)
        count += 1
        
    print(f"\nFinished updating {count} files.")
