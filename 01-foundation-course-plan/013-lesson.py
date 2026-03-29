# ============================================================
#   DARS 13: Map, Rekursiv Funksiya va *args, **kwargs
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# DARS HAQIDA
# ------------------------------------------------------------

"""
Bu darsda funksiyaga oid chuqurroq mavzular o'rganiladi:
  1. map(), filter(), zip() — funksional dasturlash
  2. Rekursiv funksiya — o'zini chaqiruvchi funksiya
  3. *args va **kwargs — moslashuvchan parametrlar
"""


# ============================================================
# 1. map() — KETMA-KETLIKKA FUNKSIYA QO'LLASH
# ============================================================

"""
map(funksiya, ketma_ketlik)
  — har bir elementga funksiyani qo'llaydi
  — map obyekti qaytaradi → list() bilan listga aylantirish kerak

Sintaksis:
  natija = list(map(funksiya, ketma_ketlik))
"""

# ── Oddiy funksiya bilan ──────────────────────────────────────
def ikki_baravar(x):
    return x * 2

sonlar = [1, 2, 3, 4, 5]
natija = list(map(ikki_baravar, sonlar))
print(natija)    # [2, 4, 6, 8, 10]

# ── Lambda bilan (qisqaroq) ───────────────────────────────────
natija = list(map(lambda x: x ** 2, sonlar))
print(natija)    # [1, 4, 9, 16, 25]

# ── String ro'yxati bilan ─────────────────────────────────────
ismlar = ["ali", "vali", "jasur", "bobur"]
natija = list(map(str.title, ismlar))
print(natija)    # ['Ali', 'Vali', 'Jasur', 'Bobur']

# ── Ikki ketma-ketlik bilan ───────────────────────────────────
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
ko_payt = list(map(lambda x, y: x * y, a, b))
print(ko_payt)   # [10, 40, 90, 160]

# ── Amaliy: Celsius → Fahrenheit ─────────────────────────────
celsius    = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: round(c * 9/5 + 32, 1), celsius))
print(fahrenheit)   # [32.0, 68.0, 98.6, 212.0]

# ── map vs for sikli ─────────────────────────────────────────
"""
For sikli (eski usul):
  natija = []
  for x in sonlar:
      natija.append(x * 2)

map (yangi usul):
  natija = list(map(lambda x: x * 2, sonlar))

Ikkalasi bir xil natija beradi.
map — qisqaroq va tezroq.
"""


# ============================================================
# 2. filter() — FILTRLASH
# ============================================================

"""
filter(funksiya, ketma_ketlik)
  — funksiya True qaytargan elementlarni oladi
  — filter obyekti qaytaradi → list() kerak
"""

sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Juft sonlar:
juftlar = list(filter(lambda x: x % 2 == 0, sonlar))
print(juftlar)    # [2, 4, 6, 8, 10]

# 5 dan katta:
kattalar = list(filter(lambda x: x > 5, sonlar))
print(kattalar)   # [6, 7, 8, 9, 10]

# ── Funksiya bilan ────────────────────────────────────────────
def musbat_mi(son):
    return son > 0

sonlar2 = [-3, -1, 0, 2, 4, -5, 7]
musbatlar = list(filter(musbat_mi, sonlar2))
print(musbatlar)   # [2, 4, 7]

# ── String filtrlash ──────────────────────────────────────────
so_zlar = ["Python", "Java", "C++", "Kotlin", "Go", "Rust"]
uzun    = list(filter(lambda s: len(s) > 4, so_zlar))
print(uzun)    # ['Python', 'Kotlin']

# ── map + filter birga ───────────────────────────────────────
# Juft sonlarning kvadratini oling:
sonlar = range(1, 11)
natija = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, sonlar)))
print(natija)   # [4, 16, 36, 64, 100]


# ============================================================
# 3. zip() — IKKI KETMA-KETLIKNI BIRLASHTIRISH
# ============================================================

"""
zip(ketma_ketlik1, ketma_ketlik2, ...)
  — har bir pozitsiyadagi elementlarni tuple qilib birlashtiradi
  — eng qisqa ketma-ketlik uzunligi bilan cheklanadi
"""

