# ============================================================
#   DARS 14: 2D Arrays (Ikki O'lchovli Massivlar)
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# 2D ARRAY NIMA?
# ------------------------------------------------------------

"""
2D Array — bu list ichida listlar (matritsa ko'rinishida).
Jadval, to'r yoki matritsa deb ham ataladi.

Kundalik hayotda:
  - Sinf jadvali (qator = dars, ustun = kun)
  - Shaxmat taxtasi (8x8 kataklar)
  - Rasm piksel ma'lumotlari
  - Excel jadval

Ko'rinishi:
       Ustun 0   Ustun 1   Ustun 2
  Qator 0: [  1,        2,        3  ]
  Qator 1: [  4,        5,        6  ]
  Qator 2: [  7,        8,        9  ]
"""

# ── 2D Array yaratish ─────────────────────────────────────────
matritsa = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matritsa)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(type(matritsa))       # <class 'list'>
print(type(matritsa[0]))    # <class 'list'>


# ============================================================
# ELEMENTLARGA MUROJAAT
# ============================================================

"""
matritsa[qator][ustun]
  — avval qator, keyin ustun indeksi
"""

matritsa = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Bitta element:
print(matritsa[0][0])    # 1   — 0-qator, 0-ustun
print(matritsa[0][2])    # 3   — 0-qator, 2-ustun
print(matritsa[1][1])    # 5   — 1-qator, 1-ustun  (markaz)
print(matritsa[2][2])    # 9   — 2-qator, 2-ustun  (oxirgi)

# Bitta qatorni olish:
print(matritsa[0])    # [1, 2, 3]
print(matritsa[1])    # [4, 5, 6]
print(matritsa[-1])   # [7, 8, 9]  — oxirgi qator

# Manfiy indeks:
print(matritsa[-1][-1])   # 9  — oxirgi qatordagi oxirgi element


# ============================================================
# 2D ARRAY CHIQARISH — FOR SIKLI
# ============================================================

matritsa = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# ── Oddiy chiqarish ───────────────────────────────────────────
for qator in matritsa:
    print(qator)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

# ── Chiroyli jadval ko'rinishida ──────────────────────────────
for qator in matritsa:
    for element in qator:
        print(f"{element:4}", end="")
    print()
#    1   2   3
#    4   5   6
#    7   8   9

# ── Indeks bilan ──────────────────────────────────────────────
for i, qator in enumerate(matritsa):
    for j, element in enumerate(qator):
        print(f"[{i}][{j}]={element}", end="  ")
    print()
# [0][0]=1  [0][1]=2  [0][2]=3
# [1][0]=4  [1][1]=5  [1][2]=6
# [2][0]=7  [2][1]=8  [2][2]=9


# ============================================================
# 2D ARRAY YARATISH USULLARI
# ============================================================

# ── Qo'lda yaratish ───────────────────────────────────────────
shaxmat = [
    ["♜","♞","♝","♛","♚","♝","♞","♜"],
    ["♟","♟","♟","♟","♟","♟","♟","♟"],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    ["♙","♙","♙","♙","♙","♙","♙","♙"],
    ["♖","♘","♗","♕","♔","♗","♘","♖"],
]

print("\nShaxmat taxtasi:")
for qator in shaxmat:
    print(" ".join(qator))

# ── Nollar matritsasi ─────────────────────────────────────────
"""
Nxn o'lchamdagi barcha nollardan iborat matritsa
"""
n = 4
nollar = [[0] * n for _ in range(n)]
for qator in nollar:
    print(qator)
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]

# ── DIQQAT: Noto'g'ri usul ────────────────────────────────────
"""
nollar = [[0] * 3] * 3   ← NOTO'G'RI!
Bu uchta bir xil ob'ektga ishora qiladi.
Bittasini o'zgartirsangiz, hammasi o'zgaradi!
"""
xato = [[0] * 3] * 3
xato[0][0] = 9
print(xato)    # [[9, 0, 0], [9, 0, 0], [9, 0, 0]]  — barchasi o'zgardi!

