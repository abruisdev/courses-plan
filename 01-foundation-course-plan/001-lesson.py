# ============================================================
#   DARS 1: Kirish, Python O'rnatish va Birinchi Dastur
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# PYTHON NIMA?
# ------------------------------------------------------------

"""
Python — bu 1991-yilda yaratilgan, hozirda dunyo bo'yicha
eng mashhur dasturlash tillaridan biri.

Qayerlarda ishlatiladi?
  - Web saytlar va ilovalar (Django, Flask)
  - Telegram botlar
  - Sun'iy intellekt va Machine Learning (AI/ML)
  - Ma'lumotlar tahlili (Data Analysis)
  - O'yinlar va animatsiyalar

Nega Python?
  - O'qish va yozish oson (ingliz tiliga o'xshash)
  - Katta jamoa va ko'p resurslar mavjud
  - Bepul va ochiq kodli (open-source)
"""

# ------------------------------------------------------------
# PYTHON O'RNATISH (qadam-ba-qadam)
# ------------------------------------------------------------

"""
QADAM 1 — Python yuklab olish:
  1. https://python.org saytiga kiring
  2. "Download Python" tugmasini bosing
  3. Eng yangi versiyani tanlang (masalan: Python 3.12)

QADAM 2 — O'rnatish:
  ✔️ "Add Python to PATH" katagini ALBATTA belgilang!
  ✔️ "Install Now" tugmasini bosing
  ✔️ O'rnatish tugashini kuting

QADAM 3 — Tekshirish:
  Terminalni oching va quyidagini yozing:

      python --version

  Agar "Python 3.x.x" chiqsa — hammasi to'g'ri o'rnatilgan!
"""

# ------------------------------------------------------------
# PYCHARM O'RNATISH (kod yozish muhiti)
# ------------------------------------------------------------

"""
PyCharm — bu Python uchun maxsus dastur (IDE).
Unda kod yozish, xatolarni topish va ishga tushirish oson.

O'rnatish:
  1. https://jetbrains.com/pycharm saytiga kiring
  2. "PyCharm Community" (bepul versiya) ni yuklab oling
  3. O'rnating va oching

Yangi project yaratish:
  File → New Project → papka nomini bering → Create

PyCharm interfeysi:
  ┌─────────────────────────────────────┐
  │  Chap taraf   │   O'ng taraf        │
  │  (Fayllar)    │   (Kod yoziladigan  │
  │               │    joy)             │
  │───────────────────────────────────  │
  │       Pastki qism (Terminal)        │
  └─────────────────────────────────────┘
"""

# ------------------------------------------------------------
# print() FUNKSIYASI — EKRANGA CHIQARISH
# ------------------------------------------------------------

"""
print() — bu Pythondagi eng asosiy buyruq.
U qavs ichidagi narsani ekranga chiqaradi.
"""

# MISOL 1 — Matn (string) chiqarish
# Matn har doim qo'shtirnoq ichida yoziladi
print("Assalomu alaykum!")
print("Mening ismim Ali")
print("Men Python o'rganmoqdaman")

# MISOL 2 — Son chiqarish
# Sonlar qo'shtirnoqsiz yoziladi
print(2025)
print(100)

# MISOL 3 — Bir nechta print() ketma-ket
print("Ism:  Ali")
print("Yosh: 15")
print("Sinf: 9-A")

# MISOL 4 — Bo'sh qator chiqarish (ajratgich sifatida)
print("Birinchi qator")
print()            # Bo'sh qator
print("Uchinchi qator")

# ------------------------------------------------------------
# IZOHLAR (Comments)
# ------------------------------------------------------------

"""
Izoh — bu kod ichidagi tushuntirish matni.
Python uni o'qimaydi va bajarmaydi.
# belgisidan keyin yozilgan har qanday narsa izoh hisoblanadi.

Izohlar nima uchun kerak?
  - Kodingizni boshqalarga tushuntirish uchun
  - O'zingiz qaytib kelbsangiz eslatma sifatida
  - Muammoli qatorni vaqtincha o'chirish uchun
"""

# Bu izoh — Python buni bajarmaydi
print("Salom!")   # Bu qator ishlaydi, lekin yonidagi izoh emas

# Izoh bilan hisob-kitob tushuntirish:
print(365 * 24)   # 1 yildagi soatlar soni
print(24 * 60)    # 1 kundagi daqiqalar soni
print(60 * 60)    # 1 soatdagi soniyalar soni

# ------------------------------------------------------------
# ARIFMETIK OPERATORLAR
# ------------------------------------------------------------

"""
Operator — bu ikki son ustida amal bajaruvchi belgi.
Python 7 ta asosiy arifmetik operatorga ega:

  Operator   Nomi                    Misol       Natija
  ────────   ──────────────────────  ─────────   ──────
  +          Qo'shish                5 + 3       8
  -          Ayirish                 10 - 4      6
  *          Ko'paytirish            3 * 7       21
  /          Bo'lish                 20 / 4      5.0
  %          Qoldiq (Modulo)         10 % 3      1
  //         Butun bo'lish           10 // 3     3
  **         Daraja (Quvvat)         2 ** 8      256
"""

# ── + Qo'shish ──────────────────────────────────────────────
print(5 + 3)        # Natija: 8
print(100 + 250)    # Natija: 350

# ── - Ayirish ───────────────────────────────────────────────
print(10 - 4)       # Natija: 6
print(1000 - 375)   # Natija: 625

