# Setup Guide

Tài liệu này dành cho người triển khai skill Pancake Commercial lần đầu.

## 1. Những dữ liệu bắt buộc phải có

### 1.1. Page ID
Là ID của fanpage / page cần monitor trên Pancake.

Ví dụ:
```json
{
  "page_id": "YOUR_PAGE_ID"
}
```

### 1.2. Page Access Token / Pancake Token
Dùng để gọi API Pancake lấy conversations và messages.

Ví dụ:
```json
{
  "page_access_token": "YOUR_PAGE_ACCESS_TOKEN"
}
```

### 1.3. Staff mapping
Cần map giữa:
- tên/tag nội bộ trên Pancake
- `tag_id` dùng để add/remove tag
- tài khoản nhận nhắc (Telegram / Slack / Discord...)

Ví dụ:
```json
{
  "staff": {
    "SALE_A": {
      "telegram": "@sale_a",
      "tag_id": 101,
      "name": "Sale A"
    }
  }
}
```

### 1.4. Destination channel
Nơi nhận alert:
- Telegram group id
- Slack channel id
- Discord channel/thread
- hoặc hệ thống chat nội bộ khác

### 1.5. Cron schedule
Ví dụ:
- 15,35,55 8-19 * * *
- hoặc lịch khác theo yêu cầu khách hàng

## 2. File config cần chuẩn bị
Khuyến nghị tạo file config riêng như:
- `config.pages.json`
- hoặc đặt secrets qua env variables / secret manager

Không commit secrets thật lên GitHub.

## 3. Dữ liệu tối thiểu để agent khác setup được
Nếu anh/chị gửi folder này cho một agent khác, họ cần biết:

### Bắt buộc
- Pancake dùng API nào
- cần `page_id`
- cần `page_access_token`
- cần mapping sale/tag_id
- cần nơi gửi alert
- cần cron schedule

### Nên có thêm
- rule brand voice
- giờ làm việc
- danh sách noise patterns riêng
- intent riêng theo ngành hàng

## 4. Các bước setup đề xuất

### Bước 1 — Chuẩn bị config
Tạo config từ file mẫu:
- `templates/config.pages.example.json`

Điền:
- page id
- token
- staff mapping

### Bước 2 — Chuẩn bị script production
Dùng:
- `templates/pancake_monitor_template.py`

rồi mở rộng thành script chạy thật theo hạ tầng của khách hàng.

### Bước 3 — Setup cron
Ví dụ cron:
```bash
15,35,55 8-19 * * *
```

### Bước 4 — Setup channel gửi cảnh báo
Ví dụ:
- Telegram bot + group id
- Slack bot + channel id
- Discord bot + channel id

### Bước 5 — Chạy debug trước production
Cần test:
- thời gian có convert đúng sang giờ Việt không
- detect đúng tin khách mới nhất không
- sale đã trả lời thì có bỏ qua đúng không
- stage có đi tuần tự 1 -> 2 -> 3 không
- remove/add tag ở lần 3 có đúng không

## 5. Rule setup quan trọng

### Rule 1 — Không hard-code dữ liệu thật
Không để trực tiếp vào source:
- token
- page access token
- group id nội bộ
- usernames nội bộ

### Rule 2 — Timezone phải chuẩn
Raw time từ Pancake cần convert sang giờ Việt Nam trước khi tính wait time.

### Rule 3 — Stage phải tuần tự
Không được nhảy cóc từ lần 1 lên lần 3 chỉ vì hội thoại đã quá 60 phút.

### Rule 4 — Handoff phải xác nhận thành công
Ở stage 3:
- remove tag sale cũ
- add 2 tag mới
- chỉ coi là handoff thành công khi cả hai bước đều OK

## 6. Checklist thông tin cần hỏi khách hàng khi onboarding
- Có bao nhiêu page cần monitor?
- Mỗi page dùng page id nào?
- Access token lấy từ đâu?
- Sale nào ứng với tag nào trên Pancake?
- Kênh nào nhận cảnh báo?
- Giờ làm việc là mấy giờ đến mấy giờ?
- Muốn cadence nhắc bao nhiêu phút?
- Có muốn stage 20 / 40 / 60 như mặc định không?
- Có muốn wording theo giọng thương hiệu riêng không?
- Có nhóm noise riêng nào cần bỏ qua không?

## 7. Các file nên public trên GitHub
Có thể public:
- README.md
- SKILL.md
- references/*.md
- templates/*.py
- templates/*.json

Không nên public:
- file config thật
- token thật
- logs thật
- state thật
- transcript thật
