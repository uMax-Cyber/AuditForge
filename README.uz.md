<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>

# Xavfsizlik auditini avtomatlashtirish
[![CI](https://github.com/uMax-Cyber/AuditForge/actions/workflows/ci.yml/badge.svg)](https://github.com/uMax-Cyber/AuditForge/actions/workflows/ci.yml)


![Namoyish](screenshots/demo.svg)
Kichik infratuzilma uchun haftalik avtomatlashtirilgan xavfsizlik auditi: SSH brute-force aniqlash, paket yangilanishlarini kuzatish, tarmoq qurilmalari holati, backup yangiqligi va port oʻzgarishlarini aniqlash. Sof Python, faqat stdlib, chiqish har qanday xabar kanaliga.

## Nima tekshiriladi

| Tekshiruv | Usul | Ogohlantirish chegarasi |
|-----------|------|-------------------------|
| SSH brute-force | journalctl auth logidagi yozuvlar soni | > 20 muvaffaqiyatsiz/hafta |
| Paket yangilanishlari | apt list --upgradable | > 100 kutilmoqda |
| Qurilma oflayn | Tarmoq kontrolleri API-si | Har qanday qurilma online emas |
| Eskirgan proshivka | Kontroller API flagi | firmwareUpdatable = true |
| Fayrvol tirikligi | API salomatlik tekshiruvi | Erishib boʻlmaydi yoki autentifikatsiya xatosi |
| Backup yangiqligi | Fayl yoshi tekshiruvi | 14 kundan beri backup yoʻq |
| Tinglanayotgan portlar | ss -tlnp diff | Yangi portlar paydo boʻldi |

## Dizayn falsafasi

- **Deterministik**: LLM yoʻq, AI yoʻq — sof mantiq, har doim takrorlanadigan natija
- **Nol bogʻliqlik**: faqat Python 3.10+ stdlib
- **Kanaldan mustaqil**: stdout-ga markdown chiqaradi — Telegram/email/Slack-ga yuboring
- **Holatsiz**: har ishga tushirish mustaqil; natijalar vaqt boʻyicha solishtiriladi

## Foydalanish

```bash
# Barcha tekshiruvlarni ishga tushirish
./scripts/secaudit.py --all

# Faqat muayyan tekshiruv
./scripts/secaudit.py --check ssh,updates

# Faylga chiqarish (alerting-ga uzatish uchun)
./scripts/secaudit.py --all > report.md
```

## Cron sozlamasi
```bash
# Haftada bir, dushanba 09:00
0 9 * * 1 /opt/secaudit/scripts/secaudit.sh 2>/dev/null
```

## Litsenziya
MIT

## 📬 Aloqa

Savollaringiz bormi? Yozing: **[allumaxmail@gmail.com](mailto:allumaxmail@gmail.com)**

---

<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>