ismlar = ["Ali", "Vali", "Jasur"]
baholar = [87, 92, 78]

juft = list(zip(ismlar, baholar))
print(juft)   # [('Ali', 87), ('Vali', 92), ('Jasur', 78)]

# Dictionary yaratish:
ma_lumot = dict(zip(ismlar, baholar))
print(ma_lumot)   # {'Ali': 87, 'Vali': 92, 'Jasur': 78}

# for bilan:
for ism, baho in zip(ismlar, baholar):
    print(f"{ism:10} : {baho}")

# ── Uch ketma-ketlik ──────────────────────────────────────────
ismlar  = ["Ali", "Vali", "Jasur"]
yoshlar = [15, 22, 18]
shaharlar = ["Toshkent", "Samarqand", "Buxoro"]

for ism, yosh, shahar in zip(ismlar, yoshlar, shaharlar):
    print(f"{ism} ({yosh} yosh) — {shahar}")


# ============================================================
# 4. REKURSIV FUNKSIYA
# ============================================================

"""
Rekursiya — funksiyaning o'ZI O'ZINI chaqirishi.

Har bir rekursiv funksiyada ALBATTA ikki qism bo'lishi kerak:
  1. Baza holat (Base case)  — rekursiya qachon TUGAYDI
  2. Rekursiv qo'ng'iroq     — funksiya o'zini chaqiradi

Baza holat bo'lmasa — cheksiz tsikl → XATO (RecursionError)!
"""

# ── MISOL 1: Hisobga sanash ───────────────────────────────────
def sanash(n):
    if n == 0:        # Baza holat
        print("Tayyor!")
        return
    print(n)
    sanash(n - 1)     # Rekursiv chaqiruv (n kamayib boradi)

sanash(5)
# 5
# 4
# 3
# 2
# 1
# Tayyor!

# ── MISOL 2: Faktorial ────────────────────────────────────────
"""
5! = 5 × 4 × 3 × 2 × 1 = 120

Rekursiv formula:
  n! = n × (n-1)!
  0! = 1  (baza holat)
"""

def faktorial(n):
    if n == 0 or n == 1:    # Baza holat
        return 1
    return n * faktorial(n - 1)   # Rekursiv chaqiruv

print(faktorial(0))    # 1
print(faktorial(1))    # 1
print(faktorial(5))    # 120
print(faktorial(10))   # 3628800

# Qanday ishlaydi:
# faktorial(5) = 5 * faktorial(4)
#                    4 * faktorial(3)
#                        3 * faktorial(2)
#                            2 * faktorial(1)
#                                1  ← baza holat
# = 5 * 4 * 3 * 2 * 1 = 120

# ── MISOL 3: Fibonacci ketma-ketligi ─────────────────────────
"""
Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
Har son = oldingi ikkita sonning yig'indisi

F(0) = 0  (baza holat)
F(1) = 1  (baza holat)
F(n) = F(n-1) + F(n-2)
"""

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")
print()
# 0 1 1 2 3 5 8 13 21 34

# ── MISOL 4: Raqamlar yig'indisi ──────────────────────────────
"""
12345 → 1 + 2 + 3 + 4 + 5 = 15
"""

