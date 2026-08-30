# ============================================================
#   DARS 26: Amaliy Loyiha — To-do / Eslatma Boti
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
LOYIHA MAQSADI:
Foydalanuvchi vazifa qo‘shadi, ko‘radi, bajarilgan deb belgilaydi
va o‘chiradi.

MAJBURIY TEXNOLOGIYALAR:
  ✔️ Aiogram Router
  ✔️ Inline Keyboard
  ✔️ PostgreSQL + SQLAlchemy
  ✔️ FSM
  ✔️ APScheduler (bonus: eslatma)
"""

from aiogram import F, Router
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


class TodoCallback(CallbackData, prefix="todo"):
    action: str
    todo_id: int


def todo_keyboard(todo_id: int, completed: bool):
    builder = InlineKeyboardBuilder()

    if not completed:
        builder.button(text="✅ Bajarildi", callback_data=TodoCallback(action="complete", todo_id=todo_id))

    builder.button(text="🗑 O‘chirish", callback_data=TodoCallback(action="delete", todo_id=todo_id))
    return builder.as_markup()


@router.message(F.text == "➕ Vazifa qo‘shish")
async def create_todo_start(message: Message):
    """Bu yerda FSM boshlanadi va vazifa nomi olinadi."""
    await message.answer("Vazifa nomini kiriting:")


@router.callback_query(TodoCallback.filter(F.action == "complete"))
async def complete_todo(callback: CallbackQuery, callback_data: TodoCallback):
    # todo_service.complete(todo_id=callback_data.todo_id, user_id=callback.from_user.id)
    await callback.answer("Vazifa bajarildi")
    await callback.message.edit_text("✅ Vazifa bajarildi")


@router.callback_query(TodoCallback.filter(F.action == "delete"))
async def delete_todo(callback: CallbackQuery, callback_data: TodoCallback):
    # todo_service.delete(todo_id=callback_data.todo_id, user_id=callback.from_user.id)
    await callback.answer("Vazifa o‘chirildi")
    await callback.message.delete()


"""
LOYIHA CHECKLIST:
  ✔️ User faqat o‘z vazifasini ko‘ra oladi.
  ✔️ Vazifa: id, user_id, title, status, reminder_at ustunlariga ega.
  ✔️ Bajarilgan va bajarilmagan vazifalar alohida ko‘rsatiladi.
  ✔️ Xato va bo‘sh inputlar tekshiriladi.
  ✔️ README.md va screenshot bor.

BONUS:
  ✔️ Deadline qo‘shish.
  ✔️ Eslatma yuborish.
  ✔️ Kategoriya va prioritet.
"""
