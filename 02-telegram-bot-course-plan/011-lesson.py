# ============================================================
#   DARS 11: Media, Deep Link va Chat Imkoniyatlari
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ Rasm, video va fayl yuborish
  ✔️ Foydalanuvchi faylini yuklab olish
  ✔️ Media Group
  ✔️ Bot komandalarini sozlash
  ✔️ Deep link
  ✔️ Kanalga a’zolikni tekshirish
"""

from aiogram import Bot, F, Router
from aiogram.filters import Command
from aiogram.types import BotCommand, FSInputFile, Message
from aiogram.utils.deep_linking import create_start_link

router = Router()


@router.message(Command("photo"))
async def send_photo_handler(message: Message):
    photo = FSInputFile("assets/python.png")
    await message.answer_photo(photo, caption="Python Foundation kursi")


@router.message(F.document)
async def download_document_handler(message: Message, bot: Bot):
    document = message.document
    await bot.download(document, destination=f"downloads/{document.file_name}")
    await message.answer("Fayl yuklab olindi.")


async def set_commands(bot: Bot):
    await bot.set_my_commands([
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="profile", description="Profil"),
        BotCommand(command="help", description="Yordam"),
    ])


@router.message(Command("referral"))
async def referral_handler(message: Message, bot: Bot):
    link = await create_start_link(bot, payload=str(message.from_user.id), encode=True)
    await message.answer(f"Sizning referral havolangiz:\n{link}")


@router.message(Command("check"))
async def membership_handler(message: Message, bot: Bot):
    channel_id = "@sizning_kanalingiz"
    member = await bot.get_chat_member(channel_id, message.from_user.id)

    if member.status in {"member", "administrator", "creator"}:
        await message.answer("Siz kanal a’zosiz.")
    else:
        await message.answer("Avval kanalga a’zo bo‘ling.")


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:
1. /video komandasi bilan video yuboring.
2. Foydalanuvchi yuborgan rasmni downloads/ papkasiga yuklab oling.
3. Bot komandalarini startup vaqtida sozlang.
4. Referral parametrini /start ichida qabul qiling va database’ga saqlang.
5. Kanalga a’zo bo‘lmagan foydalanuvchini asosiy menyuga o‘tkazmang.
"""
