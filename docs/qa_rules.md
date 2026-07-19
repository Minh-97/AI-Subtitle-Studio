# Quy tắc chất lượng và kiểm thử QA cho AI Subtitle Studio

## Mục lục
1. Mục đích
2. Tiêu chí chất lượng
3. Quy trình kiểm thử
4. Phân loại lỗi
5. Quy tắc chấp nhận sản phẩm
6. Ví dụ kiểm thử
7. Checklist

## 1. Mục đích
Tài liệu này mô tả các nguyên tắc kiểm tra chất lượng cho quy trình tạo phụ đề, từ đầu vào cho tới đầu ra cuối cùng.

## 2. Tiêu chí chất lượng
- Nội dung phụ đề phải chính xác về ý nghĩa.
- Thời gian xuất hiện phải phù hợp với âm thanh và video.
- Định dạng đầu ra phải nhất quán.
- Hệ thống phải xử lý lỗi một cách rõ ràng và không làm mất dữ liệu.
- Kết quả phải có thể kiểm tra lại bằng hồ sơ và log.

## 3. Quy trình kiểm thử
- Kiểm tra đầu vào: định dạng file, chất lượng âm thanh và khả năng đọc được.
- Kiểm tra quy trình: nhận dạng, dịch thuật, định dạng và xuất kết quả.
- Kiểm tra đầu ra: độ chính xác nội dung, thời gian và cấu trúc file.
- Kiểm tra hồi quy: các thay đổi mới không làm hỏng chức năng cũ.

## 4. Phân loại lỗi
- Lỗi dữ liệu đầu vào: file bị hỏng hoặc không hỗ trợ.
- Lỗi quy trình: nhận dạng hoặc dịch thuật sai.
- Lỗi định dạng: phụ đề không đúng cấu trúc.
- Lỗi vận hành: log thiếu, không lưu kết quả hoặc thất bại không báo rõ.

## 5. Quy tắc chấp nhận sản phẩm
Một bản phụ đề được xem là chấp nhận khi nội dung đúng, thời gian hợp lý, không có lỗi định dạng và có ghi nhận đầy đủ trong logs.

## 6. Ví dụ kiểm thử
Ví dụ: với một video có giọng nói rõ ràng, hệ thống phải tạo phụ đề có nội dung gần đúng và thời gian hiển thị khớp với câu nói. Nếu một file audio bị nhiễu nặng, hệ thống phải cảnh báo thay vì tự ý xuất kết quả sai lệch.

## 7. Checklist
- [ ] Đã kiểm tra đầu vào trước khi xử lý.
- [ ] Đã kiểm tra chất lượng nội dung phụ đề.
- [ ] Đã kiểm tra độ đồng bộ thời gian.
- [ ] Đã kiểm tra đầu ra theo đúng định dạng yêu cầu.
- [ ] Đã ghi nhận lỗi và cách xử lý.
