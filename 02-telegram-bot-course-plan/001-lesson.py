# ============================================================
#   DARS 1: Telegram Bot API, Aiogram va Birinchi Bot
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ Telegram Bot API nima
  ✔️ @BotFather orqali bot yaratish
  ✔️ venv, aiogram va python-dotenv
  ✔️ .env va .gitignore xavfsizligi
  ✔️ Polling orqali birinchi Echo Bot

LOYIHA PAPKASI:

telegram_bot/
├── main.py
├── .env
├── .gitignore
└── requirements.txt
"""

# ------------------------------------------------------------
# O‘RNATISH BUYRUQLARI
# ------------------------------------------------------------

"""
1. BotFather’ga kiring: https://t.me/BotFather
2. /newbot yuboring va bot token oling.
3. Project papkasida virtual environment yarating:

Windows:
  python -m venv .venv
  .venv\Scripts\activate

Mac / Linux:
  python3 -m venv .venv
  source .venv/bin/activate

4. Kutubxonalarni o‘rnating:
  python -m pip install aiogram python-dotenv

5. .env fayl yarating:
  BOT_TOKEN=BotFather_bergan_haqiqiy_token

6. .gitignore fayliga yozing:
  .venv/
  .env
  __pycache__/
"""

import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv


# ------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN topilmadi. .env faylni tekshiring.")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# ------------------------------------------------------------
# /start COMMAND
# ------------------------------------------------------------

@dp.message(CommandStart())
async def start_handler(message: Message):
    """Foydalanuvchi /start yuborganda ishlaydi."""
    ism = message.from_user.full_name

    await message.answer(
        f"Assalomu alaykum, {ism}!\n"
        "Men sizning birinchi Aiogram botingizman."
    )


# ------------------------------------------------------------
# ECHO BOT
# ------------------------------------------------------------

@dp.message(F.text)
async def echo_handler(message: Message):
    """Foydalanuvchi yozgan matnni qaytarib yuboradi."""
    await message.answer(f"Siz yozdingiz: {message.text}")


# ------------------------------------------------------------
# BOTNI ISHGA TUSHIRISH
# ------------------------------------------------------------

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. /start xabarini o‘zingizning kurs nomingizga moslang.
2. /start da foydalanuvchining ism va user ID sini chiqaring.
3. Echo bot javobini "Sizning xabaringiz: ..." ko‘rinishida yozing.
4. BotFather orqali bot rasmi va description sozlang.
5. Loyihani GitHub’ga tokenni yuklamasdan joylang.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ Telegram Bot API nima ekanini
✔️ BotFather orqali bot yaratishni
✔️ venv va pip ishlatishni
✔️ .env orqali tokenni xavfsiz saqlashni
✔️ Aiogram bilan Echo Bot yozishni
✔️ Polling orqali botni ishga tushirishni
"""
