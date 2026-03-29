# ============================================================
#   DARS 20: Pythonda Dunder Metodlar
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# DUNDER METODLAR NIMA?
# ------------------------------------------------------------

"""
Dunder = Double UNDERscore = __metod__
"Magic methods" yoki "Special methods" ham deyiladi.

Python'da ba'zi operatorlar (+, -, *, ==, <, print va h.k.)
aslida maxsus metodlarni chaqiradi.

Masalan:
  a + b            →  a.__add__(b)
  print(a)         →  a.__str__()
  len(a)           →  a.__len__()
  a == b           →  a.__eq__(b)
  a[0]             →  a.__getitem__(0)

Bu metodlarni O'ZIMiz yozib, operator xatti-harakatini
o'zgartira olamiz.

Asosiy dunder metodlar:
  __init__    — konstruktor (ob'ekt yaratish)
  __str__     — print() ko'rinishi
  __repr__    — developer ko'rinishi
  __len__     — len() funksiyasi
  __add__     — + operatori
  __sub__     — - operatori
  __mul__     — * operatori
  __truediv__ — / operatori
  __pow__     — ** operatori
  __eq__      — == operatori
  __ne__      — != operatori
  __lt__      — < operatori
  __le__      — <= operatori
  __gt__      — > operatori
  __ge__      — >= operatori
  __contains__— in operatori
  __getitem__ — [] operatori
  __setitem__ — []= operatori
  __call__    — () operatori (ob'ektni funksiya kabi chaqirish)
  __iter__    — for sikli
  __next__    — keyingi element
"""


# ============================================================
# __str__ va __repr__
# ============================================================

"""
__str__  — foydalanuvchi uchun (print() ga chiqadi)
__repr__ — developer uchun (interaktiv konsolda, debugging)

Agar __str__ yo'q bo'lsa, Python __repr__ ni ishlatadi.
"""

class Nuqta:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Nuqta({self.x}, {self.y})"

    def __repr__(self):
        return f"Nuqta(x={self.x}, y={self.y})"


n = Nuqta(3, 5)
print(n)           # Nuqta(3, 5)   — __str__ chaqiriladi
print(repr(n))     # Nuqta(x=3, y=5) — __repr__ chaqiriladi
print([n])         # [Nuqta(x=3, y=5)] — list ichida __repr__


# ============================================================
# __len__ — len() FUNKSIYASI
# ============================================================

class Jamoa:
    def __init__(self, nom):
        self.nom    = nom
        self.azolar = []

    def qo_sh(self, azo):
        self.azolar.append(azo)

    def __len__(self):
        return len(self.azolar)

    def __str__(self):
        return f"{self.nom} ({len(self)} a'zo)"


j = Jamoa("Python Developers")
j.qo_sh("Ali")
j.qo_sh("Vali")
j.qo_sh("Jasur")

print(len(j))   # 3  — __len__ chaqiriladi
print(j)        # Python Developers (3 a'zo)


# ============================================================
# ARIFMETIK DUNDER METODLAR
# ============================================================

# ── __add__() — + operatori ───────────────────────────────────
"""
a + b  →  a.__add__(b) chaqiriladi
"""

