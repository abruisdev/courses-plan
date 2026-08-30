# ============================================================
#   DARS 3: Komandalar, Xabarlar va Filterlar
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ CommandStart va Command filterlari
  ✔️ F.text, F.photo, F.document, F.contact, F.location
  ✔️ message.answer va message.reply
  ✔️ HTML parse mode
  ✔️ Filterlarni & | ~ bilan birlashtirish
"""

from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

router = Router()


# ------------------------------------------------------------
# KOMANDALAR
# ------------------------------------------------------------

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Botga xush kelibsiz!")


@router.message(Command("profile"))
async def profile_handler(message: Message):
    user = message.from_user
    await message.answer(
        f"<b>Ism:</b> {user.full_name}\n"
        f"<b>ID:</b> <code>{user.id}</code>",
        parse_mode=ParseMode.HTML,
    )


# ------------------------------------------------------------
# MATN VA CONTENT TURLARI
# ------------------------------------------------------------

@router.message(F.text == "Salom")
async def salom_handler(message: Message):
    await message.reply("Assalomu alaykum!")


@router.message(F.text.startswith("/kurs"))
async def kurs_handler(message: Message):
    await message.answer("Python, Telegram Bot va Backend kurslari mavjud.")


@router.message(F.photo)
async def photo_handler(message: Message):
    file_id = message.photo[-1].file_id
    await message.answer(f"Rasm qabul qilindi. File ID: <code>{file_id}</code>", parse_mode=ParseMode.HTML)


@router.message(F.document)
async def document_handler(message: Message):
    await message.answer(f"Fayl qabul qilindi: {message.document.file_name}")


@router.message(F.contact)
async def contact_handler(message: Message):
    await message.answer(f"Telefon raqam: {message.contact.phone_number}")


@router.message(F.location)
async def location_handler(message: Message):
    location = message.location
    await message.answer(f"Lokatsiya: {location.latitude}, {location.longitude}")


# ------------------------------------------------------------
# FILTERLARNI BIRLASHTIRISH
# ------------------------------------------------------------

@router.message(F.text & F.text.contains("python"))
async def python_matn_handler(message: Message):
    await message.answer("Siz Python haqida yozdingiz!")


@router.message(F.text & ~F.text.startswith("/"))
async def oddiy_matn_handler(message: Message):
    await message.answer("Bu oddiy matnli xabar.")


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. /contact komandasi bilan o‘quv markazi telefonini chiqaring.
2. F.video uchun handler yozing.
