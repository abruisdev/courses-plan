# ============================================================
#   DARS 12: Pythonda Funksiya va Lambda
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# FUNKSIYA NIMA?
# ------------------------------------------------------------

"""
Funksiya — bu bir marta yozib, ko'p marta chaqirish mumkin bo'lgan
kod bloki.

Nima uchun kerak?
  ✔️ Kodni takrorlamaslik (DRY — Don't Repeat Yourself)
  ✔️ Kodni bo'laklarga bo'lish (tartibli kod)
  ✔️ Xatoliklarni topish osonlashadi
  ✔️ Jamoa ishida kodni ulashish mumkin

Python'da funksiya turlari:
  1. Parametrsiz funksiya
  2. Parametrli funksiya
  3. Return qiymat qaytaruvchi funksiya
  4. Default parametrli funksiya
  5. Lambda funksiya
"""

# ── Funksiya yaratish sintaksisi ──────────────────────────────
"""
def funksiya_nomi(parametrlar):
    # funksiya tanasi
    bajariladigan_kod
    return qiymat   # ixtiyoriy
"""


# ============================================================
# 1. PARAMETRSIZ FUNKSIYA
# ============================================================

# Funksiya YARATISH (define):
def salom():
    print("Assalomu alaykum!")
    print("Xush kelibsiz Python kursiga!")

# Funksiya CHAQIRISH (call):
salom()    # Assalomu alaykum!
salom()    # Xush kelibsiz Python kursiga!
salom()    # Har safar chaqirish mumkin

# Chiziq chiqaruvchi funksiya:
def chiziq():
    print("=" * 40)

chiziq()
print("Dastur boshlanmoqda")
chiziq()


# ============================================================
# 2. PARAMETRLI FUNKSIYA
# ============================================================

"""
Parametr — funksiyaga beriladigan "kirish" ma'lumoti.
Argument — funksiyani chaqirganda beriladigan haqiqiy qiymat.

  def f(parametr):   ← parametr
      ...
  f(argument)        ← argument
"""

# ── Bitta parametr ────────────────────────────────────────────
def salom_ayt(ism):
    print(f"Salom, {ism}!")

salom_ayt("Ali")      # Salom, Ali!
salom_ayt("Vali")     # Salom, Vali!
salom_ayt("Jasur")    # Salom, Jasur!

# ── Bir nechta parametr ───────────────────────────────────────
def tanishtir(ism, yosh, shahar):
    print(f"Ism: {ism}, Yosh: {yosh}, Shahar: {shahar}")

tanishtir("Ali", 15, "Toshkent")
tanishtir("Vali", 22, "Samarqand")

# ── Kalit so'z argumentlar (keyword arguments) ───────────────
"""
Funksiyani chaqirganda parametr nomini yozish mumkin.
Tartib muhim bo'lmaydi.
"""
tanishtir(yosh=20, shahar="Buxoro", ism="Bobur")


# ============================================================
# 3. RETURN — QIYMAT QAYTARISH
# ============================================================

"""
return — funksiyadan natijani qaytaradi.
return dan keyin funksiya TUGAYDI.

Returnsiz funksiya None qaytaradi.
"""

# ── Oddiy return ──────────────────────────────────────────────
def qo_sh(a, b):
    natija = a + b
    return natija

yig_indi = qo_sh(10, 20)
print(yig_indi)          # 30
print(qo_sh(5, 7))       # 12
print(qo_sh(100, 200))   # 300

# ── Bir nechta return ─────────────────────────────────────────
def abs_qiymat(son):
    if son >= 0:
        return son
    else:
        return -son

print(abs_qiymat(5))    # 5
print(abs_qiymat(-8))   # 8

# ── Bir nechta qiymat return ──────────────────────────────────
def min_max(ro_yxat):
    return min(ro_yxat), max(ro_yxat)

kichik, katta = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {kichik}, Max: {katta}")   # Min: 1, Max: 9

