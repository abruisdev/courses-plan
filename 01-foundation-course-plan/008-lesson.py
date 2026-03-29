# ============================================================
#   DARS 8: String va String Metodlar
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# STRING NIMA?
# ------------------------------------------------------------

"""
String — bu matn ma'lumoti.
Qo'shtirnoq (" ") yoki apostrof (' ') ichida yoziladi.

Kundalik hayotda:
  - Ism, familiya
  - Manzil, telefon raqam
  - Xabar, sarlavha
  - Parol, foydalanuvchi nomi

Python'da string = ketma-ket harflar to'plami.
Har bir harf o'z INDEKSIGA (tartib raqamiga) ega.

  s  t  r  i  n  g
  0  1  2  3  4  5   ← musbat indekslar (chapdan)
 -6 -5 -4 -3 -2 -1   ← manfiy indekslar (o'ngdan)
"""

matn = "Python"
print(matn)            # Python
print(type(matn))      # <class 'str'>


# ============================================================
# STRING YARATISH USULLARI
# ============================================================

# ── Qo'shtirnoq bilan ────────────────────────────────────────
s1 = "Salom, Dunyo!"          # ikki qo'shtirnoq
s2 = 'Men Python o\'rganaman' # apostrof (ichida apostrof: \')
s3 = "It's easy!"             # ikki qo'shtirnoq ichida apostrof

print(s1)   # Salom, Dunyo!
print(s2)   # Men Python o'rganaman
print(s3)   # It's easy!

# ── Ko'p qatorli string — uch qo'shtirnoq ────────────────────
tarjimai_hol = """
Mening ismim Ali.
Men 15 yoshdaman.
Toshkentda yashayman.
"""
print(tarjimai_hol)


# ============================================================
# INDEKSLASH (Indexing) — Bitta Harf Olish
# ============================================================

"""
String ichidagi bitta harfni olish uchun
o'zgaruvchi nomi yoniga [indeks] yoziladi.

MUHIM:
  - Indeks 0 dan boshlanadi!
  - Oxirgi harfning indeksi = uzunlik - 1
  - Manfiy indeks: -1 = oxirgi harf, -2 = oxiridan ikkinchi...
"""

ism = "Python"
#      P  y  t  h  o  n
#      0  1  2  3  4  5

print(ism[0])    # P  — birinchi harf
print(ism[1])    # y
print(ism[5])    # n  — oxirgi harf
print(ism[-1])   # n  — oxirgi harf (manfiy)
print(ism[-2])   # o  — oxiridan ikkinchi

# ── Xato holati ──────────────────────────────────────────────
"""
Mavjud bo'lmagan indeksga murojaat qilsangiz — XATO!
  ism[10]  →  IndexError: string index out of range
"""


# ============================================================
# QIRQISH (Slicing) — Bir Qism Matnni Olish
# ============================================================

"""
Qirqish — stringning bir qismini ajratib olish.

Sintaksis:
  matn[boshlash : tugash]
  matn[boshlash : tugash : qadam]

QOIDA:
  - boshlash indeksi QO'SHILADI
  - tugash indeksi QO'SHILMAYDI (tugash - 1 gacha oladi)
  - qadam — necha tashlab o'tish (default: 1)
"""

s = "Assalomu alaykum"
#    0123456789...

# ── Asosiy qirqish ───────────────────────────────────────────
print(s[0:8])      # Assalom  (0 dan 7 gacha)
print(s[9:16])     # alaykum  (9 dan 15 gacha)

# ── Boshlashni tashlab ketish ─────────────────────────────────
print(s[:7])       # Assalom  (boshidan 7 gacha)

# ── Tugashni tashlab ketish ───────────────────────────────────
print(s[9:])       # alaykum  (9 dan oxirigacha)

# ── Hammasini olish ───────────────────────────────────────────
print(s[:])        # Assalomu alaykum

# ── Qadam bilan qirqish ───────────────────────────────────────
s2 = "0123456789"
print(s2[::2])     # 02468  (har ikkinchi harf)
print(s2[1::2])    # 13579  (1 dan boshlab har ikkinchi)

# ── Teskari qirqish ───────────────────────────────────────────
print(s2[::-1])    # 9876543210  (butun stringni teskari qiladi)
print(s2[7:2:-1])  # 76543

# ── Amaliy misollar ──────────────────────────────────────────
kod = "AB-2025-XY"
print(kod[3:7])    # 2025  — raqam qismni olish
print(kod[:2])     # AB    — prefiks
print(kod[-2:])    # XY    — suffiks

