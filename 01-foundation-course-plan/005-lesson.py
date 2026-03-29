# ============================================================
#   DARS 5: For Sikl Operatori
#           range(), Ichma-ich Sikllar
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# FOR SIKLI NIMA?
# ------------------------------------------------------------

"""
O'tgan darsda while siklini o'rgandik.
while — shart True bo'lguncha ishlaydi.

For sikli esa — ma'lum bir ketma-ketlik (ro'yxat, matn, son oralig'i)
bo'ylab BIRIN-KETIN o'tadi va har bir element uchun kod bajaradi.

  while  →  "shart bajarilguncha takrorla"
  for    →  "har bir element uchun bir marta bajara"

Qachon for ishlatiladi?
  - Aniq necha marta takrorlanishini bilganda
  - Ro'yxat yoki matn elementlarini birma-bir ko'rib chiqishda
  - Sonlar oralig'i bo'ylab yurishda

Sintaksis:
  for o'zgaruvchi in ketma_ketlik:
      bajariladigan_kod
"""


# ============================================================
# FOR + RANGE() — SONLAR BO'YLAB YURISH
# ============================================================

"""
range() — sonlar ketma-ketligini yaratadi.

  range(stop)              →  0 dan stop-1 gacha
  range(start, stop)       →  start dan stop-1 gacha
  range(start, stop, step) →  start dan stop-1 gacha, step qadam bilan

MUHIM: range() oxirgi sonni O'Z ICHIGA OLMAYDI!
  range(5)     →  0, 1, 2, 3, 4       (5 YO'Q)
  range(1, 6)  →  1, 2, 3, 4, 5       (6 YO'Q)
  range(0, 10, 2) → 0, 2, 4, 6, 8    (10 YO'Q)
"""

# ── range(stop) — 0 dan boshlab ──────────────────────────────
print("=== range(5) ===")
for i in range(5):
    print(i)
# Natija: 0 1 2 3 4

# ── range(start, stop) — boshlang'ich bilan ──────────────────
print("\n=== range(1, 6) ===")
for i in range(1, 6):
    print(i)
# Natija: 1 2 3 4 5

# ── range(start, stop, step) — qadam bilan ───────────────────
print("\n=== range(0, 20, 2) — juft sonlar ===")
for i in range(0, 20, 2):
    print(i, end=" ")
print()
# Natija: 0 2 4 6 8 10 12 14 16 18

print("\n=== range(1, 20, 2) — toq sonlar ===")
for i in range(1, 20, 2):
    print(i, end=" ")
print()
# Natija: 1 3 5 7 9 11 13 15 17 19

print("\n=== range(10, 0, -1) — ortga sanash ===")
for i in range(10, 0, -1):
    print(i, end=" ")
print()
# Natija: 10 9 8 7 6 5 4 3 2 1

print("\n=== range(0, 51, 5) — 5 lik jadval ===")
for i in range(0, 51, 5):
    print(i, end=" ")
print()
# Natija: 0 5 10 15 20 25 30 35 40 45 50

# ── While bilan taqqoslash ────────────────────────────────────
"""
Bir xil natija — ikki xil usul:

  # while bilan:          # for bilan:
  i = 1                   for i in range(1, 6):
  while i <= 5:               print(i)
      print(i)
      i += 1

For ancha qisqa va qulay!
"""


# ============================================================
# FOR + MATN (STRING) BO'YLAB YURISH
# ============================================================

"""
Matn (string) — bu harflar ketma-ketligi.
For sikli matndagi har bir harfni birin-ketin oladi.
"""

print("\n=== Matn bo'ylab yurish ===")
so_z = "Python"
for harf in so_z:
    print(harf)
# Natija:
# P
# y
# t
# h
# o
# n

print("\n=== Harflar bir qatorda ===")
for harf in "Salom":
    print(harf, end="-")
print()
# Natija: S-a-l-o-m-

print("\n=== Harflarni sanash ===")
# Matndagi harflar sonini hisoblash
so_z = "dasturlash"
hisob = 0
for harf in so_z:
    hisob += 1
print(f"'{so_z}' so'zida {hisob} ta harf bor")
# Natija: 'dasturlash' so'zida 10 ta harf bor

print("\n=== Muayyan harfni sanash ===")
# 'a' harfi necha marta uchraydi?
matn = "Assalomu alaykum"
soni = 0
for harf in matn:
    if harf == "a" or harf == "A":
        soni += 1
print(f"'a' harfi {soni} marta uchraydi")



# ============================================================
# break VA continue — FOR SIKLIDA
# ============================================================

