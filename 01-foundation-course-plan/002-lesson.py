# ============================================================
#   DARS 2: O'zgaruvchilar, Data Types, Casting, Boolean, Input()
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# O'ZGARUVCHILAR (Variables)
# ------------------------------------------------------------

"""
O'zgaruvchi — bu ma'lumotni saqlash uchun ishlatiladigan "quti".
Unga nom beramiz va ichiga qiymat joylashtiramiz.

Qoida:
  nom = qiymat

Misol:
  ism = "Ali"     →  "ism" nomli qutiga "Ali" yozildi
  yosh = 15       →  "yosh" nomli qutiga 15 raqami yozildi
"""

# O'zgaruvchi yaratish
ism = "Ali"
yosh = 15
shahar = "Toshkent"

# O'zgaruvchini ekranga chiqarish
print(ism)        # Natija: Ali
print(yosh)       # Natija: 15
print(shahar)     # Natija: Toshkent

# O'zgaruvchini matn bilan birga chiqarish
print("Mening ismim:", ism)
print("Men", yosh, "yoshdaman")
print("Men", shahar, "da yashayman")

# O'zgaruvchi qiymatini o'zgartirish
# Istalgan vaqtda yangi qiymat berish mumkin
ball = 80
print(ball)       # Natija: 80
ball = 95
print(ball)       # Natija: 95  (yangi qiymat)

# ── O'zgaruvchi nomlash qoidalari ───────────────────────────
"""
  ✅ To'g'ri:
    ism = "Ali"
    birinchi_ism = "Vali"
    yosh2 = 16
    _maxfiy = 1234

  ❌ Noto'g'ri:
    2ism = "Ali"       →  raqam bilan boshlanmaydi!
    birinchi ism = "X" →  bo'sh joy bo'lmaydi!
    ism! = "Ali"       →  maxsus belgi bo'lmaydi!

  ⚠️ Diqqat:
    ism = "Ali"
    Ism = "Vali"
    ISM = "Jasur"
    Bu uchta TURLI o'zgaruvchi! (Python katta-kichik harfni farqlaydi)
"""

# ── Bir nechta o'zgaruvchini bir qatorda yaratish ────────────
x, y, z = 10, 20, 30
print(x)    # 10
print(y)    # 20
print(z)    # 30

# Barcha o'zgaruvchilarga bir xil qiymat berish
a = b = c = 0
print(a, b, c)    # Natija: 0 0 0


# ------------------------------------------------------------
# DATA TYPES (Ma'lumot Turlari)
# ------------------------------------------------------------

"""
Python'da har bir qiymatning turi (type) bor.
Asosiy turlar:

  Tur       Nomi          Misol
  ───────   ───────────   ─────────────────
  str       String        "Salom", 'Ali'
  int       Integer       10, -5, 1000
  float     Float         3.14, -0.5, 2.0
  complex   Complex       3+2j, 1j
  bool      Boolean       True, False

type() funksiyasi — qiymatning turini ko'rsatadi
"""

# ── str (String — Matn) ─────────────────────────────────────
"""
String — bu matn ma'lumoti.
Qo'shtirnoq (" ") yoki apostrof (' ') ichida yoziladi.
"""
ism      = "Ali Karimov"
manzil   = 'Toshkent, O\'zbekiston'   # apostrof ichida apostrof: \'
xabar    = "Bugun ob-havo yaxshi"

print(ism)                  # Ali Karimov
print(type(ism))            # <class 'str'>

# Uzun matn — uch qo'shtirnoq
tarjimai_hol = """
Men Ali Karimov.
15 yoshdaman.
Toshkentda yashayman.
"""
print(tarjimai_hol)

# ── int (Integer — Butun Son) ────────────────────────────────
"""
Integer — bu manfiy yoki musbat butun son.
Kasr qismi bo'lmaydi.
"""
yosh     = 15
xona     = -3
aholi    = 1_000_000   # _ yirik sonlarni o'qishni osonlashtiradi

