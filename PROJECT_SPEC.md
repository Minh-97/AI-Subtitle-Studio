# PROJECT SPEC

Tên

AI Subtitle Studio

## Mục lục

1. Tổng quan
2. Mục tiêu
3. Các thành phần chính
4. Input
5. Output
6. Yêu cầu
7. Checklist

## 1. Tổng quan

AI Subtitle Studio là hệ thống xử lý video tự động: nhận video tiếng Trung,
tạo phụ đề và lồng tiếng/dịch sang tiếng Việt, rồi xuất video hoàn chỉnh.

Quy trình cốt lõi: tiếp nhận đầu vào → tiền xử lý → nhận dạng lời nói (transcript)
→ kiểm tra chất lượng transcript → dịch thuật → review bản dịch → định dạng
phụ đề → căn chỉnh thời gian → xuất video.

Người dùng cuối chỉ nhận file video hoàn chỉnh. Không xuất file trung gian
cho người dùng.

## 2. Mục tiêu

- Dịch theo ngữ cảnh.
- Không dịch từng câu rời rạc.
- Giữ tên riêng.
- Giữ xưng hô.
- Giữ cảm xúc.
- Đồng bộ thời gian.
- Xuất video hoàn chỉnh.

## 3. Các thành phần chính

- Module tiếp nhận và kiểm tra đầu vào (Task004).
- Module tiền xử lý âm thanh và video (Task005).
- Module chuyển đổi lời nói thành transcript (Task006).
- Module kiểm tra chất lượng transcript (Task007).
- Module dịch thuật transcript (Task008).
- Module kiểm tra và chỉnh sửa bản dịch (Task009).
- Module định dạng phụ đề (Task010).
- Module căn chỉnh thời gian phụ đề (Task011).
- Module xuất video hoàn chỉnh.

Cấu hình hệ thống tập trung tại `config/system_config.json`, tham số được
quản lý thống nhất theo Task003.

## 4. Input

movie_cn.mp4

↓

## 5. Output

movie_vi.mp4

## 6. Yêu cầu

- Dịch theo ngữ cảnh.

- Không dịch từng câu.

- Giữ tên riêng.

- Giữ xưng hô.

- Giữ cảm xúc.

- Đồng bộ thời gian.

- Xuất video hoàn chỉnh.

Không xuất file trung gian cho người dùng.

## 7. Checklist

- [x] Đã xác định mục tiêu dự án.
- [x] Đã xác định input và output.
- [x] Đã liệt kê các thành phần chính.
- [x] Đã liệt kê yêu cầu xử lý.
- [x] Đã xác định nơi lưu trữ cấu hình (config/system_config.json).
