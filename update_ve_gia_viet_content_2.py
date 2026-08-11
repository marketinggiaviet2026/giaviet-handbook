import sys

def main():
    filepath = '/Users/vobac/Downloads/gia-viet-handbook/ve-gia-viet.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Sứ mệnh card
    su_menh_card = """        <div class="bg-white rounded-xl border border-gray-100/80 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300 p-6 flex flex-col gap-2 cursor-pointer group" onclick="toggleGVCard(this)">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 rounded-full bg-blue-50 text-primary flex items-center justify-center flex-shrink-0 group-hover:scale-110 group-hover:bg-primary group-hover:text-white transition-all duration-300">
                        <span class="material-symbols-outlined text-2xl">my_location</span>
                    </div>
                    <h3 class="text-xl font-bold font-display text-[#00174f] group-hover:text-primary transition-colors">Sứ mệnh</h3>
                </div>
                <div class="w-8 h-8 rounded-full border border-gray-100 flex items-center justify-center text-gray-400 group-hover:border-primary group-hover:text-primary transition-colors">
                    <span class="material-symbols-outlined text-[20px] expand-icon transition-transform duration-300">add</span>
                </div>
            </div>
            
            <div class="gv-card-content overflow-hidden transition-all duration-500 max-h-0 opacity-0 pl-[4rem]">
                <div class="pt-2 pb-1">
                    <p class='font-medium text-gray-700'>Xây dựng môi trường giáo dục tiếng Anh chất lượng, nhân văn & bền vững.</p>
                </div>
            </div>
        </div>
        
"""
    
    content = content.replace(su_menh_card, "")

    # 2. Căn đều text (add text-justify)
    content = content.replace("class='font-medium text-gray-700'", "class='font-medium text-gray-700 text-justify'")
    content = content.replace("class='list-disc pl-5 mt-2 space-y-1.5 text-gray-600'", "class='list-disc pl-5 mt-2 space-y-1.5 text-gray-600 text-justify'")
    
    # Also for the one with the arrow right alt
    content = content.replace("<p class='mt-3 text-primary font-medium flex items-center gap-1'>", "<p class='mt-3 text-primary font-medium flex items-center gap-1 text-justify'>")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Updated successfully!")

if __name__ == '__main__':
    main()