def raqamlar_yig_indisi(n):
    if n < 10:          # Baza holat: bir xonali son
        return n
    return n % 10 + raqamlar_yig_indisi(n // 10)

print(raqamlar_yig_indisi(12345))   # 15
print(raqamlar_yig_indisi(9999))    # 36

# ── MISOL 5: Quvvat hisoblash ────────────────────────────────
"""
2^8 = 2 * 2^7 = 2 * 2 * 2^6 = ... = 256
"""

def quvvat(asos, daraja):
    if daraja == 0:          # Baza holat
        return 1
    return asos * quvvat(asos, daraja - 1)

print(quvvat(2, 8))    # 256
print(quvvat(3, 4))    # 81
print(quvvat(5, 0))    # 1

# ── Rekursiya vs Tsikl ────────────────────────────────────────
"""
REKURSIYA:
  ✔️ Kodi qisqa va chiroyli
  ✔️ Ayrim masalalar uchun tabiiy (daraxt, Fibonacci)
  ✗  Ko'p xotira ishlatadi
  ✗  Juda chuqur bo'lsa xato beradi (max ~1000)

TSIKL:
  ✔️ Tezroq va kam xotira
  ✔️ Cheksiz chuqurlik
  ✗  Ba'zan kod murakkab ko'rinadi
"""


# ============================================================
# 5. *args — NOMA'LUM MIQDORDAGI ARGUMENTLAR (chuqurroq)
# ============================================================

"""
*args — funksiyaga istalgancha pozitsion argument berish.
Funksiya ichida args = TUPLE ko'rinishida keladi.

Nomi muhim emas (args o'rniga xohlagan nom ishlatish mumkin),
lekin * belgisi muhim.
"""

# ── Asosiy ───────────────────────────────────────────────────
def hammani_chiqar(*args):
    print(f"Berilgan argumentlar: {args}")
    print(f"Turi: {type(args)}")
    for i, arg in enumerate(args, 1):
        print(f"  {i}. {arg}")

hammani_chiqar("salom", 42, True, 3.14)
# Berilgan argumentlar: ('salom', 42, True, 3.14)
# Turi: <class 'tuple'>

# ── Matematik funksiyalar ─────────────────────────────────────
def yig_indi(*sonlar):
    return sum(sonlar)

def ko_paytma(*sonlar):
    natija = 1
    for s in sonlar:
        natija *= s
    return natija

def statistika(*sonlar):
    return {
        "soni"    : len(sonlar),
        "yig'indi": sum(sonlar),
        "o'rtacha": round(sum(sonlar) / len(sonlar), 2),
        "max"     : max(sonlar),
        "min"     : min(sonlar),
    }

print(yig_indi(1, 2, 3, 4, 5))         # 15
print(ko_paytma(2, 3, 4))               # 24
print(statistika(10, 20, 30, 40, 50))   # to'liq statistika

# ── Oddiy parametr + *args ────────────────────────────────────
def xabar_yubor(kimga, *mazmun):
    print(f"Kimga: {kimga}")
    for qism in mazmun:
        print(f"  {qism}")

xabar_yubor("Ali", "Salom!", "Qalaysan?", "Ko'rishgunga qadar.")


# ============================================================
# 6. **kwargs — NOMA'LUM KALIT-QIYMAT ARGUMENTLAR (chuqurroq)
# ============================================================

"""
**kwargs — funksiyaga istalgancha kalit=qiymat argument berish.
Funksiya ichida kwargs = DICTIONARY ko'rinishida keladi.
"""

# ── Asosiy ───────────────────────────────────────────────────
def profile(**kwargs):
    print(f"Berilgan kwargs: {kwargs}")
    print(f"Turi: {type(kwargs)}")
    for kalit, qiymat in kwargs.items():
        print(f"  {kalit:12} = {qiymat}")

profile(ism="Ali", yosh=15, shahar="Toshkent", kasb="O'quvchi")

# ── HTML teg yaratuvchi funksiya ──────────────────────────────
def html_teg(teg, mazmun, **atributlar):
    attr_str = ""
    for k, v in atributlar.items():
        attr_str += f' {k}="{v}"'
    return f"<{teg}{attr_str}>{mazmun}</{teg}>"

print(html_teg("p", "Salom dunyo!"))
# <p>Salom dunyo!</p>

print(html_teg("a", "Bosing", href="https://python.org", target="_blank"))
# <a href="https://python.org" target="_blank">Bosing</a>

print(html_teg("input", "", type="text", placeholder="Ismingiz"))
# <input type="text" placeholder="Ismingiz"></input>

# ── *args va **kwargs birga ───────────────────────────────────
def super_funksiya(*args, **kwargs):
    print(f"\nargs   ({len(args)} ta)  : {args}")
    print(f"kwargs ({len(kwargs)} ta) : {kwargs}")

super_funksiya(1, 2, 3, ism="Ali", yosh=15, shahar="Toshkent")


# ============================================================
# AMALIY DASTUR — Hisobot generatori
# ============================================================

def hisobot(*talabalar, **sozlamalar):
    """
    talabalar  — (ism, ball) juftliklari
    sozlamalar — chegara, sarlavha
    """
    chegara  = sozlamalar.get("chegara", 50)
    sarlavha = sozlamalar.get("sarlavha", "TALABALAR HISOBOTI")

    print(f"\n{'=' * 45}")
    print(f"{sarlavha:^45}")
    print(f"{'=' * 45}")

    otdi  = 0
    otmadi = 0

    for talaba in talabalar:
        ism, ball = talaba
        holat = "✓ O'tdi" if ball >= chegara else "✗ O'tmadi"
        print(f"  {ism:<15} {ball:>4} ball   {holat}")

        if ball >= chegara:
            otdi += 1
        else:
            otmadi += 1

    print(f"{'─' * 45}")
    print(f"  Jami: {len(talabalar)} ta | O'tdi: {otdi} | O'tmadi: {otmadi}")
    print(f"{'=' * 45}")


hisobot(
    ("Ali Karimov",   87),
    ("Vali Rahimov",  45),
    ("Jasur Toshev",  92),
    ("Nodir Aliyev",  63),
    ("Bobur Hasanov",  38),
    sarlavha="9-A SINF MATEMATIKA IMTIHONI",
    chegara=60
)


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — map va filter (O'rta):
  sonlar = list(range(1, 21))
  a) map bilan har bir sonni 3 ga ko'paytiring
  b) filter bilan 3 ga bo'linadigan sonlarni oling
  c) zip bilan sonlar va ularning kvadratlarini juftlashtiring
     va dictionary ga aylantiring