# To'g'ri usul: list comprehension
togri = [[0] * 3 for _ in range(3)]
togri[0][0] = 9
print(togri)   # [[9, 0, 0], [0, 0, 0], [0, 0, 0]]  — faqat bittasi

# ── range bilan ───────────────────────────────────────────────
# 3x3 matritsa: 1 dan 9 gacha
matritsa = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
for qator in matritsa:
    print(qator)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]


# ============================================================
# ELEMENTNI O'ZGARTIRISH
# ============================================================

matritsa = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Bitta element:
matritsa[1][1] = 0    # markaz elementini o'zgartirish
print(matritsa[1])    # [4, 0, 6]

# Bitta qator:
matritsa[0] = [10, 20, 30]
print(matritsa)
# [[10, 20, 30], [4, 0, 6], [7, 8, 9]]


# ============================================================
# AMALIY MISOLLAR
# ============================================================

# ── MISOL 1: Barcha elementlar yig'indisi ─────────────────────
matritsa = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

jami = 0
for qator in matritsa:
    jami += sum(qator)
print(f"Yig'indi: {jami}")    # 45

# Yoki:
jami = sum(sum(qator) for qator in matritsa)
print(f"Yig'indi: {jami}")    # 45

# ── MISOL 2: Har qatorning yig'indisi ─────────────────────────
for i, qator in enumerate(matritsa):
    print(f"Qator {i}: {qator}  →  Yig'indi: {sum(qator)}")

# ── MISOL 3: Maksimal element ─────────────────────────────────
maks = matritsa[0][0]
for qator in matritsa:
    for el in qator:
        if el > maks:
            maks = el
print(f"Maksimal: {maks}")    # 9

# ── MISOL 4: Diagonal elementlar ─────────────────────────────
"""
Asosiy diagonal: [0][0], [1][1], [2][2], ...
"""
n = len(matritsa)
diagonal = [matritsa[i][i] for i in range(n)]
print(f"Diagonal: {diagonal}")       # [1, 5, 9]
print(f"Diag yig'indi: {sum(diagonal)}")   # 15

# ── MISOL 5: Transponirish ────────────────────────────────────
"""
Transponirish — qator va ustunlarni almashtirish.
  [1, 2, 3]        [1, 4, 7]
  [4, 5, 6]  →     [2, 5, 8]
  [7, 8, 9]        [3, 6, 9]
"""
matritsa = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

n = len(matritsa)
trans = [[matritsa[j][i] for j in range(n)] for i in range(n)]

print("\nAsl matritsa:")
for qator in matritsa:
    print(qator)

print("\nTransponlangan:")
for qator in trans:
    print(qator)

# ── MISOL 6: Ikkita matritsani qo'shish ───────────────────────
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

n = len(A)
C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]
print("\nA + B =")
for qator in C:
    print(qator)
# [6, 8]
# [10, 12]


# ============================================================
# AMALIY DASTUR 1 — Sinfning baholar jadvali
# ============================================================

print("\n=== BAHOLAR JADVALI ===")

fanlar = ["Matematika", "Fizika", "Ingliz"]
o_quvchilar = ["Ali", "Vali", "Jasur", "Bobur"]

# Baholar jadvali (4 o'quvchi x 3 fan):
baholar = [
    [90, 85, 88],    # Ali
    [78, 92, 75],    # Vali
    [95, 88, 91],    # Jasur
    [70, 65, 80],    # Bobur
]

# Sarlavha:
print(f"\n{'O\'quvchi':<12}", end="")
for fan in fanlar:
    print(f"{fan:>12}", end="")
print(f"{'O\'rtacha':>12}")
print("-" * 60)

# Ma'lumotlar:
for i, (ism, qator) in enumerate(zip(o_quvchilar, baholar)):
    ortacha = round(sum(qator) / len(qator), 1)
    print(f"{ism:<12}", end="")
    for baho in qator:
        print(f"{baho:>12}", end="")
    print(f"{ortacha:>12}")

