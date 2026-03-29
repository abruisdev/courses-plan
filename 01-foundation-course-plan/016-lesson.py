# ============================================================
#   DARS 16: Pythonda Modullar
#   datetime, random, math, qrcode, barcode, opencv, turtle
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# MODUL NIMA?
# ------------------------------------------------------------

"""
Modul — bu Python funksiyalari to'plami bo'lgan fayl.
import kalit so'zi bilan ulanadi.

Modul turlari:
  1. Standart (Python bilan birga keladi): math, random, datetime, os
  2. Tashqi (pip orqali o'rnatiladi): qrcode, opencv, barcode
  3. O'z modullaringiz (siz yaratgan .py fayllar)

Qanday ulanadi:
  import modul_nomi
  from modul_nomi import funksiya_nomi
  from modul_nomi import *             ← barcha funksiyalar
  import modul_nomi as qisqartma
"""


# ============================================================
# 1. O'Z MODULINGIZNI YARATISH
# ============================================================

"""
Har qanday .py fayl — bu modul!
Masalan, "hisob.py" faylini yaratsangiz:

  # hisob.py
  def qo_sh(a, b):
      return a + b

  def ayir(a, b):
      return a - b

  PI = 3.14159

Keyin boshqa fayldan:
  import hisob
  print(hisob.qo_sh(5, 3))    # 8
  print(hisob.PI)              # 3.14159

  # yoki:
  from hisob import qo_sh
  print(qo_sh(5, 3))           # 8
"""

# Misol uchun oddiy modul yaratib ko'ramiz:
# (Hozir shu faylda o'zimiz yozamiz)

def doira_yuzi(r):
    """Doiraning yuzini hisoblaydi"""
    import math
    return round(math.pi * r ** 2, 2)

def to_g_ri_to_rtburchak_perimetri(a, b):
    """To'g'ri to'rtburchak perimetrini hisoblaydi"""
    return 2 * (a + b)

# Test:
print(doira_yuzi(5))                         # 78.54
print(to_g_ri_to_rtburchak_perimetri(4, 6))  # 20


# ============================================================
# 2. datetime MODULI — SANA VA VAQT
# ============================================================

"""
datetime — sana, vaqt bilan ishlash uchun standart modul.

Asosiy classlar:
  datetime.datetime  — sana + vaqt
  datetime.date      — faqat sana
  datetime.time      — faqat vaqt
  datetime.timedelta — ikki sana orasidagi farq
"""

import datetime

# ── Hozirgi vaqt ──────────────────────────────────────────────
hozir = datetime.datetime.now()
print(hozir)
# 2025-06-15 14:30:25.123456

print(type(hozir))    # <class 'datetime.datetime'>

# ── Tarkibiy qismlar ──────────────────────────────────────────
print(hozir.year)         # Yil:    2025
print(hozir.month)        # Oy:     6
print(hozir.day)          # Kun:    15
print(hozir.hour)         # Soat:   14
print(hozir.minute)       # Daqiqa: 30
print(hozir.second)       # Soniya: 25
print(hozir.microsecond)  # Mikro:  123456

# ── date() — Faqat sana ───────────────────────────────────────
bugun = datetime.date.today()
print(bugun)              # 2025-06-15

# Sana yaratish:
yangi_yil = datetime.date(2026, 1, 1)
print(yangi_yil)          # 2026-01-01

# ── time() — Faqat vaqt ───────────────────────────────────────
vaqt = datetime.time(14, 30, 0)
print(vaqt)    # 14:30:00

# ── Sana formatlash — strftime() ──────────────────────────────
"""
strftime("format") — datetime ni stringga aylantiradi.

Asosiy format kodlari:
  %Y — to'liq yil (2025)
  %m — oy raqami (01-12)
  %d — kun (01-31)
  %H — soat 24-format (00-23)
  %M — daqiqa (00-59)
  %S — soniya (00-59)
  %A — hafta kuni nomi (Monday)
  %B — oy nomi (June)
"""

hozir = datetime.datetime.now()
print(hozir.strftime("%Y-%m-%d"))
# 2025-06-15

print(hozir.strftime("%d/%m/%Y %H:%M"))
# 15/06/2025 14:30

