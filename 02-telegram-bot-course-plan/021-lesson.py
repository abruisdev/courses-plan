# ============================================================
#   DARS 21: FastAPI — Mini App Backend
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
O‘RNATISH:
  python -m pip install fastapi "uvicorn[standard]"

Ishga tushirish:
  uvicorn main:app --reload

BUGUNGI DARSDA:
  ✔️ FastAPI
  ✔️ GET va POST endpoint
  ✔️ Pydantic schema
  ✔️ Static frontend
  ✔️ CORS
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

app = FastAPI(title="Mini Store API")

# Production’da frontend domenini aniq yozing. "*" ishlatmang.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "X-Telegram-Init-Data"],
)

# webapp/ ichida index.html, app.js va styles.css saqlanadi.
app.mount("/webapp", StaticFiles(directory="webapp", html=True), name="webapp")


class OrderCreate(BaseModel):
    product_ids: list[int] = Field(min_length=1)


PRODUCTS = [
    {"id": 1, "name": "Python Foundation", "price": 500_000},
    {"id": 2, "name": "Telegram Bot", "price": 700_000},
]


@app.get("/api/products")
async def get_products():
    return PRODUCTS


@app.post("/api/orders")
async def create_order(order: OrderCreate):
    # Keyingi darsda initData validatsiyasi va database qo‘shiladi.
    return {"ok": True, "product_ids": order.product_ids}


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:
1. /api/products endpointini JavaScript fetch() bilan chaqiring.
2. Product uchun Pydantic schema yarating.
3. /api/orders orqali mahsulot IDlarini qabul qiling.
4. CORS’da faqat o‘zingizning domeningizga ruxsat bering.
"""
