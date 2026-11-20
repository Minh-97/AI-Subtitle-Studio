# AI Subtitle Studio

## Mục lục
1. Tổng quan dự án
2. Cài đặt môi trường
3. Chạy kiểm thử
4. Quy trình vận hành
5. Checklist

## 1. Tổng quan dự án
AI Subtitle Studio là dự án nền tảng cho quy trình tạo phụ đề tự động từ video và âm thanh.

## 2. Cài đặt môi trường
- Cài Python 3.10 hoặc mới hơn.
- Tạo môi trường ảo bằng `python -m venv .venv`.
- Kích hoạt môi trường ảo và cài đặt dependency từ `requirements.txt`.
- Cấu hình biến môi trường nếu cần cho các module sau này.

## 3. Chạy kiểm thử
- Chạy `python -m unittest discover -s tests -v` để kiểm tra toàn bộ suite.
- Nếu thêm module mới, nên thêm test tương ứng và chạy lại toàn bộ suite.

## 4. Quy trình vận hành
- Luôn làm việc trong môi trường ảo.
- Giữ cấu hình và logic xử lý tách riêng.
- Ghi log và trạng thái cho từng bước xử lý.
- Cập nhật tài liệu khi thay đổi quy trình hoặc dependency.

## 5. Checklist
- [x] Đã mô tả cách cài đặt môi trường.
- [x] Đã mô tả cách chạy kiểm thử.
- [x] Đã ghi rõ quy trình vận hành cơ bản.
