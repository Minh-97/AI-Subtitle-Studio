# Task 018 - Thiết kế và chuẩn hóa quy ước đặt tên cho file và dữ liệu

## Mục tiêu
Đảm bảo mọi file, thư mục, phiên bản và kết quả xử lý đều có tên gọi nhất quán, dễ nhận diện và dễ tra cứu.

## Mô tả
Task này tập trung vào việc xây dựng quy ước đặt tên cho file đầu vào, file tạm, transcript, subtitle, log, output và phiên bản công việc. Việc đặt tên chuẩn là yếu tố quan trọng để tránh nhầm lẫn, hỗ trợ quản lý dữ liệu và làm cho hệ thống dễ mở rộng. Quy ước này cần cân đối giữa tính dễ đọc, tính nhất quán và sự phù hợp với môi trường vận hành.

## Input
- Danh sách các loại file và thư mục cần quản lý
- Quy ước không gian tên và cấu trúc dự án
- Yêu cầu phát triển và vận hành

## Output
- Bộ quy ước đặt tên đầy đủ
- Ví dụ cho từng loại file và thư mục
- Danh sách các tên không được dùng hoặc nên tránh

## Điều kiện hoàn thành
- Mỗi loại file có quy ước đặt tên rõ ràng
- Tên file không gây hiểu nhầm giữa các phiên bản dữ liệu khác nhau
- Quy ước đặt tên phù hợp với quy trình xử lý và lưu trữ
- Không có trường hợp tên file trùng nhưng nghĩa khác nhau

## Tiêu chuẩn QA
- Tên file phải mô tả ý nghĩa và trạng thái dữ liệu
- Quy ước phải dễ áp dụng cho người mới
- Không dùng ký hiệu gây khó đọc hoặc không nhất quán
- Cần có cách phân biệt giữa bản gốc, tạm thời và kết quả cuối cùng

## Test cần vượt qua
- Đặt tên một file đầu vào, một file tạm và một file đầu ra cùng một công việc mà không gây nhầm lẫn
- Kiểm tra tên được tạo theo quy ước có thể hiểu ngay mà không cần đọc thêm tài liệu
- Kiểm tra việc dùng cùng tên cho dữ liệu khác không gây xung đột

## Checklist
- [ ] Đã xác định các loại file cần đặt tên
- [ ] Đã xây dựng quy ước tên cho từng loại
- [ ] Đã đưa ví dụ vào tài liệu
- [ ] Đã xác định tên không nên dùng
- [ ] Đã áp dụng quy ước vào quy trình nội bộ

## Độ ưu tiên
Trung bình

## Module liên quan
- File Management
- Naming Convention
- Storage
