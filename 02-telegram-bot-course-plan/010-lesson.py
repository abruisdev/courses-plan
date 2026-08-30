# ============================================================
#   DARS 10: Middleware va Dependency Injection
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ Middleware nima
  ✔️ Outer va inner middleware
  ✔️ Database session uzatish
  ✔️ Admin filter
  ✔️ Rate limiting g‘oyasi
"""

from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.filters import BaseFilter
from aiogram.types import Message, TelegramObject

ADMIN_IDS = {123456789}  # O‘zingizning haqiqiy Telegram ID’ingizni yozing


class AdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in ADMIN_IDS


class DatabaseMiddleware(BaseMiddleware):
    """Har update uchun database session yaratib handlerga uzatadi."""

    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        async with self.session_factory() as session:
            data["session"] = session
            return await handler(event, data)


"""
main.py ichida middleware ulash:

dp.update.outer_middleware(DatabaseMiddleware(session_factory))

Handler ichida dependency olish:

@router.message(AdminFilter(), Command("stats"))
async def stats(message: Message, session: AsyncSession):
    await message.answer("Faqat admin uchun statistika")

MUSTAQIL MASHQ TOPSHIRIQLARI:
1. Foydalanuvchini har /start’da database’ga yozuvchi middleware yarating.
2. Adminlar uchun /broadcast komandasi yarating.
3. Bir foydalanuvchi ketma-ket juda ko‘p xabar yuborsa cheklaydigan middleware rejasini tuzing.

BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ Middleware nima ekanini
✔️ Admin filter yaratishni
✔️ Dependency Injection bilan session uzatishni
✔️ Production arxitektura asoslarini
"""
