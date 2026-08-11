import io

file_path = '/Users/vobac/Downloads/gia-viet-handbook/tieng-anh-thieu-nhi-thieu-nien.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find the cards container
start_marker = '<div class="grid grid-cols-1 gap-8">'
end_marker = '</div>\n\n</div>\n\n                    <!-- Right Column: Sidebar -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    cards_html = html[start_idx:end_idx]
    
    # Now let's transform each card
    # We'll replace '<div class="card group">'
    cards_html = cards_html.replace(
        '<div class="card group">', 
        '<div class="card group cursor-pointer" onclick="toggleAccordion(this)">'
    )
    
    # Modify the header
    header_original = '<div class="flex items-center gap-3 mb-4 border-b border-gray-100 pb-4">'
    header_new = '''<div class="flex items-center justify-between gap-3 mb-4 border-b border-gray-100 pb-4 w-full">
            <div class="flex items-center gap-3">'''
    cards_html = cards_html.replace(header_original, header_new)
    
    # Close the new inner div and add chevron
    # We know the original header ends with </h3>\n        </div>
    cards_html = cards_html.replace(
        '</h3>\n        </div>',
        '</h3>\n            </div>\n            <span class="material-symbols-outlined text-gray-400 group-hover:text-primary transition-transform duration-300 transform rotate-0 toggle-icon">expand_more</span>\n        </div>'
    )
    
    # Hide the content by default
    content_original = '<div class="text-gray-600 text-[15px] space-y-3 leading-relaxed font-body">'
    content_new = '<div class="text-gray-600 text-[15px] space-y-3 leading-relaxed font-body card-content hidden">'
    cards_html = cards_html.replace(content_original, content_new)
    
    # We need to add the JS function before </body>
    script = """
    <script>
        function toggleAccordion(element) {
            const content = element.querySelector('.card-content');
            const icon = element.querySelector('.toggle-icon');
            
            if (content.classList.contains('hidden')) {
                // Open it
                content.classList.remove('hidden');
                icon.style.transform = 'rotate(180deg)';
                element.style.borderColor = '#0d59f2';
            } else {
                // Close it
                content.classList.add('hidden');
                icon.style.transform = 'rotate(0deg)';
                element.style.borderColor = 'white';
            }
        }
    </script>
</body>
"""
    new_html = html[:start_idx] + cards_html + html[end_idx:]
    if '<script>\n        function toggleAccordion' not in new_html:
        new_html = new_html.replace('</body>', script)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Accordion applied successfully!")
else:
    print("Could not find the cards container.")
