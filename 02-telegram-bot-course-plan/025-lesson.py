# ============================================================
#   DARS 25: Bot + Mini App Deploy
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ Bot, FastAPI va PostgreSQL arxitekturasi
  ✔️ Docker Compose
  ✔️ HTTPS va Nginx
  ✔️ Production xavfsizligi

ARXITEKTURA:

Telegram → Aiogram Bot
                 ↓
           FastAPI API ← Telegram Mini App
                 ↓
             PostgreSQL
"""

"""
docker-compose.yml namunasi:

services:
  api:
    build: .
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000
    env_file: .env
    restart: unless-stopped
  bot:
    build: .
    command: python -m app.bot_main
    env_file: .env
    restart: unless-stopped
  postgres:
    image: postgres:17
    env_file: .env
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
"""

"""
NGINX VAZIFASI:
  ✔️ https://miniapp.example.com ga HTTPS beradi.
  ✔️ /api so‘rovlarini FastAPI’ga uzatadi.
  ✔️ Static index.html, CSS va JS fayllarini beradi.

PRODUCTION CHECKLIST:
  ✔️ HTTPS sertifikat ishlayapti.
  ✔️ BOT_TOKEN faqat .env’da.
  ✔️ PostgreSQL backup bor.
  ✔️ CORS faqat kerakli domen uchun.
  ✔️ initData backendda tekshiriladi.
  ✔️ Loglar yozilyapti.
  ✔️ Docker containerlar restart policy bilan ishlaydi.
"""


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:
1. Lokal Docker Compose bilan api va database’ni ishga tushiring.
2. Domena kerak bo‘ladigan qismlarni yozib chiqing.
3. Mini App HTTPSsiz nima uchun ochilmasligini tekshiring.
4. Production checklistni o‘z loyihangizga qo‘llang.
"""