print(yosh)             # 15
print(type(yosh))       # <class 'int'>
print(aholi)            # 1000000

# ── float (Haqiqiy Son — O'nlik kasr) ───────────────────────
"""
Float — bu kasr qismli son.
Nuqta (.) bilan yoziladi.
"""
narx     = 29.99
harorat  = -5.5
pi       = 3.14159

print(narx)             # 29.99
print(type(narx))       # <class 'float'>

# DIQQAT: Bo'lish (/) har doim float qaytaradi
print(10 / 2)           # Natija: 5.0  (int emas, float!)
print(type(10 / 2))     # <class 'float'>

# ── complex (Kompleks Son) ───────────────────────────────────
"""
Complex — bu haqiqiy va mavhum qismdan iborat son.
Matematikada: a + bi  →  Python'da: a + bj
"""
z1 = 3 + 2j
z2 = 1j

print(z1)               # (3+2j)
print(type(z1))         # <class 'complex'>
print(z1.real)          # 3.0  — haqiqiy qism
print(z1.imag)          # 2.0  — mavhum qism

# ── type() funksiyasi — turni aniqlash ───────────────────────
print(type("Salom"))    # <class 'str'>
print(type(42))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type(2+3j))       # <class 'complex'>
print(type(True))       # <class 'bool'>


# ------------------------------------------------------------
# CASTING (Bir Turdan Boshqa Turga O'tkazish)
# ------------------------------------------------------------

"""
Casting — bu qiymatning turini o'zgartirish.

  str()    →  istalgan narsani matnga aylantiradi
  int()    →  butun songa aylantiradi
  float()  →  o'nlik songa aylantiradi

Qachon kerak?
  - input() faqat string qaytaradi,
    shuning uchun sonlar bilan hisob qilish uchun
    int() yoki float() ishlatish kerak.
"""

# ── str() — Songa aylantirish ────────────────────────────────
son = 42
matn = str(son)
print(matn)               # "42"
print(type(matn))         # <class 'str'>

# Foydalanish misoli: son va matnni birlashtirish
yosh = 15
print("Men " + str(yosh) + " yoshdaman")   # Men 15 yoshdaman

# ── int() — Butun songa aylantirish ─────────────────────────
# Matndan songa
matn_son = "25"
son = int(matn_son)
print(son)                # 25
print(type(son))          # <class 'int'>

# Floatdan intga (kasr qismini tashlab ketadi)
print(int(3.9))           # Natija: 3  (3.9 → 3, YAXLITLAMAYDI!)
print(int(7.1))           # Natija: 7
print(int(-2.8))          # Natija: -2

# ── float() — O'nlik songa aylantirish ───────────────────────
print(float("3.14"))      # 3.14
print(float(5))           # 5.0
print(float("10"))        # 10.0

# ── XATO holatlari ───────────────────────────────────────────
"""
Quyidagilar XATOGA olib keladi:

  int("3.14")      →  XATO! (float ko'rinishidagi matnni int() qabul qilmaydi)
  int("salom")     →  XATO! (harf bo'lsa, songa aylantirish mumkin emas)

To'g'ri usul:
  int(float("3.14"))  →  avval floatga, keyin intga
"""

# To'g'ri yo'l:
print(int(float("3.14")))  # Natija: 3


# ------------------------------------------------------------
# BOOLEAN (Mantiqiy Qiymat)
# ------------------------------------------------------------

"""
Boolean — faqat ikkita qiymat oladi:
  True   (To'g'ri, Ha, 1)
  False  (Noto'g'ri, Yo'q, 0)

Katta harf bilan boshlanadi: True, False

Qachon ishlatiladi?
  - Shartlarni tekshirishda
  - Solishtirishlarda
"""

# Boolean qiymatlar
rost   = True
yolg_on = False
print(rost)              # True
print(yolg_on)           # False
print(type(rost))        # <class 'bool'>

