# ============================================================
#   DARS 2: O‘zgaruvchilar, Data Types, Casting, Input()
#           va Sonlar bilan Ishlash
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================


# ------------------------------------------------------------
# DARSNING MAQSADI
# ------------------------------------------------------------

"""
Bugungi darsda:

  ✔️ O‘zgaruvchi nima ekanini bilib olamiz
  ✔️ Python’dagi asosiy data typelarni o‘rganamiz
  ✔️ type() bilan ma’lumot turini aniqlaymiz
  ✔️ Casting — ma’lumot turini o‘zgartirishni o‘rganamiz
  ✔️ input() orqali foydalanuvchidan ma’lumot olamiz
  ✔️ Arifmetik operatorlar bilan ishlaymiz
  ✔️ abs(), round(), max(), min(), pow() funksiyalarini o‘rganamiz
"""


# ------------------------------------------------------------
# O‘ZGARUVCHI NIMA?
# ------------------------------------------------------------

"""
O‘zgaruvchi — bu ma’lumotni saqlash uchun ishlatiladigan nom.

Oddiy misol:

    ism = "Ali"

Bu yerda:

    ism       → o‘zgaruvchi nomi
    =         → qiymat berish belgisi
    "Ali"     → qiymat

O‘zgaruvchini quti deb tasavvur qilish mumkin:

    ism  ┌───────┐
         │  Ali  │
         └───────┘
"""


# O‘zgaruvchiga matn saqlash
ism = "Ali"
familiya = "Karimov"

print(ism)
print(familiya)

# O‘zgaruvchiga son saqlash
yosh = 18
baho = 95

print(yosh)
print(baho)

# O‘zgaruvchiga kasr son saqlash
narx = 12500.50
harorat = 36.6

print(narx)
print(harorat)


# ------------------------------------------------------------
# O‘ZGARUVCHI NOMLASH QOIDALARI
# ------------------------------------------------------------

"""
O‘zgaruvchi nomini yozishda quyidagi qoidalarga amal qilinadi:

  ✔️ Harf bilan boshlanishi mumkin
  ✔️ _ (pastki chiziq) bilan boshlanishi mumkin
  ✔️ Raqam bilan BOSHLANISHI mumkin emas
  ✔️ Bo‘sh joy ishlatib bo‘lmaydi
  ✔️ Maxsus belgilar ishlatib bo‘lmaydi: !, @, #, $, %
  ✔️ Python kalit so‘zlarini ishlatib bo‘lmaydi:
      if, else, for, while, class, def va hokazo
"""


# TO‘G‘RI yozilgan o‘zgaruvchilar
ism = "Vali"
yosh = 20
telefon_raqam = "998901234567"
tugilgan_yil = 2005
_fayl_nomi = "malumot.txt"

# NOTO‘G‘RI o‘zgaruvchilar:
# 1ism = "Ali"              # Raqam bilan boshlanmaydi
# mening ismim = "Ali"      # Bo‘sh joy ishlatib bo‘lmaydi
# telefon-raqam = "123"     # - belgisi ishlatib bo‘lmaydi
# class = "Python"          # class — Python kalit so‘zi


# ------------------------------------------------------------
# SNAKE_CASE USULI
# ------------------------------------------------------------

"""
Python’da bir nechta so‘zdan iborat o‘zgaruvchilarni
snake_case usulida yozish tavsiya qilinadi.

So‘zlar _ belgisi bilan ajratiladi.
"""

talaba_ismi = "Aziz"
talaba_yoshi = 19
telefon_raqami = "+998 90 123 45 67"
oylik_maosh = 4500000

print(talaba_ismi)
print(talaba_yoshi)


# ------------------------------------------------------------
# O‘ZGARUVCHI QIYMATINI O‘ZGARTIRISH
# ------------------------------------------------------------

"""
O‘zgaruvchining qiymatini istalgan vaqtda o‘zgartirish mumkin.
"""

yosh = 18
print(yosh)      # Natija: 18

yosh = 19
print(yosh)      # Natija: 19

