# ============================================================
#   DARS 10: Pythonda Tuple va Set
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================


# ============================================================
# TUPLE NIMA?
# ============================================================

"""
Tuple — bu listga o'xshash, lekin O'ZGARMAS (immutable) to'plam.
Oddiy qavs () ichida yoziladi.

List vs Tuple:
  List  []  →  o'zgaruvchan  (element qo'shish, o'chirish mumkin)
  Tuple ()  →  o'zgarmas     (yaratilgandan keyin o'zgartirib bo'lmaydi)

Qachon Tuple ishlatiladi?
  - O'zgarmasligi kerak bo'lgan ma'lumotlar uchun
    (masalan: koordinatalar, hafta kunlari, oylar)
  - Listdan tezroq ishlaydi
  - Dictionary kalit (key) sifatida ishlatish mumkin
"""

# ── Tuple yaratish ────────────────────────────────────────────
bo_sh      = ()
sonlar     = (1, 2, 3, 4, 5)
ismlar     = ("Ali", "Vali", "Jasur")
aralash    = (1, "Python", 3.14, True)
koordinata = (41.2995, 69.2401)          # Toshkent koordinatalari

print(sonlar)       # (1, 2, 3, 4, 5)
print(type(sonlar)) # <class 'tuple'>

# ── Bitta elementli tuple ─────────────────────────────────────
"""
DIQQAT: Bitta elementli tuple yaratishda vergul SHART!
  (5)   →  bu int!  (5)  ==  5
  (5,)  →  bu tuple!
"""
bitta     = (5,)         # to'g'ri — tuple
xato      = (5)          # noto'g'ri — bu int!
print(type(bitta))   # <class 'tuple'>
print(type(xato))    # <class 'int'>

# ── Qavsiz ham tuple yozish mumkin ────────────────────────────
koordinata2 = 41.2995, 69.2401
print(type(koordinata2))   # <class 'tuple'>


# ============================================================
# TUPLE ELEMENTLARIGA KIRISH
# ============================================================

"""
Xuddi list kabi — indeks va slicing ishlaydi.
Lekin O'ZGARTIRISH mumkin emas!
"""

mevalar = ("olma", "banan", "uzum", "shaftoli")

print(mevalar[0])     # olma
print(mevalar[-1])    # shaftoli
print(mevalar[1:3])   # ('banan', 'uzum')
print(mevalar[::-1])  # ('shaftoli', 'uzum', 'banan', 'olma')

# O'zgartirishga urinish — XATO!
# mevalar[0] = "anor"   →  TypeError: 'tuple' object does not support item assignment


# ============================================================
# TUPLE METODLARI
# ============================================================

"""
Tuple o'zgarmas bo'lgani uchun juda kam metodga ega:
  count()  — element necha marta uchraydi
  index()  — elementning birinchi indeksini topadi
"""

sonlar = (1, 2, 2, 3, 2, 4, 5)

# ── count() ───────────────────────────────────────────────────
print(sonlar.count(2))    # 3  — 2 uchta bor
print(sonlar.count(9))    # 0  — 9 yo'q

# ── index() ───────────────────────────────────────────────────
print(sonlar.index(3))    # 3  — 3 ning indeksi
# print(sonlar.index(9)) → XATO! ValueError

# ── len(), type(), in ─────────────────────────────────────────
print(len(sonlar))        # 7
print(type(sonlar))       # <class 'tuple'>
print(2 in sonlar)        # True
print(9 in sonlar)        # False


# ============================================================
# TUPLE — QO'SHISH VA KO'PAYTIRISH
# ============================================================

"""
Tuple o'zgarmas, lekin + va * ishlaydi (yangi tuple hosil qiladi).
"""

a = (1, 2, 3)
b = (4, 5, 6)

print(a + b)      # (1, 2, 3, 4, 5, 6)
print(a * 3)      # (1, 2, 3, 1, 2, 3, 1, 2, 3)


# ============================================================
# TUPLE — PACKING VA UNPACKING
# ============================================================

"""
Packing   — bir nechta qiymatni tuplega yig'ish
Unpacking — tuple elementlarini alohida o'zgaruvchilarga ajratish
"""

# Packing:
ma_lumot = ("Ali", 15, "Toshkent")
print(ma_lumot)     # ('Ali', 15, 'Toshkent')

# Unpacking:
ism, yosh, shahar = ma_lumot
print(ism)     # Ali
print(yosh)    # 15
print(shahar)  # Toshkent

# Swap (almashtirish) — tuple unpacking bilan:
x, y = 10, 20
print(f"Oldin: x={x}, y={y}")
x, y = y, x
print(f"Keyin: x={x}, y={y}")   # x=20, y=10


# ============================================================
# TUPLE — AFZALLIK VA KAMCHILIKLAR
# ============================================================

"""
  AFZALLIKLAR:
    ✔️ Listdan TEZROQ ishlaydi
    ✔️ Ma'lumot o'zgarmasligini KAFOLATLAYDI
    ✔️ Dictionary kalit sifatida ishlatish mumkin
    ✔️ Kam xotira (memory) egallaydi

  KAMCHILIKLAR:
    ✗ Elementlarni qo'shish/o'chirish/o'zgartirish MUMKIN EMAS
    ✗ Metodlari kamligi
"""

