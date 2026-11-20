# Quy trình đồng bộ phụ đề với thời gian video

## Mục lục
1. Tổng quan
2. Nguồn dữ liệu đồng bộ
3. Quy tắc đồng bộ
4. Xử lý chênh lệch và ngắt lời
5. Kiểm tra độ đồng bộ
6. Checklist

## 1. Tổng quan
Tài liệu này mô tả cách gắn thời gian bắt đầu và kết thúc cho mỗi đoạn phụ đề để phù hợp với lời nói và thời gian phát của video.

## 2. Nguồn dữ liệu đồng bộ
- Phụ đề đã được định dạng và có nội dung ổn định.
- Thời gian bắt đầu và kết thúc cần căn theo audio và video đầu vào.

## 3. Quy tắc đồng bộ
- sync_rules: mỗi đoạn phụ đề cần có thời gian bắt đầu và kết thúc rõ ràng.
- time_offset_handling: nếu có chênh lệch nhỏ, điều chỉnh theo mức tối thiểu để giữ trải nghiệm xem tự nhiên.
- pause_handling: nếu lời nói ngắt quãng hoặc có pause, nên kéo dài hoặc rút ngắn đoạn phụ đề phù hợp.

## 4. Xử lý chênh lệch và ngắt lời
- Nếu chênh lệch nhỏ dưới ngưỡng cho phép, chỉnh thời gian ngay.
- Nếu có ngắt lời rõ ràng, ưu tiên giữ câu đọc đúng nhịp thay vì giữ nguyên thời lượng dài.

## 5. Kiểm tra độ đồng bộ
- Sau khi đồng bộ, cần kiểm tra xem phụ đề có hiển thị đúng thời điểm và đủ thời gian đọc không.

## 5. Checklist
- [x] Đã xác định quy tắc đồng bộ thời gian.
- [x] Đã xác định cách xử lý chênh lệch nhỏ.
- [x] Đã xác định cách xử lý ngắt lời và nhịp phát âm.
