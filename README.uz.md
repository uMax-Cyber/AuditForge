<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>

# Xavfsizlik auditini avtomatlashtirish
[![CI](https://github.com/uMax-Cyber/AuditForge/actions/workflows/ci.yml/badge.svg)](https://github.com/uMax-Cyber/AuditForge/actions/workflows/ci.yml)


![Namoyish](screenshots/demo.svg)
Kichik infratuzilma uchun haftalik avtomatlashtirilgan xavfsizlik auditi: SSH brute-force aniqlash, paket yangilanishlarini kuzatish, tarmoq qurilmalari holati, backup yangiqligi va port oʻzgarishlari. Sof Python, faqat stdlib; natija markdown koʻrinishida chiqadi va xohlagan xabar kanaliga yuboriladi.

## Nima tekshiriladi

| Tekshiruv | Usul | Ogohlantirish chegarasi |
|-----------|------|-------------------------|
| SSH brute-force | journalctl auth logini sanash | Haftada 20 dan ortiq muvaffaqiyatsiz urinish |
| Paket yangilanishlari | apt list --upgradable | 100 dan ortiq yangilanish kutilmoqda |
| Qurilma oflayn | Tarmoq kontrolleri API-si | Kamida bitta qurilma online emas |
| Eskirgan proshivka | Kontroller API flagi | firmwareUpdatable = true |
| Fayrvol jonliligi | API health-check | Javob bermasa yoki autentifikatsiya xatosi |
| Backup yangiqligi | Fayl yoshini tekshirish | 14 kundan ortiq backup yoʻq |
| Tinglanayotgan portlar | ss -tlnp farqi | Yangi port paydo boʻlsa |

## Dizayn falsafasi

- **Deterministik**: LLM ham, AI ham yoʻq — sof mantiq, natija har doim bir xil
- **Nol bogʻliqlik**: faqat Python 3.10+ stdlib
- **Kanaldan mustaqil**: markdown stdout-ga chiqadi — Telegram, email yoki Slack-ga oʻtkazib yuborish mumkin
- **Holatsiz**: har ishga tushirish mustaqil, natijalarni vaqt boʻyicha solishtirish mumkin

## Foydalanish

```bash
# Barcha tekshiruvlarni oʻtkazish
./scripts/secaudit.py --all

# Faqat tanlangan tekshiruvlar
./scripts/secaudit.py --check ssh,updates

# Hisobotni faylga yozish (alerting-ga uzatish uchun)
./scripts/secaudit.py --all > report.md
```

## Cron sozlamasi
```bash
# Haftada bir, dushanba soat 09:00
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
