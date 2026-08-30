# ============================================================
#   DARS 22: Yakuniy Loyiha Rejasini Tuzish
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ Loyiha tanlash
  ✔️ Texnik topshiriq yozish
  ✔️ GitHub repository yaratish
  ✔️ Papkalar strukturasini tuzish
  ✔️ Funksiya va classlarni rejalash
  ✔️ JSON yoki SQLite tanlash
"""


# ------------------------------------------------------------
# LOYIHA VARIANTLARI
# ------------------------------------------------------------

"""
Yakuniy loyiha quyidagilardan biri bo‘lishi mumkin:

  1. O‘quv markazi boshqaruv tizimi
  2. Xarajatlar hisoblash dasturi
  3. Kontaktlar boshqaruv tizimi
  4. Mini online do‘kon
  5. Kutubxona tizimi
  6. Ombor tizimi

Loyiha kamida quyidagilarni ishlatishi kerak:
  ✔️ Funksiyalar
  ✔️ List yoki Dictionary
  ✔️ OOP
  ✔️ try / except
  ✔️ JSON yoki SQLite
  ✔️ GitHub repository
"""


# ------------------------------------------------------------
# TEXNIK TOPSHIRIQ SHABLONI
# ------------------------------------------------------------

LOYIHA_TOPSHIRIGI = """
LOYIHA NOMI: O‘quv markazi boshqaruv tizimi

MUAMMO:
  O‘quvchilar ma’lumotini qog‘ozda saqlash noqulay.

MAQSAD:
  O‘quvchi qo‘shish, ko‘rish, qidirish, yangilash va o‘chirish.

FOYDALANUVCHI:
  O‘quv markazi administratori.

ASOSIY FUNKSIYALAR:
  1. O‘quvchi qo‘shish.
  2. Barcha o‘quvchilarni ko‘rish.
  3. ID bo‘yicha qidirish.
  4. Kursni yangilash.
  5. O‘quvchini o‘chirish.
  6. Chiqish.

MA’LUMOTLAR BAZASI:
  SQLite: oquvchilar jadvali.
"""

print(LOYIHA_TOPSHIRIGI)


# ------------------------------------------------------------
# PAPKALAR STRUKTURASI
# ------------------------------------------------------------

"""
Tavsiya qilinadigan loyiha tuzilishi:

oquv_markazi/
├── main.py              # Dasturni ishga tushirish
├── database.py          # SQLite funksiyalari
├── models.py            # Classlar
├── requirements.txt     # Kerakli kutubxonalar
├── README.md            # Loyiha hujjati
├── .gitignore
└── tests/               # Testlar
"""


# ------------------------------------------------------------
# FUNKSIYA VA CLASSLARNI REJALASH
# ------------------------------------------------------------


class Oquvchi:
    """Loyihadagi Oquvchi modelining reja namunasi."""

    def __init__(self, ism, yosh, kurs):
        self.ism = ism
        self.yosh = yosh
        self.kurs = kurs


def oquvchi_qoshish():
    """Yangi o‘quvchi qo‘shish uchun reja funksiyasi."""
    pass


def oquvchilarni_korish():
    """Barcha o‘quvchilarni chiqarish uchun reja funksiyasi."""
    pass


def oquvchini_qidirish():
    """ID bo‘yicha o‘quvchi qidirish uchun reja funksiyasi."""
    pass


# ------------------------------------------------------------
# JSON YOKI SQLite?
# ------------------------------------------------------------

"""
JSON tanlang, agar:
  - Kichik loyiha bo‘lsa.
  - Ma’lumot kam bo‘lsa.
  - Bitta fayl bilan ishlash qulay bo‘lsa.

SQLite tanlang, agar:
  - Qidirish, yangilash va o‘chirish ko‘p bo‘lsa.
  - Ma’lumotlar soni ortishi mumkin bo‘lsa.
  - Backendga tayyorgarlik ko‘rmoqchi bo‘lsangiz.
"""


"""
UYGA VAZIFA:

1. Yakuniy loyiha variantini tanlang.
2. Yuqoridagi shablon bo‘yicha texnik topshiriq yozing.
3. GitHub’da alohida repository yarating.
4. README.md ichida loyiha maqsadini yozing.
5. Ertangi darsga papkalar strukturasini tayyorlab keling.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ Loyiha tanlashni
✔️ Texnik topshiriq yozishni
✔️ Papkalar strukturasini rejalashni
✔️ Funksiya va classlar rejasini tuzishni
✔️ JSON va SQLite orasidan tanlashni
"""