ism = "Ali"
print(ism)       # Natija: Ali

ism = "Vali"
print(ism)       # Natija: Vali


# ------------------------------------------------------------
# BIR NECHTA O‘ZGARUVCHI BILAN ISHLASH
# ------------------------------------------------------------

# Har bir o‘zgaruvchiga alohida qiymat berish
ism = "Madina"
yosh = 20
shahar = "Toshkent"

print(ism)
print(yosh)
print(shahar)

# Bir qatorda bir nechta o‘zgaruvchiga qiymat berish
ism, yosh, shahar = "Ali", 18, "Samarqand"

print(ism)
print(yosh)
print(shahar)

# Bir xil qiymatni bir nechta o‘zgaruvchiga berish
x = y = z = 10

print(x)
print(y)
print(z)


# ------------------------------------------------------------
# DATA TYPES — MA’LUMOT TURLARI
# ------------------------------------------------------------

"""
Data Type — bu o‘zgaruvchi ichida qanday turdagi ma’lumot
saqlanayotganini bildiradi.

Bugun 4 ta asosiy data type bilan ishlaymiz:

    str      — matn
    int      — butun son
    float    — kasr son
    bool     — True yoki False
"""


# ------------------------------------------------------------
# str — STRING (MATN)
# ------------------------------------------------------------

"""
str — string so‘zidan olingan.

Matnlar qo‘shtirnoq yoki birtirnoq ichida yoziladi.
"""

ism = "Rustam"
familiya = 'Isroilov'
shahar = "Farg‘ona"
telefon = "+998901234567"

print(ism)
print(familiya)
print(shahar)
print(telefon)


# ------------------------------------------------------------
# int — BUTUN SON
# ------------------------------------------------------------

"""
int — integer so‘zidan olingan.

Butun sonlar kasrsiz bo‘ladi.
"""

yosh = 20
sinf = 11
aholi_soni = 37000000
qarz = -50000

print(yosh)
print(sinf)
print(aholi_soni)
print(qarz)


# ------------------------------------------------------------
# float — KASR SON
# ------------------------------------------------------------

"""
float — kasr sonlar uchun ishlatiladi.

Python’da kasr son ajratishda vergul emas, nuqta ishlatiladi.
"""

narx = 12500.50
boy = 1.75
harorat = 36.6
pi = 3.14

print(narx)
print(boy)
print(harorat)
print(pi)

# NOTO‘G‘RI:
# narx = 12,5       # Bu Python’da kasr son hisoblanmaydi

# TO‘G‘RI:
narx = 12.5


# ------------------------------------------------------------
# bool — BOOLEAN
# ------------------------------------------------------------

"""
bool — faqat 2 ta qiymat saqlaydi:

    True    — rost, ha, to‘g‘ri
    False   — yolg‘on, yo‘q, noto‘g‘ri

True va False katta harf bilan yoziladi.
"""

talaba = True
tizim_ochiq = False

print(talaba)
print(tizim_ochiq)

# Misollar
yosh = 20
balog_atga_yetgan = yosh >= 18

print(balog_atga_yetgan)     # Natija: True

baho = 45
imtihondan_otdi = baho >= 60

print(imtihondan_otdi)       # Natija: False


# ------------------------------------------------------------
# type() — MA’LUMOT TURINI ANIQLASH
# ------------------------------------------------------------

"""
type() funksiyasi o‘zgaruvchining data type’ini ko‘rsatadi.
"""

ism = "Ali"
yosh = 18
narx = 12.5
talaba = True

print(type(ism))       # Natija: <class 'str'>
print(type(yosh))      # Natija: <class 'int'>
print(type(narx))      # Natija: <class 'float'>
print(type(talaba))    # Natija: <class 'bool'>


# ------------------------------------------------------------
# CASTING — MA’LUMOT TURINI O‘ZGARTIRISH
# ------------------------------------------------------------

"""
Casting — ma’lumot turini boshqa turga o‘zgartirish.

Asosiy casting funksiyalari:

    str()       → matnga aylantiradi
    int()       → butun songa aylantiradi
    float()     → kasr songa aylantiradi
    bool()      → True yoki False’ga aylantiradi
"""