# ── Solishtirish natijalari Boolean qaytaradi ─────────────────
print(5 > 3)             # True   (5 katta)
print(5 < 3)             # False  (5 kichik emas)
print(5 == 5)            # True   (teng)
print(5 != 3)            # True   (teng emas)
print(10 >= 10)          # True   (katta yoki teng)
print(7 <= 5)            # False  (kichik yoki teng emas)

# ── bool() funksiyasi ────────────────────────────────────────
"""
bool() — qiymatning True yoki False ekanini ko'rsatadi.

Quyidagilar DOIM False:
  0, 0.0, "" (bo'sh matn), None

Boshqa barcha qiymatlar True.
"""
print(bool(0))            # False
print(bool(1))            # True
print(bool(-5))           # True
print(bool(""))           # False  (bo'sh matn)
print(bool("Salom"))      # True
print(bool(0.0))          # False
print(bool(3.14))         # True

# ── Boolean va sonlar ─────────────────────────────────────────
# True = 1, False = 0 sifatida hisob-kitobda ishlatiladi
print(True + True)        # 2
print(True + False)       # 1
print(False + False)      # 0


# ------------------------------------------------------------
# input() FUNKSIYASI — FOYDALANUVCHIDAN MA'LUMOT OLISH
# ------------------------------------------------------------

"""
input() — bu foydalanuvchidan klaviaturadan ma'lumot oladi.
Qavs ichidagi matn ekranda ko'rsatiladi (so'rov sifatida).

MUHIM: input() DOIM string (matn) qaytaradi!
       Hisob-kitob qilish uchun int() yoki float() ishlatish kerak.
"""

# ASOSIY ISHLATISH:
# (Quyidagi qatorlar dastur ishga tushganda so'raydi)

ism = input("Ismingizni kiriting: ")
print("Salom,", ism)

# ── Sonlar bilan ishlash: int() orqali o'tkazish ─────────────
"""
Agar raqam kiritishni so'rasak:
  n = input("Son: ")     →  n = "15"  (string!)
  print(n + 1)           →  XATO! Matnga son qo'shib bo'lmaydi

To'g'ri yo'l:
  n = int(input("Son: "))  →  n = 15  (int)
  print(n + 1)             →  16  ✅
"""

# MISOLLAR (# ni olib tashlang va ishga tushiring):

# MISOL 1 — Ismni so'rash
ism = input("Ismingizni kiriting: ")
print("Assalomu alaykum,", ism + "!")

# MISOL 2 — Yosh hisoblash
tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))
yosh = 2025 - tugilgan_yil
print("Sizning yoshingiz:", yosh)

# MISOL 3 — Ikki son qo'shish
a = int(input("Birinchi son: "))
b = int(input("Ikkinchi son: "))
natija = a + b
print("Yig'indi:", natija)

# MISOL 4 — Kasr son bilan ishlash
narx = float(input("Narxni kiriting: "))
soni = int(input("Nechta? "))
jami = narx * soni
print("Jami to'lov:", jami)


# ------------------------------------------------------------
# SONLAR BILAN ISHLASH (Qo'shimcha funksiyalar)
# ------------------------------------------------------------

"""
Python'da sonlar bilan ishlash uchun qulay funksiyalar:

  abs(x)       — mutlaq qiymat (manfiy bo'lsa musbatga aylantiradi)
  round(x, n)  — yaxlitlash (n — o'nlik raqamlar soni)
  max(a, b, c) — eng katta son
  min(a, b, c) — eng kichik son
  pow(x, y)    — x ** y  (darajaga ko'tarish)
"""

# abs() — mutlaq qiymat
print(abs(-15))          # 15
print(abs(7))            # 7
print(abs(-3.14))        # 3.14

# round() — yaxlitlash
print(round(3.7))        # 4
print(round(3.2))        # 3
print(round(3.14159, 2)) # 3.14   (2 ta o'nlik raqam)
print(round(3.14159, 4)) # 3.1416 (4 ta o'nlik raqam)

# max() va min()
print(max(10, 5, 8))     # 10  (eng katta)
print(min(10, 5, 8))     # 5   (eng kichik)
print(max(3, 3, 3))      # 3

