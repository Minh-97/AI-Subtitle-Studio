# Kiến trúc hệ thống AI Subtitle Studio

## Mục lục
1. Tổng quan
2. Mục tiêu hệ thống
3. Các thành phần chính
4. Luồng xử lý dữ liệu
5. Quy ước kiến trúc
6. Ví dụ vận hành
7. Checklist

## 1. Tổng quan
AI Subtitle Studio là hệ thống hỗ trợ tạo phụ đề tự động cho video bằng quy trình kết hợp nhận dạng giọng nói, dịch thuật, sắp xếp thời gian và render phụ đề. Mục tiêu là giảm thời gian xử lý thủ công, tăng độ nhất quán và hỗ trợ xuất bản đa định dạng.

## 2. Mục tiêu hệ thống
- Nhận đầu vào là video hoặc âm thanh.
- Tạo bản ghi phụ đề ban đầu từ giọng nói.
- Dịch nội dung sang ngôn ngữ mục tiêu.
- Chia nhỏ, căn chỉnh thời gian và định dạng phụ đề.
- Xuất kết quả ra các định dạng phù hợp cho phân phối.

## 3. Các thành phần chính
### 3.1 Module nhập liệu
- Chấp nhận file video, âm thanh hoặc dữ liệu đã có sẵn.
- Kiểm tra định dạng, kích thước và chất lượng file.
- Tạo bản ghi metadata ban đầu.

### 3.2 Module tiền xử lý
- Tách âm thanh khỏi video.
- Chuẩn hóa âm lượng, loại bỏ nhiễu và chuẩn bị dữ liệu cho nhận dạng.
- Tạo bản sao tạm thời để xử lý an toàn.

### 3.3 Module nhận dạng giọng nói
- Chuyển âm thanh thành văn bản.
- Trả về các đoạn văn bản cùng thời điểm bắt đầu và kết thúc.
- Hỗ trợ xử lý từ nhiều giọng nói, ngôn ngữ khác nhau.

### 3.4 Module dịch thuật và chỉnh sửa
- Dịch bản văn bản sang ngôn ngữ mục tiêu.
- Giữ nguyên ý nghĩa, ngữ cảnh và phong cách phù hợp.
- Cho phép kiểm duyệt và chỉnh sửa thủ công.

### 3.5 Module định dạng phụ đề
- Chia đoạn văn bản theo độ dài phụ đề phù hợp.
- Căn thời gian để đồng bộ với video.
- Áp dụng quy tắc xuất hiện, ngắt dòng và đánh dấu thời gian.

### 3.6 Module xuất kết quả
- Xuất sang file phụ đề tiêu chuẩn và bản render video.
- Lưu trữ kết quả vào thư mục output và logs.
- Tạo bản ghi quá trình xử lý để kiểm tra lại.

## 4. Luồng xử lý dữ liệu
1. Người dùng cung cấp video hoặc âm thanh.
2. Hệ thống chuẩn bị file và tạo bản ghi công việc.
3. Âm thanh được tách và tiền xử lý.
4. Bản ghi nhận dạng được tạo.
5. Bản ghi được dịch và chỉnh sửa.
6. Phụ đề được định dạng và đồng bộ thời gian.
7. Kết quả được xuất ra file và lưu trữ.

## 5. Quy ước kiến trúc
- Tách rõ các lớp xử lý: nhập, xử lý, dịch, xuất.
- Mọi dữ liệu trung gian cần được lưu trong thư mục temp hoặc output.
- Log phải ghi đầy đủ tác vụ, thời gian và trạng thái.
- Cấu hình nên được giữ ở thư mục config và không hardcode trong code.
- Mọi thay đổi quan trọng phải có ghi chú và kiểm tra bằng tài liệu.

## 6. Ví dụ vận hành
Ví dụ: một video dài 10 phút được tải lên. Hệ thống tách âm thanh, tạo phụ đề ban đầu, dịch sang tiếng Anh, căn thời gian và xuất file phụ đề SRT cùng bản render có phụ đề hiển thị.

## 7. Checklist
- [ ] Đã xác định rõ đầu vào và đầu ra.
- [ ] Đã phân chia trách nhiệm giữa các module.
- [ ] Đã xác định nơi lưu trữ dữ liệu tạm và dữ liệu cuối.
- [ ] Đã quy định cách ghi log và theo dõi tiến độ.
- [ ] Đã xác định cách xử lý lỗi và dữ liệu không hợp lệ.