print(hozir.strftime("%A, %B %d, %Y"))
# Sunday, June 15, 2025

# ── timedelta — Farq hisoblash ────────────────────────────────
"""
timedelta — ikki vaqt orasidagi farqni ifodalaydi.
"""

bugun = datetime.date.today()
bir_hafta_keyin = bugun + datetime.timedelta(days=7)
print(bir_hafta_keyin)

yangi_yil = datetime.date(2026, 1, 1)
qolgan = yangi_yil - bugun
print(f"Yangi yilgacha: {qolgan.days} kun")

# ── strptime() — Stringdan datetime ──────────────────────────
sana_matn = "15.06.2025"
sana = datetime.datetime.strptime(sana_matn, "%d.%m.%Y")
print(sana)           # 2025-06-15 00:00:00
print(sana.year)      # 2025

# ── Amaliy: Yosh hisoblash ────────────────────────────────────
def yoshni_hisobla(tugilgan_kun):
    bugun = datetime.date.today()
    yosh = bugun.year - tugilgan_kun.year
    if (bugun.month, bugun.day) < (tugilgan_kun.month, tugilgan_kun.day):
        yosh -= 1
    return yosh

tugilgan = datetime.date(2010, 3, 15)
print(f"Yosh: {yoshni_hisobla(tugilgan)}")


# ============================================================
# 3. random MODULI — TASODIFIY SONLAR
# ============================================================

"""
random — tasodifiy sonlar va tanlovlar uchun.
"""

import random

# ── randint() — Tasodifiy butun son ──────────────────────────
"""
random.randint(a, b)  — a dan b gacha butun son (ikkalasi kiritiladi)
"""
print(random.randint(1, 10))      # masalan: 7
print(random.randint(0, 100))     # masalan: 43
print(random.randint(-5, 5))      # masalan: -2

# Zar otish simulyatsiyasi:
zar = random.randint(1, 6)
print(f"Zar: {zar}")

# ── random() — 0.0 dan 1.0 gacha float ───────────────────────
print(random.random())    # masalan: 0.7324...

# ── uniform() — Berilgan oralikda float ──────────────────────
print(random.uniform(1.5, 5.5))   # masalan: 3.2145...

# ── choice() — Ro'yxatdan tasodifiy tanlash ──────────────────
"""
random.choice(ketma_ketlik)  — bitta element tanlaydi
"""
mevalar = ["olma", "banan", "uzum", "shaftoli"]
print(random.choice(mevalar))      # masalan: uzum

ranglar  = ["qizil", "yashil", "ko'k", "sariq"]
print(random.choice(ranglar))

# ── choices() — Bir nechta tanlash (qaytarish bilan) ─────────
print(random.choices(mevalar, k=3))   # masalan: ['banan', 'banan', 'olma']

# ── sample() — Bir nechta tanlash (qaytarmasdan) ─────────────
"""
random.sample(ketma_ketlik, k)  — k ta element, takrorsiz
"""
print(random.sample(mevalar, 2))   # masalan: ['shaftoli', 'uzum']
print(random.sample(range(1, 50), 6))   # lottereya kabi 6 ta son

# ── shuffle() — Aralash ───────────────────────────────────────
"""
random.shuffle(ro'yxat)  — ro'yxatni tasodifiy aralashtirasdi (o'zi o'zgaradi)
"""
kartalar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(kartalar)
print(kartalar)   # masalan: [5, 2, 9, 1, 7, 3, 8, 4, 10, 6]

# ── seed() — Natijani takrorlanadigan qilish ──────────────────
"""
random.seed(n)  — har safar bir xil "tasodifiy" natija beradi.
Test va debugging uchun foydali.
"""
random.seed(42)
print(random.randint(1, 100))   # har doim bir xil: 82
random.seed(42)
print(random.randint(1, 100))   # yana xuddi shu: 82

# ── Amaliy: Parol generatori ──────────────────────────────────
import string

def parol_yaratish(uzunlik=12):
    belgilar = string.ascii_letters + string.digits + "!@#$%"
    parol = ''.join(random.choices(belgilar, k=uzunlik))
    return parol