"""
break va continue for siklida ham xuddi while dagi kabi ishlaydi.
(O'tgan darsda while bilan ko'rgandik)

  break    →  siklni butunlay to'xtatadi
  continue →  joriy qadamni o'tkazadi, davom etadi
"""

# ── break — for siklida ───────────────────────────────────────
print("\n=== break — for siklida ===")
for i in range(1, 11):
    if i == 6:
        print("6 ga yetdik, to'xtatamiz!")
        break
    print(i, end=" ")
print()
# Natija: 1 2 3 4 5 → to'xtaydi

print("\n=== break — ro'yxatda qidirish ===")
talabalar = ["Ali", "Vali", "Jasur", "Sardor", "Kamol"]
qidirilayotgan = "Jasur"

for ism in talabalar:
    if ism == qidirilayotgan:
        print(f"{qidirilayotgan} ro'yxatda bor!")
        break
else:
    print(f"{qidirilayotgan} topilmadi")
# Natija: Jasur ro'yxatda bor!

# ── continue — for siklida ────────────────────────────────────
print("\n=== continue — for siklida ===")
for i in range(1, 11):
    if i % 2 == 0:
        continue    # juft sonlarni o'tkazib yubor
    print(i, end=" ")
print()
# Natija: 1 3 5 7 9

print("\n=== continue — manfiy sonlarni o'tkazish ===")
sonlar = [5, -3, 8, -1, 12, -7, 4]
print("Faqat musbatlar:", end=" ")
for son in sonlar:
    if son < 0:
        continue
    print(son, end=" ")
print()
# Natija: Faqat musbatlar: 5 8 12 4


# ============================================================
# FOR + ELSE
# ============================================================

"""
For siklida ham else ishlatish mumkin.
else — sikl ODATIY tugaganda bajariladi (break bo'lmasa).

  for element in ketma_ketlik:
      kod...
  else:
      # break bo'lmasa — bu bajariladi
"""

print("\n=== for + else ===")
# Juft sonni qidirish — topilmasa xabar ber
sonlar = [3, 7, 11, 15, 9]
for son in sonlar:
    if son % 2 == 0:
        print(f"Juft son topildi: {son}")
        break
else:
    print("Ro'yxatda juft son yo'q!")
# Natija: Ro'yxatda juft son yo'q!


# ============================================================
# ICHMA-ICH SIKLLAR (Nested Loops)
# ============================================================

"""
Ichma-ich sikl — bir siklning ichida boshqa sikl.

  for tashqi in ...:
      for ichki in ...:
          kod...

ISHLASH TARTIBI:
  Tashqi siklning har bir qadami uchun
  ichki sikl TO'LIQLIGICHA bajariladi.

  Misol: tashqi 3 marta, ichki 4 marta ishlasa
         kod jami: 3 × 4 = 12 marta bajariladi.

  ┌─────────────────────────────────────────────────┐
  │  tashqi: i=1                                    │
  │    ichki: j=1, j=2, j=3, j=4  (4 marta)        │
  │  tashqi: i=2                                    │
  │    ichki: j=1, j=2, j=3, j=4  (4 marta)        │
  │  tashqi: i=3                                    │
  │    ichki: j=1, j=2, j=3, j=4  (4 marta)        │
  │  Jami: 3 × 4 = 12 marta                        │
  └─────────────────────────────────────────────────┘
"""

# ── ENG ODDIY ICHMA-ICH SIKL ─────────────────────────────────
print("\n=== Oddiy ichma-ich ===")
for i in range(1, 4):       # tashqi: 1, 2, 3
    for j in range(1, 4):   # ichki:  1, 2, 3
        print(f"i={i}, j={j}")

# Natija:
# i=1, j=1
# i=1, j=2
# i=1, j=3
# i=2, j=1
# i=2, j=2
# ... va hokazo


# ============================================================
# ICHMA-ICH SIKL — KO'PAYTMA JADVALI
# ============================================================

print("\n=== Ko'paytma jadvali (1 dan 5 gacha) ===")
for i in range(1, 6):           # tashqi: 1 dan 5 gacha
    for j in range(1, 6):       # ichki:  1 dan 5 gacha
        natija = i * j
        print(f"{natija:3}", end=" ")   # :3 — 3 belgili joy (tekis chiqarish)
    print()   # har qator tugagach yangi qatorga o't
# Natija:
#   1  2  3  4  5
#   2  4  6  8 10
#   3  6  9 12 15
#   4  8 12 16 20
#   5 10 15 20 25

print("\n=== Faqat 3 ning jadvali (for bilan) ===")
for i in range(1, 11):
    print(f"3 × {i:2} = {3*i:3}")