matn = "Python dasturlash"
print(matn[::-1])  # hsalrutsad nohtyP — teskari


# ============================================================
# len() — UZUNLIKNI ANIQLASH
# ============================================================

"""
len() — string ichidagi harflar (belgilar) sonini qaytaradi.
Bo'sh joy ham belgi hisoblanadi!
"""

print(len("Salom"))          # 5
print(len("Python 3.12"))    # 11  (bo'sh joy ham hisoblanadi)
print(len(""))               # 0   (bo'sh string)

ism = "Ali Karimov"
print(len(ism))              # 11

# Amaliy: oxirgi harf indeksi = len(matn) - 1
print(ism[len(ism) - 1])     # v  (oxirgi harf)
print(ism[-1])               # v  (xuddi shu natija, qisqaroq usul)


# ============================================================
# STRING + ARIFMETIKA
# ============================================================

"""
Stringlarda faqat + va * operatorlari ishlaydi.

  +   →  ikki stringni birlashtiradi (concatenation)
  *   →  stringni n marta takrorlaydi
"""

# ── + Birlashtirish ───────────────────────────────────────────
ism    = "Ali"
familya = "Karimov"
tolik  = ism + " " + familya
print(tolik)            # Ali Karimov

salom  = "Salom" + ", " + "Dunyo" + "!"
print(salom)            # Salom, Dunyo!

# ── * Takrorlash ─────────────────────────────────────────────
chiziq = "-" * 30
print(chiziq)           # ------------------------------

print("Ha! " * 3)       # Ha! Ha! Ha!
print("*" * 10)         # **********

# ── DIQQAT: str + int bo'lmaydi! ─────────────────────────────
"""
yosh = 15
print("Yosh: " + yosh)     →  XATO!  str + int bo'lmaydi

To'g'ri usullar:
  print("Yosh: " + str(yosh))   # str() bilan aylantirish
  print("Yosh:", yosh)           # vergul bilan
  print(f"Yosh: {yosh}")         # f-string
"""
yosh = 15
print("Yosh: " + str(yosh))   # Yosh: 15
print("Yosh:", yosh)           # Yosh: 15
print(f"Yosh: {yosh}")         # Yosh: 15


# ============================================================
# f-STRING — ZAMONAVIY MATN FORMATLASH
# ============================================================

"""
f-string — string ichiga o'zgaruvchi qiymatini joylashtirish.
f" ... {o'zgaruvchi} ... "  —  f harfi qo'shtirnoqdan OLDIN yoziladi.

Qachon ishlatiladi?
  - Matn va o'zgaruvchilarni aralashtirganда
  - format() dan qisqaroq va o'qishga qulay
"""

ism  = "Ali"
yosh = 15
ball = 87.5

# Oddiy usul (noqulay):
print("Ism: " + ism + ", Yosh: " + str(yosh))

# f-string (qulay):
print(f"Ism: {ism}, Yosh: {yosh}")        # Ism: Ali, Yosh: 15
print(f"Ball: {ball}")                     # Ball: 87.5

# ── f-string ichida hisob-kitob ───────────────────────────────
a = 10
b = 3
print(f"{a} + {b} = {a + b}")             # 10 + 3 = 13
print(f"{a} * {b} = {a * b}")             # 10 * 3 = 30
print(f"2 daraja 8 = {2 ** 8}")           # 2 daraja 8 = 256

# ── f-string bilan formatlash ─────────────────────────────────
narx = 29990.5
print(f"Narx: {narx:.2f} so'm")           # Narx: 29990.50 so'm
pi = 3.14159265
print(f"Pi ≈ {pi:.3f}")                   # Pi ≈ 3.142

# ── Katta amaliy misol ────────────────────────────────────────
ism        = "Jasur"
tugilgan   = 2010
boy        = 175.3
shahar     = "Samarqand"
yosh       = 2025 - tugilgan

print(f"""
╔══════════════════════════╗
║      SHAXSIY KARTA       ║
╠══════════════════════════╣
║  Ism    : {ism:<15}  ║
║  Yosh   : {yosh:<15}  ║
║  Bo'y   : {boy:<15}  ║
║  Shahar : {shahar:<15}  ║
╚══════════════════════════╝
""")


# ============================================================
# STRING METODLARI
# ============================================================

"""
Metod — bu string ustida amal bajaruvchi maxsus funksiya.
Qo'llanishi:
  matn.metod_nomi()

Metodlar stringning O'ZINI O'ZGARTIRMAYDI!
Yangi string qaytaradi, shuning uchun natijani saqlash kerak.
"""

