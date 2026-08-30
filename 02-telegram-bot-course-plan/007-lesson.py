# ============================================================
#   DARS 7: FSM — Storage, Validatsiya va Murakkab Dialog
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ MemoryStorage va RedisStorage
  ✔️ state.clear()
  ✔️ Validatsiya
  ✔️ Ortga va bekor qilish tugmalari
  ✔️ Buyurtma formasi
"""

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

router = Router()

"""
MemoryStorage — faqat development uchun. Bot qayta ishga tushsa, holatlar yo‘qoladi.

Production uchun RedisStorage ishlatiladi:
  python -m pip install "aiogram[redis]"
  from aiogram.fsm.storage.redis import RedisStorage
  storage = RedisStorage.from_url("redis://localhost:6379/0")
"""


class OrderForm(StatesGroup):
    mahsulot = State()
    miqdor = State()
    manzil = State()


@router.message(F.text == "🛒 Buyurtma")
async def order_start(message: Message, state: FSMContext):
    await state.set_state(OrderForm.mahsulot)
    await message.answer("Mahsulot nomini kiriting. Bekor qilish: /cancel")


@router.message(OrderForm.mahsulot, F.text)
async def order_product(message: Message, state: FSMContext):
    await state.update_data(mahsulot=message.text)
    await state.set_state(OrderForm.miqdor)
    await message.answer("Nechta mahsulot kerak?")


@router.message(OrderForm.miqdor, F.text)
async def order_quantity(message: Message, state: FSMContext):
    if not message.text.isdigit() or int(message.text) <= 0:
        await message.answer("Miqdor musbat butun son bo‘lishi kerak.")
        return

    await state.update_data(miqdor=int(message.text))
    await state.set_state(OrderForm.manzil)
    await message.answer("Yetkazib berish manzilini kiriting:")


@router.message(OrderForm.manzil, F.text)
async def order_address(message: Message, state: FSMContext):
    await state.update_data(manzil=message.text)
    data = await state.get_data()
    await message.answer(
        f"Buyurtma qabul qilindi!\n{data['mahsulot']} x {data['miqdor']}\n"
        f"Manzil: {data['manzil']}"
    )
    await state.clear()


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:
1. Buyurtmaga telefon va izoh bosqichlarini qo‘shing.
2. "Ortga" tugmasi bilan oldingi holatga qaytishni yarating.
3. Forma yakunida inline Ha/Yo‘q tasdiqlashini qo‘shing.
4. Buyurtmani database’ga saqlashga tayyorlab qo‘ying.

BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ FSM storage turlarini
✔️ Foydalanuvchi inputini tekshirishni
✔️ Buyurtma formasini
✔️ Production uchun Redis kerakligini
"""
