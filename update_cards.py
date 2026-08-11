import os
import re

user_content_cards = """
<div class="grid grid-cols-1 gap-8">
    <div class="card group">
        <div class="flex items-center gap-3 mb-4 border-b border-gray-100 pb-4">
            <div class="w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
                <span class="material-symbols-outlined text-2xl">child_care</span>
            </div>
            <h3 class="text-[#00174f] text-2xl font-bold font-display m-0">1. Kinder Play & Happy Kinder</h3>
        </div>
        <div class="text-gray-600 text-[15px] space-y-3 leading-relaxed">
            <p>Kinder Play và Happy Kinder là các chương trình tiếng Anh dành cho trẻ mầm non từ 3,5 đến 5 tuổi, được thiết kế theo lộ trình học tập bài bản gồm 06 cấp độ liên tiếp, trong đó có 02 cấp độ Kinder Play và 04 cấp độ Happy Kinder. Lộ trình học đảm bảo tính liên tục và sự phát triển phù hợp với đặc điểm nhận thức và tâm sinh lý của trẻ trong giai đoạn mầm non.</p>
            <p>Chương trình hướng đến việc giúp trẻ làm quen với tiếng Anh một cách tự nhiên, thông qua các hoạt động học tập mang tính tương tác cao, vui nhộn và phù hợp với độ tuổi như trò chơi, bài hát, vận động, kể chuyện và các hoạt động trải nghiệm. Trẻ được tiếp cận ngôn ngữ trong bối cảnh quen thuộc, tạo điều kiện để hình thành phản xạ nghe – nói một cách tự nhiên, không áp lực.</p>
            <p>Song song với việc xây dựng nền tảng tiếng Anh, chương trình còn chú trọng phát triển toàn diện cho trẻ ở các khía cạnh nhận thức, cảm xúc – xã hội và kỹ năng sống. Thông qua các hoạt động học tập được thiết kế có chủ đích, trẻ từng bước hình thành thói quen học tập tích cực, khả năng tương tác, hợp tác và tự tin thể hiện bản thân.</p>
            <p>Với thời lượng học phù hợp cùng phương pháp giảng dạy lấy trẻ làm trung tâm, chương trình Happy Kinder không chỉ khơi dậy hứng thú và tình yêu đối với việc học tiếng Anh ngay từ những năm đầu đời, mà còn đóng vai trò là nền tảng quan trọng, chuẩn bị cho trẻ sẵn sàng chuyển tiếp lên các cấp độ học tiếng Anh cao hơn trong tương lai.</p>
        </div>
    </div>

    <div class="card group">
        <div class="flex items-center gap-3 mb-4 border-b border-gray-100 pb-4">
            <div class="w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
                <span class="material-symbols-outlined text-2xl">face_5</span>
            </div>
            <h3 class="text-[#00174f] text-2xl font-bold font-display m-0">2. First Friends</h3>
        </div>
        <div class="text-gray-600 text-[15px] space-y-3 leading-relaxed">
            <p>First Friends là chương trình tiếng Anh dành cho trẻ từ 5 đến 6 tuổi, đặc biệt phù hợp với các học viên đang trong giai đoạn chuẩn bị vào tiểu học. Chương trình được thiết kế nhằm hỗ trợ trẻ làm quen và phát triển những năng lực tiếng Anh nền tảng, tạo bước đệm vững chắc trước khi chuyển sang các cấp độ học tập cao hơn.</p>
            <p>Chương trình tập trung phát triển hai kỹ năng trọng tâm là nghe và nói, đồng thời giúp học viên nhận biết tiếng Anh cơ bản thông qua việc tiếp cận bảng chữ cái, từ vựng và các mẫu câu đơn giản, gắn liền với những chủ đề quen thuộc trong đời sống hằng ngày. Nội dung học được xây dựng phù hợp với đặc điểm nhận thức và khả năng tập trung của trẻ ở giai đoạn mầm non cuối cấp.</p>
            <p>Quá trình giảng dạy được triển khai thông qua sự kết hợp hài hòa giữa hoạt động học và hoạt động chơi, cùng với các sản phẩm học tập được hoàn thành sau mỗi bài học. Cách tiếp cận này giúp học viên củng cố kiến thức một cách trực quan, sinh động thông qua hình ảnh và đồ vật, đồng thời tăng cường khả năng ghi nhớ và duy trì hứng thú học tập.</p>
            <p>Sau khi hoàn thành chương trình First Friends, học viên có khả năng giao tiếp cơ bản bằng tiếng Anh, hình thành phản xạ nghe - nói với các thông tin quen thuộc của bản thân như tên, tuổi, màu sắc, con vật, món ăn yêu thích. Bên cạnh đó, học viên có khả năng nhận diện và phản hồi bằng nghe - nói đối với nhiều chủ đề đa dạng như nông trại, nghề nghiệp, trang phục và trường học. Trẻ cũng được làm quen và phát âm được các chữ cái trong bảng chữ cái tiếng Anh cùng các số đếm cơ bản, tạo nền tảng quan trọng cho việc phát triển kỹ năng đọc - viết ở các giai đoạn học tập tiếp theo.</p>
        </div>
    </div>

    <div class="card group">
        <div class="flex items-center gap-3 mb-4 border-b border-gray-100 pb-4">
            <div class="w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
                <span class="material-symbols-outlined text-2xl">diversity_3</span>
            </div>
            <h3 class="text-[#00174f] text-2xl font-bold font-display m-0">3. Family and Friends</h3>
        </div>
        <div class="text-gray-600 text-[15px] space-y-3 leading-relaxed">
            <p>Family and Friends là chương trình tiếng Anh dành cho học viên bậc Tiểu học từ 6 đến 11 tuổi, được thiết kế nhằm xây dựng và phát triển năng lực sử dụng tiếng Anh một cách toàn diện, phù hợp với đặc điểm nhận thức và khả năng học tập của học sinh trong giai đoạn này.</p>
            <p>Nội dung chương trình xoay quanh các chủ đề gần gũi với đời sống hằng ngày, được minh họa bằng hệ thống hình ảnh sinh động và trực quan. Cách thiết kế này giúp học viên dễ dàng tiếp cận bài học, nâng cao khả năng hiểu bài và từng bước hình thành sự hứng thú, yêu thích đối với việc học tiếng Anh, đặc biệt phù hợp đối với những học viên mới bắt đầu.</p>
            <p>Chương trình hướng đến việc phát triển đồng đều các kỹ năng ngôn ngữ, trong đó ngữ âm và kỹ năng giao tiếp được chú trọng nhằm giúp học viên hình thành phát âm chuẩn, tăng cường khả năng nghe - nói và sử dụng tiếng Anh trong các tình huống quen thuộc. Song song với đó, giáo trình Family & Friends được xây dựng theo định hướng giảng dạy ngữ pháp kết hợp với luyện tập kỹ năng, giúp học viên hiểu và vận dụng các cấu trúc ngôn ngữ một cách linh hoạt, phù hợp với ngữ cảnh giao tiếp thực tế.</p>
            <p>Các hoạt động học tập trong chương trình tập trung vào việc hoàn thiện kỹ năng nghe - nói thông qua hệ thống từ vựng và tình huống giao tiếp đơn giản, sát với đời sống. Cách tiếp cận này không chỉ giúp học viên phát triển sự tự tin khi sử dụng tiếng Anh, đồng thời nâng cao khả năng tiếp nhận, hiểu và xử lý thông tin từ nhiều nguồn khác nhau.</p>
        </div>
    </div>

    <div class="card group">
        <div class="flex items-center gap-3 mb-4 border-b border-gray-100 pb-4">
            <div class="w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
                <span class="material-symbols-outlined text-2xl">public</span>
            </div>
            <h3 class="text-[#00174f] text-2xl font-bold font-display m-0">4. EFT - Foundation / EFT - Global Teens</h3>
        </div>
        <div class="text-gray-600 text-[15px] space-y-3 leading-relaxed">
            <p>EFT - Foundation và EFT - Global Teens là chương trình tiếng Anh dành cho học viên bậc Trung học cơ sở (từ 11 đến 15 tuổi), được xây dựng với mục tiêu phát triển năng lực ngôn ngữ vững chắc, đồng thời hình thành những kỹ năng cần thiết để học viên sẵn sàng hội nhập trong bối cảnh toàn cầu. Chương trình mang đến cho học viên những giờ học giàu tính khám phá, khơi gợi sự tò mò và nuôi dưỡng hứng thú học tập thông qua nội dung và phương pháp giảng dạy phù hợp với lứa tuổi thiếu niên.</p>
            <p>Chương trình được thiết kế theo lộ trình phát triển năng lực tiếng Anh từ trình độ A1+ đến B1+ theo Khung Tham chiếu Ngôn ngữ Chung Châu Âu (CEFR), đáp ứng nhu cầu học tập đa dạng của học viên ở các mức độ đầu vào khác nhau.</p>
            <p>Dựa trên nền tảng của giáo trình Harmonize, chương trình tập trung phát triển 04 khía cạnh cốt lõi trong mỗi chủ đề học: năng lực ngôn ngữ (Competence); sự sáng tạo (Creativity); kỹ năng hợp tác (Collaboration) và khơi dậy sự tò mò (Curiosity) của học viên. Với các chủ đề được cập nhật phù hợp với lứa tuổi thiếu niên, từng bài học được xây dựng trên nền tảng chủ đạo là các dự án và nhiệm vụ (Projects and Tasks) mang tính thực tiễn cao. Với thiết kế này, học viên được hướng dẫn xử lý các ngữ liệu đầu vào một cách hiệu quả và ứng dụng ngôn ngữ vào giao tiếp một cách tự nhiên thông qua các dự án trong mỗi bài học.</p>
            <p>Song song với việc phát triển năng lực ngôn ngữ, chương trình còn lồng ghép các kỹ năng và giá trị sống quan trọng của công dân toàn cầu như: kỹ năng tự chăm sóc bản thân, quản trị cảm xúc cá nhân, ý thức bảo vệ môi trường, sự tôn trọng và chấp nhận khác biệt, lòng yêu thương, tinh thần sẻ chia và lòng biết ơn. Những nội dung này được tích hợp xuyên suốt các cấp độ học, góp phần hỗ trợ sự phát triển toàn diện cho học viên.</p>
            <p>Bên cạnh đó, chương trình EFT – Global Teens còn tích hợp hai khóa luyện thi chứng chỉ quốc tế Cambridge, bao gồm KET for Schools (A2) và PET for Schools (B1). Các khóa học này giúp học viên làm quen với chuẩn đánh giá quốc tế, đồng thời tạo điều kiện để học viên đánh giá và khẳng định năng lực tiếng Anh của bản thân theo các tiêu chuẩn được công nhận trên toàn cầu.</p>
        </div>
    </div>

    <div class="card group">
        <div class="flex items-center gap-3 mb-4 border-b border-gray-100 pb-4">
            <div class="w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
                <span class="material-symbols-outlined text-2xl">workspace_premium</span>
            </div>
            <h3 class="text-[#00174f] text-2xl font-bold font-display m-0">5. Luyện thi YLE Starters / Movers / Flyers</h3>
        </div>
        <div class="text-gray-600 text-[15px] space-y-3 leading-relaxed">
            <p>Chương trình Luyện thi Cambridge Young Learners English (YLE) được thiết kế dành cho học viên bậc Tiểu học, nhằm trang bị cho các em nền tảng tiếng Anh vững chắc và sự chuẩn bị toàn diện cho các kỳ thi YLE Starters, YLE Movers và YLE Flyers theo chuẩn Cambridge.</p>
            <p>Chương trình được xây dựng theo lộ trình luyện thi phân cấp rõ ràng, tương ứng với từng trình độ YLE, giúp học viên phát triển đồng đều bốn kỹ năng Nghe – Nói – Đọc – Viết, đồng thời làm quen và từng bước thành thạo định dạng bài thi quốc tế ngay từ sớm. Nội dung học tập gắn liền với các chủ đề quen thuộc trong đời sống hằng ngày, được minh họa sinh động, qua đó tạo hứng thú học tập và nuôi dưỡng niềm yêu thích tiếng Anh cho học viên.</p>
            <ul class="list-disc pl-5 space-y-2 mt-2">
                <li><strong class="text-primary">YLE Starters:</strong> Cấp độ khởi đầu dành cho học viên mới làm quen với tiếng Anh và các kỳ thi Cambridge... Bài thi Starters thông qua các hoạt động luyện tập nhẹ nhàng. Cách tiếp cận này giúp học viên hình thành sự tự tin và phản xạ giao tiếp ban đầu.</li>
                <li><strong class="text-primary">YLE Movers:</strong> Ở cấp độ Movers, chương trình tập trung mở rộng vốn từ vựng, cấu trúc câu và nâng cao khả năng hiểu ngôn ngữ trong ngữ cảnh. Học viên được rèn luyện kỹ năng làm bài ở mức độ cao hơn, song song với việc nâng cao kỹ năng giao tiếp và phát âm chuẩn, đáp ứng yêu cầu của kỳ thi.</li>
                <li><strong class="text-primary">YLE Flyers:</strong> Cấp độ Flyers là bước chuẩn bị quan trọng trước khi học viên chuyển tiếp sang các kỳ thi Cambridge ở trình độ cao hơn. Chương trình giúp học viên hoàn thiện các kỹ năng ngôn ngữ, sử dụng tiếng Anh linh hoạt trong giao tiếp và học thuật.</li>
            </ul>
            <p>Xuyên suốt chương trình, ngữ âm và kỹ năng giao tiếp luôn được đặc biệt chú trọng, kết hợp với các hoạt động luyện thi có định hướng rõ ràng. Qua đó, học viên không chỉ đạt kết quả tốt trong kỳ thi chính thức và xây dựng nền tảng tiếng Anh vững chắc cho các cấp độ học tập tiếp theo.</p>
        </div>
    </div>

    <div class="card group">
        <div class="flex items-center gap-3 mb-4 border-b border-gray-100 pb-4">
            <div class="w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-white transition-colors">
                <span class="material-symbols-outlined text-2xl">school</span>
            </div>
            <h3 class="text-[#00174f] text-2xl font-bold font-display m-0">6. Luyện thi KET for Schools</h3>
        </div>
        <div class="text-gray-600 text-[15px] space-y-3 leading-relaxed">
            <p>Chương trình Luyện thi KET for Schools (A2) được thiết kế dành riêng cho học viên bậc Tiểu học và Trung học cơ sở có nhu cầu sử dụng chứng chỉ KET nhằm phục vụ cho các mục tiêu học tập và đánh giá năng lực tiếng Anh theo chuẩn quốc tế.</p>
            <p>Với thời lượng 12 tuần mỗi khóa, chương trình giúp học viên hệ thống hóa và củng cố kiến thức ngôn ngữ cốt lõi, đồng thời rèn luyện đầy đủ bốn kỹ năng Nghe – Nói – Đọc – Viết bám sát cấu trúc bài thi Cambridge. Song song với việc học kiến thức, học viên còn được trang bị các kỹ năng và chiến lược làm bài thi hiệu quả, thông qua việc thực hành các bài thi thử (Mock Tests) thường xuyên trong suốt khóa học. Thông qua quá trình luyện tập có định hướng và đánh giá liên tục, học viên từng bước nâng cao sự tự tin, làm quen với áp lực phòng thi và sẵn sàng đạt kết quả tốt trong kỳ thi chính thức.</p>
        </div>
    </div>
</div>
"""

