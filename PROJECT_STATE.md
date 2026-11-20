# PROJECT STATE

Trạng thái hiện tại của dự án AI Subtitle Studio.

Cập nhật lần cuối: 2026-07-21 (sau Task002)

## Tổng quan

Dự án đang triển khai theo pipeline Task001 → Task030. Mỗi task có tài liệu
đặc tả trong `tasks/`, baseline implementation trong `src/` và test regression
trong `tests/`. Đã hoàn thành rà soát lại Task001 và Task002.

## Trạng thái task

| Task   | Trạng thái     | Ghi chú                                                          |
|--------|----------------|------------------------------------------------------------------|
| Task001| DONE           | Tài liệu quy chuẩn & phạm vi dự án. Tests pass (2/2).            |
| Task002| DONE           | Môi trường & quy trình vận hành. Tests pass (1/1). Đã rà soát lại 2026-07-21. |
| Task003| IN PROGRESS    | Quản lý cấu hình. Test hiện đang FAIL, cần xử lý trong task này. |
| Task004| TODO           | Tiếp nhận & kiểm tra đầu vào.                                    |
| Task005| BLOCKED        | Tiền xử lý media.                                                |
| Task006–Task011| DONE | Baseline validator & docs đã có, tests pass.                    |
| Task012–Task030| TODO | Chưa triển khai.                                                |

## Kết quả test gần nhất

Chạy bằng `.venv` tại thư mục `AI-Subtitle-Studio`:

- `tests/test_task001.py`: 2 passed.
- Toàn bộ suite: 14 passed, 1 failed (`tests/test_task003.py`).

Lưu ý: failure của Task003 nằm ngoài phạm vi Task001 và đang được theo dõi
tại Task003 (IN PROGRESS). Theo AGENT_RULES (quy tắc 3 — không sửa file ngoài
phạm vi Task), không sửa trong phiên Task001 này.

## Môi trường

- Python: 3.14.3 (virtualenv `.venv` ở thư mục workspace gốc).
- pytest: 9.1.1.
- Hệ điều hành: Windows 11.

## Bước tiếp theo

- Tiếp tục xử lý Task003 (sửa failure của `test_required_configuration_docs_and_files_exist`).
