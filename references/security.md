# Security / Commercial Packaging

## Không được đóng gói các dữ liệu sau
- token Pancake thật
- page_access_token thật
- page_id thật của khách hàng
- file state thật
- log vận hành thật
- transcript khách hàng thật
- chat id nhóm nội bộ thật
- telegram usernames nội bộ thật nếu không được phép chia sẻ

## Nên thay bằng
- config mẫu
- placeholder values
- fake sample ids
- fake sample staff mapping
- ví dụ message đã ẩn danh

## Khi bán skill
- cung cấp template + docs + script mẫu
- khách hàng tự điền token / page id của họ
- khuyến nghị lưu secrets qua env hoặc secret manager
- không hard-code dữ liệu thật trong source