# ── Return yo'q → None ────────────────────────────────────────
def hech_narsa():
    print("Men hech narsa qaytarmayman")

natija = hech_narsa()
print(natija)    # None


# ============================================================
# 4. DEFAULT PARAMETR QIYMATLARI
# ============================================================

"""
Funksiya chaqirilganda argument berilmasa,
default qiymat ishlatiladi.
"""

def salom_til(ism, til="uz"):
    if til == "uz":
        print(f"Salom, {ism}!")
    elif til == "en":
        print(f"Hello, {ism}!")
    elif til == "ru":
        print(f"Привет, {ism}!")

salom_til("Ali")           # Salom, Ali!  (default: "uz")
salom_til("John", "en")    # Hello, John!
salom_til("Ivan", "ru")    # Привет, Ivan!

# ── Bir nechta default ────────────────────────────────────────
def to_lov(narx, soni=1, chegirma=0):
    jami = narx * soni
    jami -= jami * chegirma / 100
    return round(jami, 2)

print(to_lov(10000))               # 10000    (1 ta, 0% chegirma)
print(to_lov(10000, 3))            # 30000    (3 ta, 0% chegirma)
print(to_lov(10000, 3, 10))        # 27000.0  (3 ta, 10% chegirma)


# ============================================================
# 5. *args — NOMA'LUM MIQDORDAGI ARGUMENTLAR
# ============================================================

"""
*args — funksiyaga istalgancha argument berish imkonini beradi.
Ichida ular tuple sifatida keladi.
"""

def yig_indi(*sonlar):
    print(f"Berilgan sonlar: {sonlar}")
    return sum(sonlar)

print(yig_indi(1, 2))              # 3
print(yig_indi(1, 2, 3, 4, 5))    # 15
print(yig_indi(10, 20, 30))        # 60

# ── Amaliy misol ─────────────────────────────────────────────
def eng_katta(*sonlar):
    return max(sonlar)

print(eng_katta(3, 1, 7, 2, 9, 4))    # 9

def barchani_chiqar(*narsalar):
    for narsa in narsalar:
        print(f"  → {narsa}")

barchani_chiqar("Ali", 15, "Python", True)


# ============================================================
# 6. **kwargs — NOMA'LUM MIQDORDAGI KALIT-QIYMAT ARGUMENTLAR
# ============================================================

"""
**kwargs — funksiyaga istalgancha kalit=qiymat berish imkonini beradi.
Ichida ular dictionary sifatida keladi.
"""

def ma_lumot_chiqar(**kwargs):
    for kalit, qiymat in kwargs.items():
        print(f"  {kalit:12} : {qiymat}")

ma_lumot_chiqar(ism="Ali", yosh=15, shahar="Toshkent")
# ism          : Ali
# yosh         : 15
# shahar       : Toshkent

ma_lumot_chiqar(mahsulot="Non", narx=3000, soni=5)

# ── *args va **kwargs birga ───────────────────────────────────
def universal(*args, **kwargs):
    print(f"args   : {args}")
    print(f"kwargs : {kwargs}")

universal(1, 2, 3, ism="Ali", yosh=15)
# args   : (1, 2, 3)
# kwargs : {'ism': 'Ali', 'yosh': 15}


# ============================================================
# 7. SCOPE — O'ZGARUVCHILAR DOIRASI
# ============================================================

"""
Local   — funksiya ICHIDA yaratilgan o'zgaruvchi
Global  — funksiya TASHQARISIDA yaratilgan o'zgaruvchi

Local o'zgaruvchi tashqarida ko'rinmaydi!
"""

x = 10   # global

def sinov():
    y = 20          # local
    print(f"Ichida: x={x}, y={y}")

sinov()             # Ichida: x=10, y=20
print(f"Tashqarida: x={x}")
# print(y)          → XATO! y faqat funksiya ichida mavjud

# ── global kalit so'zi ────────────────────────────────────────
hisoblagich = 0

