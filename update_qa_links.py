import glob
import re

def update_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Targets:
    # <a href="#" class="[^"]*">Dự giờ đồng nghiệp (Peer-Observation)</a>
    # <a href="#" class="[^"]*">Chương trình CPD</a>
    # <a href="#" class="[^"]*">Chương trình CoP</a>
    # <a href="#" class="[^"]*">Hỗ trợ Fast-Track Training</a>
    # <a href="#" class="[^"]*">Hỗ trợ Mentoring 1-1</a>

    pattern1 = re.compile(r'(<a\s+href=")("#)("\s+class="[^"]*">Dự giờ đồng nghiệp \(Peer-Observation\)</a>)')
    content = pattern1.sub(r'\g<1>du-gio-dong-nghiep.html\g<3>', content)

    pattern2 = re.compile(r'(<a\s+href=")("#)("\s+class="[^"]*">Chương trình CPD</a>)')
    content = pattern2.sub(r'\g<1>cpd.html\g<3>', content)

    pattern3 = re.compile(r'(<a\s+href=")("#)("\s+class="[^"]*">Chương trình CoP</a>)')
    content = pattern3.sub(r'\g<1>chuong-trinh-cop.html\g<3>', content)

    pattern4 = re.compile(r'(<a\s+href=")("#)("\s+class="[^"]*">Hỗ trợ Fast-Track Training</a>)')
    content = pattern4.sub(r'\g<1>fast-track-training.html\g<3>', content)

    pattern5 = re.compile(r'(<a\s+href=")("#)("\s+class="[^"]*">Hỗ trợ Mentoring 1-1</a>)')
    content = pattern5.sub(r'\g<1>mentoring-1-1.html\g<3>', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated QA links in {filepath.split('/')[-1]}")

if __name__ == '__main__':
    for f in glob.glob('/Users/vobac/Downloads/gia-viet-handbook/*.html'):
        update_links(f)