# ------------------------------------------------------------
# str() — MATNGA AYLANTIRISH
# ------------------------------------------------------------

yosh = 18
yosh_matn = str(yosh)

print(yosh_matn)             # Natija: 18
print(type(yosh_matn))       # Natija: <class 'str'>

# Son va matnni birlashtirish
ism = "Ali"
yosh = 18

print(ism + " " + str(yosh) + " yoshda")


# ------------------------------------------------------------
# int() — BUTUN SONGA AYLANTIRISH
# ------------------------------------------------------------

yosh_matn = "20"
yosh = int(yosh_matn)

print(yosh)                  # Natija: 20
print(type(yosh))            # Natija: <class 'int'>

# float sonni int ga aylantirish
narx = 12.9
butun_narx = int(narx)

print(butun_narx)            # Natija: 12
# int() kasr qismini tashlab yuboradi

# DIQQAT:
# int("12.5") xato beradi!
# Chunki "12.5" matn ichida kasr son bor.


# ------------------------------------------------------------
# float() — KASR SONGA AYLANTIRISH
# ------------------------------------------------------------

son = 25
kasr_son = float(son)

print(kasr_son)              # Natija: 25.0
print(type(kasr_son))        # Natija: <class 'float'>

narx_matn = "12500.50"
narx = float(narx_matn)

print(narx)                  # Natija: 12500.5


# ------------------------------------------------------------
# bool() — BOOLEAN’GA AYLANTIRISH
# ------------------------------------------------------------

"""
bool() funksiyasi qiymatni True yoki False’ga aylantiradi.

Quyidagilar False bo‘ladi:

    bool(False)
    bool(0)
    bool(0.0)
    bool("")
    bool(None)

Qolgan deyarli barcha qiymatlar True bo‘ladi.
"""

print(bool(True))        # Natija: True
print(bool(False))       # Natija: False

print(bool(1))           # Natija: True
print(bool(0))           # Natija: False

print(bool("Ali"))       # Natija: True
print(bool(""))          # Natija: False

# DIQQAT:
# "False" — bu matn, shuning uchun True hisoblanadi!
print(bool("False"))     # Natija: True


# ------------------------------------------------------------
# input() — FOYDALANUVCHIDAN MA’LUMOT OLISH
# ------------------------------------------------------------

"""
input() — foydalanuvchidan ma’lumot olish uchun ishlatiladi.

Muhim qoida:

    input() DOIM str, ya’ni matn qaytaradi.

Foydalanuvchi 18 sonini yozsa ham,
input() uni "18" ko‘rinishida matn sifatida oladi.
"""

ism = input("Ismingizni kiriting: ")

print("Assalomu alaykum, " + ism + "!")

# input() orqali yosh olish
yosh = input("Yoshingizni kiriting: ")

print("Sizning yoshingiz: " + yosh)

# type() bilan tekshirish
print(type(yosh))        # Natija: <class 'str'>


# ------------------------------------------------------------
# input() VA CASTING BILAN ISHLASH
# ------------------------------------------------------------

"""
Agar input orqali son olish kerak bo‘lsa,
uni int() yoki float() bilan aylantirish kerak.
"""

yosh = int(input("Yoshingizni kiriting: "))
print(yosh)
print(type(yosh))        # Natija: <class 'int'>

narx = float(input("Mahsulot narxini kiriting: "))
print(narx)
print(type(narx))        # Natija: <class 'float'>


# ------------------------------------------------------------
# ARIFMETIK OPERATORLAR
# ------------------------------------------------------------

"""
Operator — bu sonlar ustida amal bajaruvchi belgi.

Python’da 7 ta asosiy arifmetik operator bor:

  Operator   Nomi                    Misol       Natija
  ────────   ──────────────────────  ─────────   ──────
  +          Qo‘shish                5 + 3       8
  -          Ayirish                 10 - 4      6
  *          Ko‘paytirish            3 * 7       21
  /          Bo‘lish                 20 / 4      5.0
  %          Qoldiq                  10 % 3      1
  //         Butun bo‘lish           10 // 3     3
  **         Daraja                   2 ** 8     256
"""


