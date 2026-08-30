# ============================================================
#   DARS 6: FSM — Holatlar Mashinasi I qism
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
FSM — Finite State Machine. U foydalanuvchi bilan ko‘p bosqichli suhbat yoki forma yaratish uchun kerak.

BUGUNGI DARSDA:
  ✔️ StatesGroup va State
  ✔️ FSMContext
  ✔️ set_state, update_data, get_data
  ✔️ Ro‘yxatdan o‘tish formasi
"""

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

router = Router()


class Registration(StatesGroup):
    ism = State()
    yosh = State()
    telefon = State()


@router.message(Command("register"))
async def register_start(message: Message, state: FSMContext):
    await state.set_state(Registration.ism)
    await message.answer("Ismingizni kiriting:")


@router.message(Registration.ism, F.text)
async def get_ism(message: Message, state: FSMContext):
    await state.update_data(ism=message.text.strip().title())
    await state.set_state(Registration.yosh)
    await message.answer("Yoshingizni kiriting:")


@router.message(Registration.yosh, F.text)
async def get_yosh(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Yosh butun son bo‘lishi kerak.")
        return

    await state.update_data(yosh=int(message.text))
    await state.set_state(Registration.telefon)
    await message.answer("Telefon raqamingizni kiriting:")


@router.message(Registration.telefon, F.text)
async def get_telefon(message: Message, state: FSMContext):
    telefon = message.text.replace(" ", "").replace("-", "")

    if not telefon.startswith("+998") or not telefon[1:].isdigit():
        await message.answer("Telefon raqam noto‘g‘ri. Masalan: +998901234567")
        return

    await state.update_data(telefon=telefon)
    data = await state.get_data()

    await message.answer(
        "Ro‘yxatdan o‘tish tugadi!\n"
        f"Ism: {data['ism']}\n"
        f"Yosh: {data['yosh']}\n"
        f"Telefon: {data['telefon']}"
    )
    await state.clear()


@router.message(Command("cancel"))
async def cancel_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Jarayon bekor qilindi.")


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:
1. /register formasiga shahar bosqichini qo‘shing.
2. /cancel ni faqat holatda bo‘lgan foydalanuvchi uchun ishlating.
3. Telefon o‘rniga request_contact Reply Keyboard ishlating.
4. Yakunda foydalanuvchi ma’lumotlarini JSON faylga saqlang.

BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ FSM nima ekanini
✔️ State va StatesGroup yaratishni
✔️ state ichiga ma’lumot saqlashni
✔️ Ko‘p bosqichli forma yaratishni
✔️ state.clear() bilan jarayonni tugatishni
"""
