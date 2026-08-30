# ============================================================
#   DARS 5: Inline Keyboard va Callback Query
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ InlineKeyboardButton
  ✔️ callback_data
  ✔️ CallbackData factory
  ✔️ callback.answer()
  ✔️ edit_text()
  ✔️ Pagination va tasdiqlash tugmalari
"""

from aiogram import F, Router
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


class MenuCallback(CallbackData, prefix="menu"):
    action: str


def inline_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="📚 Kurslar", callback_data=MenuCallback(action="courses"))
    builder.button(text="ℹ️ Biz haqimizda", callback_data=MenuCallback(action="about"))
    builder.button(text="🌐 Sayt", url="https://example.com")
    builder.adjust(2, 1)
    return builder.as_markup()


@router.message(F.text == "/inline")
async def inline_menu_handler(message: Message):
    await message.answer("Kerakli bo‘limni tanlang:", reply_markup=inline_menu())


@router.callback_query(MenuCallback.filter(F.action == "courses"))
async def courses_callback(callback: CallbackQuery):
    await callback.answer("Kurslar ochildi")
    await callback.message.edit_text("Kurslar: Python, Telegram Bot, Backend")


@router.callback_query(MenuCallback.filter(F.action == "about"))
async def about_callback(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Abruisdev Academy — dasturlash kurslari.")


# ------------------------------------------------------------
# HA / YO‘Q TASDIQLASHI
# ------------------------------------------------------------

@router.message(F.text == "/delete")
async def delete_question(message: Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Ha", callback_data="delete:yes")
    builder.button(text="❌ Yo‘q", callback_data="delete:no")
    builder.adjust(2)

    await message.answer("Rostdan o‘chirasizmi?", reply_markup=builder.as_markup())


@router.callback_query(F.data == "delete:yes")
async def delete_yes(callback: CallbackQuery):
    await callback.answer("O‘chirildi")
    await callback.message.edit_text("Ma’lumot o‘chirildi.")


@router.callback_query(F.data == "delete:no")
async def delete_no(callback: CallbackQuery):
    await callback.answer("Bekor qilindi")
    await callback.message.edit_text("O‘chirish bekor qilindi.")


# ------------------------------------------------------------
# SODDA PAGINATION
# ------------------------------------------------------------

MAHSULOTLAR = ["Python kursi", "Telegram Bot kursi", "Backend kursi"]


def pagination_keyboard(sahifa):
    builder = InlineKeyboardBuilder()

    if sahifa > 0:
        builder.button(text="⬅️", callback_data=f"page:{sahifa - 1}")

    if sahifa < len(MAHSULOTLAR) - 1:
        builder.button(text="➡️", callback_data=f"page:{sahifa + 1}")

    return builder.as_markup()


@router.message(F.text == "/catalog")
async def catalog_handler(message: Message):
    await message.answer(MAHSULOTLAR[0], reply_markup=pagination_keyboard(0))


@router.callback_query(F.data.startswith("page:"))
async def page_handler(callback: CallbackQuery):
    sahifa = int(callback.data.split(":")[1])
    await callback.answer()
    await callback.message.edit_text(MAHSULOTLAR[sahifa], reply_markup=pagination_keyboard(sahifa))


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. 3 ta inline tugmali menyu yarating.
2. CallbackData yordamida product_id uzating.
3. 5 ta mahsulotli pagination yarating.
4. "Savatga qo‘shish" va "Ortga" tugmalarini yozing.
5. callback.answer() ishlatilmasa, Telegram’da nima bo‘lishini tekshiring.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ Inline Keyboard yaratishni
✔️ callback_data bilan ma’lumot uzatishni
✔️ CallbackData factory ishlatishni
✔️ Xabarni edit qilishni
✔️ Tasdiqlash va pagination yaratishni
"""
