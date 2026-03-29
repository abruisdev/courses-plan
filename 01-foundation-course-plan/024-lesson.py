# ============================================================
#   DARS 24: Algoritmlash — Sorting (Saralash)
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# DARS HAQIDA
# ------------------------------------------------------------

"""
Bugun uch xil saralash algoritmini o'rganamiz:

  1️⃣  Bubble Sort   — Pufakchali saralash   O(n²)
  2️⃣  Quick Sort    — Tez saralash          O(n log n)
  3️⃣  Merge Sort    — Qo'shib saralash      O(n log n)

Nima uchun muhim?
  - Amalda eng ko'p ishlatiladigan algoritmlar
  - Murakkablik va samaradorlikni tushunish uchun asos
  - Interview savollarining asosiy qismi

Saralash = massivni o'sish yoki kamayish tartibida joylashtirish
"""

import time
import random


# ============================================================
#   1. BUBBLE SORT — Pufakchali saralash
# ============================================================

# ------------------------------------------------------------
# NAZARIYA
# ------------------------------------------------------------

"""
Bubble Sort — qo'shni elementlarni solishtiradi va kattasini
o'ngga suradi. Katta elementlar "pufakcha" kabi yuqoriga ko'tariladi.

Ishlash tartibi:
  [5, 3, 8, 1, 9]
  1-o'tish:
    (5,3) → (3,5)  → [3, 5, 8, 1, 9]
    (5,8) → o'zgarishsiz
    (8,1) → (1,8)  → [3, 5, 1, 8, 9]
    (8,9) → o'zgarishsiz
    → [3, 5, 1, 8, 9]  (9 o'z joyida)
  2-o'tish:
    (3,5) → o'zgarishsiz
    (5,1) → (1,5)
    (5,8) → o'zgarishsiz
    → [3, 1, 5, 8, 9]  (8 ham o'z joyida)
  ...va hokazo

Vaqt murakkabligi:
  Eng yaxshi: O(n)   — tartiblangan massiv
  O'rtacha:   O(n²)
  Eng yomoni: O(n²)
"""

print("=" * 55)
print("    1. BUBBLE SORT — Pufakchali saralash")
print("=" * 55)


def bubble_sort(arr):
    """
    Bubble sort algoritmi.
    arr ni o'sish tartibida saralaydi (o'zi o'zgaradi).
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]    # almashtirish


# Test:
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"\nBoshlang'ich: {arr}")
bubble_sort(arr)
print(f"Saralangan:   {arr}")


# ── Optimallashtirilgan versiya ───────────────────────────────
def bubble_sort_optim(arr):
    """
    Agar bir o'tishda almashtirilmasa — massiv tartiblangan.
    Erta to'xtatish bilan tezlashtirilgan versiya.
    """
    n = len(arr)
    for i in range(n):
        almashtirildi = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                almashtirildi = True
        if not almashtirildi:
            break   # Almashuv bo'lmadi = tartiblangan!


# ── Jarayonni ko'rsatuvchi versiya ───────────────────────────
print("\n--- Bubble Sort jarayoni ---")

def bubble_sort_batafsil(arr):
    arr = arr.copy()
    n = len(arr)
    print(f"Boshlang'ich: {arr}")
    for i in range(n):
        almashtirildi = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                almashtirildi = True
        print(f"  {i+1}-o'tish: {arr}")
        if not almashtirildi:
            print("  Almashuv yo'q — tugatildi!")
            break
    return arr

bubble_sort_batafsil([5, 3, 8, 1, 9, 2])


# ============================================================
#   2. QUICK SORT — Tez saralash
# ============================================================

# ------------------------------------------------------------
# NAZARIYA
# ------------------------------------------------------------

"""
Quick Sort — "bo'l va boshqar" (divide and conquer) strategyasi.
Amalda eng tez ishlatiladigan algoritmlardan biri.

Ishlash tartibi:
  1. PIVOT (tayanch) elementni tanlash (odatda oxirgi)
  2. Pivot dan kichik elementlar → CHAP
     Pivot dan katta elementlar  → O'NG
  3. Har ikki yarmiga REKURSIV qaytarish

Misol: [3, 6, 8, 10, 1, 2, 1], pivot = 1
  Chap (≤1): [1]
  O'ng (>1): [3, 6, 8, 10, 2]
  Natija: [1] + [1] + [3, 6, 8, 10, 2 — davom etadi]

Vaqt murakkabligi:
  Eng yaxshi: O(n log n)
  O'rtacha:   O(n log n)
  Eng yomoni: O(n²)       — tartiblangan massivda (pivot yomon)