matn = "python dasturlash tili"

# ============================================================
# REGISTR METODLARI (Katta/kichik harf)
# ============================================================

# ── upper() — Hammasini KATTA HARFGA ─────────────────────────
print(matn.upper())          # PYTHON DASTURLASH TILI
print("salom".upper())       # SALOM

# ── lower() — Hammasini kichik harfga ────────────────────────
print("SALOM DUNYO".lower()) # salom dunyo
print(matn.lower())          # python dasturlash tili (o'zgarmadi)

# ── capitalize() — FAQAT birinchi harf katta ─────────────────
print(matn.capitalize())     # Python dasturlash tili
print("ali karimov".capitalize())  # Ali karimov (qolganlar kichik!)

# ── title() — Har So'zning Birinchi Harfi Katta ───────────────
print(matn.title())          # Python Dasturlash Tili
print("ali karimov".title()) # Ali Karimov

# ── swapcase() — Katta ↔ kichik almashtiradi ─────────────────
print("PyThOn".swapcase())   # pYtHoN

# ── Amaliy: Foydalanuvchi ismini to'g'ri formatlash ──────────
ism = input("Ismingiz: ")
print(f"Salom, {ism.title()}!")   # Har harf qanday kiritilsa ham to'g'ri chiqadi


# ============================================================
# QIDIRISH VA TEKSHIRISH METODLARI
# ============================================================

matn = "Python dasturlash tili"

# ── find() — Topilgan joyning indeksini beradi ────────────────
"""
find(qidirilayotgan)  →  topilsa indeksini, topilmasa -1 qaytaradi
"""
print(matn.find("das"))      # 7   — "das" 7-indeksdan boshlanadi
print(matn.find("Java"))     # -1  — topilmadi
print(matn.find("i"))        # 16  — birinchi "i" ning indeksi

# ── index() — find() ga o'xshash, lekin topilmasa XATO beradi ─
print(matn.index("das"))     # 7
# print(matn.index("Java")) →  XATO! ValueError

# ── count() — Necha marta uchrashini sanaydi ──────────────────
print(matn.count("a"))       # 3   — "a" harfi 3 marta bor
print(matn.count("tili"))    # 1
print(matn.count("Java"))    # 0   — yo'q

# ── startswith() — Shu bilan boshlanadi? ─────────────────────
print(matn.startswith("Python"))    # True
print(matn.startswith("Java"))      # False
print(matn.startswith("das", 7))    # True  — 7-indeksdan tekshiradi

# ── endswith() — Shu bilan tugaydi? ──────────────────────────
print(matn.endswith("tili"))        # True
print(matn.endswith("Python"))      # False

# ── in operatori — mavjudligini tekshirish ────────────────────
"""
'qidirilayotgan' in matn  →  True yoki False
Bu metod emas, operator — lekin ko'p ishlatiladi
"""
print("Python" in matn)      # True
print("Java" in matn)        # False
print("java" in matn)        # False  (katta-kichik harf farq qiladi!)
print("python" in matn)      # False  (kichik harf!)

# if bilan birga:
if "Python" in matn:
    print("Python topildi!")


# ============================================================
# O'ZGARTIRISH METODLARI
# ============================================================

# ── replace() — Bir qismni boshqa narsa bilan almashtirish ────
"""
replace(eski, yangi)          — hammani almashtiradi
replace(eski, yangi, nechta)  — faqat 'nechta' marta
"""
gap = "Men Java o'rganaman. Java yaxshi!"
print(gap.replace("Java", "Python"))
# Men Python o'rganaman. Python yaxshi!

print(gap.replace("Java", "Python", 1))
# Men Python o'rganaman. Java yaxshi!  (faqat 1 ta)

# ── strip() — Bosh va oxirdagi bo'sh joy/belgilarni olib tashlash
"""
strip()        — ikki tarafdan
lstrip()       — faqat chapdan
rstrip()       — faqat o'ngdan
strip("belgi") — belgilangan belgilarni olib tashlaydi
"""
s = "   Salom Dunyo!   "
print(s.strip())             # "Salom Dunyo!"  — bo'sh joylar ketdi
print(s.lstrip())            # "Salom Dunyo!   "
print(s.rstrip())            # "   Salom Dunyo!"

s2 = "***Python***"
print(s2.strip("*"))         # Python

