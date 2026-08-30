# ============================================================
#   DARS 12: Logging, Xatolar va Background Tasklar
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ logging
  ✔️ Global error handler
  ✔️ Foydalanuvchiga tushunarli xato xabari
  ✔️ APScheduler bilan rejalashtirilgan xabarlar
  ✔️ Flood va spamdan himoyalanish
"""

import logging

from aiogram import Router
from aiogram.types import ErrorEvent

router = Router()
logger = logging.getLogger(__name__)


@router.error()
async def global_error_handler(event: ErrorEvent):
    logger.exception("Handler xatosi: %s", event.exception)

    if event.update.message:
        await event.update.message.answer("Kutilmagan xato yuz berdi. Qayta urinib ko‘ring.")


"""
APScheduler o‘rnatish:
  python -m pip install apscheduler

Misol:

from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()
scheduler.add_job(
    bot.send_message,
    trigger="date",
    run_date=kerakli_sana,
    args=[chat_id, "Eslatma vaqti keldi!"],
)
scheduler.start()

Spamdan himoyalanish uchun:
  ✔️ Middleware orqali vaqt oralig‘ini tekshiring.
  ✔️ Bir foydalanuvchi uchun limit saqlang.
  ✔️ Og‘ir ishlarni handlerda bloklamang.
"""


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:
1. Logging’ni konsol va bot.log fayliga yozadigan qiling.
2. 1 daqiqadan keyin eslatma yuboradigan funksiya yozing.
3. Xato beradigan handler yarating va global error handlerda tekshiring.
4. Bir foydalanuvchiga 3 soniyada faqat bitta buyruq ruxsatini beruvchi middleware yozing.
"""
