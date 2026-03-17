# Pancake Commercial Skill

[🇻🇳 Tiếng Việt](#-tiếng-việt) | [🇬🇧 English](#-english)

---

## 🇻🇳 Tiếng Việt

Kỹ năng thương mại (commercial skill) dành cho OpenClaw, dùng để theo dõi hội thoại Pancake/Facebook và nhắc nhở đội sales khi khách hàng đang chờ phản hồi.

### Tính năng chính
- Đọc dữ liệu hội thoại/tin nhắn từ Pancake
- Phát hiện yêu cầu mới nhất của khách hàng
- Kiểm tra xem sales đã trả lời chưa
- Gửi nhắc nhở theo 3 giai đoạn: 20 / 40 / 60 phút
- Chuyển giao giai đoạn 3 bằng cách đổi tag trên Pancake
- Nội dung nhắc nhở bằng tiếng Việt, gắn liền với tin nhắn thực tế của khách
- Đóng gói an toàn, không chứa bí mật hay dữ liệu khách hàng thật

### Thông tin agent OpenClaw cần thu thập từ người dùng
Trước khi triển khai, agent cần yêu cầu các thông tin bắt buộc sau:
- `page_id` cho mỗi trang cần theo dõi
- `page_access_token` hoặc Pancake API token
- Bảng ánh xạ sales: `sale -> tag_id -> tài khoản nhận cảnh báo`
- Kênh nhận cảnh báo (Telegram / Slack / Discord / chat nội bộ)
- Lịch chạy cron
- Múi giờ hoạt động

Tùy chọn (khuyến nghị):
- Giờ làm việc
- Phong cách thương hiệu / tuỳ chỉnh nội dung nhắc nhở
- Mẫu tin nhắn tự động / nhiễu cần bỏ qua
- Quy tắc nhận diện ý định theo ngành

### Cấu trúc thư mục
- `SKILL.md` — hướng dẫn chính cho OpenClaw
- `README.md` — tổng quan trên GitHub
- `install.md` — hướng dẫn cài đặt/chia sẻ
- `ONBOARDING_TEMPLATE.md` — checklist onboarding khách hàng
- `INPUT_FORM.md` — form thông số triển khai bắt buộc
- `RELEASE_NOTES.md` — tóm tắt phiên bản
- `LICENSE` — giấy phép MIT
- `references/` — quy tắc nghiệp vụ, kiến trúc, hướng dẫn cài đặt, bảo mật, checklist
- `templates/config.pages.example.json` — file cấu hình mẫu với placeholder
- `templates/pancake_monitor_template.py` — template triển khai sạch
- `.gitignore` — ngăn commit các file bí mật/trạng thái/log

### Hướng dẫn sử dụng
1. Cài đặt/copy skill vào đường dẫn skill của OpenClaw.
2. Cho agent OpenClaw đọc `SKILL.md`.
3. Agent sẽ yêu cầu người dùng cung cấp các thông số triển khai còn thiếu.
4. Tạo file cấu hình riêng từ `templates/config.pages.example.json`.
5. Mở rộng `templates/pancake_monitor_template.py` thành script production.
6. Chạy test/debug trước, sau đó gắn cron.

### Ví dụ cấu hình
```json
{
  "pages": {
    "example-page": {
      "page_id": "YOUR_PAGE_ID",
      "page_access_token": "YOUR_PAGE_ACCESS_TOKEN"
    }
  },
  "staff": {
    "SALE_A": {
      "telegram": "@sale_a",
      "tag_id": 101,
      "name": "Sale A"
    }
  }
}
```

### Lưu ý
- Giữ các bí mật thật bên ngoài repository này.
- Nên sử dụng biến môi trường hoặc secret manager cho production.
- Xem lại `references/setup-guide.md` và `references/deployment-checklist.md` trước khi bàn giao.

### Quy tắc an toàn khi công khai
Repo này chỉ an toàn để công khai khi **không** chứa:
- Token Pancake thật
- Page ID thật
- Đoạn hội thoại khách hàng thật
- Log thật
- File trạng thái thật
- ID nhóm/chat nội bộ thật
- Tên tài khoản nội bộ thật (trừ khi được phê duyệt)

---

## 🇬🇧 English

GitHub-ready commercial skill for OpenClaw that monitors Pancake/Facebook conversations and reminds sales teams when customers are waiting for a reply.

### What this skill does
- Reads Pancake conversation/message data
- Detects the latest customer request
- Checks whether sales already replied
- Sends reminders in 3 sequential stages: 20 / 40 / 60 minutes
- Performs stage-3 handoff by switching Pancake tags
- Uses Vietnamese reminder wording tied to the customer's actual message
- Ships as a public-safe package with no real secrets or customer data

### What the downstream OpenClaw agent should ask the user for
Before deployment, the agent should ask for these required inputs:
- `page_id` for each monitored page
- `page_access_token` or Pancake API token
- sales mapping: `sale -> tag_id -> alert destination account`
- alert destination (Telegram / Slack / Discord / internal chat)
- cron schedule
- operating timezone

Optional but recommended:
- working hours
- brand voice / reminder wording preferences
- noise / auto-message patterns to ignore
- industry-specific intent rules

### Repository structure
- `SKILL.md` — main skill instructions for OpenClaw
- `README.md` — GitHub-facing overview
- `install.md` — installation/share flow
- `ONBOARDING_TEMPLATE.md` — customer onboarding checklist/form
- `INPUT_FORM.md` — required deployment parameters form
- `RELEASE_NOTES.md` — version summary
- `LICENSE` — MIT license
- `references/` — business rules, architecture, setup, security, checklist
- `templates/config.pages.example.json` — example config with placeholders
- `templates/pancake_monitor_template.py` — clean implementation template
- `.gitignore` — prevents committing secrets/state/logs

### Public-safe packaging rules
This repo is safe to publish only if it does **not** include:
- real Pancake tokens
- real page IDs
- real customer transcripts
- real logs
- real state files
- real internal group/chat IDs
- real internal usernames (unless explicitly approved)

### Suggested usage
1. Install/copy the skill into an OpenClaw skill path.
2. Let the downstream OpenClaw agent read `SKILL.md`.
3. The agent should request the missing deployment inputs from the user.
4. Create a private config from `templates/config.pages.example.json`.
5. Extend `templates/pancake_monitor_template.py` into a production script.
6. Run tests/debug first, then attach cron.

### Example required config
```json
{
  "pages": {
    "example-page": {
      "page_id": "YOUR_PAGE_ID",
      "page_access_token": "YOUR_PAGE_ACCESS_TOKEN"
    }
  },
  "staff": {
    "SALE_A": {
      "telegram": "@sale_a",
      "tag_id": 101,
      "name": "Sale A"
    }
  }
}
```

### Notes
- Keep real secrets outside this repository.
- Prefer env vars or a secret manager for production.
- Review `references/setup-guide.md` and `references/deployment-checklist.md` before handoff.
