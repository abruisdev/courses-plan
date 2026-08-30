# ============================================================
#   DARS 9: CRUD, Service va Repository Qatlamlari
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ Create, Read, Update, Delete
  ✔️ Repository nima
  ✔️ Service nima
  ✔️ Handlerni database kodidan ajratish
"""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import User


class UserRepository:
    """Faqat database so‘rovlari joylashadigan qatlam."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_telegram_id(self, telegram_id: int) -> User | None:
        query = select(User).where(User.telegram_id == telegram_id)
        return await self.session.scalar(query)

    async def create(self, telegram_id: int, full_name: str, username: str | None) -> User:
        user = User(telegram_id=telegram_id, full_name=full_name, username=username)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user


class UserService:
    """Biznes qoidalari joylashadigan qatlam."""

    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def get_or_create_user(self, telegram_user) -> User:
        user = await self.repository.get_by_telegram_id(telegram_user.id)

        if user:
            return user

        return await self.repository.create(
            telegram_id=telegram_user.id,
            full_name=telegram_user.full_name,
            username=telegram_user.username,
        )


"""
handlers/user.py ichida:

@router.message(CommandStart())
async def start(message: Message, user_service: UserService):
    await user_service.get_or_create_user(message.from_user)
    await message.answer("Xush kelibsiz!")

MUSTAQIL MASHQ TOPSHIRIQLARI:
1. ProductRepository yarating.
2. Barcha mahsulotlarni olish uchun get_all() yozing.
3. OrderService orqali buyurtma yaratishni yozing.
4. Handler ichida SQL so‘rov yozmaslik qoidasiga amal qiling.

BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ CRUD nima ekanini
✔️ Repository qatlamini
✔️ Service qatlamini
✔️ Toza arxitektura asoslarini
"""