# Natija:
# 3 ×  1 =   3
# 3 ×  2 =   6
# ...
# 3 × 10 =  30


# ============================================================
# ICHMA-ICH SIKL — SHAKLLAR CHIZISH
# ============================================================

"""
Ichma-ich sikllarning eng yaxshi mashqi — shakllar chizish.
Tashqi sikl — QATORLARNI boshqaradi (nechta qator)
Ichki sikl  — USTUNLARNI boshqaradi (har qatorda nechta belgi)
"""

# ── To'g'ri to'rtburchak ──────────────────────────────────────
print("\n=== To'g'ri to'rtburchak (4×6) ===")
for i in range(4):          # 4 ta qator
    for j in range(6):      # har qatorda 6 ta yulduz
        print("*", end="")
    print()   # qator tugadi → yangi qatorga
# Natija:
# ******
# ******
# ******
# ******

# ── O'ng uchburchak ───────────────────────────────────────────
print("\n=== O'ng uchburchak ===")
for i in range(1, 6):       # 1, 2, 3, 4, 5
    for j in range(i):      # i marta yulduz
        print("*", end="")
    print()
# Natija:
# *
# **
# ***
# ****
# *****

# ── Teskari uchburchak ────────────────────────────────────────
print("\n=== Teskari uchburchak ===")
for i in range(5, 0, -1):   # 5, 4, 3, 2, 1
    for j in range(i):
        print("*", end="")
    print()
# Natija:
# *****
# ****
# ***
# **
# *

# ── Son uchburchak ────────────────────────────────────────────
print("\n=== Son uchburchagi ===")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# Natija:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# ── Piramida ─────────────────────────────────────────────────
print("\n=== Piramida ===")
n = 5
for i in range(1, n + 1):
    # Oldin bo'sh joy (chapga tekislash uchun)
    for j in range(n - i):
        print(" ", end="")
    # Keyin yulduzlar
    for j in range(2 * i - 1):
        print("*", end="")
    print()
# Natija:
#     *
#    ***
#   *****
#  *******
# *********

# ── Raqamli kvadrat ───────────────────────────────────────────
print("\n=== Raqamli kvadrat ===")
for i in range(1, 5):
    for j in range(1, 5):
        print(i * j, end="\t")   # \t — tab belgisi (tekis joy)
    print()
# Natija:
# 1	2	3	4
# 2	4	6	8
# 3	6	9	12
# 4	8	12	16


# ============================================================
# ICHMA-ICH SIKL — AMALIY MISOLLAR
# ============================================================

print("\n=== Tub sonlar (1 dan 30 gacha) ===")
# Tub son — faqat 1 ga va o'ziga bo'linadigan son (2, 3, 5, 7, 11...)
for son in range(2, 31):
    tub = True
    for bolovchi in range(2, son):   # 2 dan son-1 gacha tekshir
        if son % bolovchi == 0:
            tub = False
            break
    if tub:
        print(son, end=" ")
print()
# Natija: 2 3 5 7 11 13 17 19 23 29

print("\n=== Juft × toq juftlari ===")
# 1-5 orasidagi juft va toq sonlarning barcha juftlari
for juft in range(2, 11, 2):    # juft: 2, 4, 6, 8, 10
    for toq in range(1, 10, 2): # toq:  1, 3, 5, 7, 9
        print(f"({juft},{toq})", end=" ")
    print()


# ============================================================
# FOR VA WHILE — QACHON QAYSI?
# ============================================================

"""
  ┌──────────────────────────────────────────────────────────┐
  │              FOR yoki WHILE?                             │
  ├─────────────────────┬────────────────────────────────────┤
  │        FOR          │            WHILE                   │
  ├─────────────────────┼────────────────────────────────────┤
  │ Necha marta         │ Qachon to'xtashini oldindan        │
  │ takrorlanishini     │ bilmaganingizda                    │
  │ bilganda            │                                    │
  │                     │                                    │
  │ Ro'yxat, matn       │ Foydalanuvchi "chiq" deyguncha     │
  │ bo'ylab yurganda    │                                    │
  │                     │                                    │
  │ range() bilan       │ while True + break bilan           │
  │ aniq oraliqda       │                                    │
  └─────────────────────┴────────────────────────────────────┘

Amalda:
  "5 marta bajara"        →  for i in range(5)
  "Ro'yxatni ko'rib chiq" →  for element in ro'yxat
  "To'g'ri javob berilguncha so'ra" →  while True + break
"""


# ============================================================
# TO'LIQ AMALIY DASTUR
# ============================================================

# --- Ko'paytma Jadvali Generatori ---

