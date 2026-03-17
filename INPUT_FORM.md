# Input Form — Required Deployment Parameters

Give this form to the receiving user so OpenClaw or the operator can collect everything needed to activate the skill.

## Required inputs

### 1. Page configuration
For each page, provide:
- `page_id`
- `page_access_token` or Pancake API token

Example:
```json
{
  "pages": {
    "example-page": {
      "page_id": "YOUR_PAGE_ID",
      "page_access_token": "YOUR_PAGE_ACCESS_TOKEN"
    }
  }
}
```

### 2. Sales mapping
For each salesperson, provide:
- internal key
- display name
- Pancake `tag_id`
- alert destination account

Example:
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

### 3. Alert destination
Provide:
- platform (`Telegram`, `Slack`, `Discord`, ...)
- channel / group / thread ID
- mention style

### 4. Scheduler
Provide:
- cron schedule
- timezone
- working hours (optional but recommended)

Example:
```bash
15,35,55 8-19 * * *
```

## Optional inputs
- brand voice / reminder tone
- noise patterns to ignore
- industry-specific intent rules
- outside-hours escalation policy

## Minimal handoff bundle
A deployment is considered minimally complete only when all of these are available:
- [ ] `page_id`
- [ ] token
- [ ] sales mapping
- [ ] alert destination
- [ ] cron schedule
- [ ] timezone