"""

print("\n" + "=" * 55)
print("    2. QUICK SORT — Tez saralash")
print("=" * 55)


def quick_sort(arr):
    """
    Quick sort rekursiv algoritmi.
    Yangi ro'yxat qaytaradi (asl o'zgarmaydi).
    """
    if len(arr) <= 1:
        return arr                          # baza holat

    pivot = arr[len(arr) // 2]             # o'rtadagi elementni pivot qilamiz
    chap   = [x for x in arr if x < pivot]
    o_rta  = [x for x in arr if x == pivot]
    ong    = [x for x in arr if x > pivot]

    return quick_sort(chap) + o_rta + quick_sort(ong)


# Test:
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"\nBoshlang'ich: {arr}")
natija = quick_sort(arr)
print(f"Saralangan:   {natija}")

# Turli testlar:
print("\n--- Quick Sort testlar ---")
testlar = [
    [3, 6, 8, 10, 1, 2, 1],
    [1],
    [],
    [5, 5, 5, 5],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
]
for t in testlar:
    print(f"  {t:30s} → {quick_sort(t)}")


# ── In-place Quick Sort ───────────────────────────────────────
print("\n--- In-place Quick Sort (Xotira samarali) ---")

def quick_sort_inplace(arr, chap=0, ong=None):
    """
    Yangi ro'yxat yaratmasdan, asl massivni o'zgartiradigan versiya.
    """
    if ong is None:
        ong = len(arr) - 1

    if chap < ong:
        pivot_idx = bo_lish(arr, chap, ong)
        quick_sort_inplace(arr, chap, pivot_idx - 1)
        quick_sort_inplace(arr, pivot_idx + 1, ong)

def bo_lish(arr, chap, ong):
    """Lomuto partition sxemasi"""
    pivot = arr[ong]        # oxirgi element pivot
    i = chap - 1
    for j in range(chap, ong):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[ong] = arr[ong], arr[i + 1]
    return i + 1

arr2 = [10, 7, 8, 9, 1, 5]
print(f"Boshlang'ich: {arr2}")
quick_sort_inplace(arr2)
print(f"Saralangan:   {arr2}")


# ============================================================
#   3. MERGE SORT — Qo'shib saralash
# ============================================================

# ------------------------------------------------------------
# NAZARIYA
# ------------------------------------------------------------

"""
Merge Sort — "bo'l va birlashtir" strategiyasi.
Har doim O(n log n) — ishonchli algoritm.

Ishlash tartibi:
  1. Massivni ikkiga BO'L (rekursiv)
  2. Har bir yarmini alohida SARALASH
  3. Saralangan ikkala yarmini birlashtirish (MERGE)

Misol: [38, 27, 43, 3, 9, 82, 10]
  BO'LISH:
    [38, 27, 43]    [3, 9, 82, 10]
    [38][27, 43]    [3, 9][82, 10]
    [38][27][43]    [3][9][82][10]

  BIRLASHTIRISH:
    [27, 43]        [3, 9]  [10, 82]
    [27, 38, 43]    [3, 9, 10, 82]
    [3, 9, 10, 27, 38, 43, 82]

Vaqt murakkabligi:
  Eng yaxshi: O(n log n)
  O'rtacha:   O(n log n)
  Eng yomoni: O(n log n)  ← har doim bir xil!
Xotira: O(n) — qo'shimcha xotira talab qiladi
"""

print("\n" + "=" * 55)
print("    3. MERGE SORT — Qo'shib saralash")
print("=" * 55)


def merge_sort(arr):
    """
    Merge sort rekursiv algoritmi.
    Yangi ro'yxat qaytaradi.
    """
    if len(arr) <= 1:
        return arr                          # baza holat

    orta = len(arr) // 2
    chap = merge_sort(arr[:orta])          # chap yarmini saralash
    ong  = merge_sort(arr[orta:])          # o'ng yarmini saralash

    return birlashtir(chap, ong)           # birlashtirish


def birlashtir(chap, ong):
    """
    Ikki tartiblangan ro'yxatni birlashtirib, yangi tartiblangan ro'yxat hosil qiladi.
    """
    natija = []
    i = j = 0

    while i < len(chap) and j < len(ong):
        if chap[i] <= ong[j]:
            natija.append(chap[i])
            i += 1
        else:
            natija.append(ong[j])
            j += 1

    # Qolganlarini qo'shish:
    natija.extend(chap[i:])
    natija.extend(ong[j:])
    return natija


# Test:
arr = [38, 27, 43, 3, 9, 82, 10]
print(f"\nBoshlang'ich: {arr}")
print(f"Saralangan:   {merge_sort(arr)}")

# ── Jarayonni ko'rsatuvchi versiya ───────────────────────────
print("\n--- Merge Sort jarayoni ---")

daraja = 0

def merge_sort_batafsil(arr):
    global daraja
    daraja += 1
    chegara = "  " * daraja
    print(f"{chegara}bo'lish: {arr}")

    if len(arr) <= 1:
        daraja -= 1
        return arr

    orta = len(arr) // 2
    chap = merge_sort_batafsil(arr[:orta])
    ong  = merge_sort_batafsil(arr[orta:])
    natija = birlashtir(chap, ong)
    print(f"{chegara}birlashtirish: {chap} + {ong} → {natija}")
    daraja -= 1
    return natija

merge_sort_batafsil([5, 2, 4, 1, 3])


# ============================================================
# BARCHA ALGORITMLAR: TEZLIK TAQQOSLASH
# ============================================================

print("\n" + "=" * 55)
print("    TEZLIK TAQQOSLASH")
print("=" * 55)

def vaqt_olchash(funkiya, arr):
    arr_nusxa = arr.copy()
    boshlanish = time.perf_counter()
    funkiya(arr_nusxa)
    return time.perf_counter() - boshlanish

def tezlik_sinoyi(n):
    arr = [random.randint(1, 10000) for _ in range(n)]
    print(f"\nn = {n:,} element:")

    # Bubble Sort
    v1 = vaqt_olchash(bubble_sort, arr)
    print(f"  Bubble Sort : {v1:.6f} s")

    # Quick Sort (in-place)
    v2 = vaqt_olchash(quick_sort_inplace, arr)
    print(f"  Quick Sort  : {v2:.6f} s")

    # Merge Sort (yangi ro'yxat qaytaradi, shuning uchun boshqacha o'lchaymiz)
    boshlanish = time.perf_counter()
    merge_sort(arr)
    v3 = time.perf_counter() - boshlanish
    print(f"  Merge Sort  : {v3:.6f} s")

    # Python built-in
    boshlanish = time.perf_counter()
    sorted(arr)
    v4 = time.perf_counter() - boshlanish
    print(f"  Python sort : {v4:.6f} s (Timsort)")

tezlik_sinoyi(500)
tezlik_sinoyi(2000)

print("""
┌────────────────────────────────────────────────────────────┐
│                 SARALASH ALGORITMLARI JADVALI              │
├─────────────────┬──────────────┬────────────┬─────────────┤
│ Algoritm        │  Eng yaxshi  │  O'rtacha  │  Eng yomoni │
├─────────────────┼──────────────┼────────────┼─────────────┤
│ Bubble Sort     │  O(n)        │  O(n²)     │  O(n²)      │
│ Quick Sort      │  O(n log n)  │  O(n log n)│  O(n²)      │
│ Merge Sort      │  O(n log n)  │  O(n log n)│  O(n log n) │
│ Python sort()   │  O(n)        │  O(n log n)│  O(n log n) │
└─────────────────┴──────────────┴────────────┴─────────────┘