# ── Amaliy: foydalanuvchi kiritgan ma'lumotni tozalash ────────
parol = input("Parol: ")
parol = parol.strip()        # tasodifiy bo'sh joylarni olib tashlash
print(f"Parol: '{parol}'")


# ============================================================
# BO'LISH VA BIRLASHTIRISH METODLARI
# ============================================================

# ── split() — Stringni bo'laklarga ajratadi ───────────────────
"""
split()         — bo'sh joy bo'yicha ajratadi → list qaytaradi
split("belgi")  — belgilangan joy bo'yicha ajratadi
"""
gap = "Python Java C++ Kotlin"
print(gap.split())
# ['Python', 'Java', 'C++', 'Kotlin']

sana = "2025-06-15"
print(sana.split("-"))
# ['2025', '06', '15']

email = "ali.karimov@gmail.com"
print(email.split("@"))
# ['ali.karimov', 'gmail.com']
print(email.split("@")[0])   # ali.karimov  — foydalanuvchi nomi
print(email.split("@")[1])   # gmail.com    — domen

# ── join() — Listni stringga birlashtiradi ────────────────────
"""
"ajratgich".join(list)  →  listdagi elementlarni birlashtiradi
"""
sozlar = ["Python", "Java", "C++"]
print(", ".join(sozlar))     # Python, Java, C++
print(" | ".join(sozlar))    # Python | Java | C++
print("".join(sozlar))       # PythonJavaC++  (bo'sh)

harflar = ["P", "y", "t", "h", "o", "n"]
print("".join(harflar))       # Python


# ============================================================
# format() METODI
# ============================================================

"""
format() — string ichiga qiymat joylashtirish.
f-stringdan oldin ishlatilgan usul.
Hozir ham keng qo'llaniladi.

Sintaksis:
  "... {} ...".format(qiymat)
  "... {0} ... {1} ...".format(qiymat1, qiymat2)
  "... {nom} ...".format(nom=qiymat)
"""

# ── Asosiy ishlatish ─────────────────────────────────────────
ism = "Ali"
yosh = 15
print("Mening ismim {}, yoshim {}".format(ism, yosh))
# Mening ismim Ali, yoshim 15

# ── Indeks bilan ─────────────────────────────────────────────
print("{0} va {1} do'st".format("Ali", "Vali"))   # Ali va Vali do'st
print("{1} va {0} do'st".format("Ali", "Vali"))   # Vali va Ali do'st

# ── Nom bilan ────────────────────────────────────────────────
print("Ism: {ism}, Ball: {ball}".format(ism="Jasur", ball=95))
# Ism: Jasur, Ball: 95

# ── Raqam formatlash ─────────────────────────────────────────
narx = 15990.756
print("Narx: {:.2f} so'm".format(narx))    # Narx: 15990.76 so'm

# ── f-string vs format() ─────────────────────────────────────
"""
  f-string (yangi, tavsiya etiladi):
    f"Salom, {ism}!"

  format() (eski, hali ham ishlaydi):
    "Salom, {}!".format(ism)

  Ikkalasi ham bir xil natija beradi.
  f-string o'qishga qulayroq.
"""


# ============================================================
# TEKSHIRISH METODLARI (isdigit, isalpha va boshqalar)
# ============================================================

"""
Bu metodlar string haqida True/False qaytaradi.
"""

# ── isdigit() — Faqat raqamlardan iboratmi? ──────────────────
print("12345".isdigit())     # True
print("12.34".isdigit())     # False  (nuqta bor)
print("123ab".isdigit())     # False  (harf bor)
print("".isdigit())          # False  (bo'sh)

# ── isalpha() — Faqat harflardan iboratmi? ───────────────────
print("Python".isalpha())    # True
print("Python3".isalpha())   # False  (raqam bor)
print("Ali Vali".isalpha())  # False  (bo'sh joy bor)

# ── isalnum() — Harf yoki raqamlardan iboratmi? ──────────────
print("Python3".isalnum())   # True   (harf + raqam)
print("abc123".isalnum())    # True
print("abc 123".isalnum())   # False  (bo'sh joy bor)

# ── isspace() — Faqat bo'sh joylardan iboratmi? ──────────────
print("   ".isspace())       # True
print("  a  ".isspace())     # False

# ── isupper() / islower() ────────────────────────────────────
print("PYTHON".isupper())    # True
print("python".islower())    # True
print("Python".isupper())    # False
print("Python".islower())    # False

# ── Amaliy: Foydalanuvchi kiritgan sonni tekshirish ───────────
kiritilgan = input("Son kiriting: ")
if kiritilgan.isdigit():
    son = int(kiritilgan)
    print(f"Siz {son} kiritdingiz")