print(f"Yangi parol: {parol_yaratish()}")
print(f"Yangi parol: {parol_yaratish(8)}")


# ============================================================
# 4. math MODULI — MATEMATIK FUNKSIYALAR
# ============================================================

"""
math — ilg'or matematik hisob-kitoblar uchun.
"""

import math

# ── Konstantalar ─────────────────────────────────────────────
print(math.pi)     # 3.141592653589793  — π
print(math.e)      # 2.718281828459045  — Eyler soni
print(math.inf)    # inf  — cheksizlik
print(math.tau)    # 6.283185307...     — 2π

# ── sqrt() — Kvadrat ildiz ────────────────────────────────────
print(math.sqrt(25))     # 5.0
print(math.sqrt(2))      # 1.4142135623...
print(math.sqrt(144))    # 12.0

# ── ceil() va floor() — Yaxlitlash ───────────────────────────
"""
ceil()  — yuqoriga yaxlitlash (katta butun songa)
floor() — pastga yaxlitlash (kichik butun songa)
"""
print(math.ceil(3.2))    # 4   (yuqoriga)
print(math.ceil(3.9))    # 4
print(math.floor(3.9))   # 3   (pastga)
print(math.floor(3.2))   # 3
print(math.floor(-3.2))  # -4  (manfiy uchun diqqat!)

# ── pow() va log() ────────────────────────────────────────────
print(math.pow(2, 10))       # 1024.0  (2^10)
print(math.log(100, 10))     # 2.0     (log10(100) = 2)
print(math.log2(8))          # 3.0     (log2(8) = 3)
print(math.log(math.e))      # 1.0     (ln(e) = 1)

# ── sin(), cos(), tan() ───────────────────────────────────────
"""
Trigonometrik funksiyalar RADIAN qabul qiladi!
Gradusdan radianga: radians = daraja * π / 180
"""
print(math.sin(math.pi / 2))   # 1.0   — sin(90°)
print(math.cos(0))             # 1.0   — cos(0°)
print(math.sin(math.radians(30)))  # 0.5  — sin(30°)

# ── factorial(), gcd(), lcm() ────────────────────────────────
print(math.factorial(5))      # 120  — 5!
print(math.gcd(12, 8))        # 4    — eng katta umumiy bo'luvchi
print(math.lcm(4, 6))         # 12   — eng kichik umumiy karrali (Python 3.9+)

# ── Amaliy: Gipotenuz hisoblash ───────────────────────────────
def gipotenuz(a, b):
    return math.sqrt(a**2 + b**2)

print(gipotenuz(3, 4))    # 5.0
print(gipotenuz(5, 12))   # 13.0

# ── Amaliy: Doira ────────────────────────────────────────────
r = 7
print(f"Yuzi      : {math.pi * r**2:.2f}")
print(f"Uzunligi  : {2 * math.pi * r:.2f}")


# ============================================================
# 5. qrcode MODULI — QR KOD YARATISH
# ============================================================

"""
O'rnatish:
  pip install qrcode[pil]

Keyin ishlatish:
"""

# import qrcode
#
# def qr_yaratish(mazmun, fayl_nomi="qr.png"):
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(mazmun)
#     qr.make(fit=True)
#     img = qr.make_image(fill_color="black", back_color="white")
#     img.save(fayl_nomi)
#     print(f"QR kod saqlandi: {fayl_nomi}")
#
# qr_yaratish("https://python.org", "python_qr.png")
# qr_yaratish("Salom, men Pythonni o'rganaman!", "salom_qr.png")

print("""
qrcode o'rnatish:
  pip install qrcode[pil]

Ishlatish:
  import qrcode
  img = qrcode.make("https://python.org")
  img.save("qr.png")
""")


# ============================================================
# 6. barcode MODULI — SHTRIX KOD
# ============================================================

"""
O'rnatish:
  pip install python-barcode[images]
"""

# from barcode import Code128
# from barcode.writer import ImageWriter
#
# def shtrix_yaratish(kod, fayl_nomi="shtrix"):
#     barcode = Code128(kod, writer=ImageWriter())
#     barcode.save(fayl_nomi)
#     print(f"Shtrix kod saqlandi: {fayl_nomi}.png")
#
# shtrix_yaratish("12345678")
# shtrix_yaratish("PYTHON2025")

