# Gia Viet English Center Handbook

Website giới thiệu về Trung tâm Anh ngữ Gia Việt.

## Chạy local

### Cách 1: Sử dụng Python (khuyến nghị)
```bash
cd /Users/vobac/Downloads/gia-viet-handbook
python3 -m http.server 8000
```

Sau đó mở trình duyệt và truy cập: http://localhost:8000

### Cách 2: Sử dụng Node.js
```bash
cd /Users/vobac/Downloads/gia-viet-handbook
npx serve .
```

### Cách 3: Mở trực tiếp
Mở file `index.html` trực tiếp trong trình duyệt (có thể có một số hạn chế do CORS).

## Tính năng
- Responsive design
- Dark mode support
- Modern UI với Tailwind CSS
- Material Icons
- Vietnamese content

## Quy tắc Layout (Layout Rules)

### Cấu trúc Sidebar & Main Content
- **Tất cả các trang nội dung** đều sử dụng Layout 2 cột trên màn hình máy tính (Desktop):
  - **Cột Trái (Main Content)**: Chiếm chiều rộng `w-full md:w-[70%] lg:w-[75%]`.
  - **Cột Phải (Sidebar - Danh mục bài viết)**: Chiếm chiều rộng `w-full md:w-[30%] lg:w-[25%]`, có thuộc tính `sticky` tự động ghim khi cuộn (`sticky top-32 self-start`).
- **Trên thiết bị di động (Mobile < 768px)**:
  - Hai cột sẽ xếp chồng lên nhau theo chiều dọc.
  - Cột Nội dung chính (Main Content) sẽ hiển thị ở trên.
  - Cột Danh mục bài viết (Sidebar) sẽ xếp ở dưới và có khoảng cách phía trên (`mt-8 md:mt-0`).
- **Ngoại lệ**: Quy tắc này không áp dụng cho trang đăng nhập `login.html` và trang chủ `index.html`.

### Cú pháp HTML chuẩn
Khi chỉnh sửa hoặc tạo trang mới, hãy sử dụng cấu trúc HTML sau:

```html
<!-- 2 Column Layout -->
<div class="w-full max-w-[1440px] px-4 md:px-10 py-16 mx-auto">
    <div class="flex flex-col md:flex-row gap-8 lg:gap-16 items-start">
        
        <!-- Left Column: Content -->
        <div class="w-full md:w-[70%] lg:w-[75%] font-body text-gray-800 leading-relaxed space-y-8">
            <!-- Nội dung chính của trang -->
        </div>
        
        <!-- Right Column: Sidebar -->
        <div class="w-full md:w-[30%] lg:w-[25%] flex flex-col gap-10 mt-8 md:mt-0 sticky top-32 self-start">
            <!-- Danh mục bài viết / Điều hướng phụ -->
        </div>
        
    </div>
</div>
```

### Lưu ý quan trọng
- Luôn giữ comment định danh `<!-- Left Column: Content -->` và `<!-- Right Column: Sidebar -->` để các công cụ tự động phân tích chính xác cấu trúc trang.
- Danh mục bài viết (Sidebar) phải luôn nằm ở vị trí thứ hai trong thẻ chứa để đảm bảo xếp bên dưới nội dung chính khi hiển thị trên thiết bị di động.