# ── + Qo‘shish ──────────────────────────────────────────────

print(5 + 3)            # Natija: 8
print(100 + 250)        # Natija: 350


# ── - Ayirish ───────────────────────────────────────────────

print(10 - 4)           # Natija: 6
print(1000 - 375)       # Natija: 625


# ── * Ko‘paytirish ──────────────────────────────────────────

print(3 * 7)            # Natija: 21
print(12 * 12)          # Natija: 144


# ── / Bo‘lish ───────────────────────────────────────────────

"""
/ bilan bo‘lishda natija har doim float bo‘ladi.
"""

print(20 / 4)           # Natija: 5.0
print(7 / 2)            # Natija: 3.5


# ── % Qoldiq ────────────────────────────────────────────────

"""
% — bo‘lishdan qolgan qoldiqni beradi.
"""

print(10 % 3)           # Natija: 1
print(15 % 4)           # Natija: 3
print(10 % 2)           # Natija: 0

# Sonning juft yoki toqligini aniqlash
print(14 % 2)           # Natija: 0 → juft son
print(17 % 2)           # Natija: 1 → toq son


# ── // Butun bo‘lish ────────────────────────────────────────

"""
// bilan bo‘lganda faqat butun qismi olinadi.

Masalan:

    10 / 3     → 3.333...
    10 // 3    → 3
"""