print("""
barcode o'rnatish:
  pip install python-barcode[images]

Ishlatish:
  from barcode import EAN13
  from barcode.writer import ImageWriter
  ean = EAN13("123456789012", writer=ImageWriter())
  ean.save("shtrix")
""")


# ============================================================
# 7. opencv MODULI — RASM VA VIDEO BILAN ISHLASH
# ============================================================

"""
OpenCV — rasmlar va video bilan ishlash uchun kuchli kutubxona.

O'rnatish:
  pip install opencv-python

Nima qilish mumkin:
  - Rasm ochish va saqlash
  - Ranglarni o'zgartirish
  - Yuzlarni aniqlash (face detection)
  - Video o'qish
"""

# import cv2
#
# # Rasm ochish:
# rasm = cv2.imread("rasm.jpg")
# print(f"O'lcham: {rasm.shape}")   # (balandlik, kenglik, kanal)
#
# # Kulrang rangga aylantirish:
# kulrang = cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY)
#
# # Saqlash:
# cv2.imwrite("kulrang.jpg", kulrang)
#
# # Ko'rsatish:
# cv2.imshow("Rasm", rasm)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print("""
opencv o'rnatish:
  pip install opencv-python

Asosiy amallar:
  import cv2
  rasm = cv2.imread("rasm.jpg")
  kulrang = cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY)
  cv2.imwrite("natija.jpg", kulrang)
  cv2.imshow("Ko'rish", rasm)
  cv2.waitKey(0)
""")


# ============================================================
# 8. turtle MODULI — GRAFIKA VA CHIZISH
# ============================================================

"""
turtle — qiziqarli grafik chizish uchun standart modul.
O'rnatish shart emas — Python bilan birga keladi.

Asosiy buyruqlar:
  forward(n)   / fd(n)   — n qadam oldinga
  backward(n)  / bk(n)   — n qadam orqaga
  right(daraja)/ rt(...)  — o'ngga burish
  left(daraja) / lt(...)  — chapga burish
  penup()      / pu()    — qalamni ko'tarish (iz qoldirmaydi)
  pendown()    / pd()    — qalamni tushirish
  pencolor(rang)          — rang o'rnatish
  pensize(n)              — qalem qalinligi
  speed(n)                — tezlik (1-10, 0 = tezkor)
  circle(r)               — doira chizish
  goto(x, y)              — koordinataga o'tish
  hideturtle()            — toshbaqani yashirish
  bgcolor(rang)           — fon rangini o'zgartirish
"""

# ── Turtle misollari ─────────────────────────────────────────
# (Kommentdan olib ishlating)

# MISOL 1 — To'rtburchak:
# import turtle
# t = turtle.Turtle()
# for _ in range(4):
#     t.forward(100)
#     t.right(90)
# turtle.done()

# MISOL 2 — Yulduz:
# import turtle
# t = turtle.Turtle()
# t.speed(0)
# for _ in range(5):
#     t.forward(100)
#     t.right(144)   # yulduz burchagi
# turtle.done()

# MISOL 3 — Spiral:
# import turtle
# t = turtle.Turtle()
# t.speed(0)
# ranglar = ["red", "orange", "yellow", "green", "blue", "purple"]
# for i in range(200):
#     t.pencolor(ranglar[i % 6])
#     t.forward(i * 0.5)
#     t.right(59)
# turtle.done()

# MISOL 4 — Ko'pburchak:
# import turtle
# def ko_pburchak(n, tomon):
#     t = turtle.Turtle()
#     burchak = 360 / n
#     for _ in range(n):
#         t.forward(tobon)
#         t.right(burchak)
# ko'pburchak(6, 80)   # Oltiburchak
# turtle.done()

print("""
turtle ishlatish uchun kommentdan oling:

  import turtle
  t = turtle.Turtle()
  t.speed(3)
  for _ in range(4):
      t.forward(100)
      t.right(90)
  turtle.done()
