import glob
import re

def make_interactive(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The interaction classes to append
    inter_classes = " hover:-translate-y-1 hover:shadow-md active:scale-[0.98] transition-all duration-300 cursor-pointer"
    
    # We want to target inner cards that typically have: bg-white... rounded-xl/lg... shadow-sm... border...
    # BUT EXCLUDE the main container which usually has "lg:w-[75%]" or "md:w-[70%]"
    
    # Let's find all class="..." strings
    pattern = re.compile(r'class="([^"]*)"')
    
    def replacer(match):
        classes = match.group(1)
        
        # Conditions to identify a "card"
        is_card = False
        if ('rounded-xl' in classes or 'rounded-lg' in classes or 'rounded-2xl' in classes):
            if ('p-4' in classes or 'p-5' in classes or 'p-6' in classes or 'p-8' in classes):
                if ('bg-white' in classes or 'bg-gray-50' in classes or 'bg-blue-50' in classes or 'bg-[#00174f]' in classes or '-50' in classes):
                    is_card = True
                    
        # Exclusions (Don't touch the main wrappers or dropdowns or tiny buttons)
        if ('w-full' in classes and 'lg:w-[75%]' in classes) or ('absolute' in classes) or ('fixed' in classes) or ('flex-1' not in classes and 'w-full' in classes and 'min-h-screen' in classes):
            is_card = False
            
        if 'hover:-translate-y-1' in classes: # already interactive
            is_card = False

        if is_card:
            # Prevent double adding
            return f'class="{classes}{inter_classes}"'
            
        return match.group(0)

    # Let's also do a specific string replace for the 'quy-dinh-phu-dao.html' grid cards which might be missed
    new_content = pattern.sub(replacer, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added interactive effects to cards in {filepath.split('/')[-1]}")

if __name__ == '__main__':
    target_files = [
        '/Users/vobac/Downloads/gia-viet-handbook/quy-dinh-phu-dao.html',
        '/Users/vobac/Downloads/gia-viet-handbook/chinh-sach-hoc-bong.html',
        '/Users/vobac/Downloads/gia-viet-handbook/quy-dinh-khao-thi.html',
        '/Users/vobac/Downloads/gia-viet-handbook/quy-dinh-nghi-phep.html',
        '/Users/vobac/Downloads/gia-viet-handbook/quy-dinh-diem-danh.html',
        '/Users/vobac/Downloads/gia-viet-handbook/quy-trinh-giang-day.html',
        '/Users/vobac/Downloads/gia-viet-handbook/quy-dinh-so-lien-lac.html',
        '/Users/vobac/Downloads/gia-viet-handbook/giao-trinh-tai-lieu.html'
    ]
    for f in target_files:
        try:
            make_interactive(f)
        except Exception as e:
            print(f"Skipped {f}: {e}")
