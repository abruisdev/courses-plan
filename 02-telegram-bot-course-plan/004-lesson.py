# ============================================================
#   DARS 4: Reply Keyboard — Oddiy Klaviaturalar
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ ReplyKeyboardMarkup va KeyboardButton
  ✔️ ReplyKeyboardBuilder
  ✔️ resize_keyboard va input_field_placeholder
  ✔️ Kontakt va lokatsiya so‘rash
  ✔️ ReplyKeyboardRemove
"""

from aiogram import F, Router
from aiogram.types import KeyboardButton, Message, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router()


def asosiy_menu():
    """Botning asosiy Reply Keyboard menyusini qaytaradi."""
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text="📚 Kurslar"),
        KeyboardButton(text="💰 Narxlar"),
        KeyboardButton(text="📞 Kontakt"),
        KeyboardButton(text="📍 Manzil"),
    )
    builder.adjust(2, 2)

    return builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Menyudan tanlang...",
    )


@router.message(F.text == "/menu")
async def menu_handler(message: Message):
    await message.answer("Asosiy menyu:", reply_markup=asosiy_menu())


@router.message(F.text == "📚 Kurslar")
async def kurslar_handler(message: Message):
    await message.answer("Python Foundation, Telegram Bot va Backend kurslari mavjud.")


@router.message(F.text == "💰 Narxlar")
async def narxlar_handler(message: Message):
    await message.answer("Narxlar uchun administrator bilan bog‘laning.")


@router.message(F.text == "📞 Kontakt")
async def contact_request_handler(message: Message):
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(KeyboardButton(text="☎️ Raqamni yuborish", request_contact=True))
    keyboard.add(KeyboardButton(text="❌ Bekor qilish"))

    await message.answer(
        "Telefon raqamingizni yuboring:",
        reply_markup=keyboard.as_markup(resize_keyboard=True),
    )


@router.message(F.contact)
async def contact_handler(message: Message):
    await message.answer(
        "Telefon raqamingiz qabul qilindi.",
        reply_markup=asosiy_menu(),
    )


@router.message(F.text == "📍 Manzil")
async def location_request_handler(message: Message):
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(KeyboardButton(text="📍 Lokatsiya yuborish", request_location=True))
    keyboard.add(KeyboardButton(text="❌ Bekor qilish"))

    await message.answer("Lokatsiyangizni yuboring:", reply_markup=keyboard.as_markup(resize_keyboard=True))


@router.message(F.text == "❌ Bekor qilish")
async def cancel_handler(message: Message):
    await message.answer("Bekor qilindi.", reply_markup=ReplyKeyboardRemove())


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. 6 tugmali asosiy menyu yarating.
2. "Biz haqimizda" tugmasi uchun handler yozing.
3. ReplyKeyboardRemove bilan klaviaturani olib tashlang.
4. Foydalanuvchidan request_contact orqali telefon oling.
"""