else:
    print("Xato! Bu son emas!")


# ============================================================
# AMALIY DASTURLAR — HAMMASI BIRGALIKDA
# ============================================================

# ── DASTUR 1: Matn tahlilchisi ───────────────────────────────
print("\n=== DASTUR 1: Matn tahlilchisi ===")
matn = input("Matn kiriting: ")

print(f"Uzunligi      : {len(matn)}")
print(f"Katta harfda  : {matn.upper()}")
print(f"Kichik harfda : {matn.lower()}")
print(f"So'zlar soni  : {len(matn.split())}")
print(f"Teskari       : {matn[::-1]}")

# ── DASTUR 2: Ism formatlash ─────────────────────────────────
print("\n=== DASTUR 2: Ism formatlash ===")
tolik_ism = input("To'liq ismingizni kiriting: ")
qismlar   = tolik_ism.split()

if len(qismlar) >= 2:
    ism     = qismlar[0].capitalize()
    familya = qismlar[1].capitalize()
    print(f"Ism     : {ism}")
    print(f"Familya : {familya}")
    print(f"Boshlari: {ism[0]}.{familya[0]}.")
else:
    print("Iltimos, ism va familyangizni kiriting")

# ── DASTUR 3: Parol tekshirgich ───────────────────────────────
print("\n=== DASTUR 3: Parol tekshirgich ===")
parol = input("Parol yarating: ")
parol = parol.strip()

xatolar = []
if len(parol) < 8:
    xatolar.append("Kamida 8 ta belgi bo'lishi kerak")
if not any(c.isdigit() for c in parol):
    xatolar.append("Kamida bitta raqam bo'lishi kerak")
if not any(c.isalpha() for c in parol):
    xatolar.append("Kamida bitta harf bo'lishi kerak")
if parol.lower() in ["password", "12345678", "qwerty123"]:
    xatolar.append("Juda oddiy parol, o'zgartiring")

if xatolar:
    print("Parol zaif:")
    for x in xatolar:
        print(f"  ✗ {x}")
else:
    print("✓ Parol kuchli!")


# ============================================================
# STRING METODLARI — TO'LIQ JADVAL
# ============================================================

"""
┌─────────────────────┬──────────────────────────────────────────────┐
│ METOD               │ NIMA QILADI                                  │
├─────────────────────┼──────────────────────────────────────────────┤
│ REGISTR             │                                              │
│  upper()            │  Hammasini KATTA HARFGA                      │
│  lower()            │  Hammasini kichik harfga                     │
│  capitalize()       │  Faqat birinchi harf katta                   │
│  title()            │  Har So'zning Birinchi Harfi Katta           │
│  swapcase()         │  Katta ↔ kichik almashtiradi                 │
├─────────────────────┼──────────────────────────────────────────────┤
│ QIDIRISH            │                                              │
│  find(s)            │  Topilsa indeksi, topilmasa -1               │
│  index(s)           │  Topilsa indeksi, topilmasa XATO             │
│  count(s)           │  Necha marta uchraydi                        │
│  startswith(s)      │  Shu bilan boshlanadi? (True/False)          │
│  endswith(s)        │  Shu bilan tugaydi? (True/False)             │
│  "s" in matn        │  Mavjudligini tekshirish (True/False)        │
├─────────────────────┼──────────────────────────────────────────────┤
│ O'ZGARTIRISH        │                                              │
│  replace(e, y)      │  Eski → yangi bilan almashtiradi             │
│  strip()            │  Ikki tarafdan bo'sh joy/belgi olib tashlash │
│  lstrip()           │  Chapdan                                     │
│  rstrip()           │  O'ngdan                                     │
├─────────────────────┼──────────────────────────────────────────────┤
│ BO'LISH/BIRLASHTIR  │                                              │
│  split(s)           │  Stringni listga ajratadi                    │
│  join(list)         │  Listni stringga birlashtiradi               │
├─────────────────────┼──────────────────────────────────────────────┤
│ FORMATLASH          │                                              │
│  format(...)        │  {} o'rnilariga qiymat joylashtiradi         │
│  f"...{var}..."     │  f-string (zamonaviy usul)                   │
├─────────────────────┼──────────────────────────────────────────────┤
│ TEKSHIRISH          │                                              │
│  isdigit()          │  Faqat raqamlardan iboratmi?                 │
│  isalpha()          │  Faqat harflardan iboratmi?                  │
│  isalnum()          │  Harf yoki raqamlardan iboratmi?             │
│  isspace()          │  Faqat bo'sh joylardan iboratmi?             │
│  isupper()          │  Hammasi katta harfmi?                       │
│  islower()          │  Hammasi kichik harfmi?                      │
└─────────────────────┴──────────────────────────────────────────────┘
"""


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Indekslash va qirqish (Oson):
  s = "Assalomu alaykum, Python!"
  Quyidagilarni chiqaring:
    a) Birinchi harf
    b) Oxirgi harf
    c) "Python" qismi (slicing bilan)
    d) Teskari string
    e) Har ikkinchi harf (::2)

