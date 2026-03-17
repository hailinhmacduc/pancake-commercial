# Deployment Checklist

## A. Cấu hình
- [ ] Đã có `page_id`
- [ ] Đã có `page_access_token`
- [ ] Đã có mapping staff -> tag_id -> account nhận nhắc
- [ ] Đã có destination channel
- [ ] Đã có cron schedule
- [ ] Đã xác định timezone vận hành

## B. Logic
- [ ] Timestamp từ Pancake đã convert sang giờ Việt Nam
- [ ] Đã bỏ qua noise / auto / spam
- [ ] Đã xác định đúng tin khách mới nhất
- [ ] Đã xác định đúng tin sale mới nhất
- [ ] Chỉ nhắc khi sale chưa trả lời sau tin khách mới nhất
- [ ] Stage đi tuần tự 1 -> 2 -> 3
- [ ] Wording bằng tiếng Việt hoàn toàn
- [ ] Wording bám sát câu khách đang nói
- [ ] Wording nêu rõ next action cho sale

## C. Escalation
- [ ] Stage 3 remove đúng tag sale cũ
- [ ] Stage 3 add đúng 2 tag sale mới
- [ ] Chỉ coi handoff thành công khi remove/add đều thành công
- [ ] Có log / trạng thái handoff để kiểm tra

## D. Public / thương mại
- [ ] Không còn token thật
- [ ] Không còn page id thật
- [ ] Không còn log thật
- [ ] Không còn state thật
- [ ] Không còn transcript thật
- [ ] Không còn group id nội bộ thật
- [ ] README đủ rõ để agent khác đọc và setup
