# Task 015 - Xây dựng cơ chế quản lý phiên làm việc và dữ liệu tạm

## Mục tiêu
Quản lý dữ liệu trung gian và phiên xử lý một cách an toàn, dễ theo dõi và có thể phục hồi nếu phát sinh lỗi.

## Mô tả
Task này tập trung vào việc thiết kế việc lưu trữ dữ liệu tạm cho mỗi công việc. Điều này bao gồm việc tạo thư mục riêng cho từng job, lưu phiên làm việc, lưu trạng thái hiện tại, lưu checkpoint và cho phép tiếp tục xử lý nếu công việc bị dừng giữa chừng. Mục tiêu là tránh mất dữ liệu và làm cho pipeline có thể phục hồi tốt hơn.

## Input
- Thông tin công việc và trạng thái hiện tại
- Dữ liệu từ các module trước đó
- Quy định về thư mục temp và output

## Output
- Cấu trúc quản lý phiên làm việc
- Dữ liệu tạm và checkpoint được lưu đúng
- Metadata trạng thái công việc cho việc tiếp tục

## Điều kiện hoàn thành
- Mỗi công việc có thể được theo dõi riêng biệt
- Dữ liệu tạm được lưu ở nơi phù hợp và dễ khôi phục
- Nếu bị dừng, công việc có thể được tiếp tục mà không cần bắt đầu lại hoàn toàn
- Không có dữ liệu tạm bị trùng hoặc ghi sai

## Tiêu chuẩn QA
- Quản lý session phải rõ ràng và nhất quán
- Không để dữ liệu tạm bị ghi đè không chủ ý
- Bản ghi trạng thái phải phản ánh đúng tình hình hiện tại
- Hệ thống phải có cách nhận diện công việc đang chạy hoặc đã chạy xong

## Test cần vượt qua
- Tạo một công việc mẫu, dừng giữa chừng và kiểm tra dữ liệu tạm còn tồn tại
- Tiếp tục công việc đó mà không cần khởi động lại từ đầu
- Kiểm tra tên và vị trí dữ liệu tạm không bị trùng

## Checklist
- [ ] Đã xác định cấu trúc session/job
- [ ] Đã xác định quy tắc lưu checkpoint
- [ ] Đã xác định cách tiếp tục công việc sau khi dừng
- [ ] Đã kiểm tra với tình huống bị gián đoạn
- [ ] Đã lưu trạng thái công việc rõ ràng

## Độ ưu tiên
Trung bình

## Module liên quan
- Session Management
- Temp Storage
- Recovery
