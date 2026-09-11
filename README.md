# Security Audit Automation
[![CI](https://github.com/uMax-Cyber/AuditForge/actions/workflows/ci.yml/badge.svg)](https://github.com/uMax-Cyber/AuditForge/actions/workflows/ci.yml)

Weekly automated security audit for small infrastructure: SSH brute-force detection, package update tracking, network device state, backup freshness, and port change detection. Pure Python, stdlib only, outputs to any messaging channel.

## What It Checks

| Check | Method | Alert Threshold |
|-------|--------|----------------|
| SSH brute-force | journalctl auth log count | > 20 failures/week |
| Package updates | apt list --upgradable | > 100 pending |
| Device offline | Network controller API | Any device not online |
| Firmware outdated | Controller API flag | firmwareUpdatable = true |
| Firewall liveness | API health check | Unreachable or auth failure |
| Backup freshness | File age check | No backup in 14 days |
| Listening ports | ss -tlnp diff | New ports appeared |

## Design Philosophy

- **Deterministic**: No LLM, no AI — pure logic, always reproducible
- **Zero dependencies**: Python 3.10+ stdlib only
- **Channel-agnostic**: Outputs markdown to stdout — pipe to Telegram/email/Slack
- **Stateless**: Each run is independent; results are comparable across time

## Usage

```bash
# Run all checks
./scripts/secaudit.py --all

# Specific check only
./scripts/secaudit.py --check ssh,updates

# Output to file (for piping to alerting)
./scripts/secaudit.py --all > report.md
```

## Cron Setup
```bash
# Weekly Monday 09:00
0 9 * * 1 /opt/secaudit/scripts/secaudit.sh 2>/dev/null
```

## License
MIT