# ── * Ko'paytirish ──────────────────────────────────────────
print(3 * 7)        # Natija: 21
print(12 * 12)      # Natija: 144

# ── / Bo'lish ───────────────────────────────────────────────
# Natija har doim o'nlik son (float) bo'ladi
print(20 / 4)       # Natija: 5.0
print(7 / 2)        # Natija: 3.5

# ── % Qoldiq (Modulo) ───────────────────────────────────────
# Bo'linganda qoladigan qoldiqni beradi
# Masalan: 10 ni 3 ga bo'lsak → 3*3=9, qoldiq = 1
print(10 % 3)       # Natija: 1
print(15 % 4)       # Natija: 3
print(10 % 2)       # Natija: 0  (juft son — qoldiq yo'q)

# ── // Butun bo'lish ────────────────────────────────────────
# Bo'lganda faqat butun qismini beradi, kasr qismini tashlab yuboradi
# Masalan: 10 / 3 = 3.333...  →  // bilan natija: 3
print(10 // 3)      # Natija: 3
print(7 // 2)       # Natija: 3
print(15 // 4)      # Natija: 3

# ── ** Daraja (Quvvat) ──────────────────────────────────────
# Birinchi sonni ikkinchi son darajasiga ko'taradi
# Masalan: 2 ** 8  →  2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 = 256
print(2 ** 8)       # Natija: 256
print(3 ** 3)       # Natija: 27   (3 kub)
print(5 ** 2)       # Natija: 25   (5 kvadrat)

# ── Amaliy misollar ─────────────────────────────────────────

# MISOL 1 — Doiraning yuzini hisoblash (r = 7)
print(3.14 * 7 ** 2)        # Natija: 153.86

# MISOL 2 — Sonning juft yoki toq ekanini tekshirish
# Agar % 2 == 0 bo'lsa — juft, bo'lmasa — toq
print(14 % 2)               # Natija: 0  → 14 juft son
print(17 % 2)               # Natija: 1  → 17 toq son

# MISOL 3 — Daqiqani soat va daqiqaga aylantirish
daqiqalar = 150
print(daqiqalar // 60)      # Natija: 2  (soat)
print(daqiqalar % 60)       # Natija: 30 (qolgan daqiqa)
# Ya'ni 150 daqiqa = 2 soat 30 daqiqa

# MISOL 4 — Amallari ketma-ketligi (matematikadagi kabi)
# Python: avval ** → keyin *, / → keyin +, -
print(2 + 3 * 4)            # Natija: 14  (avval 3*4=12, keyin 2+12)
print((2 + 3) * 4)          # Natija: 20  (qavs ichini avval hisoblaydi)

# MISOL 5 — Kombinatsiyalangan hisob
# 1 yilda nechta soniya bor?
print(365 * 24 * 60 * 60)   # Natija: 31536000


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Oson:
  Quyidagi ma'lumotlarni ekranga chiqaring:
    - Ismingiz
    - Yoshingiz
    - Sevimli rangingiz

TOPSHIRIQ 2 — O'rta:
  Quyidagi hisob-kitoblarni print() orqali chiqaring:
    - 2025 yildan tug'ilgan yilingizni ayiring (yoshingiz)
    - 7 kunda nechta soat borligini hisoblang (7 * 24)
    - 1 oy nechta daqiqa ekanligini hisoblang (30 * 24 * 60)

TOPSHIRIQ 3 — Qiziqarli:
  O'zingiz haqingizda "ID karta" chiqaring:
    ┌─────────────────────┐
    │   SHAXSIY ID KARTA  │
    │  Ism  : Ali Karimov │
    │  Yosh : 15          │
    │  Sinf : 9-A         │
    └─────────────────────┘

TOPSHIRIQ 4 — Izoh bilan:
  5 ta turli hisob-kitob yozing.
  Har birining yoniga izoh qo'ying, nima hisoblanayotganini tushuntiring.

TOPSHIRIQ 5 — Ijodiy:
  Sevimli qo'shig'ingiz yoki kitobingizning
  nomini ekranga chiqaring va yoniga izoh bilan
  nima ekanligini tushuntiring.
"""


# ------------------------------------------------------------
# QUSHIMCHA RESURSLAR (Uyga vazifa uchun)
# ------------------------------------------------------------

"""
📚 RASMIY HUJJATLAR:
   https://docs.python.org/3/tutorial/index.html
   — Python yaratuvchilari yozgan to'liq qo'llanma (inglizcha)

🌐 W3SCHOOLS (boshlang'ichlar uchun eng qulay):
   https://www.w3schools.com/python/
   — Oson tushuntirishlar va amaliy misollar

🎥 YOUTUBE (o'zbekcha darslar):
   "Python o'zbekcha" deb qidiring
   — Ko'plab bepul video darslar mavjud
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ Python nima va qayerlarda ishlatilishi
✔️ Python va PyCharm o'rnatish
✔️ PyCharm interfeysini tanish
✔️ print() funksiyasi bilan ekranga chiqarish
✔️ Izoh yozish (#)
✔️ Arifmetik operatorlar:
    +   Qo'shish
    -   Ayirish
    *   Ko'paytirish
    /   Bo'lish          → natija har doim float (5.0)
    %   Qoldiq           → 10 % 3 = 1
    //  Butun bo'lish    → 10 // 3 = 3
    **  Daraja           → 2 ** 8 = 256
"""

