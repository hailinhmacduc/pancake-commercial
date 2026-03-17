---
name: pancake-commercial
description: Skill theo dõi hội thoại Pancake/Facebook chưa được sale xử lý, phân tích nội dung khách hàng và nhắc sale theo 3 giai đoạn 20/40/60 phút với wording tiếng Việt, escalation và handoff tuần tự. Phiên bản đóng gói thương mại, đã loại bỏ dữ liệu nhạy cảm.
---

# Pancake Commercial Skill

Triển khai logic nhắc sale từ dữ liệu hội thoại Pancake/Facebook theo hướng thương mại hóa.

## Mục tiêu
- Đọc dữ liệu hội thoại Pancake
- Xác định khách đang hỏi gì
- Xác định sale đã trả lời chưa
- Nhắc sale theo 3 giai đoạn: 20 / 40 / 60 phút
- Escalation tuần tự, không nhảy cóc
- Handoff tag sale trên Pancake khi đến lần nhắc 3
- Dùng tiếng Việt hoàn toàn, bám sát đúng câu khách đang nói

## Bắt buộc hỏi đủ input trước khi triển khai
Nếu người dùng chưa cung cấp đủ cấu hình, hỏi gộp trong một lần với checklist rõ ràng. Không tự giả định secret hoặc ID thật.

### Input bắt buộc
- `page_id` cho từng page cần monitor
- `page_access_token` hoặc Pancake API token cho từng page
- mapping `sale -> tag_id -> tài khoản nhận nhắc`
- kênh nhận cảnh báo (`Telegram` / `Slack` / `Discord` / hệ thống chat nội bộ)
- cron schedule
- timezone vận hành

### Input nên hỏi thêm
- giờ làm việc
- brand voice / wording mong muốn
- noise patterns / auto-message patterns cần bỏ qua
- intent rules riêng theo ngành hàng

## Mẫu câu hỏi đề xuất
Hãy cung cấp các thông tin sau để em cấu hình skill Pancake reminder:
1. Page ID của từng page cần monitor
2. Page Access Token hoặc Pancake API token
3. Mapping sale: tên sale, tag_id trên Pancake, tài khoản nhận cảnh báo
4. Kênh nhận cảnh báo (Telegram / Slack / Discord...)
5. Cron schedule mong muốn
6. Timezone vận hành
7. (Tuỳ chọn) Giờ làm việc, brand voice, noise rules, intent rules riêng

## Quy trình dùng skill
1. Đọc `references/setup-guide.md` để nắm input bắt buộc.
2. Đọc `references/rules.md` và `references/architecture.md` khi cần triển khai logic.
3. Tạo config mới từ `templates/config.pages.example.json`.
4. Sao chép `templates/pancake_monitor_template.py` làm script triển khai riêng.
5. Điền secrets bằng env variables, secret manager hoặc file config riêng của khách hàng.
6. Chạy debug trước khi bật cron production.
7. Kiểm tra `references/deployment-checklist.md` trước khi bàn giao.

## Cấu trúc skill
- `references/product-overview.md` — mô tả sản phẩm / use case / value proposition
- `references/rules.md` — toàn bộ rule nghiệp vụ
- `references/architecture.md` — kiến trúc xử lý dữ liệu và flow nhắc sale
- `references/security.md` — nguyên tắc loại bỏ dữ liệu nhạy cảm khi đóng gói / triển khai
- `references/setup-guide.md` — hướng dẫn setup, onboarding input, checklist thông tin cần hỏi
- `references/deployment-checklist.md` — checklist bàn giao/production
- `templates/pancake_monitor_template.py` — script mẫu sạch, không kèm token thật
- `templates/config.pages.example.json` — cấu hình mẫu

## Ghi chú thương mại
- Skill này không chứa token thật, page id thật, log thật, state thật hoặc dữ liệu khách hàng thực tế.
- Không đóng gói các file như `.pancake_monitor_state.json`, `pancake_pages.json` thật, logs hoặc session transcripts.
- Luôn yêu cầu người dùng tự cung cấp cấu hình riêng của họ trước khi vận hành.