print(10 // 3)          # Natija: 3
print(7 // 2)           # Natija: 3
print(15 // 4)          # Natija: 3


# ── ** Daraja ───────────────────────────────────────────────

"""
** — bir sonni boshqa son darajasiga ko‘taradi.
"""

print(2 ** 8)           # Natija: 256
print(3 ** 3)           # Natija: 27
print(5 ** 2)           # Natija: 25


# ------------------------------------------------------------
# ARIFMETIK AMALLAR KETMA-KETLIGI
# ------------------------------------------------------------

"""
Python amallarni quyidagi tartibda bajaradi:

  1. Qavs ichidagi amal: ()
  2. Daraja: **
  3. Ko‘paytirish va bo‘lish: *, /, //, %
  4. Qo‘shish va ayirish: +, -
"""

print(2 + 3 * 4)        # Natija: 14
# Avval 3 * 4 = 12, keyin 2 + 12 = 14

print((2 + 3) * 4)      # Natija: 20
# Avval qavs ichidagi 2 + 3 = 5, keyin 5 * 4 = 20


# ------------------------------------------------------------
# SONLAR BILAN ISHLASH FUNKSIYALARI
# ------------------------------------------------------------

"""
Python’da sonlar bilan ishlash uchun foydali funksiyalar bor:

    abs()       → sonning mutlaq qiymati
    round()     → sonni yaxlitlash
    max()       → eng katta son
    min()       → eng kichik son
    pow()       → darajaga ko‘tarish
"""


# ── abs() — Mutlaq qiymat ───────────────────────────────────

"""
abs() manfiy sonni musbat qiymatga aylantiradi.
"""

print(abs(-10))         # Natija: 10
print(abs(15))          # Natija: 15
print(abs(-3.5))        # Natija: 3.5


# ── round() — Yaxlitlash ────────────────────────────────────

print(round(3.4))       # Natija: 3
print(round(3.7))       # Natija: 4
print(round(12.567))    # Natija: 13

# Verguldan keyin nechta xona qolishini ko‘rsatish
print(round(3.14159, 2))    # Natija: 3.14
print(round(12.5678, 3))    # Natija: 12.568


# ── max() — Eng katta son ───────────────────────────────────

print(max(5, 10, 3))        # Natija: 10
print(max(100, 25, 999))    # Natija: 999


# ── min() — Eng kichik son ──────────────────────────────────

print(min(5, 10, 3))        # Natija: 3
print(min(100, 25, 999))    # Natija: 25


# ── pow() — Darajaga ko‘tarish ──────────────────────────────

print(pow(2, 8))            # Natija: 256
print(pow(5, 2))            # Natija: 25

# pow(2, 8) va 2 ** 8 bir xil natija beradi
print(2 ** 8)               # Natija: 256


# ------------------------------------------------------------
# AMALIY MISOLLAR
# ------------------------------------------------------------

# MISOL 1 — Foydalanuvchi ma’lumotlari
ism = input("Ismingizni kiriting: ")
yosh = int(input("Yoshingizni kiriting: "))

print("Assalomu alaykum, " + ism + "!")
print("Siz " + str(yosh) + " yoshdasiz.")


# MISOL 2 — Tug‘ilgan yilni aniqlash
joriy_yil = 2026
yosh = int(input("Yoshingizni kiriting: "))

tugilgan_yil = joriy_yil - yosh

print("Siz taxminan " + str(tugilgan_yil) + "-yilda tug‘ilgansiz.")


# MISOL 3 — Ikki sonning yig‘indisi
son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))

yigindi = son1 + son2

print("Yig‘indi:", yigindi)


# MISOL 4 — Doiraning yuzini hisoblash
radius = float(input("Doira radiusini kiriting: "))

pi = 3.14
yuza = pi * radius ** 2

print("Doiraning yuzasi:", yuza)


# MISOL 5 — Daqiqani soat va daqiqaga aylantirish
daqiqalar = int(input("Daqiqani kiriting: "))

soat = daqiqalar // 60
qolgan_daqiqa = daqiqalar % 60

print(daqiqalar, "daqiqa =", soat, "soat", qolgan_daqiqa, "daqiqa")


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Oson:

  Quyidagi o‘zgaruvchilarni yarating:

    - ism
    - familiya
    - yosh
    - shahar
    - talaba

  So‘ng ularni print() orqali ekranga chiqaring.


TOPSHIRIQ 2 — Data Type:

  Quyidagi qiymatlarning type()ini ekranga chiqaring:

    "Python"
    2026
    3.14
    True
    -50


TOPSHIRIQ 3 — Casting:

  Quyidagi o‘zgaruvchilarni kerakli type’ga o‘tkazing:

    yosh = "18"        → int
    narx = "12500.5"   → float
    son = 50           → str


TOPSHIRIQ 4 — Foydalanuvchi ma’lumotlari:

  Foydalanuvchidan quyidagilarni so‘rang:

    - Ismi
    - Yoshi
    - Shahrini

  Quyidagiga o‘xshash natija chiqaring:

    Assalomu alaykum, Ali!
    Siz 18 yoshdasiz.
    Siz Toshkent shahrida yashaysiz.


TOPSHIRIQ 5 — Hisob-kitob:

  Foydalanuvchidan 2 ta son oling.

  Quyidagilarni ekranga chiqaring:

    - Yig‘indisi
    - Ayirmasi
    - Ko‘paytmasi
    - Bo‘linmasi


TOPSHIRIQ 6 — Qiziqarli:

  Foydalanuvchidan umumiy soniyalarni so‘rang.

  Uni soat, daqiqa va soniyaga aylantiring.

  Masalan:

    3675 soniya = 1 soat 1 daqiqa 15 soniya
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O‘RGANDIK?
# ------------------------------------------------------------

"""
✔️ O‘zgaruvchi nima ekanini
✔️ O‘zgaruvchi nomlash qoidalarini
✔️ str — matn
✔️ int — butun son
✔️ float — kasr son
✔️ bool — True va False
✔️ type() bilan data type aniqlashni
✔️ str(), int(), float(), bool() casting funksiyalarini
✔️ input() bilan foydalanuvchidan ma’lumot olishni
✔️ Arifmetik operatorlarni:
    +   Qo‘shish
    -   Ayirish
    *   Ko‘paytirish
    /   Bo‘lish
    %   Qoldiq
    //  Butun bo‘lish
    **  Daraja
✔️ abs(), round(), max(), min(), pow() funksiyalarini
"""
