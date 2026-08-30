# ============================================================
#   DARS 14: Deploy, Docker va Webhook
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ Polling va Webhook
  ✔️ Docker
  ✔️ VPS va systemd
  ✔️ HTTPS
  ✔️ Production checklist

Polling — development yoki oddiy botlar uchun qulay.
Webhook — production uchun samarali, lekin HTTPS talab qiladi.
"""

"""
Dockerfile namunasi:

FROM python:3.14-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]

docker-compose.yml namunasi:

services:
  bot:
    build: .
    env_file: .env
    restart: unless-stopped
  postgres:
    image: postgres:17
    environment:
      POSTGRES_DB: bot_db
      POSTGRES_USER: bot_user
      POSTGRES_PASSWORD: change_me
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
"""

"""
PRODUCTION CHECKLIST:
  ✔️ Token .env’da saqlangan.
  ✔️ .env GitHub’da yo‘q.
  ✔️ PostgreSQL backup rejalashtirilgan.
  ✔️ Logging ishlayapti.
  ✔️ HTTPS sozlangan.
  ✔️ Docker container qayta ishga tushadi.
  ✔️ Webhook URL maxfiy path bilan ishlaydi.
"""


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:
1. Bot uchun Dockerfile yarating.
2. docker compose up --build bilan lokal ishga tushiring.
3. VPS va domen tanlash bo‘yicha reja yozing.
4. Polling va Webhookning 3 tadan farqini yozing.
"""
