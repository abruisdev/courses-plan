# ============================================================
#   DARS 23: Algoritmlash — Search (Qidirish)
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# DARS HAQIDA
# ------------------------------------------------------------

"""
Algoritm — muammoni hal qilish uchun aniq ketma-ket qadamlar.

Bugun ikki xil qidirish algoritmini o'rganamiz:

  1️⃣  Linear Search  (Chiziqli qidirish)
  2️⃣  Binary Search  (Ikkilik qidirish)

Nima uchun muhim?
  - Interview savollarida tez-tez uchraydi
  - Samarali dastur yozish uchun zarur
  - Katta ma'lumotlarda tezlik farqi juda katta!

Vaqt murakkabligi (Time Complexity):
  Linear Search  → O(n)        — eng yomoni n ta tekshiruv
  Binary Search  → O(log n)    — eng yomoni log₂(n) ta tekshiruv

  Misol: 1 million elementli massiv
  Linear Search  → 1,000,000 ta tekshiruv
  Binary Search  →        20 ta tekshiruv (2^20 = 1,048,576)
"""


# ============================================================
#   1. LINEAR SEARCH — Chiziqli qidirish
# ============================================================

# ------------------------------------------------------------
# NAZARIYA
# ------------------------------------------------------------

"""
Linear Search — eng oddiy qidirish algoritmi.

Ishlash tartibi:
  1. Ro'yxatning BIRINCHI elementidan boshla
  2. Har bir elementni MAQSAD bilan solishtir
  3. Topilsa → indeksni qaytariladi
  4. Topilmasa → keyingisiga o'tadi
  5. Oxirigacha topilmasa → -1 qaytariladi

Xususiyatlari:
  ✔️ Tartiblangan bo'lishi SHART EMAS
  ✔️ Har qanday ma'lumot turi bilan ishlaydi
  ✔️ Kichik massivlar uchun yaxshi
  ✗ Katta massivlarda SEKIN (O(n))
"""

print("=" * 55)
print("    1. LINEAR SEARCH — Chiziqli qidirish")
print("=" * 55)

# ── Asosiy Linear Search ──────────────────────────────────────
def linear_search(arr, maqsad):
    """
    Ro'yxatdan maqsadni qidiradi.
    Topilsa: indeks raqamini qaytaradi
    Topilmasa: -1 qaytaradi
    """
    for i in range(len(arr)):
        if arr[i] == maqsad:
            return i        # topildi — indeksni qaytaradi
    return -1               # topilmadi


# Test:
sonlar = [64, 34, 25, 12, 22, 11, 90]
print(f"\nMassiv: {sonlar}")

maqsad = 22
natija = linear_search(sonlar, maqsad)
if natija != -1:
    print(f"✓ {maqsad} topildi — {natija}-indeksda")
else:
    print(f"✗ {maqsad} topilmadi")

# Topilmaydigan son:
maqsad2 = 99
natija2 = linear_search(sonlar, maqsad2)
if natija2 != -1:
    print(f"✓ {maqsad2} topildi — {natija2}-indeksda")
else:
    print(f"✗ {maqsad2} topilmadi")


# ── Qidiruv jarayonini ko'rsatuvchi versiya ───────────────────
print("\n--- Qidiruv jarayoni ---")

def linear_search_batafsil(arr, maqsad):
    """Har bir qadamni ko'rsatadi"""
    print(f"Qidirilyapti: {maqsad}")
    print(f"Massiv: {arr}")
    print()
    for i in range(len(arr)):
        print(f"  Qadam {i+1}: arr[{i}] = {arr[i]}", end="")
        if arr[i] == maqsad:
            print(f"  ← TOPILDI! ✓")
            return i
        else:
            print(f"  ≠ {maqsad}")
    print(f"\n  Topilmadi ✗")
    return -1

linear_search_batafsil([5, 3, 8, 1, 9, 2], 9)


# ── String ro'yxatida qidirish ────────────────────────────────
print("\n--- String ro'yxatida ---")

def ism_qidirish(ismlar, maqsad):
    for i, ism in enumerate(ismlar):
        if ism.lower() == maqsad.lower():   # katta/kichik harfsiz
            return i
    return -1

ismlar = ["Ali", "Vali", "Jasur", "Bobur", "Nodir"]
print(f"Ro'yxat: {ismlar}")

for qidirilayotgan in ["Jasur", "VALI", "Zafar"]:
    idx = ism_qidirishing = ism_qidirish(ismlar, qidirilayotgan)
    if idx != -1:
        print(f"  '{qidirilayotgan}' → topildi ({idx}-indeks)")
    else:
        print(f"  '{qidirilayotgan}' → topilmadi")


# ── Barcha uchrashuv joylarini topish ─────────────────────────
print("\n--- Barcha uchrashuvlar ---")

def barcha_joylar(arr, maqsad):
    """Elementning barcha indekslarini qaytaradi"""
    joylar = []
    for i in range(len(arr)):
        if arr[i] == maqsad:
            joylar.append(i)
    return joylar