# pow()
print(pow(2, 8))         # 256  (2 ** 8 bilan bir xil)
print(pow(3, 3))         # 27


# ------------------------------------------------------------
# AMALIY MISOL — Hammasi birgalikda
# ------------------------------------------------------------

"""
Quyidagi kod foydalanuvchidan ma'lumot olib,
hisob-kitob qiladi va chiqaradi.
(# ni olib tashlang va ishga tushiring)
"""

# --- MISOL: To'liq hisob ---
ism         = input("Ismingiz: ")
tugilgan    = int(input("Tug'ilgan yilingiz: "))
boy_cm      = float(input("Bo'yingiz (sm da): "))

yosh        = 2025 - tugilgan
boy_m       = round(boy_cm / 100, 2)

print()
print("=== SHAXSIY MA'LUMOTLAR ===")
print("Ism      :", ism)
print("Yosh     :", yosh)
print("Bo'y (sm):", boy_cm)
print("Bo'y (m) :", boy_m)


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — O'zgaruvchilar:
  Quyidagi o'zgaruvchilarni yarating va ekranga chiqaring:
    - sevimli_rang  (string)
    - sinf_raqami   (int)
    - o'rtacha_ball (float)
    - faol          (bool — True/False)

TOPSHIRIQ 2 — Casting:
  Quyidagilarni hisoblang va turini tekshiring:
    - "2025" mantn  →  int ga aylantiring
    - 7 soni        →  float ga aylantiring
    - 3.99 float    →  int ga aylantiring (natija qanday?)

TOPSHIRIQ 3 — Boolean:
  Quyidagilarni tasavvur qiling va True/False ni chiqaring:
    - 100 > 50
    - 7 == 8
    - "python" != "java"
    - bool(0) va bool(100)

TOPSHIRIQ 4 — input() bilan kalkulator:
  Foydalanuvchidan ikkita son oling (int yoki float sifatida),
  keyin ekranga chiqaring:
    - Yig'indi (+)
    - Ayirma  (-)
    - Ko'paytma (*)
    - Bo'linma  (/)

TOPSHIRIQ 5 — Yoshni hisoblash:
  Foydalanuvchidan ismini va tug'ilgan yilini so'rang.
  Yoshini hisoblab, quyidagi formatda chiqaring:
    "Salom, [ism]! Siz [yosh] yoshdasiz."
"""


# ------------------------------------------------------------
# QUSHIMCHA RESURSLAR (Uyga vazifa uchun)
# ------------------------------------------------------------

"""
📚 RASMIY HUJJATLAR:
   https://docs.python.org/3/library/stdtypes.html
   — Python ma'lumot turlari haqida to'liq ma'lumot (inglizcha)

🌐 W3SCHOOLS:
   https://www.w3schools.com/python/python_variables.asp
   — O'zgaruvchilar

   https://www.w3schools.com/python/python_datatypes.asp
   — Data Types

   https://www.w3schools.com/python/python_casting.asp
   — Casting

   https://www.w3schools.com/python/python_booleans.asp
   — Boolean

   https://www.w3schools.com/python/python_user_input.asp
   — input() funksiyasi
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ O'zgaruvchilar — nom = qiymat
✔️ Data Types:
    str      — matn ("Salom", 'Ali')
    int      — butun son (15, -3, 1000)
    float    — kasr son (3.14, -0.5)
    complex  — kompleks son (3+2j)
✔️ type()   — qiymat turini aniqlash
✔️ Casting:
    str()   — matnga aylantirish
    int()   — butun songa aylantirish
    float() — kasr songa aylantirish
✔️ Boolean:
    True / False
    Solishtirish operatorlari: >, <, ==, !=, >=, <=
    bool() funksiyasi
✔️ input()  — foydalanuvchidan ma'lumot olish (DOIM string qaytaradi!)
✔️ Sonlar bilan ishlash:
    abs()   — mutlaq qiymat
    round() — yaxlitlash
    max()   — eng katta son
    min()   — eng kichik son
    pow()   — daraja
"""