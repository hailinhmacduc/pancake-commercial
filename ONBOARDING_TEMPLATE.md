# Onboarding Template — Pancake Commercial Skill

Use this form when onboarding a new customer/project.

## 1) Customer profile
- Customer / brand name:
- Industry:
- Main contact:
- Technical contact:
- Go-live target date:

## 2) Pages to monitor
List every Pancake/Facebook page that should be monitored.

| Page label | Page ID | Notes |
|---|---|---|
| example-page | YOUR_PAGE_ID | Main sales page |

## 3) API access
- Pancake API token / Page access token provided: Yes / No
- Secret delivery method: env / secret manager / private config file
- Who is responsible for storing secrets:

## 4) Sales mapping
Map each salesperson to Pancake tags and notification destination.

| Sale name | Internal key | Pancake tag_id | Alert destination | Backup / escalation notes |
|---|---|---:|---|---|
| Sale A | SALE_A | 101 | @sale_a | Backup: Sale B |

## 5) Alert destination
- Platform: Telegram / Slack / Discord / Other
- Channel / group / thread ID:
- Mention format:
- Send individual alerts, grouped alerts, or both:

## 6) Runtime schedule
- Cron schedule:
- Timezone:
- Working hours:
- Weekend policy:
- Outside-hours behavior:

## 7) Reminder behavior
- Stage 1 timing (default 20m):
- Stage 2 timing (default 40m):
- Stage 3 timing (default 60m):
- Escalation enabled at stage 3: Yes / No
- Handoff target rule:

## 8) Brand voice / wording
- Tone of voice:
- Formality level:
- Example reminder wording the customer likes:
- Words/phrases to avoid:

## 9) Noise filtering
List messages that should be ignored.

Examples:
- auto greetings
- system messages
- spam
- low-signal acknowledgements (`ok`, `dạ`, `vâng`)

Customer-specific noise rules:
- 
- 
- 

## 10) Industry-specific intent rules
Examples:
- asking price
- stock / availability
- shipping / address
- installment
- warranty / repair
- closing / ready to buy

Customer-specific intent notes:
- 
- 
- 

## 11) Acceptance checklist
- [ ] Required inputs collected
- [ ] Placeholder config prepared
- [ ] Secrets stored privately
- [ ] Reminder wording reviewed
- [ ] Debug test completed
- [ ] Cron enabled
- [ ] First-day monitoring owner assigned