arr = [3, 1, 4, 1, 5, 9, 2, 6, 1, 3]
print(f"Massiv: {arr}")
print(f"1 ning joylari: {barcha_joylar(arr, 1)}")   # [1, 3, 8]
print(f"3 ning joylari: {barcha_joylar(arr, 3)}")   # [0, 9]


# ============================================================
#   2. BINARY SEARCH — Ikkilik qidirish
# ============================================================

# ------------------------------------------------------------
# NAZARIYA
# ------------------------------------------------------------

"""
Binary Search — tartiblangan massivda tez qidirishning eng samarali usuli.

Ishlash tartibi (telefon kitobidan qidirish kabi):
  1. O'RTADAGI elementni tanlang
  2. Maqsad > o'rta → O'NG yarmiga o'ting
  3. Maqsad < o'rta → CHAP yarmiga o'ting
  4. Maqsad == o'rta → TOPILDI!
  5. Massiv qolmasa → TOPILMADI

MUHIM SHART: Massiv TARTIBLANGAN bo'lishi SHART!

Misol: [1, 3, 5, 7, 9, 11, 13, 15] da 11 ni qidirish
  1-qadam: o'rta = arr[4] = 9,   11 > 9  → o'ng
  2-qadam: o'rta = arr[6] = 13,  11 < 13 → chap
  3-qadam: o'rta = arr[5] = 11,  11 == 11 → TOPILDI! ✓
  Faqat 3 ta tekshiruv (8 ta elementda)!
"""

print("\n" + "=" * 55)
print("    2. BINARY SEARCH — Ikkilik qidirish")
print("=" * 55)


# ── Iterativ Binary Search ────────────────────────────────────
def binary_search(arr, maqsad):
    """
    Tartiblangan massivda binary search.
    Topilsa: indeks qaytaradi
    Topilmasa: -1 qaytaradi
    """
    chap  = 0
    ong   = len(arr) - 1

    while chap <= ong:
        orta = (chap + ong) // 2        # o'rta indeks

        if arr[orta] == maqsad:
            return orta                  # topildi!
        elif arr[orta] < maqsad:
            chap = orta + 1             # o'ng yarmiga o't
        else:
            ong = orta - 1              # chap yarmiga o't

    return -1                           # topilmadi


# Test:
tartiblangan = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"\nTartiblangan massiv: {tartiblangan}")

for maqsad in [11, 1, 19, 8]:
    idx = binary_search(tartiblangan, maqsad)
    if idx != -1:
        print(f"  {maqsad} → topildi ({idx}-indeksda)")
    else:
        print(f"  {maqsad} → topilmadi")


# ── Binary Search jarayonini ko'rsatuvchi versiya ─────────────
print("\n--- Binary Search jarayoni ---")

def binary_search_batafsil(arr, maqsad):
    """Har bir qadamni ko'rsatadi"""
    chap, ong = 0, len(arr) - 1
    qadam = 0
    print(f"Qidirilyapti: {maqsad}")
    print(f"Massiv: {arr}\n")

    while chap <= ong:
        qadam += 1
        orta = (chap + ong) // 2
        print(f"  Qadam {qadam}: chap={chap}, ong={ong}, orta={orta}, arr[{orta}]={arr[orta]}")

        if arr[orta] == maqsad:
            print(f"  ✓ TOPILDI! {maqsad} → {orta}-indeksda ({qadam} ta qadam)")
            return orta
        elif arr[orta] < maqsad:
            print(f"    {arr[orta]} < {maqsad} → o'ng yarmiga o'tamiz")
            chap = orta + 1
        else:
            print(f"    {arr[orta]} > {maqsad} → chap yarmiga o'tamiz")
            ong = orta - 1

    print(f"  ✗ Topilmadi ({qadam} ta qadam)")
    return -1

