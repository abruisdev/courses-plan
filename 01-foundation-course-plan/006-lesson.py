# ============================================================
#   TAKRORLASH DARSI: 1—5 Mavzular
#   Kirish → O'zgaruvchilar → if/elif/else → while → for
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# TAKRORLASH DARSI HAQIDA
# ------------------------------------------------------------

"""
Bu darsda 1—5-mavzularda o'rganilgan barcha tushunchalar
qisqa va aniq ko'rinishda takrorlanadi.

  1-Mavzu  →  print(), izohlar, arifmetik operatorlar
  2-Mavzu  →  O'zgaruvchilar, Data Types, Casting, Boolean, input()
  3-Mavzu  →  if, elif, else, and, or, not
  4-Mavzu  →  while sikli, break, continue
  5-Mavzu  →  for sikli, range(), ichma-ich sikllar
"""


# ============================================================
# print(), IZOHLAR, ARIFMETIK OPERATORLAR
# ============================================================

# ── print() ─────────────────────────────────────────────────
print("Salom, Dunyo!")           # matn chiqarish
print(2025)                      # son chiqarish
print("Ism:", "Ali", "Yosh:", 15)# bir nechta qiymat
print()                          # bo'sh qator
print("A", "B", "C", sep="-")   # ajratgich: A-B-C
print("Salom", end=" ")          # yangi qator o'rniga bo'sh joy
print("Dunyo!")                  # Natija: Salom Dunyo!

# ── Izohlar ─────────────────────────────────────────────────
# Bu — bir qatorli izoh
"""
Bu — ko'p qatorli izoh (docstring).
Python buni bajarmaydi.
"""

