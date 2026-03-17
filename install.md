# Install / Share Guide

## Goal
Share this repository or zip file so another OpenClaw instance can copy the skill into its skills directory.

## Recommended flow
1. Clone or download this repository/zip.
2. Place the `pancake-commercial/` folder into the target machine's skills directory.
3. Ask OpenClaw to use the skill for Pancake reminder / sales escalation tasks.
4. OpenClaw should read `SKILL.md` and request the missing inputs from the user.

## Inputs the receiving user must provide
- `page_id`
- `page_access_token` or Pancake API token
- staff mapping (`sale -> tag_id -> alert account`)
- alert destination
- cron schedule
- timezone

## Do not include in the shared package
- real secrets
- real customer logs
- real transcripts
- runtime state files