class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vektor({self.x}, {self.y})"

    def __repr__(self):
        return f"Vektor({self.x}, {self.y})"

    def __add__(self, other):
        return Vektor(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vektor(self.x - other.x, self.y - other.y)

    def __mul__(self, skalyar):
        # Vektor * son
        return Vektor(self.x * skalyar, self.y * skalyar)

    def __rmul__(self, skalyar):
        # son * Vektor  (teskari tartib)
        return self.__mul__(skalyar)

    def __pow__(self, daraja, module=None):
        # Vektor ** n — har koordinatani n darajaga ko'taradi
        return Vektor(self.x ** daraja, self.y ** daraja)

    def uzunlik(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)


v1 = Vektor(1, 2)
v2 = Vektor(3, 4)

print(v1 + v2)      # Vektor(4, 6)   — __add__ chaqiriladi
print(v1 - v2)      # Vektor(-2, -2) — __sub__ chaqiriladi
print(v1 * 3)       # Vektor(3, 6)   — __mul__ chaqiriladi
print(3 * v1)       # Vektor(3, 6)   — __rmul__ chaqiriladi
print(v1 ** 2)      # Vektor(1, 4)   — __pow__ chaqiriladi
print(f"Uzunlik: {v2.uzunlik():.2f}")    # 5.00


# ============================================================
# TAQQOSLASH DUNDER METODLAR
# ============================================================

"""
__eq__  — ==
__ne__  — !=
__lt__  — <
__le__  — <=
__gt__  — >
__ge__  — >=
"""

class Talaba:
    def __init__(self, ism, ball):
        self.ism  = ism
        self.ball = ball

    def __str__(self):
        return f"{self.ism} ({self.ball})"

    def __eq__(self, other):
        return self.ball == other.ball

    def __ne__(self, other):
        return self.ball != other.ball

    def __lt__(self, other):
        return self.ball < other.ball

    def __le__(self, other):
        return self.ball <= other.ball

    def __gt__(self, other):
        return self.ball > other.ball

    def __ge__(self, other):
        return self.ball >= other.ball


t1 = Talaba("Ali",  85)
t2 = Talaba("Vali", 92)
t3 = Talaba("Jasur", 85)

print(t1 == t3)    # True   (ikkalasi 85)
print(t1 == t2)    # False
print(t1 < t2)     # True   (85 < 92)
print(t2 > t1)     # True
print(t1 >= t3)    # True   (85 >= 85)

# sorted() bilan ishlaydi (__lt__ yetarli):
talabalar = [t2, t1, t3, Talaba("Bobur", 78)]
saralangan = sorted(talabalar)
for t in saralangan:
    print(t)
# Bobur (78)
# Ali (85)
# Jasur (85)
# Vali (92)


# ============================================================
# __contains__ — in OPERATORI
# ============================================================

class Sinf:
    def __init__(self):
        self.o_quvchilar = []

    def qo_sh(self, ism):
        self.o_quvchilar.append(ism)

    def __contains__(self, ism):
        return ism in self.o_quvchilar

    def __len__(self):
        return len(self.o_quvchilar)


sinf = Sinf()
sinf.qo_sh("Ali")
sinf.qo_sh("Vali")
sinf.qo_sh("Jasur")

print("Ali" in sinf)      # True   — __contains__ chaqiriladi
print("Nodir" in sinf)    # False
print(f"O'quvchilar soni: {len(sinf)}")   # 3


# ============================================================
# __getitem__ va __setitem__ — [] OPERATORI
# ============================================================

"""
__getitem__(self, indeks)     — ob'ekt[indeks] o'qish
__setitem__(self, indeks, val)— ob'ekt[indeks] = qiymat
"""

class Matritsa:
    def __init__(self, qatorlar, ustunlar):
        self.q = qatorlar
        self.u = ustunlar
        self.data = [[0] * ustunlar for _ in range(qatorlar)]

    def __getitem__(self, key):
        qator, ustun = key
        return self.data[qator][ustun]

    def __setitem__(self, key, qiymat):
        qator, ustun = key
        self.data[qator][ustun] = qiymat

    def __str__(self):
        return '\n'.join(str(q) for q in self.data)


m = Matritsa(3, 3)
m[0, 0] = 1    # __setitem__
m[1, 1] = 5
m[2, 2] = 9
print(m[1, 1])  # 5  — __getitem__
print(m)
# [1, 0, 0]
# [0, 5, 0]
# [0, 0, 9]


# ============================================================
# __call__ — OB'EKTNI FUNKSIYA KABI CHAQIRISH
# ============================================================

"""
__call__ — ob'ektni funksiya kabi chaqirish imkonini beradi.
ob'ekt()  →  ob'ekt.__call__() chaqiriladi
"""

class Hisoblagich:
    def __init__(self):
        self.hisob = 0

    def __call__(self, qadam=1):
        self.hisob += qadam
        return self.hisob

    def __str__(self):
        return f"Hisob: {self.hisob}"


h = Hisoblagich()
print(h())      # 1  — ob'ektni funksiya kabi chaqirish
print(h())      # 2
print(h(5))     # 7
print(h)        # Hisob: 7

# ── Kuchaytirgich funksiya ────────────────────────────────────
class Kuchaytir:
    def __init__(self, daraja):
        self.daraja = daraja

    def __call__(self, son):
        return son ** self.daraja


kvadrat = Kuchaytir(2)
kub     = Kuchaytir(3)

print(kvadrat(5))    # 25
print(kub(3))        # 27
print(list(map(kvadrat, range(1, 6))))    # [1, 4, 9, 16, 25]


# ============================================================
# __iter__ va __next__ — FOR SIKLI
# ============================================================

"""
__iter__ — ob'ektni iteratsiya qilish imkonini beradi
__next__ — keyingi elementni beradi
StopIteration — tugashini bildiradi
"""

class Hisoblash:
    def __init__(self, boshlash, tugash):
        self.joriy  = boshlash
        self.tugash = tugash

    def __iter__(self):
        return self   # o'zini qaytaradi

    def __next__(self):
        if self.joriy > self.tugash:
            raise StopIteration    # for sikli tugaydi
        qiymat = self.joriy
        self.joriy += 1
        return qiymat


# for sikli bilan:
for son in Hisoblash(1, 5):
    print(son, end=" ")   # 1 2 3 4 5
print()

# list() bilan:
print(list(Hisoblash(0, 10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ============================================================
# AMALIY DASTUR — Kasr sinfi
# ============================================================

import math

class Kasr:
    """To'liq ishlovchi kasr sinfi"""

    def __init__(self, surat, maxraj=1):
        if maxraj == 0:
            raise ValueError("Maxraj nol bo'lishi mumkin emas!")
        # Avval manfiy belgini surtatga o'tkaz
        if maxraj < 0:
            surat, maxraj = -surat, -maxraj
        # Qisqaytirish
        ekub = math.gcd(abs(surat), abs(maxraj))
        self.surat  = surat // ekub
        self.maxraj = maxraj // ekub

    def __str__(self):
        if self.maxraj == 1:
            return str(self.surat)
        return f"{self.surat}/{self.maxraj}"

    def __repr__(self):
        return f"Kasr({self.surat}, {self.maxraj})"

    def __add__(self, other):
        yangi_surat  = self.surat * other.maxraj + other.surat * self.maxraj
        yangi_maxraj = self.maxraj * other.maxraj
        return Kasr(yangi_surat, yangi_maxraj)

    def __sub__(self, other):
        yangi_surat  = self.surat * other.maxraj - other.surat * self.maxraj
        yangi_maxraj = self.maxraj * other.maxraj
        return Kasr(yangi_surat, yangi_maxraj)

    def __mul__(self, other):
        return Kasr(self.surat * other.surat, self.maxraj * other.maxraj)

    def __truediv__(self, other):
        return Kasr(self.surat * other.maxraj, self.maxraj * other.surat)

    def __pow__(self, daraja, module=None):
        return Kasr(self.surat ** daraja, self.maxraj ** daraja)

    def __eq__(self, other):
        return self.surat * other.maxraj == other.surat * self.maxraj

    def __lt__(self, other):
        return self.surat * other.maxraj < other.surat * self.maxraj

    def __le__(self, other):
        return self == other or self < other

    def __float__(self):
        return self.surat / self.maxraj


# Test:
a = Kasr(1, 2)    # 1/2
b = Kasr(1, 3)    # 1/3

print(f"{a} + {b} = {a + b}")    # 1/2 + 1/3 = 5/6
print(f"{a} - {b} = {a - b}")    # 1/2 - 1/3 = 1/6
print(f"{a} * {b} = {a * b}")    # 1/2 * 1/3 = 1/6
print(f"{a} / {b} = {a / b}")    # 1/2 / 1/3 = 3/2
print(f"{a} ** 2 = {a ** 2}")    # 1/2 ** 2 = 1/4

print(f"{a} == {b}: {a == b}")   # False
print(f"{a} > {b}: {a > b}")     # True (1/2 > 1/3)

# Decimal qiymat:
print(f"float({a}) = {float(a)}")   # 0.5

# Saralash:
kasrlar = [Kasr(3, 4), Kasr(1, 2), Kasr(2, 3), Kasr(1, 4)]
print(sorted(kasrlar))
# [1/4, 1/2, 2/3, 3/4]


# ------------------------------------------------------------
# DUNDER METODLAR — TO'LIQ JADVAL
# ------------------------------------------------------------

"""
┌──────────────────┬────────────────────────────────────────────┐
│ DUNDER METOD     │ QACHON CHAQIRILADI                         │
├──────────────────┼────────────────────────────────────────────┤
│ __init__         │ ob'ekt = Klass(...)                        │
│ __str__          │ print(ob'ekt), str(ob'ekt)                 │
│ __repr__         │ repr(ob'ekt), interaktiv konsol            │
│ __len__          │ len(ob'ekt)                                │
├──────────────────┼────────────────────────────────────────────┤
│ __add__          │ a + b                                      │
│ __sub__          │ a - b                                      │
│ __mul__          │ a * b                                      │
│ __truediv__      │ a / b                                      │
│ __floordiv__     │ a // b                                     │
│ __mod__          │ a % b                                      │
│ __pow__          │ a ** b                                      │
│ __neg__          │ -a                                         │
│ __abs__          │ abs(a)                                     │
├──────────────────┼────────────────────────────────────────────┤
│ __eq__           │ a == b                                     │
│ __ne__           │ a != b                                     │
│ __lt__           │ a < b                                      │
│ __le__           │ a <= b                                     │
│ __gt__           │ a > b                                      │
│ __ge__           │ a >= b                                     │
├──────────────────┼────────────────────────────────────────────┤
│ __contains__     │ x in ob'ekt                                │
│ __getitem__      │ ob'ekt[key]                                │
│ __setitem__      │ ob'ekt[key] = val                          │
│ __delitem__      │ del ob'ekt[key]                            │
├──────────────────┼────────────────────────────────────────────┤
│ __call__         │ ob'ekt(...)                                │
│ __iter__         │ for x in ob'ekt                            │
│ __next__         │ next(ob'ekt)                               │
│ __bool__         │ bool(ob'ekt), if ob'ekt                    │
│ __float__        │ float(ob'ekt)                              │
│ __int__          │ int(ob'ekt)                                │
└──────────────────┴────────────────────────────────────────────┘
"""


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Asosiy (Oson):
  Temperatura classini yarating:
    - qiymat (Celsius)
    - __str__  — "25°C"
    - __add__  — ikki haroratni qo'shish
    - __sub__  — ayirish
    - __eq__   — teng?
    - __lt__   — kichik?

TOPSHIRIQ 2 — O'rta:
  Stack (stek) classini yarating:
    - __init__  — bo'sh list
    - __len__   — elementlar soni
    - __str__   — chiroyli chiqarish
    - __contains__ — element bormi?
    - push(el)  — qo'shish
    - pop()     — oxirgisini olib chiqarish
    - peek()    — oxirgisini ko'rish (o'chirmasdan)
    - is_empty()— bo'shmi?

TOPSHIRIQ 3 — Qiyin:
  Matritsa classini to'liq yozing:
    - __init__(qatorlar, ustunlar, data=None)
    - __str__    — chiroyli ko'rinish
    - __add__    — matritsa qo'shish
    - __mul__    — skalyar ko'paytirish
    - __eq__     — tenglik
    - __getitem__— m[i, j]
    - transpose()— transponlash
    Qo'shimcha: ikkita matritsa ko'paytmasini hisoblang (__matmul__ yoki metod)
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ Dunder (Magic) metodlar nima
✔️ __str__ va __repr__ farqi
✔️ __len__    — len() uchun
✔️ Arifmetik:
    __add__      — a + b
    __sub__      — a - b
    __mul__      — a * b
    __truediv__  — a / b
    __pow__      — a ** b  (daraja, module=None)
    __rmul__     — b * a (teskari tartib)
✔️ Taqqoslash:
    __eq__, __ne__, __lt__, __le__, __gt__, __ge__
✔️ __contains__ — in operatori
✔️ __getitem__, __setitem__ — [] operatori
✔️ __call__   — ob'ektni funksiya kabi chaqirish
✔️ __iter__, __next__ — for sikli uchun
✔️ Amaliy misol: Kasr sinfi (barcha arifmetik operatorlar)
"""