# ── Arifmetik operatorlar ────────────────────────────────────
print("\n--- Arifmetik operatorlar ---")
print(10 + 3)    # 13    — qo'shish
print(10 - 3)    # 7     — ayirish
print(10 * 3)    # 30    — ko'paytirish
print(10 / 3)    # 3.333 — bo'lish (DOIM float)
print(10 % 3)    # 1     — qoldiq
print(10 // 3)   # 3     — butun bo'lish
print(2 ** 8)    # 256   — daraja

# ── Amallar ketma-ketligi ────────────────────────────────────
print(2 + 3 * 4)     # 14  (avval *, keyin +)
print((2 + 3) * 4)   # 20  (qavs birinchi)


# ============================================================
# O'ZGARUVCHILAR, DATA TYPES, CASTING, BOOLEAN
# ============================================================

print("\n--- O'zgaruvchilar ---")
ism    = "Ali"          # str
yosh   = 15             # int
ball   = 87.5           # float
faol   = True           # bool

print(ism, yosh, ball, faol)
print(type(ism))        # <class 'str'>
print(type(yosh))       # <class 'int'>
print(type(ball))       # <class 'float'>
print(type(faol))       # <class 'bool'>

# ── Data Types qisqacha ──────────────────────────────────────
"""
  str     →  "Salom", 'Ali'          matn
  int     →  15, -3, 1000            butun son
  float   →  3.14, -0.5              kasr son
  complex →  3+2j                    kompleks son
  bool    →  True, False             mantiqiy qiymat
"""

# ── Casting ──────────────────────────────────────────────────
print("\n--- Casting ---")
print(int("25"))         # str → int:   25
print(float("3.14"))     # str → float: 3.14
print(str(100))          # int → str:  "100"
print(int(9.9))          # float → int: 9  (kasr tashlanadi!)
print(int(float("7.5"))) # str("7.5") → float → int: 7

# ── Boolean ──────────────────────────────────────────────────
print("\n--- Boolean ---")
print(5 > 3)             # True
print(5 == 5)            # True
print(5 != 5)            # False
print(bool(0))           # False
print(bool(""))          # False
print(bool(42))          # True
print(bool("Salom"))     # True

# ── Sonlar bilan ishlash ─────────────────────────────────────
print("\n--- Sonlar funksiyalari ---")
print(abs(-15))          # 15
print(round(3.7))        # 4
print(round(3.14159, 2)) # 3.14
print(max(3, 8, 1))      # 8
print(min(3, 8, 1))      # 1
print(pow(2, 10))        # 1024

# ── input() eslatmasi ────────────────────────────────────────
"""
input() DOIM string qaytaradi!

# Xato:
son = input("Son: ")
print(son + 1)          # XATO! str + int bo'lmaydi

# To'g'ri:
son = int(input("Son: "))
print(son + 1)          # ishlaydi
"""


# ============================================================
# if, elif, else — TARMOQLANISH
# ============================================================

print("\n--- Solishtirish operatorlari ---")
a, b = 10, 20
print(a == b)   # False
print(a != b)   # True
print(a < b)    # True
print(a > b)    # False
print(a <= b)   # True
print(a >= b)   # False

print("\n--- Mantiq operatorlari ---")
#  and  — ikkalasi True bo'lsa True
print(True and True)    # True
print(True and False)   # False

#  or   — biri True bo'lsa True
print(True or False)    # True
print(False or False)   # False

#  not  — teskarisi
print(not True)         # False
print(not False)        # True

print("\n--- if / elif / else ---")
# if — oddiy shart
ball = 75
if ball >= 50:
    print("O'tdingiz!")   # chiqadi

# if-else — ikki yo'l
son = -4
if son > 0:
    print("Musbat")
else:
    print("Manfiy yoki nol")   # chiqadi

# if-elif-else — bir nechta shart
ball = 82
if ball >= 90:
    print("A")
elif ball >= 80:
    print("B")          # chiqadi
elif ball >= 70:
    print("C")
else:
    print("F")

# Qisqa if (ternary)
yosh = 20
toifa = "katta" if yosh >= 18 else "yosh"
print(toifa)            # katta

# and, or, not — shartda
yosh = 22
talaba = True
if yosh >= 18 and talaba:
    print("Talabalar chegirmasi!")   # chiqadi

kun = "Yakshanba"
if kun == "Shanba" or kun == "Yakshanba":
    print("Dam olish kuni!")         # chiqadi

kirgan = False
if not kirgan:
    print("Iltimos, tizimga kiring!")  # chiqadi


# ============================================================
# while SIKLI
# ============================================================

print("\n--- while asosi ---")
# Hisoblagich bilan
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1
print()   # Natija: 1 2 3 4 5

# while True + break
print("\n--- while True + break ---")
i = 0
while True:
    i += 1
    if i == 5:
        break
    print(i, end=" ")
print()   # Natija: 1 2 3 4

# continue
print("\n--- continue ---")
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue       # juft → o'tkazib yubor
    print(i, end=" ")
print()   # Natija: 1 3 5 7 9

# end=" " bilan
print("\n--- end=\" \" ---")
i = 1
while i <= 5:
    print(i, end=" | ")
    i += 1
print()   # Natija: 1 | 2 | 3 | 4 | 5 |

# ── Qisqa eslatma ─────────────────────────────────────────────
"""
  break    →  siklni TO'XTATADI (chiqadi)
  continue →  shu qadamni o'TKAZADI (davom etadi)
  end=" "  →  yangi qator o'rniga belgi qo'yadi
"""


# ============================================================
# for SIKLI
# ============================================================

print("\n--- range() ---")
# range(stop)
for i in range(5):
    print(i, end=" ")       # 0 1 2 3 4
print()

# range(start, stop)
for i in range(1, 6):
    print(i, end=" ")       # 1 2 3 4 5
print()

# range(start, stop, step)
for i in range(0, 20, 4):
    print(i, end=" ")       # 0 4 8 12 16
print()

# Teskari
for i in range(5, 0, -1):
    print(i, end=" ")       # 5 4 3 2 1
print()

# for + matn
print("\n--- for + matn ---")
for harf in "Python":
    print(harf, end="-")    # P-y-t-h-o-n-
print()

# for + break/continue
print("\n--- for + break ---")
for i in range(1, 11):
    if i == 6:
        break
    print(i, end=" ")       # 1 2 3 4 5
print()

print("\n--- for + continue ---")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")       # 1 2 4 5 7 8 10
print()

# ── Ichma-ich sikllar ─────────────────────────────────────────
print("\n--- Ichma-ich sikl ---")
for i in range(1, 4):       # tashqi: 1, 2, 3
    for j in range(1, 4):   # ichki:  1, 2, 3
        print(f"{i}×{j}={i*j}", end="  ")
    print()
# Natija:
# 1×1=1  1×2=2  1×3=3
# 2×1=2  2×2=4  2×3=6
# 3×1=3  3×2=6  3×3=9

# Uchburchak
print("\n--- Uchburchak ---")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
# *
# **
# ***
# ****
# *****

# ── for vs while ─────────────────────────────────────────────
"""
  for   →  necha marta ekanini BILSANGiZ  →  for i in range(n)
  while →  qachon tugashini BILMASANGIZ   →  while True + break
"""


# ============================================================
#   UMUMIY XULOSA — BARCHA MAVZULAR JADVALDA
# ============================================================

"""
┌────────────────────────────────────────────────────────────────────────┐
│                     1—5 MAVZU: UMUMIY JADVAL                          │
├─────────────────┬──────────────────────────────────────────────────────┤
│ MAVZU           │ ASOSIY TUSHUNCHALAR                                  │
├─────────────────┼──────────────────────────────────────────────────────┤
│ 1. Kirish       │ print(), # izoh, +  -  *  /  %  //  **              │
├─────────────────┼──────────────────────────────────────────────────────┤
│ 2. O'zgaruvchi  │ str int float bool, type(), Casting, input(),        │
│                 │ abs() round() max() min() pow()                      │
├─────────────────┼──────────────────────────────────────────────────────┤
│ 3. Shartlar     │ == != > < >= <=, and or not,                         │
│                 │ if / elif / else, ternary                             │
├─────────────────┼──────────────────────────────────────────────────────┤
│ 4. while        │ while shart, i+=1, break, continue, end=" ",         │
│                 │ while True, while+else                                │
├─────────────────┼──────────────────────────────────────────────────────┤
│ 5. for          │ for x in ..., range(stop/start,stop/start,stop,step),│
│                 │ for+matn, for+ro'yxat, ichma-ich, shakllar           │
└─────────────────┴──────────────────────────────────────────────────────┘
"""


# ============================================================
#   ARALASH AMALIY MASHQLAR (Darsda birga ishlash uchun)
# ============================================================

# MASHQ 1 — Barcha mavzulardan: Sonni tahlil qilish
print("\n=== MASHQ 1: Son tahlili ===")
son = 36
print("Son:", son)
print("Mutlaq qiymat:", abs(son))
print("Juft mi?", son % 2 == 0)
print("100 gacha mi?", son <= 100)

# MASHQ 2 — while + if: 1 dan 20 gacha, juft bo'lsa 2 ga ko'paytir
print("\n=== MASHQ 2: while + if ===")
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i * 2, end=" ")
    i += 1
print()   # 4 8 12 16 20 24 28 32 36 40

# MASHQ 3 — for + shakllar + sonlar
print("\n=== MASHQ 3: Son uchburchagi ===")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5