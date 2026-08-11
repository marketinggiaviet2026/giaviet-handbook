import os
import glob
import re

AUTH_SCRIPT = """
    <!-- Authentication Check -->
    <script>
        (function() {
            if (localStorage.getItem('gv_auth_token') !== 'giaviet_v1') {
                let isLocal = window.location.protocol === 'file:';
                let loginPath = '/login.html';
                
                if (isLocal) {
                    let parts = window.location.pathname.split('/');
                    let baseIndex = parts.indexOf('gia-viet-handbook');
                    if (baseIndex !== -1) {
                        let depth = parts.length - baseIndex - 2;
                        loginPath = (depth > 0 ? '../'.repeat(depth) : './') + 'login.html';
                    } else {
                        loginPath = 'login.html';
                    }
                } else {
                    // Check depth by counting slashes after root to handle subdirectories on Vercel
                    let pathDepth = window.location.pathname.replace(/^\\/|\\/$/g, '').split('/').length;
                    if (window.location.pathname === '/' || window.location.pathname === '') pathDepth = 0;
                    
                    if (pathDepth > 0 && !window.location.pathname.endsWith('.html')) {
                        loginPath = '../'.repeat(pathDepth) + 'login.html';
                    } else if (pathDepth > 1) {
                         loginPath = '../'.repeat(pathDepth - 1) + 'login.html';
                    } else {
                        loginPath = '/login.html';
                    }
                }
                
                const currentUrl = encodeURIComponent(isLocal ? window.location.href : window.location.pathname + window.location.search);
                window.location.replace(loginPath + '?redirect=' + currentUrl);
            }
        })();
    </script>
"""

def add_auth_to_html(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    # Check if already has auth script
    if "gv_auth_token" in content and "loginPath" in content:
        print(f"Skipping {file_path}, already has auth script.")
        return

    # Find <head> and insert script
    head_tag = '<head>'
    
    # We want to insert right after <head> or <head ...>
    if head_tag in content:
        new_content = content.replace(head_tag, head_tag + AUTH_SCRIPT)
    else:
        new_content = re.sub(r'(<head[^>]*>)', r'\1' + AUTH_SCRIPT, content, count=1, flags=re.IGNORECASE)

    if new_content == content:
        print(f"Warning: Could not find <head> tag in {file_path}")
        return

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added auth requirement to {os.path.basename(file_path)}")
    except Exception as e:
        print(f"Error writing to {file_path}: {e}")

if __name__ == "__main__":
    # Use current directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Find all HTML files recursively
    html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)
    
    count = 0
    for file_path in html_files:
        if os.path.basename(file_path) == "login.html":
            continue
        add_auth_to_html(file_path)
        count += 1
        
    print(f"\\nProcessed completely. Applied auth to {count} files.")