# Fan bo'yicha o'rtacha:
print("-" * 60)
print(f"{'O\'rtacha':<12}", end="")
for j in range(len(fanlar)):
    ustun = [baholar[i][j] for i in range(len(o_quvchilar))]
    print(f"{round(sum(ustun)/len(ustun), 1):>12}", end="")
print()


# ============================================================
# AMALIY DASTUR 2 — Tic-Tac-Toe o'yini
# ============================================================

def taxta_chiqar(taxta):
    print("\n  0   1   2")
    for i, qator in enumerate(taxta):
        print(f"{i} {' | '.join(qator)}")
        if i < 2:
            print("  ─────────")
    print()

def g_olib_mi(taxta, belgi):
    # Qatorlar
    for qator in taxta:
        if all(x == belgi for x in qator):
            return True
    # Ustunlar
    for j in range(3):
        if all(taxta[i][j] == belgi for i in range(3)):
            return True
    # Diagonallar
    if all(taxta[i][i] == belgi for i in range(3)):
        return True
    if all(taxta[i][2 - i] == belgi for i in range(3)):
        return True
    return False

def tic_tac_toe():
    taxta = [[" "] * 3 for _ in range(3)]
    navbat = "X"

    for qadam in range(9):
        taxta_chiqar(taxta)
        print(f"Navbat: {navbat}")

        while True:
            try:
                qator = int(input("Qator (0-2): "))
                ustun = int(input("Ustun (0-2): "))
                if taxta[qator][ustun] == " ":
                    break
                print("Bu katakda allaqachon belgi bor!")
            except (ValueError, IndexError):
                print("Noto'g'ri kiritish!")

        taxta[qator][ustun] = navbat

        if g_olib_mi(taxta, navbat):
            taxta_chiqar(taxta)
            print(f"🎉 {navbat} g'olib bo'ldi!")
            return

        navbat = "O" if navbat == "X" else "X"

    taxta_chiqar(taxta)
    print("Durrang!")

# O'yinni ishga tushirish:
# tic_tac_toe()


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Asosiy (Oson):
  3x4 o'lchamdagi matritsa yarating (o'zingiz istagancha sonlar).
  a) Birinchi va oxirgi qatorni chiqaring
  b) Har qatorning yig'indisini chiqaring
  c) Barcha elementlarning yig'indisini chiqaring

TOPSHIRIQ 2 — O'rta:
  5x5 nollar matritsasi yarating.
  a) Asosiy diagonalga 1 larni joylashtiring
  b) Natijani chiqaring (bu birlik matritsa — Identity matrix)
     [1, 0, 0, 0, 0]
     [0, 1, 0, 0, 0]
     ...

TOPSHIRIQ 3 — Ko'paytma jadval (O'rta):
  10x10 ko'paytma jadvali matritsasini yarating.
  Har bir [i][j] = (i+1) * (j+1)
  Chiroyli jadval ko'rinishida chiqaring.

TOPSHIRIQ 4 — Qiyin:
  Foydalanuvchidan 3x3 matritsa kiriting (har qator uchun 3 son).
  a) Eng katta elementni toping
  b) Asosiy diagonal yig'indisini hisoblang
  c) Matritsani transponlang va chiqaring

TOPSHIRIQ 5 — Ijodiy:
  Labirint — 0 yo'l, 1 devor:
    labirint = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]
  Labirintni chiroyli chiqaring (0 = " ", 1 = "█").
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ 2D Array nima — list ichida listlar
✔️ Murojaat: matritsa[qator][ustun]
✔️ For sikli bilan ko'rib chiqish (ichma-ich)
✔️ 2D Array yaratish usullari:
    - Qo'lda
    - List comprehension: [[0]*n for _ in range(n)]
    - XATO usul: [[0]*n]*n (hammasi bir xil ob'ekt!)
✔️ Elementni o'zgartirish
✔️ Amaliy amallar:
    - Yig'indi
    - Maksimal/minimal element
    - Diagonal elementlar
    - Transponirish
    - Ikki matritsani qo'shish
✔️ Amaliy dasturlar:
    - Baholar jadvali
    - Tic-Tac-Toe o'yini
"""