def oshir():
    global hisoblagich    # global o'zgaruvchini o'zgartirish uchun
    hisoblagich += 1

oshir()
oshir()
oshir()
print(hisoblagich)   # 3


# ============================================================
# 8. LAMBDA FUNKSIYA
# ============================================================

"""
Lambda — bu bir qatorli anonim (nomsiz) funksiya.
Kichik, oddiy funksiyalar uchun ishlatiladi.

Sintaksis:
  lambda parametrlar: ifoda

Odatiy funksiya vs Lambda:
  def ikki_baravar(x): return x * 2
  ikki_baravar = lambda x: x * 2
"""

# ── Oddiy lambda ──────────────────────────────────────────────
ikki_baravar = lambda x: x * 2
print(ikki_baravar(5))    # 10
print(ikki_baravar(15))   # 30

kvadrat = lambda x: x ** 2
print(kvadrat(4))    # 16
print(kvadrat(7))    # 49

# ── Bir nechta parametrli lambda ──────────────────────────────
qo_sh   = lambda a, b: a + b
ko_payt = lambda a, b: a * b
katta   = lambda a, b: a if a > b else b

print(qo_sh(3, 4))     # 7
print(ko_payt(3, 4))   # 12
print(katta(10, 7))    # 10

# ── Lambda bilan shart ────────────────────────────────────────
toifa   = lambda yosh: "katta" if yosh >= 18 else "yosh"
juft_mi = lambda x: "Juft" if x % 2 == 0 else "Toq"

print(toifa(20))     # katta
print(toifa(15))     # yosh
print(juft_mi(4))    # Juft
print(juft_mi(7))    # Toq


# ============================================================
# 9. LAMBDA + sorted(), max(), min(), filter(), map()
# ============================================================

# ── sorted() bilan saralash ───────────────────────────────────
talabalar = [
    {"ism": "Vali",  "ball": 87},
    {"ism": "Ali",   "ball": 95},
    {"ism": "Jasur", "ball": 78},
    {"ism": "Bobur", "ball": 91},
]

# Ball bo'yicha saralash:
saralangan = sorted(talabalar, key=lambda x: x["ball"])
for t in saralangan:
    print(f"{t['ism']:10} : {t['ball']}")

# Kamayish tartibida:
saralangan = sorted(talabalar, key=lambda x: x["ball"], reverse=True)
print("\nTop ro'yxat:")
for i, t in enumerate(saralangan, 1):
    print(f"  {i}. {t['ism']:10} — {t['ball']}")

# ── max() va min() bilan ──────────────────────────────────────
eng_yaxshi = max(talabalar, key=lambda x: x["ball"])
eng_yomon  = min(talabalar, key=lambda x: x["ball"])
print(f"\nEng yuqori: {eng_yaxshi['ism']} ({eng_yaxshi['ball']})")
print(f"Eng past  : {eng_yomon['ism']}  ({eng_yomon['ball']})")

# ── filter() — Filtrlash ──────────────────────────────────────
"""
filter(funksiya, ketma_ketlik)
  — True qaytargan elementlarni oladi
"""
sonlar   = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
juftlar  = list(filter(lambda x: x % 2 == 0, sonlar))
print(juftlar)   # [2, 4, 6, 8, 10]

kattalar = list(filter(lambda x: x > 5, sonlar))
print(kattalar)  # [6, 7, 8, 9, 10]

# ── map() — O'zgartirish ──────────────────────────────────────
"""
map(funksiya, ketma_ketlik)
  — har bir elementga funksiya qo'llaydi
"""
sonlar     = [1, 2, 3, 4, 5]
kvadratlar = list(map(lambda x: x ** 2, sonlar))
print(kvadratlar)   # [1, 4, 9, 16, 25]

ismlar  = ["ali", "vali", "jasur"]
katta_h = list(map(lambda x: x.title(), ismlar))
print(katta_h)      # ['Ali', 'Vali', 'Jasur']


