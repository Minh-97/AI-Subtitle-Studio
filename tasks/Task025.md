# Task 025 - Xây dựng quy trình kiểm tra tính nhất quán của thuật ngữ và bản dịch

## Mục tiêu
Đảm bảo các thuật ngữ chuyên môn, tên riêng và cách gọi trong toàn bộ dự án luôn nhất quán giữa transcript, bản dịch và phụ đề.

## Mô tả
Task này tập trung vào việc kiểm tra và quản lý thuật ngữ đúng cách để tránh tình trạng cùng một khái niệm được gọi bằng nhiều tên hoặc cách dịch khác nhau. Điều này đặc biệt quan trọng khi làm việc với nhiều ngôn ngữ, nhiều file và nhiều phiên bản phụ đề. Hệ thống cần có quy trình xác định thuật ngữ chuẩn, kiểm tra các bản dịch có tuân thủ hay không và cảnh báo khi có sự lệch chuẩn.

## Input
- Glossary thuật ngữ
- Bản dịch và transcript
- Quy tắc dịch thuật và terminology

## Output
- Báo cáo về các thuật ngữ không nhất quán
- Danh sách thuật ngữ chuẩn và bản dịch được phép
- Cảnh báo khi phát hiện lệch quy ước

## Điều kiện hoàn thành
- Các thuật ngữ chính có được chuẩn hóa và ghi nhận lại
- Nếu một đoạn văn dùng thuật ngữ không thống nhất, hệ thống hoặc người review có thể phát hiện được
- Người chỉnh sửa có thể rà soát nhanh các mục cần xử lý
- Kết quả đầu ra không còn tình trạng một từ có nhiều nghĩa cách dịch khác nhau

## Tiêu chuẩn QA
- Thuật ngữ phải nhất quán trong toàn bộ sản phẩm
- Không được dịch sai hoặc thay đổi ý nghĩa của thuật ngữ chuyên môn
- Cần có đủ thông tin để người chỉnh sửa hiểu vì sao một thuật ngữ là chuẩn
- Báo cáo phải dễ đọc và có thể dùng ngay trong review

## Test cần vượt qua
- Một thuật ngữ chuyên môn xuất hiện ở nhiều đoạn và phải được giữ nguyên hoặc dịch đúng theo glossary
- Một trường hợp dùng tên riêng không thống nhất phải được phát hiện
- Một bản dịch không tuân thủ glossary phải được cảnh báo

## Checklist
- [ ] Đã chuẩn hóa glossary thuật ngữ
- [ ] Đã xác định cách kiểm tra tính nhất quán
- [ ] Đã thiết kế cảnh báo cho thuật ngữ lệch chuẩn
- [ ] Đã kiểm tra trên dữ liệu mẫu có nhiều thuật ngữ
- [ ] Đã ghi lại kết quả kiểm tra cho review

## Độ ưu tiên
Trung bình

## Module liên quan
- Terminology Management
- Translation Review
- Quality Assurance