# copy() o'rniga to'g'ridan-to'g'ri tayinlash ishlatiladi:
asl   = (1, 2, 3)
nusxa = asl          # tuple o'zgarmas, shuning uchun xavfsiz


# ============================================================
#   SET NIMA?
# ============================================================

"""
Set — bu TAKRORLASHSIZ va TARTIBSIZ elementlar to'plami.
Jingalak qavs {} ichida yoziladi.

Xususiyatlari:
  ✔️ Har bir element YAGONA (takrorlanmaydi)
  ✔️ TARTIBSIZ — elementlar tartibini kafolatlamaydi
  ✔️ O'zgaruvchan — element qo'shish/o'chirish mumkin
  ✗  Indeks ishlamaydi — set[0] → XATO!

Qachon Set ishlatiladi?
  - Takroriy elementlarni olib tashlash uchun
  - Ikki ro'yxatning umumiy/farqli elementlarini topish uchun
  - Tez qidirish kerak bo'lganda (listdan tezroq)
"""

# ── Set yaratish ──────────────────────────────────────────────
bo_sh   = set()            # bo'sh set — set() ishlatiladi ({} emas!)
sonlar  = {1, 2, 3, 4, 5}
mevalar = {"olma", "banan", "uzum"}
aralash = {1, "Python", 3.14}

print(sonlar)       # {1, 2, 3, 4, 5}  (tartib o'zgarishi mumkin)
print(type(sonlar)) # <class 'set'>

# ── Takrorlar avtomatik olib tashlanadi ───────────────────────
takrorli = {1, 2, 2, 3, 3, 3, 4}
print(takrorli)    # {1, 2, 3, 4}  — faqat unikal elementlar

# ── Listdan set yaratish (takrorlarni olib tashlash) ──────────
ro_yxat = [1, 2, 2, 3, 3, 4, 5, 5]
unikal  = set(ro_yxat)
print(unikal)    # {1, 2, 3, 4, 5}

# Qayta listga aylantirish:
tozalangan = list(set(ro_yxat))
print(tozalangan)    # [1, 2, 3, 4, 5]  (tartib farq qilishi mumkin)


# ============================================================
# SET — ELEMENTLARGA KIRISH
# ============================================================

"""
Set tartibsiz, shuning uchun:
  set[0]  →  XATO! (indeks ishlamaydi)

Elementlarni ko'rish uchun for sikli ishlatiladi.
"""

mevalar = {"olma", "banan", "uzum"}

for meva in mevalar:
    print(meva)    # tartib har safar boshqacha bo'lishi mumkin

# Mavjudligini tekshirish — in (juda tez ishlaydi):
print("banan" in mevalar)     # True
print("anor" in mevalar)      # False


# ============================================================
# SET METODLARI
# ============================================================

s = {1, 2, 3}

# ── add() — Bitta element qo'shish ───────────────────────────
s.add(4)
print(s)    # {1, 2, 3, 4}

s.add(2)    # takror qo'shilmaydi
print(s)    # {1, 2, 3, 4}

# ── update() — Bir nechta element qo'shish ───────────────────
s.update([5, 6, 7])
print(s)    # {1, 2, 3, 4, 5, 6, 7}

s.update({8, 9})
print(s)    # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# ── remove() — Element o'chirish (topilmasa XATO) ────────────
s = {1, 2, 3, 4, 5}
s.remove(3)
print(s)    # {1, 2, 4, 5}
# s.remove(9)  →  XATO! KeyError

# ── discard() — Element o'chirish (topilmasa XATO YO'Q) ──────
s.discard(4)
print(s)    # {1, 2, 5}
s.discard(9)   # xato bermaydi
print(s)    # {1, 2, 5}

# ── pop() — Tasodifiy elementni o'chirib qaytaradi ───────────
s = {10, 20, 30, 40}
chiqarilgan = s.pop()
print(chiqarilgan)   # (qaysi biri chiqishini bilmayiz)
print(s)

# ── clear() — Tozalash ───────────────────────────────────────
s = {1, 2, 3}
s.clear()
print(s)    # set()

# ── copy() — Nusxa ───────────────────────────────────────────
asl   = {1, 2, 3}
nusxa = asl.copy()
nusxa.add(4)
print(asl)    # {1, 2, 3}   — o'zgarmadi
print(nusxa)  # {1, 2, 3, 4}

# ── len() va del ─────────────────────────────────────────────
s = {1, 2, 3}
print(len(s))   # 3
del s           # butun setni o'chiradi


# ============================================================
# SET AMALIYOTLARI (Matematikadagi to'plamlar)
# ============================================================

"""
Set matematikadagi to'plam nazariyasidan kelib chiqadi.
Juda foydali amaliyotlar:

  union()        — birlashtirish  ( A ∪ B )
  intersection() — kesishma       ( A ∩ B )
  difference()   — farq           ( A - B )
  symmetric_difference() — simmetrik farq ( A △ B )
"""

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# ── union() — Ikkalasini birlashtirish (takrorsiz) ────────────
print(A | B)              # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))         # {1, 2, 3, 4, 5, 6, 7, 8}

