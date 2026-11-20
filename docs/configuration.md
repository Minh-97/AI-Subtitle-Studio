# Cấu hình hệ thống AI Subtitle Studio

## Mục lục
1. Tổng quan
2. Các tham số cấu hình chính
3. Cách sử dụng cấu hình
4. Cập nhật cấu hình
5. Checklist

## 1. Tổng quan
Tài liệu này ghi nhận cấu hình cốt lõi của hệ thống để quản lý đường dẫn, tham số xử lý, ngôn ngữ và mức log một cách thống nhất.

## 2. Các tham số cấu hình chính
- input_dir: thư mục chứa dữ liệu đầu vào.
- output_dir: thư mục lưu kết quả đầu ra.
- temp_dir: thư mục lưu file tạm.
- subtitle_duration_seconds: thời lượng hiển thị của mỗi phụ đề.
- language: ngôn ngữ mặc định cho quá trình xử lý.
- log_level: mức log dùng cho vận hành.

## 3. Cách sử dụng cấu hình
- Đọc cấu hình từ file config/system_config.json.
- Truy cập các tham số bằng tên rõ ràng và không hardcode giá trị trong code.
- Khi thêm tham số mới, cập nhật cả file cấu hình lẫn tài liệu này.

## 4. Cập nhật cấu hình
- Luôn cập nhật tài liệu này khi thay đổi tham số hoặc quy trình.
- Đảm bảo cấu hình có thể chỉnh sửa mà không cần sửa nhiều module.

## 5. Checklist
- [x] Đã liệt kê các tham số chính.
- [x] Đã mô tả cách dùng cấu hình.
- [x] Đã ghi rõ quy trình cập nhật cấu hình.
