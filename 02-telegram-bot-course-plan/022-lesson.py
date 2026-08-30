# ============================================================
#   DARS 22: Telegram initData Validatsiyasi
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
MUHIM XAVFSIZLIK QOIDASI:
Telegram.WebApp.initDataUnsafe ichidagi ma’lumotga backendda ishonmang.
Frontend initData qiymatini backendga yuboradi. Backend uning hash qiymatini
bot token orqali tekshiradi.
"""

import hashlib
import hmac
import json
import time
from urllib.parse import parse_qsl

from fastapi import Header, HTTPException


def validate_init_data(init_data: str, bot_token: str, max_age_seconds: int = 3600) -> dict:
    values = dict(parse_qsl(init_data, keep_blank_values=True))
    received_hash = values.pop("hash", None)

    if not received_hash:
        raise ValueError("initData ichida hash yo‘q")

    data_check_string = "\n".join(f"{key}={value}" for key, value in sorted(values.items()))
    secret_key = hmac.new(b"WebAppData", bot_token.encode(), hashlib.sha256).digest()
    calculated_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

    if not hmac.compare_digest(calculated_hash, received_hash):
        raise ValueError("Telegram initData imzosi noto‘g‘ri")

    auth_date = int(values.get("auth_date", 0))
    if time.time() - auth_date > max_age_seconds:
        raise ValueError("Telegram initData eskirgan")

    return json.loads(values["user"])


def current_telegram_user(
    x_telegram_init_data: str = Header(...),
) -> dict:
    """FastAPI endpointiga dependency sifatida beriladi."""
    from app.config import settings

    try:
        return validate_init_data(x_telegram_init_data, settings.bot_token)
    except (ValueError, json.JSONDecodeError) as error:
        raise HTTPException(status_code=401, detail=str(error)) from error


"""
Frontenddan yuborish:

fetch("/api/orders", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "X-Telegram-Init-Data": Telegram.WebApp.initData,
  },
  body: JSON.stringify({ product_ids: [1, 2] }),
})

MUSTAQIL MASHQ TOPSHIRIQLARI:
1. current_telegram_user dependency’sini /api/profile endpointiga ulang.
2. Telegram user ID bo‘yicha database’dan foydalanuvchini toping yoki yarating.
3. initDataUnsafe yordamida serverda ruxsat berish nega xavfli ekanini tushuntiring.
"""