# ============================================================
# AMALIY DASTUR — Kalkulyator
# ============================================================

def qo_sh(a, b):    return a + b
def ayir(a, b):     return a - b
def ko_payt(a, b):  return a * b
def bo_l(a, b):
    if b == 0:
        return "Xato: nolga bo'lish mumkin emas!"
    return round(a / b, 4)

amallar = {
    "+": qo_sh,
    "-": ayir,
    "*": ko_payt,
    "/": bo_l,
}

print("\n=== KALKULYATOR ===")
while True:
    kiritish = input("\nHisob (masalan: 10 + 5) yoki 'chiq': ").strip()
    if kiritish == "chiq":
        break
    try:
        qismlar = kiritish.split()
        a, amal, b = float(qismlar[0]), qismlar[1], float(qismlar[2])
        if amal in amallar:
            natija = amallar[amal](a, b)
            print(f"Natija: {a} {amal} {b} = {natija}")
        else:
            print("Noma'lum amal! Faqat + - * / ishlating.")
    except:
        print("Noto'g'ri format! Masalan: 10 + 5")


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Oddiy funksiyalar (Oson):
  Quyidagi funksiyalarni yozing:
    a) murabba(son)    — sonning kvadratini qaytaradi
    b) kub(son)        — sonning kubini qaytaradi
    c) doira_yuzi(r)   — doira yuzini qaytaradi (π*r²)
    d) salom(ism, til) — "uz"/"en"/"ru" tilida salomlashadi

TOPSHIRIQ 2 — Return bilan (O'rta):
  Quyidagi funksiyalarni yozing:
    a) o'rtacha(*sonlar)   — istalgancha sonning o'rtachasini qaytaradi
    b) palindrom(so'z)     — so'z teskari ham xuddi shunday bo'lsa True
    c) faktoriyel(n)       — n! ni hisoblaydi (1*2*3*...*n)

TOPSHIRIQ 3 — Lambda (O'rta):
  Quyidagilarni lambda bilan yozing:
    a) uch baravar ko'paytiruvchi lambda
    b) sonning mutlaq qiymatini qaytaruvchi lambda
    c) Celsius → Fahrenheit aylantiruvchi lambda: F = C*9/5 + 32

TOPSHIRIQ 4 — filter va map (Qiyin):
  sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
  a) filter bilan 3 ga bo'linadigan sonlarni oling
  b) map bilan har bir sonni 2 ga bo'ling
  c) filter + map birga: juft sonlarni 3 ga ko'paytiring

TOPSHIRIQ 5 — Murakkab (Ijodiy):
  Talabalar ro'yxati (dictionary list):
    [{"ism": "Ali", "matematika": 90, "fizika": 80},
     {"ism": "Vali", "matematika": 75, "fizika": 88}, ...]
  Funksiya yozing:
    a) o'rtacha_ball(talaba) — talabaning o'rtacha bahosini qaytaradi
    b) reytng(talabalar) — o'rtacha ball bo'yicha tartiblangan list
    c) A_talabalar(talabalar) — o'rtacha bali 85+ bo'lgan talabalar
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ Funksiya nima va nima uchun kerak
✔️ def bilan funksiya yaratish
✔️ Parametr va argument farqi
✔️ Kalit so'z argumentlar (keyword args)
✔️ return — qiymat qaytarish
✔️ Bir nechta qiymat return (tuple)
✔️ Default parametr qiymatlari
✔️ *args  — noma'lum miqdor argumentlar (tuple)
✔️ **kwargs — noma'lum miqdor kalit-qiymat (dict)
✔️ Scope — local va global o'zgaruvchilar
✔️ global kalit so'zi
✔️ Lambda funksiya — lambda x: x*2
✔️ Lambda + sorted(), max(), min()
✔️ filter() — filtrlash
✔️ map()    — o'zgartirish
"""