# Quy trình tiếp nhận và kiểm tra đầu vào

## Mục lục
1. Tổng quan
2. Các loại đầu vào chính
3. Quy trình kiểm tra đầu vào
4. Metadata và ghi nhận trạng thái
5. Xử lý đầu vào không hợp lệ
6. Checklist

## 1. Tổng quan
Tài liệu này mô tả cách hệ thống tiếp nhận video và audio từ người dùng, kiểm tra tính hợp lệ và ghi nhận metadata trước khi xử lý tiếp.

## 2. Các loại đầu vào chính
- video: file video được tải lên để xử lý phụ đề.
- audio: file âm thanh được tải lên riêng hoặc tách từ video.

## 3. Quy trình kiểm tra đầu vào
1. Kiểm tra định dạng file và kích thước.
2. Kiểm tra tính tồn tại và khả năng đọc file.
3. Kiểm tra độ dài và chất lượng dữ liệu.
4. Ghi nhận trạng thái kiểm tra và lỗi nếu có.

## 4. Metadata và ghi nhận trạng thái
- source_file: đường dẫn hoặc tên file đầu vào.
- file_type: loại file như video hoặc audio.
- duration_seconds: thời lượng của file.
- metadata: thông tin bổ sung về file và quá trình nhập.

## 5. Xử lý đầu vào không hợp lệ
- Nếu định dạng không được hỗ trợ, hệ thống cảnh báo và từ chối file.
- Nếu file bị hỏng hoặc không đọc được, ghi nhận lỗi và dừng xử lý.
- Nếu file hợp lệ nhưng chất lượng thấp, ghi log và cho phép tiếp tục với cảnh báo.

## 5. Checklist
- [x] Đã xác định các loại đầu vào chính.
- [x] Đã mô tả quy trình kiểm tra file.
- [x] Đã xác định metadata và cách ghi nhận trạng thái.
- [x] Đã xác định cách xử lý đầu vào không hợp lệ.
