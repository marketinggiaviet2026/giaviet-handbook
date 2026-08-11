import os
import glob

html_files = glob.glob('*.html')

vercel_script = """    <!-- Vercel Analytics -->
    <script>
        window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
    </script>
    <script defer src="/_vercel/insights/script.js"></script>
</head>"""

count = 0
for file_path in html_files:
    if file_path == 'get-started-ui.html':
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'window.va =' in content or '/_vercel/insights/script.js' in content:
        continue # Already has analytics
        
    # Replace the closing </head> with the script + </head>
    if '</head>' in content:
        content = content.replace('</head>', vercel_script)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        
print(f"Successfully added Vercel Analytics to {count} HTML files.")