binary_search_batafsil([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 13)


# ── Rekursiv Binary Search ────────────────────────────────────
print("\n--- Rekursiv Binary Search ---")

def binary_search_rekursiv(arr, maqsad, chap=0, ong=None):
    """Rekursiv usuldagi binary search"""
    if ong is None:
        ong = len(arr) - 1

    # Baza holat: massiv qolmadi
    if chap > ong:
        return -1

    orta = (chap + ong) // 2

    if arr[orta] == maqsad:
        return orta
    elif arr[orta] < maqsad:
        return binary_search_rekursiv(arr, maqsad, orta + 1, ong)
    else:
        return binary_search_rekursiv(arr, maqsad, chap, orta - 1)


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(f"Massiv: {arr}")
print(f"14 → indeks: {binary_search_rekursiv(arr, 14)}")   # 6
print(f"7  → indeks: {binary_search_rekursiv(arr, 7)}")    # -1


# ============================================================
# LINEAR vs BINARY: TAQQOSLASH
# ============================================================

print("\n" + "=" * 55)
print("    LINEAR vs BINARY: Tezlik taqqoslash")
print("=" * 55)

import time
import random

def tezlik_sinoyi(n):
    """n ta elementli massivda tezlikni o'lchaydi"""
    arr = sorted(random.sample(range(n * 10), n))
    maqsad = random.choice(arr)

    # Linear search
    t1 = time.perf_counter()
    for _ in range(1000):
        linear_search(arr, maqsad)
    linear_vaqt = (time.perf_counter() - t1) / 1000

    # Binary search
    t2 = time.perf_counter()
    for _ in range(1000):
        binary_search(arr, maqsad)
    binary_vaqt = (time.perf_counter() - t2) / 1000

    print(f"\nn = {n:,} element:")
    print(f"  Linear Search : {linear_vaqt:.8f} soniya")
    print(f"  Binary Search : {binary_vaqt:.8f} soniya")
    if linear_vaqt > 0:
        print(f"  Binary {linear_vaqt/binary_vaqt:.0f}x marta tezroq!")

tezlik_sinoyi(1000)
tezlik_sinoyi(10000)
tezlik_sinoyi(100000)

# ── Nazariy taqqoslash ────────────────────────────────────────
print("""
┌─────────────────────────────────────────────────────────┐
│              TAQQOSLASH JADVALI                         │
├──────────────────┬──────────────────┬───────────────────┤
│ Xususiyat        │  Linear Search   │  Binary Search    │
├──────────────────┼──────────────────┼───────────────────┤
│ Vaqt murakkabligi│  O(n)            │  O(log n)         │
│ Tartib talabi    │  Shart emas      │  TARTIBLANGAN!    │
│ Kichik massiv    │  Yaxshi          │  Yaxshi           │
│ Katta massiv     │  Sekin           │  Juda tez         │
│ Amalga oshirish  │  Oson            │  O'rta            │
├──────────────────┼──────────────────┼───────────────────┤
│ 100 element      │  100 ta tekshiruv│  7 ta tekshiruv   │
│ 1000 element     │  1000 ta         │  10 ta            │
│ 1,000,000 element│  1,000,000 ta    │  20 ta            │
└──────────────────┴──────────────────┴───────────────────┘
""")


# ============================================================
# AMALIY DASTUR — Lug'at qidiruvi
# ============================================================

print("=== LEKSIKON QIDIRISH ===")

lug_at = sorted([
    "algoritm", "massiv", "funksiya", "sikl", "o'zgaruvchi",
    "sinf", "metod", "rekursiya", "saralash", "qidirish",
    "stack", "navbat", "daraxt", "bog'lamli", "ro'yxat"
])

print(f"Lug'at: {lug_at}\n")

def lug_at_qidirish(lug_at, so_z):
    """Binary search yordamida lug'atdan qidirish"""
    idx = binary_search(lug_at, so_z)
    if idx != -1:
        print(f"✓ '{so_z}' lug'atda bor ({idx}-tartib)")
    else:
        print(f"✗ '{so_z}' lug'atda yo'q")

lug_at_qidirish(lug_at, "massiv")
lug_at_qidirish(lug_at, "rekursiya")
lug_at_qidirish(lug_at, "python")


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Linear Search (Oson):
  Ro'yxatda eng katta va eng kichik elementni
  LINEAR SEARCH yordamida (max(), min() ishlatmasdan) toping.

TOPSHIRIQ 2 — Linear Search (O'rta):
  Talabalar ro'yxati:
    [{"ism": "Ali", "ball": 87}, {"ism": "Vali", "ball": 92}, ...]
  a) Ism bo'yicha linear search qiling
  b) Ball bo'yicha 90+ olganlarni linear search bilan toping

TOPSHIRIQ 3 — Binary Search (O'rta):
  Tartiblangan ro'yxatda birinchi va oxirgi uchrash joyini toping:
    arr = [1, 2, 2, 2, 3, 4, 4, 5]
    2-ning birinchi joyi: 1
    2-ning oxirgi joyi: 3

TOPSHIRIQ 4 — Qiyin:
  "Telefon kitobi" dasturi:
  - Kontaktlar tartiblangan bo'lsin (ismga ko'ra)
  - Yangi kontakt qo'shganda tartibini saqlasin
  - Binary search bilan qidirsin
  - Qancha qadam ketganini ko'rsatsin
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ Algoritm nima va nima uchun muhim
✔️ Vaqt murakkabligi — O(n) va O(log n)

LINEAR SEARCH:
  ✔️ Tartiblangan bo'lishi shart emas
  ✔️ Boshlangichdan oxirigacha tekshiradi
  ✔️ O(n) — katta massivlarda sekin

BINARY SEARCH:
  ✔️ Massiv TARTIBLANGAN bo'lishi shart
  ✔️ Har qadamda yarmini kesib tashlaydi
  ✔️ O(log n) — katta massivlarda juda tez
  ✔️ Iterativ va rekursiv usullarda yozish
  ✔️ 1 million elementda faqat 20 ta qadam!
"""