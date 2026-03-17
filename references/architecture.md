# Architecture

## Input
- Pancake conversations API
- Pancake messages API
- Cấu hình pages/tokens riêng cho từng khách hàng

## Processing flow
1. Lấy danh sách conversations
2. Lọc unread conversations
3. Lấy message detail cho từng conversation
4. Parse timestamp -> convert sang giờ Việt Nam
5. Loại noise / auto / spam
6. Tìm tin khách mới nhất chưa được sale trả lời
7. Detect intent
8. Tính wait time
9. Xác định `desired_stage`
10. Xác định `actual_stage` tuần tự
11. Build wording theo stage + intent
12. Nếu stage 3 thì handoff tag trên Pancake
13. Gửi 1 tin tổng hợp vào nhóm quản lý sale

## Output
- Alert tiếng Việt
- Có thể gửi Telegram / Slack / Discord tùy triển khai
- Có state file để theo dõi stage

## Thành phần cần tách riêng khi thương mại
- config pages
- mapping sale/tag
- token API
- cron schedule
- destination channel
- brand voice / wording
