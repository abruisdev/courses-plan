# ============================================================
#   DARS 13: Testing, Security va Configuration
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ .env va .env.example
  ✔️ Pydantic Settings
  ✔️ pytest asoslari
  ✔️ Handler va service testlari
  ✔️ GitHub xavfsizligi
"""

"""
O‘RNATISH:
  python -m pip install pydantic-settings pytest

.env.example fayli:
  BOT_TOKEN=your_bot_token
  DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/bot_db

Haqiqiy .env fayli GitHub’ga yuklanmaydi.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str
    database_url: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()


def chegirma_narxi(narx: int, foiz: int) -> int:
    if not 0 <= foiz <= 100:
        raise ValueError("Foiz 0 dan 100 gacha bo‘lishi kerak")

    return narx - narx * foiz // 100


"""
tests/test_price.py fayli:

from app.services.price import chegirma_narxi

def test_chegirma_narxi():
    assert chegirma_narxi(100_000, 10) == 90_000

def test_noto_gri_foiz():
    with pytest.raises(ValueError):
        chegirma_narxi(100, 120)

Testni ishga tushirish:
  pytest
"""


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:
1. .env.example yarating.
2. Settings classiga admin_ids qiymatini qo‘shing.
3. 2 ta service funksiyasi uchun pytest yozing.
4. GitHub’dan tokenni qidirib, tasodifan yuklanmaganini tekshiring.
"""
