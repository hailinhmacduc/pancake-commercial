# Pancake Commercial Rules

## 1. Nguồn dữ liệu
- Dữ liệu lấy từ API Pancake conversations + messages.
- Timestamp từ API phải được convert sang giờ Việt Nam trước khi tính toán wait time.
- Nếu timestamp không có timezone, coi là UTC rồi convert sang `Asia/Saigon`.

## 2. Cách xác định hội thoại cần nhắc
- Chỉ xét các hội thoại unread / cần xử lý.
- Xác định tin khách mới nhất.
- Xác định tin sale mới nhất.
- Nếu sale đã trả lời sau tin khách mới nhất thì không nhắc.
- Chỉ nhắc khi có nhu cầu thật sự, không nhắc chat rác / auto / noise.

## 3. Noise / chat rác
Các case sau cần bỏ qua:
- lời chào tự động
- tin hệ thống
- spam
- câu vô nghĩa / không có nhu cầu rõ ràng
- hội thoại không đủ dữ kiện để xác định next action

## 4. Intent chính
- `price_quote`
- `availability`
- `shipping`
- `installment`
- `repair_warranty`
- `closing`
- `product_consult`
- `general`

## 5. Rule wording
- Viết hoàn toàn bằng tiếng Việt.
- Bám sát đúng câu khách đang nói.
- Nêu rõ sale cần làm gì tiếp theo.
- Không dùng wording nửa Anh nửa Việt như `lead`, `follow`, `case cần xử lý`.

## 6. 3 giai đoạn nhắc
### Lần 1 — 20 phút
- Nhắc nhẹ
- Nêu câu khách đang hỏi
- Nêu next action cụ thể cho sale

### Lần 2 — 40 phút
- Giọng mạnh hơn
- Nói rõ khách đã chờ lâu
- Cảnh báo nếu sale không trả lời thì chuẩn bị chuyển người khác xử lý

### Lần 3 — 60 phút
- Chỉ được lên lần 3 sau khi đã đi qua lần 1 và lần 2
- Không được nhảy cóc stage
- Nói rõ đã nhắc trước đó
- Chuyển hội thoại sang 2 sale còn lại
- Remove tag sale cũ trên Pancake
- Add 2 tag sale mới

## 7. Logic stage tuần tự
- `desired_stage` = stage theo số phút chờ
- `actual_stage = min(desired_stage, last_notified_stage + 1)`
- Bắt buộc đi theo thứ tự: `1 -> 2 -> 3`

## 8. Handoff tag trên Pancake
Khi đến lần nhắc 3:
1. Remove đúng tag sale đang bị gán
2. Add 2 tag sale còn lại
3. Chỉ coi là handoff thành công nếu remove + add đều thành công
4. Phải log rõ trạng thái handoff

## 9. Rule thời gian
- Thời gian hiển thị trong alert phải là giờ Việt Nam.
- Không hard-code kiểu `đã chờ 1 tiếng` nếu thực tế wait time dài hơn / ngắn hơn.
- Alert phải phản ánh đúng wait time thật.

## 10. Rule an toàn
- Nếu dữ liệu hội thoại không đáng tin cậy hoặc API trả thiếu timeline cuối, ưu tiên không nhắc hơn là nhắc oan.