# ── intersection() — Umumiy elementlar ───────────────────────
print(A & B)              # {4, 5}
print(A.intersection(B))  # {4, 5}

# ── difference() — A da bor, B da yo'q ───────────────────────
print(A - B)              # {1, 2, 3}
print(A.difference(B))    # {1, 2, 3}
print(B - A)              # {6, 7, 8}

# ── symmetric_difference() — Faqat bittasida bor ─────────────
print(A ^ B)                       # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))   # {1, 2, 3, 6, 7, 8}

# ── Amaliy misol: Ikki sinfning umumiy o'quvchilari ──────────
sinf_A = {"Ali", "Vali", "Jasur", "Bobur"}
sinf_B = {"Jasur", "Bobur", "Nodir", "Sanjar"}

print("Ikkalasida bor:", sinf_A & sinf_B)        # {'Jasur', 'Bobur'}
print("Faqat A da:", sinf_A - sinf_B)             # {'Ali', 'Vali'}
print("Faqat B da:", sinf_B - sinf_A)             # {'Nodir', 'Sanjar'}
print("Hammasi:", sinf_A | sinf_B)


# ============================================================
# LIST vs TUPLE vs SET — TAQQOSLASH
# ============================================================

"""
┌────────────────┬──────────────┬──────────────┬──────────────┐
│ Xususiyat      │ LIST  []     │ TUPLE ()     │ SET   {}     │
├────────────────┼──────────────┼──────────────┼──────────────┤
│ Tartibli       │ ✔️  Ha        │ ✔️  Ha        │ ✗  Yo'q      │
│ O'zgaruvchan   │ ✔️  Ha        │ ✗  Yo'q      │ ✔️  Ha        │
│ Takrorlanuvchi │ ✔️  Ha        │ ✔️  Ha        │ ✗  Yo'q      │
│ Indeks         │ ✔️  Ha        │ ✔️  Ha        │ ✗  Yo'q      │
│ Tezlik         │ O'rta        │ Tez          │ Juda tez     │
├────────────────┼──────────────┼──────────────┼──────────────┤
│ Ishlatilishi   │ Umumiy       │ O'zgarmas    │ Unikal       │
│                │ maqsad       │ ma'lumot     │ elementlar   │
└────────────────┴──────────────┴──────────────┴──────────────┘
"""


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Tuple (Oson):
  Hafta kunlarini tuple sifatida saqlang.
  a) Birinchi va oxirgi kunni chiqaring
  b) "Shanba" tupleda bormi? tekshiring
  c) Tupleni for sikli bilan chiqaring
  d) Nechta kun borligini chiqaring (len)

TOPSHIRIQ 2 — Tuple unpacking (O'rta):
  Foydalanuvchidan: ism, yosh, shahar oling.
  Ularni tuplega soling va unpackig bilan chiqaring.

TOPSHIRIQ 3 — Set (O'rta):
  Foydalanuvchidan 7 ta son oling (takror bo'lishi mumkin).
  Set yordamida:
  a) Nechta UNIKAL son borligini chiqaring
  b) Qanday unikal sonlar borligini chiqaring

TOPSHIRIQ 4 — Set amaliyotlari (Qiyin):
  Ikkita o'quvchilar ro'yxati yarating (har birida 5 ta ism).
  Set yordamida:
  a) Ikkalasida ham bo'lgan o'quvchilar
  b) Faqat birinchisida bo'lgan o'quvchilar
  c) Jami nechta unikal o'quvchi bor

TOPSHIRIQ 5 — Ijodiy:
  Matndan takroriy so'zlarni olib tashlang:
    gap = "men sen u men sen sen biz"
  Set va join() yordamida unikal so'zlarni chiqaring.
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
TUPLE:
  ✔️ Tuple nima — () o'zgarmas to'plam
  ✔️ Bitta elementli tuple — (5,)  (vergul shart!)
  ✔️ Indekslash va slicing — tuple[0], tuple[1:3]
  ✔️ Metodlar: count(), index()
  ✔️ len(), type(), in
  ✔️ + qo'shish, * takrorlash
  ✔️ Packing va Unpacking
  ✔️ Swap: x, y = y, x

SET:
  ✔️ Set nima — {} tartibsiz, takrorlashsiz to'plam
  ✔️ Bo'sh set — set()  ({} emas!)
  ✔️ Takrorlar avtomatik olib tashlanadi
  ✔️ Indeks ishlamaydi — for sikli bilan ko'rish
  ✔️ Metodlar:
      add()     — bitta qo'shish
      update()  — ko'p qo'shish
      remove()  — o'chirish (xato beradi)
      discard() — o'chirish (xato bermaydi)
      pop()     — tasodifiy o'chirish
      clear()   — tozalash
      copy()    — nusxa
  ✔️ Set amaliyotlari:
      |  union()               — birlashtirish
      &  intersection()        — kesishma
      -  difference()          — farq
      ^  symmetric_difference()— simmetrik farq
"""