Tavsiya:
  ✔️ Kichik massiv  → Bubble Sort (oddiy, tushunish oson)
  ✔️ O'rtacha       → Quick Sort  (amalda eng tez)
  ✔️ Ishonchlilik   → Merge Sort  (har doim O(n log n))
  ✔️ Amaliy dastur  → Python sort() — ichida Timsort ishlatadi
""")


# ============================================================
# AMALIY DASTUR — Talabalar baholarini saralash
# ============================================================

print("=== BAHOLAR REYTINGI ===")

talabalar = [
    {"ism": "Ali",    "ball": 85},
    {"ism": "Vali",   "ball": 92},
    {"ism": "Jasur",  "ball": 78},
    {"ism": "Bobur",  "ball": 95},
    {"ism": "Nodir",  "ball": 88},
    {"ism": "Sanjar", "ball": 72},
]

# Lambda bilan saralash:
saralangan = sorted(talabalar, key=lambda x: x["ball"], reverse=True)

print(f"\n{'O\'rin':<6} {'Ism':<12} {'Ball':<6}")
print("─" * 26)
for i, t in enumerate(saralangan, 1):
    print(f"{i:<6} {t['ism']:<12} {t['ball']:<6}")


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Bubble Sort (Oson):
  [5, 1, 4, 2, 8] massivini Bubble Sort bilan saralang.
  Har bir o'tishni ekranga chiqaring.
  Nechta almashtirish bo'lganini sanang.

TOPSHIRIQ 2 — Quick Sort (O'rta):
  Quick sort yordamida strings ro'yxatini alifbo tartibida saralang:
    ["banana", "apple", "mango", "cherry", "grape"]

TOPSHIRIQ 3 — Merge Sort (O'rta):
  Ikki tartiblangan ro'yxatni birlashtiring va natijasi ham
  tartiblangan bo'lsin (merge() funksiyasini alohida yozing):
    [1, 3, 5, 7] va [2, 4, 6, 8] → [1, 2, 3, 4, 5, 6, 7, 8]

TOPSHIRIQ 4 — Qiyin:
  Quyidagi strukturani ball bo'yicha saralang (merge sort bilan):
    [{"ism": "Ali", "matematika": 90, "fizika": 85},
     {"ism": "Vali", "matematika": 78, "fizika": 92}, ...]
  Umumiy ball (matematika + fizika) bo'yicha o'sish tartibida.
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ Bubble Sort:
    — Qo'shni elementlarni solishtiradi va almashtiradi
    — O(n²) — katta massivlarda sekin
    — Erta to'xtash optimallashtirishi

✔️ Quick Sort:
    — Pivot tanlab, ikkiga bo'ladi
    — O(n log n) o'rtacha, amalda eng tez
    — Rekursiv algorit, "bo'l va boshqar"

✔️ Merge Sort:
    — Ikkiga bo'ladi, saralaydi, birlashtiradi
    — Har doim O(n log n) — eng barqaror
    — Qo'shimcha xotira talab qiladi

✔️ Taqqoslash va qachon qaysinisini ishlatish
✔️ Python sorted() va sort() — Timsort (Merge + Insertion)
"""