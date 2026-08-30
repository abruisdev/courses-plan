# ============================================================
#   DARS 24: Buyurtma API va Bot Integratsiyasi
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ Mini App buyurtmasini qabul qilish
  ✔️ initData orqali foydalanuvchini aniqlash
  ✔️ Narxni serverda hisoblash
  ✔️ Administratorga bot orqali xabar yuborish
  ✔️ Database’ga saqlash rejasini tuzish
"""

import os

from aiogram import Bot
from fastapi import Depends, FastAPI
from pydantic import BaseModel, Field

from app.security import current_telegram_user

app = FastAPI()
bot = Bot(token=os.getenv("BOT_TOKEN"))
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

PRODUCTS = {
    1: {"name": "Python Foundation", "price": 500_000},
    2: {"name": "Telegram Bot", "price": 700_000},
}


class CartItem(BaseModel):
    id: int
    quantity: int = Field(ge=1, le=20)


class OrderCreate(BaseModel):
    items: list[CartItem] = Field(min_length=1)


@app.post("/api/orders")
async def create_order(
    order: OrderCreate,
    telegram_user: dict = Depends(current_telegram_user),
):
    total = 0
    order_lines = []

    for item in order.items:
        product = PRODUCTS.get(item.id)

        if not product:
            return {"ok": False, "message": "Mahsulot topilmadi"}

        line_total = product["price"] * item.quantity
        total += line_total
        order_lines.append(f"{product['name']} x {item.quantity}")

    # Production’da bu yerda Order va OrderItem jadvallariga saqlanadi.
    order_id = 1001

    if ADMIN_ID:
        await bot.send_message(
            ADMIN_ID,
            "🛒 Yangi buyurtma\n"
            f"Mijoz: {telegram_user['first_name']}\n"
            f"Telegram ID: {telegram_user['id']}\n"
            f"Mahsulotlar: {', '.join(order_lines)}\n"
            f"Jami: {total:,} so‘m",
        )

    return {"ok": True, "order_id": order_id, "total": total}


"""
PROFESSIONAL QOIDALAR:
  ✔️ Frontend yuborgan narxga ishonmang; narxni serverda hisoblang.
  ✔️ User ID’ni initData validatsiyasidan oling.
  ✔️ Har buyurtmani PostgreSQL’ga transaction ichida saqlang.
  ✔️ Stock qiymatini server tomonda tekshiring.

MUSTAQIL MASHQ TOPSHIRIQLARI:
1. Order va OrderItem SQLAlchemy modellarini yarating.
2. Mahsulot stock qiymatini tekshiring.
3. Buyurtma holatlarini yarating: new, confirmed, delivered, cancelled.
4. Administrator inline tugma bilan buyurtmani tasdiqlasin.
"""
