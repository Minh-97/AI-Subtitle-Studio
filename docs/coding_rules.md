# Quy tắc lập trình cho AI Subtitle Studio

## Mục lục
1. Mục đích
2. Nguyên tắc chung
3. Quy ước đặt tên
4. Cấu trúc tổ chức source
5. Quy ước ghi chú và tài liệu
6. Quy trình kiểm thử
7. Ví dụ thực hành
8. Checklist

## 1. Mục đích
Tài liệu này định nghĩa quy tắc phát triển để giữ mã nguồn dễ đọc, dễ bảo trì và nhất quán giữa các thành viên.

## 2. Nguyên tắc chung
- Ưu tiên sự rõ ràng trước khi tối ưu hóa.
- Mỗi module nên có trách nhiệm rõ ràng.
- Tránh lặp lại logic không cần thiết.
- Mọi thay đổi quan trọng cần được ghi lại và giải thích.
- Không để mã nguồn phụ thuộc vào dữ liệu cứng không cần thiết.

## 3. Quy ước đặt tên
- Tên biến, hàm và module nên mô tả ý nghĩa rõ ràng.
- Tránh tên quá ngắn hoặc mang tính mơ hồ.
- Dùng kiểu đặt tên nhất quán trong toàn bộ dự án.
- Tên file nên phản ánh chức năng chính của module.

## 4. Cấu trúc tổ chức source
- Chia source theo chức năng: nhập liệu, tiền xử lý, nhận dạng, dịch thuật, định dạng, xuất kết quả.
- Mỗi lớp hoặc module nên có một trách nhiệm duy nhất.
- Tách cấu hình khỏi logic nghiệp vụ.
- Giữ các hàm phụ trợ nhỏ, dễ kiểm thử và tái sử dụng.

## 5. Quy ước ghi chú và tài liệu
- Ghi chú nên giải thích vì sao, không chỉ viết cái gì.
- Tài liệu nên cập nhật đồng bộ với bản thay đổi.
- Khi thêm tính năng mới, phải cập nhật tài liệu liên quan.

## 6. Quy trình kiểm thử
- Mỗi thay đổi cần có kiểm thử phù hợp với phạm vi.
- Nếu thay đổi ảnh hưởng tới luồng phụ đề, cần kiểm tra đầu vào và đầu ra.
- Đảm bảo kết quả có thể kiểm chứng bằng dữ liệu mẫu.

## 7. Ví dụ thực hành
Ví dụ: nếu một module xử lý âm thanh được đổi tên, tên mới phải phản ánh việc tách âm thanh và chuẩn hóa. Nếu một hàm xử lý thời gian được thêm vào, nên đặt tên dễ hiểu như normalize_timing thay vì dùng tên mơ hồ.

## 8. Checklist
- [ ] Mã nguồn có cấu trúc rõ ràng.
- [ ] Tên gọi nhất quán và dễ hiểu.
- [ ] Tài liệu và ghi chú được cập nhật.
- [ ] Có kiểm thử cho thay đổi quan trọng.
- [ ] Không để logic sai lệch trong các module không liên quan.
