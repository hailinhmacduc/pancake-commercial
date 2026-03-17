# Pancake Commercial Skill

GitHub-ready commercial skill for OpenClaw that monitors Pancake/Facebook conversations and reminds sales teams when customers are waiting for a reply.

## What this skill does
- Reads Pancake conversation/message data
- Detects the latest customer request
- Checks whether sales already replied
- Sends reminders in 3 sequential stages: 20 / 40 / 60 minutes
- Performs stage-3 handoff by switching Pancake tags
- Uses Vietnamese reminder wording tied to the customer’s actual message
- Ships as a public-safe package with no real secrets or customer data

## What the downstream OpenClaw agent should ask the user for
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

## Repository structure
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

## Public-safe packaging rules
This repo is safe to publish only if it does **not** include:
- real Pancake tokens
- real page IDs
- real customer transcripts
- real logs
- real state files
- real internal group/chat IDs
- real internal usernames (unless explicitly approved)

## Suggested usage
1. Install/copy the skill into an OpenClaw skill path.
2. Let the downstream OpenClaw agent read `SKILL.md`.
3. The agent should request the missing deployment inputs from the user.
4. Create a private config from `templates/config.pages.example.json`.
5. Extend `templates/pancake_monitor_template.py` into a production script.
6. Run tests/debug first, then attach cron.

## Example required config
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

## Notes
- Keep real secrets outside this repository.
- Prefer env vars or a secret manager for production.
- Review `references/setup-guide.md` and `references/deployment-checklist.md` before handoff.
