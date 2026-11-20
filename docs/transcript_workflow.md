# Quy trình chuyển đổi lời nói thành transcript

## Mục lục
1. Tổng quan
2. Nguồn dữ liệu đầu vào
3. Cấu trúc transcript
4. Gắn thời điểm và phân đoạn
5. Xử lý nhận dạng không chắc chắn
6. Đầu ra cho module tiếp theo
7. Checklist

## 1. Tổng quan
Tài liệu này mô tả cách hệ thống chuyển audio đã tiền xử lý thành transcript có cấu trúc để phục vụ cho phụ đề và dịch thuật.

## 2. Nguồn dữ liệu đầu vào
- Audio đã được chuẩn hóa từ module tiền xử lý.
- Dữ liệu đầu vào có thể là file .wav hoặc các định dạng âm thanh tương thích.

## 3. Cấu trúc transcript
- transcript_segments: danh sách các đoạn lời nói đã phân đoạn.
- start_time: thời điểm bắt đầu của đoạn.
- end_time: thời điểm kết thúc của đoạn.
- confidence: mức độ tin cậy của kết quả nhận dạng.

## 4. Gắn thời điểm và phân đoạn
- Mỗi đoạn lời nói cần có thời điểm bắt đầu và kết thúc rõ ràng.
- Các đoạn nên được chia theo câu hoặc nhóm câu phù hợp để tiện theo dõi.

## 5. Xử lý nhận dạng không chắc chắn
- Nếu confidence thấp, hệ thống ghi nhận cảnh báo và đánh dấu đoạn cần review.
- Nếu không đủ thông tin để nhận dạng, giữ placeholder và ghi nhận lỗi.

## 6. Đầu ra cho module tiếp theo
- Transcript được lưu dưới dạng JSON hoặc file text có cấu trúc rõ ràng.
- Dữ liệu này sẽ được dùng cho module kiểm tra chất lượng transcript và dịch thuật.

## 5. Checklist
- [x] Đã xác định cấu trúc transcript.
- [x] Đã xác định cách gắn thời điểm cho mỗi đoạn.
- [x] Đã xác định quy tắc xử lý trường hợp nhận dạng không chắc chắn.
- [x] Đã xác định đầu ra cho module tiếp theo.
