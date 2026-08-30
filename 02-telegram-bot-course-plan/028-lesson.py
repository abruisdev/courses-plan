# ============================================================
#   DARS 28: Amaliy Loyiha — Mini Store Web App
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
YAKUNIY MINI APP LOYIHASI:

Telegram ichida ochiladigan online do‘kon yoki kursga yozilish Mini App’i.

TEXNOLOGIYALAR:
  Frontend: HTML, CSS, JavaScript, Telegram WebApp API
  Backend: FastAPI, Pydantic
  Database: PostgreSQL, SQLAlchemy Async
  Bot: Aiogram 3
  Deploy: Docker, HTTPS, Nginx

PAPKALAR STRUKTURASI:

mini_store/
├── app/
│   ├── api/
│   ├── bot/
│   ├── database/
│   ├── services/
│   ├── security.py
│   └── main.py
├── webapp/
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .env.example
"""

"""
MAJBURIY FUNKSIYALAR:
  ✔️ Botda "Do‘konni ochish" Web App tugmasi.
  ✔️ Mini App’da mahsulotlar katalogi.
  ✔️ Savat va jami narx.
  ✔️ Telegram initData backendda validatsiya qilinishi.
  ✔️ Buyurtma PostgreSQL’ga saqlanishi.
  ✔️ Admin botiga yangi buyurtma yuborilishi.
  ✔️ HTTPS’da deploy qilinishi.

BAHOLASH:
  Frontend UX va mobile UI        — 20 ball
  Telegram WebApp API             — 15 ball
  Backend va initData security    — 25 ball
  Database va buyurtma logikasi   — 20 ball
  GitHub, README, deploy          — 20 ball
"""