print("Ko'paytma jadvali generatori")
son = int(input("Qaysi sonning jadvalini ko'rmoqchisiz? "))
gacha = int(input("Qancha gacha? (masalan 10): "))

print(f"\n{'='*25}")
print(f"  {son} ning ko'paytma jadvali")
print(f"{'='*25}")

for i in range(1, gacha + 1):
    natija = son * i
    print(f"  {son} × {i:2} = {natija:4}")

print(f"{'='*25}")

# --- Sinf Baholar Tahlili ---

n = int(input("Nechta talaba bor? "))
baholar = []

for i in range(1, n + 1):
    ball = int(input(f"{i}-talabaning bali (0-100): "))
    baholar.append(ball)

# Tahlil
eng_yuqori = baholar[0]
eng_past    = baholar[0]
jami        = 0
a_soni      = 0

for ball in baholar:
    jami += ball
    if ball > eng_yuqori:
        eng_yuqori = ball
    if ball < eng_past:
        eng_past = ball
    if ball >= 90:
        a_soni += 1

print(f"\n{'='*30}")
print("  SINF NATIJALARI")
print(f"{'='*30}")
print(f"  O'rtacha ball  : {round(jami/n, 1)}")
print(f"  Eng yuqori ball: {eng_yuqori}")
print(f"  Eng past ball  : {eng_past}")
print(f"  'A' olganlar   : {a_soni} ta")
print(f"{'='*30}")


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — range() bilan:
  a) 1 dan 100 gacha barcha sonlarni bir qatorda chiqaring
  b) 100 dan 1 gacha teskari chiqaring
  c) 1 dan 50 gacha faqat 3 ga bo'linadigan sonlarni chiqaring

TOPSHIRIQ 2 — Matn bilan:
  Foydalanuvchidan so'z oling.
    - Harflarini birin-ketin chiqaring (har biri yangi qatorda)
    - So'zdagi harflar sonini hisoblang (len() ishlatmasdan!)
    - So'zdagi 'a' yoki 'A' harflari necha marta uchrashini toping

TOPSHIRIQ 3 — Ko'paytma jadvali:
  For sikli bilan 1 dan 10 gacha barcha sonlarning
  ko'paytma jadvalini chiqaring:
    1 × 1 = 1   1 × 2 = 2  ...
    2 × 1 = 2   2 × 2 = 4  ...
    ...

TOPSHIRIQ 4 — Shakllar:
  Quyidagi shakllarni for + ichma-ich for bilan chiqaring:

  a) To'g'ri to'rtburchak (5×10):
     **********
     **********
     **********
     **********
     **********

  b) Chap uchburchak:
     *
     **
     ***
     ****
     *****

  c) Teskari piramida:
     *********
      *******
       *****
        ***
         *

TOPSHIRIQ 5 — Yig'indi va ko'paytma:
  For sikli bilan:
    a) 1 dan 10 gacha sonlar yig'indisi
    b) 1 dan 10 gacha sonlar ko'paytmasi (faktorial emas, shunchaki 1×2×3...×10)
    c) 1 dan 100 gacha toq sonlar yig'indisi

TOPSHIRIQ 6 (Qo'shimcha) — Tub sonlar:
  Foydalanuvchidan ikkita son oling (start va end).
  O'sha oraliqda barcha TUB sonlarni chiqaring.
  (Tub son — 1 va o'zidan boshqa hech narsaga bo'linmaydi)
"""


# ------------------------------------------------------------
# QUSHIMCHA RESURSLAR (Uyga vazifa uchun)
# ------------------------------------------------------------

"""
📚 RASMIY HUJJATLAR:
   https://docs.python.org/3/tutorial/controlflow.html#for-statements
   — for sikli haqida rasmiy ma'lumot

🌐 W3SCHOOLS:
   https://www.w3schools.com/python/python_for_loops.asp
   — for sikli, range(), ichma-ich sikllar
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ for sikli — sintaksis va ishlash tartibi
✔️ range() — uch xil ishlatish:
     range(stop)
     range(start, stop)
     range(start, stop, step)
✔️ for + matn  — har bir harfni birin-ketin olish
✔️ for + ro'yxat — har bir elementni ko'rib chiqish
✔️ break va continue — for siklida ham ishlaydi
✔️ for + else — shart bajarilmay tugaganda
✔️ Ichma-ich sikllar (nested loops):
     tashqi sikl × ichki sikl = jami bajarilish
✔️ Shakllar chizish:
     to'rtburchak, uchburchak, piramida
✔️ Amaliy misollar:
     ko'paytma jadvali, tub sonlar, baholar tahlili
✔️ for vs while — qachon qaysi birini tanlash
"""