file_path = '/Users/vobac/Downloads/gia-viet-handbook/tieng-anh-thieu-nhi-thieu-nien.html'
with open(file_path, 'r') as f:
    content = f.read()

# Replace starting from <div class="space-y-8"> to the end of that div (before the right column div)
pattern = r'<div class="space-y-8">.*?</div>\s*(?=</div>\s*<!-- Right Column: Sidebar -->)'
# Since there are multiple nested divs, regex might fail with .*?</div>.
# But wait, looking at my previous script, I just have a <div class="space-y-8"> followed by sections and then closing </div>.
# Let's use a more robust split or just replace explicitly.
start_str = '<div class="space-y-8">'
start_idx = content.find(start_str)
end_str = '</div>\n\n</div>\n\n                    <!-- Right Column: Sidebar -->'
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + user_content_cards + content[end_idx:]
    with open(file_path, 'w') as f:
        f.write(new_content)
    print("Cards added successfully!")
else:
    print("Could not find boundaries for replacement.")
    # let's try regex fallback
    new_content = re.sub(r'<div class="space-y-8">.*?(</div>\s*)(?=</div>\s*<!-- Right Column: Sidebar -->)', user_content_cards + r'\1', content, flags=re.DOTALL)
    with open(file_path, 'w') as f:
        f.write(new_content)
    print("Regex fallback used.")

