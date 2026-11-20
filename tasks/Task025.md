# Task 025 - Thiết lập quy trình kiểm tra tính nhất quán của thuật ngữ và bản dịch

## Mục tiêu
Đảm bảo các thuật ngữ chuyên môn, tên riêng và cách gọi trong toàn bộ dự án luôn nhất quán giữa transcript, bản dịch và phụ đề.

## Mô tả
Task này tập trung vào việc xác định quy trình kiểm tra và quản lý thuật ngữ đúng cách để tránh cùng một khái niệm được gọi bằng nhiều tên hoặc cách dịch khác nhau.

## Input
- PLAN.md
- docs/translation_rules.md
- docs/terminology.md

## Output
- Quy trình kiểm tra tính nhất quán thuật ngữ
- Báo cáo về các thuật ngữ không nhất quán
- Danh sách thuật ngữ chuẩn và bản dịch được phép

## API
- Không áp dụng API trong task này.
- Tập trung vào kiểm tra thuật ngữ và bản dịch.

## Test
- Kiểm tra một thuật ngữ chuyên môn xuất hiện ở nhiều đoạn được giữ nhất quán.
- Kiểm tra một trường hợp tên riêng không thống nhất được phát hiện.
- Kiểm tra một bản dịch không tuân thủ glossary được cảnh báo.

## Điều kiện hoàn thành
- Các thuật ngữ chính được chuẩn hóa và ghi nhận lại.
- Nếu một đoạn văn dùng thuật ngữ không thống nhất, hệ thống hoặc người review có thể phát hiện được.
- Người chỉnh sửa có thể rà soát nhanh các mục cần xử lý.

## Checklist
- [ ] Đã chuẩn hóa glossary thuật ngữ.
- [ ] Đã xác định cách kiểm tra tính nhất quán.
- [ ] Đã thiết kế cảnh báo cho thuật ngữ lệch chuẩn.
- [ ] Đã kiểm tra trên dữ liệu mẫu có nhiều thuật ngữ.
- [ ] Đã ghi lại kết quả kiểm tra cho review.
