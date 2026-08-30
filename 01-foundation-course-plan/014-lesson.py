# ============================================================
#   DARS 14: Virtual Environment, pip va Tashqi Kutubxonalar
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ pip nima
  ✔️ Virtual environment nima
  ✔️ venv yaratish va faollashtirish
  ✔️ requests va python-dotenv o‘rnatish
  ✔️ requirements.txt
  ✔️ .env va .gitignore xavfsizligi
"""


# ------------------------------------------------------------
# pip NIMA?
# ------------------------------------------------------------

"""
pip — Python kutubxonalarini o‘rnatish vositasi.

Tekshirish:
  python -m pip --version

Kutubxona o‘rnatish:
  python -m pip install requests

Kutubxonani o‘chirish:
  python -m pip uninstall requests

O‘rnatilgan kutubxonalarni ko‘rish:
  python -m pip list

python -m pip yozilishi tavsiya qilinadi: shu project ishlatayotgan
Python interpreterining pip’i aniq ishlatiladi.
"""


# ------------------------------------------------------------
# VIRTUAL ENVIRONMENT (venv)
# ------------------------------------------------------------

"""
Virtual environment — har bir loyiha uchun alohida kutubxonalar
saqlanadigan muhit.

Nima uchun kerak?
  ✔️ Bir loyiha kutubxonalari boshqasiga aralashmaydi
  ✔️ Har loyiha kerakli versiyani alohida ishlatadi
  ✔️ Loyihani boshqa kompyuterda ishga tushirish osonlashadi

Loyiha papkasida yaratish:

Windows:
  python -m venv .venv
  .venv\Scripts\activate

Mac / Linux:
  python3 -m venv .venv
  source .venv/bin/activate

Faol muhitdan chiqish:
  deactivate
"""


# ------------------------------------------------------------
# requirements.txt
# ------------------------------------------------------------

"""
requirements.txt — loyiha kerak qiladigan kutubxonalar ro‘yxati.

Yaratish:
  python -m pip freeze > requirements.txt

O‘rnatish:
  python -m pip install -r requirements.txt

Misol requirements.txt:

  requests
  python-dotenv
"""


# ------------------------------------------------------------
# .env FAYLI
# ------------------------------------------------------------

"""
.env — token, parol va API key kabi maxfiy ma’lumotlarni
koddan ajratib saqlash uchun fayl.

.env ichidagi misol:

  BOT_TOKEN=bu_haqiqiy_token_emas
  WEATHER_API_KEY=bu_haqiqiy_key_emas

Muhim qoida:
  ✔️ Haqiqiy tokenni GitHub’ga yuklamang.
  ✔️ .env faylini .gitignore ichiga qo‘shing.
"""

# .gitignore fayli:
# .venv/
# .env
# __pycache__/


# ------------------------------------------------------------
# python-dotenv BILAN ISHLASH
# ------------------------------------------------------------

"""
O‘rnatish:
  python -m pip install python-dotenv

Ishlatish namunasi quyidagicha:
"""

# from dotenv import load_dotenv
# import os
#
# load_dotenv()
# bot_token = os.getenv("BOT_TOKEN")
# print(bot_token)


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. Yangi loyiha papkasi yarating va .venv yarating.
2. requests kutubxonasini o‘rnating.
3. requirements.txt yarating.
4. .env va .gitignore fayllarini yarating.
5. .env ichidan TEST_NOM qiymatini o‘qib chiqaring.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ pip bilan kutubxona boshqarishni
✔️ Virtual environment yaratishni
✔️ requirements.txt ishlatishni
✔️ .env orqali maxfiy qiymatlarni saqlashni
✔️ .gitignore orqali maxfiy fayllarni GitHub’dan himoyalashni
"""
