# ============================================================
#   DARS 27: Amaliy Loyiha — Viktorina / Test Boti
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
LOYIHA MAQSADI:
Foydalanuvchiga savollar ko‘rsatish, javobni tekshirish,
ball berish va reyting chiqarish.
"""

from aiogram import F, Router
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

QUESTIONS = [
    {
        "id": 1,
        "text": "Python’da ekranga chiqarish funksiyasi qaysi?",
        "answers": ["print", "input", "type", "range"],
        "correct": 0,
    },
]


class AnswerCallback(CallbackData, prefix="answer"):
    question_id: int
    answer_index: int


def question_keyboard(question):
    builder = InlineKeyboardBuilder()

    for index, answer in enumerate(question["answers"]):
        builder.button(text=answer, callback_data=AnswerCallback(question_id=question["id"], answer_index=index))

    builder.adjust(1)
    return builder.as_markup()


@router.message(F.text == "🧠 Testni boshlash")
async def start_quiz(message: Message):
    question = QUESTIONS[0]
    await message.answer(question["text"], reply_markup=question_keyboard(question))


@router.callback_query(AnswerCallback.filter())
async def answer_handler(callback: CallbackQuery, callback_data: AnswerCallback):
    question = next(item for item in QUESTIONS if item["id"] == callback_data.question_id)

    if callback_data.answer_index == question["correct"]:
        await callback.answer("To‘g‘ri javob!", show_alert=True)
        await callback.message.edit_text("✅ To‘g‘ri javob!")
        # score_service.add_point(callback.from_user.id)
    else:
        await callback.answer("Noto‘g‘ri javob", show_alert=True)
        await callback.message.edit_text("❌ Noto‘g‘ri javob")


"""
LOYIHA CHECKLIST:
  ✔️ Savollar database’da saqlanadi.
  ✔️ Har foydalanuvchining javobi faqat bir marta qabul qilinadi.
  ✔️ Ballar jadvali bor.
  ✔️ /leaderboard eng yaxshi 10 foydalanuvchini chiqaradi.
  ✔️ Admin yangi savol qo‘sha oladi.

BONUS:
  ✔️ Har savol uchun timer.
  ✔️ Rasmli savollar.
  ✔️ Guruh ichida viktorina.
"""