TOPSHIRIQ 2 — Rekursiya (O'rta):
  Quyidagi rekursiv funksiyalarni yozing:
    a) countdown(n) — n dan 1 gacha sanab chiqadigan funksiya
    b) juft_yig'indi(n) — 0 dan n gacha juft sonlar yig'indisi
    c) palindrom(so'z) — so'z palindrom ekanini rekursiv tekshirish

TOPSHIRIQ 3 — *args (O'rta):
  Quyidagi funksiyalarni yozing:
    a) o'rtacha(*sonlar) — istalgancha sonning o'rtachasini qaytaradi
    b) eng_uzun(*so'zlar) — eng uzun so'zni qaytaradi
    c) filtr(*sonlar, chegara) — chegara dan katta sonlarni qaytaradi

TOPSHIRIQ 4 — **kwargs (Qiyin):
  talaba_qo'sh(**ma'lumot) funksiyasini yozing:
    - ism va ball MAJBURIY (agar yo'q bo'lsa — xabar bering)
    - sinf ixtiyoriy (default: "Noma'lum")
    - email ixtiyoriy
    - Barcha ma'lumotni chiroyli formatda chiqaring

TOPSHIRIQ 5 — Hammasi birgalikda (Qiyin):
  Mahsulot katalogi dasturi:
    - mahsulot_qo'sh(nom, narx, **xususiyatlar) funksiyasi
    - katalog = [] ga qo'shilsin
    - qidirish(katalog, **filtrlar) — narx, kategori bo'yicha filtr
    - hisobot(katalog) — jami, o'rtacha narx chiqarsin
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ map(f, lst)    — har elementga funksiya qo'llash
✔️ filter(f, lst) — shartga mos elementlarni olish
✔️ zip(a, b)      — ikki ketma-ketlikni birlashtirish
✔️ Rekursiya nima:
    - Baza holat (to'xtash sharti)
    - Rekursiv chaqiruv
✔️ Rekursiv misollar:
    - sanash(n)
    - faktorial(n)
    - fibonacci(n)
    - raqamlar_yig'indisi(n)
    - quvvat(asos, daraja)
✔️ *args   — noma'lum miqdor pozitsion arg → tuple
✔️ **kwargs — noma'lum miqdor kalit-qiymat → dict
✔️ *args va **kwargs birga ishlatish
"""