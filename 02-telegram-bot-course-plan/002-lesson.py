# ============================================================
#   DARS 2: Asyncio va Aiogram Arxitekturasi
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ async def va await
  ✔️ Bot, Dispatcher va Router
  ✔️ Routerlarni ajratish
  ✔️ Professional loyiha strukturasi
"""

import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv


# ------------------------------------------------------------
# ASYNCIO NIMA?
# ------------------------------------------------------------

"""
Telegram API bilan so‘rov yuborish va javob kutish vaqt oladi.
asyncio botga shu vaqt ichida boshqa foydalanuvchi update’larini ham
qabul qilishga yordam beradi.

async def  → asinxron funksiya
await      → asinxron vazifa tugashini kutish
"""

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()
user_router = Router()


# ------------------------------------------------------------
# ROUTER
# ------------------------------------------------------------

"""
Router handlerlarni mavzu bo‘yicha ajratadi.

Katta loyihada odatda:

app/
├── handlers/
│   ├── user.py
│   ├── admin.py
│   └── errors.py
├── keyboards/
├── services/
├── database/
├── config.py
└── main.py
"""


@user_router.message(Command("about"))
async def about_handler(message: Message):
    await message.answer("Bu bot Aiogram 3 yordamida yozilgan.")


@user_router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer("Mavjud komandalar: /start, /about, /help")


# Router Dispatcher’ga ulanadi
dp.include_router(user_router)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. user_router’dan tashqari admin_router yarating.
2. /admin komandasi uchun handler yozing.
3. Loyihada handlers, keyboards va services papkalarini yarating.
4. Har bir router nima uchun kerakligini izohda yozing.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ async def va await ni
✔️ Bot, Dispatcher va Router farqini
✔️ Handlerlarni routerga yozishni
✔️ Routerni Dispatcher’ga ulashni
✔️ Professional loyiha strukturasi asoslarini
"""