""")


# ============================================================
# AMALIY DASTUR — Barcha modullardan foydalanish
# ============================================================

import datetime
import random
import math

def haftalik_hisobot():
    hozir = datetime.datetime.now()
    print(f"\n{'=' * 50}")
    print(f"{'HAFTALIK HISOBOT':^50}")
    print(f"Sana: {hozir.strftime('%d.%m.%Y %H:%M')}")
    print(f"{'=' * 50}")

    # Random statistika (misol uchun)
    kunlar = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma"]
    daromad = [random.randint(500000, 2000000) for _ in range(5)]
    xarajat = [random.randint(100000, 500000) for _ in range(5)]

    print(f"\n{'Kun':<12} {'Daromad':>15} {'Xarajat':>15} {'Foyda':>15}")
    print("-" * 60)

    jami_daromad = 0
    jami_xarajat = 0

    for kun, d, x in zip(kunlar, daromad, xarajat):
        foyda = d - x
        jami_daromad += d
        jami_xarajat += x
        print(f"{kun:<12} {d:>15,} {x:>15,} {foyda:>15,}")

    print("-" * 60)
    jami_foyda = jami_daromad - jami_xarajat
    print(f"{'JAMI':<12} {jami_daromad:>15,} {jami_xarajat:>15,} {jami_foyda:>15,}")
    print(f"\nO'rtacha kunlik foyda: {jami_foyda // 5:,} so'm")
    print(f"Yillik prognoz: {jami_foyda * 52:,} so'm")

haftalik_hisobot()


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — datetime (O'rta):
  a) Bugungi sanani DD.MM.YYYY formatda chiqaring
  b) Ertangi sanani hisoblang
  c) Tug'ilgan kuningizgacha necha kun qolganini hisoblang
  d) Hozirgi vaqtni HH:MM:SS formatda chiqaring

TOPSHIRIQ 2 — random (O'rta):
  a) 1 dan 100 gacha 10 ta tasodifiy son ro'yxati yarating
  b) Bu ro'yxatdan tasodifiy 3 ta element tanlang
  c) Ro'yxatni aralashtiring
  d) 8 belgidan iborat tasodifiy parol yarating (harf + raqam)

TOPSHIRIQ 3 — math (O'rta):
  a) 1 dan 20 gacha sonlarning kvadrat ildizini hisoblang
  b) Uchburchak tomonlari a=3, b=4, c=5 — to'g'ri burchaklimi? (Pifagor)
  c) Doira r=10 uchun: yuzi, uzunligi
  d) log2(1024) ni hisoblang

TOPSHIRIQ 4 — O'z moduli (Qiyin):
  "geometriya.py" faylini yarating:
    - to'rtburchak_yuzi(a, b)
    - uchburchak_yuzi(a, h)
    - doira_yuzi(r)
    - doira_uzunligi(r)
    - kub_hajmi(a)
  Bosh faylda import qilib ishlating.

TOPSHIRIQ 5 — Turtle (Ijodiy):
  turtle bilan quyidagilarni chizing:
    a) Uchburchak
    b) Yulduz (5 ta uchi bor)
    c) Rang-barang spiral
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ Modul nima va qanday ulanadi (import)
✔️ O'z modulingizni yaratish
✔️ datetime moduli:
    datetime.now()      — hozirgi vaqt
    date.today()        — bugungi sana
    strftime()          — formatlash
    strptime()          — stringdan parsing
    timedelta()         — vaqt farqi
✔️ random moduli:
    randint(a, b)       — butun son
    random()            — 0.0 dan 1.0
    choice(lst)         — bitta tanlash
    choices(lst, k=n)   — n ta tanlash
    sample(lst, k)      — n ta takrorisiz
    shuffle(lst)        — aralash
    seed(n)             — qayta takrorlanadigan
✔️ math moduli:
    pi, e               — konstantalar
    sqrt()              — kvadrat ildiz
    ceil(), floor()     — yaxlitlash
    pow(), log()        — quvvat, logarifm
    sin(), cos(), tan() — trigonometrik
    factorial()         — faktorial
    gcd(), lcm()        — EKUB, EKUK
✔️ qrcode, barcode     — kod yaratish (pip)
✔️ opencv              — rasm/video (pip)
✔️ turtle              — grafika (standart)
"""