# ============================================================
#   DARS 8: PostgreSQL va SQLAlchemy Async
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ SQLite va PostgreSQL farqi
  ✔️ SQLAlchemy Async
  ✔️ Model yaratish
  ✔️ Async engine va session

O‘RNATISH:
  python -m pip install sqlalchemy asyncpg

.env:
  DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/bot_db
"""

import os

from dotenv import load_dotenv
from sqlalchemy import BigInteger, String
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    full_name: Mapped[str] = mapped_column(String(255))
    username: Mapped[str | None] = mapped_column(String(255), nullable=True)


engine = create_async_engine(DATABASE_URL, echo=False)
session_factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def create_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


"""
PROFESSIONAL QOIDA:
create_all() development uchun qulay. Production’da jadval o‘zgarishlarini Alembic migration orqali boshqaring.

MUSTAQIL MASHQ TOPSHIRIQLARI:
1. Product modeli yarating: id, name, price, stock.
2. Order modeli yarating: id, user_id, total_price, status.
3. DATABASE_URL ni .env’da saqlang.
4. Alembic nima uchun kerakligini o‘rganing.

BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ PostgreSQL nima ekanini
✔️ Async engine va sessionni
✔️ SQLAlchemy model yaratishni
✔️ Database URL’ni xavfsiz saqlashni
"""
