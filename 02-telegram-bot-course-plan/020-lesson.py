# ============================================================
#   DARS 20: Botdan Telegram Web App Ochish
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ WebAppInfo
  ✔️ Reply va Inline Web App tugmalari
  ✔️ Menu Button
  ✔️ web_app_data
  ✔️ sendData() qachon ishlatilishi

MUHIM:
web_app tugmasi user va botning private chatida ishlatiladi.
Production URL HTTPS bo‘lishi kerak.
"""

import json

from aiogram import Bot, F, Router
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    MenuButtonWebApp,
    Message,
    ReplyKeyboardMarkup,
    WebAppInfo,
)

router = Router()
WEB_APP_URL = "https://example.com/miniapp"


@router.message(F.text == "/webapp")
async def open_webapp(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🛍 Do‘konni ochish", web_app=WebAppInfo(url=WEB_APP_URL))]],
        resize_keyboard=True,
    )
    await message.answer("Mini App’ni oching:", reply_markup=keyboard)


@router.message(F.text == "/inline_webapp")
async def open_inline_webapp(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="🛒 Mini Store", web_app=WebAppInfo(url=WEB_APP_URL))]]
    )
    await message.answer("Inline tugma orqali oching:", reply_markup=keyboard)


async def set_menu_button(bot: Bot):
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(text="Do‘kon", web_app=WebAppInfo(url=WEB_APP_URL))
    )


@router.message(F.web_app_data)
async def web_app_data_handler(message: Message):
    """sendData() orqali yuborilgan kichik ma’lumotni qabul qiladi."""
    try:
        data = json.loads(message.web_app_data.data)
        await message.answer(f"Web App dan qabul qilindi: {data}")
    except json.JSONDecodeError:
        await message.answer("Web App noto‘g‘ri formatdagi ma’lumot yubordi.")


"""
sendData() faqat kichik, bir martalik ma’lumot uchun qulay.
Masalan: tanlangan kurs IDsi.

Haqiqiy buyurtma, login va database bilan ishlashda frontend initData’ni FastAPI backendga yuboradi.
Backend initData’ni validate qiladi, keyin buyurtmani saqlaydi.

MUSTAQIL MASHQ TOPSHIRIQLARI:
1. /webapp komandasi bilan kursga yozilish Mini App’ini oching.
2. Menu Button sozlang.
3. JavaScript’da tg.sendData(JSON.stringify({course_id: 1})) yuboring.
4. Botda kelgan WebAppData ni JSON sifatida o‘qing.
"""