TOPSHIRIQ 2 — Metodlar (O'rta):
  Foydalanuvchidan bir jumla oling.
  Quyidagilarni chiqaring:
    a) Katta harfda
    b) So'zlar soni (split bilan)
    c) "a" harfi necha marta uchraydi (count bilan)
    d) Birinchi so'z (split()[0] bilan)
    e) Teskari yozilgan jumla

TOPSHIRIQ 3 — replace va strip (O'rta):
  Quyidagi matndagi barcha "narx" so'zini "price" bilan almashtiring:
    "Mahsulot narxi: 15000. Eski narx: 20000."
  Natija: "Mahsulot pricesi: 15000. Eski price: 20000."

TOPSHIRIQ 4 — format() va f-string (O'rta):
  Foydalanuvchidan: ism, yosh, shahar, kasb oling.
  f-string bilan quyidagi formatda chiqaring:
    ╔═══════════════════════╗
    ║  Ism    : Ali         ║
    ║  Yosh   : 22          ║
    ║  Shahar : Toshkent    ║
    ║  Kasb   : Dasturchi   ║
    ╚═══════════════════════╝

TOPSHIRIQ 5 — Email tekshirgich (Qiyin):
  Foydalanuvchidan email manzil oling.
  Tekshiring:
    - "@" belgisi bormi?
    - "." belgisi bormi?
    - Uzunligi 5 dan ko'pmi?
  Agar hammasi to'g'ri → "Email to'g'ri!"
  Aks holda → qaysi xato ekanligini chiqaring.

TOPSHIRIQ 6 — So'z sanagich (Ijodiy):
  Foydalanuvchidan matn oling.
  Har bir so'z va u necha marta uchrashini chiqaring.
  Masalan: "men sen men u sen"
  →
    men  : 2
    sen  : 2
    u    : 1
"""


# ------------------------------------------------------------
# QUSHIMCHA RESURSLAR
# ------------------------------------------------------------

"""
📚 RASMIY HUJJATLAR:
   https://docs.python.org/3/library/stdtypes.html#string-methods
   — Barcha string metodlari ro'yxati

🌐 W3SCHOOLS:
   https://www.w3schools.com/python/python_strings.asp
   — String asoslari

   https://www.w3schools.com/python/python_strings_slicing.asp
   — Slicing (qirqish)

   https://www.w3schools.com/python/python_string_formatting.asp
   — format() va f-string

   https://www.w3schools.com/python/python_ref_string.asp
   — Barcha string metodlari (jadval ko'rinishida)
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ String nima va yaratish usullari
✔️ Indekslash — matn[0], matn[-1]
✔️ Qirqish (Slicing) — matn[2:8], matn[::-1]
✔️ len() — uzunlikni aniqlash
✔️ + (birlashtirish) va * (takrorlash)
✔️ f-string — f"Salom, {ism}!"
✔️ Registr metodlari:
    upper()      — KATTA HARF
    lower()      — kichik harf
    capitalize() — Birinchi katta
    title()      — Har So'z Katta
    swapcase()   — Almashtirish
✔️ Qidirish metodlari:
    find()       — indeks yoki -1
    index()      — indeks yoki XATO
    count()      — necha marta
    startswith() — shu bilan boshlanadi?
    endswith()   — shu bilan tugaydi?
    "x" in matn — mavjudmi?
✔️ O'zgartirish metodlari:
    replace()    — almashtirish
    strip()      — bo'sh joy/belgi olib tashlash
✔️ Bo'lish/Birlashtirish:
    split()      — listga ajratish
    join()       — listdan string
✔️ format()      — {} bilan formatlash
✔️ Tekshirish metodlari:
    isdigit()    — faqat raqammi?
    isalpha()    — faqat harfmi?
    isalnum()    — harf yoki raqammi?
    isupper()    — hammasi katta harfmi?
    islower()    — hammasi kichik harfmi?
"""