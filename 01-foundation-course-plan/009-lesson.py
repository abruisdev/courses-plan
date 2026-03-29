# ============================================================
#   DARS 9: Pythonda List (Ro'yxat)
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# LIST NIMA?
# ------------------------------------------------------------

"""
List — bu bir nechta qiymatni ketma-ket saqlovchi to'plam.
Kvadrat qavs [] ichida yoziladi, elementlar vergul bilan ajratiladi.

Kundalik hayotda:
  - Do'kon ro'yxati: ["non", "sut", "tuxum"]
  - Baholar ro'yxati: [85, 90, 78, 92]
  - O'quvchilar: ["Ali", "Vali", "Jasur"]

Xususiyatlari:
  ✔️ Tartibli         — elementlar kiritilgan tartibda saqlanadi
  ✔️ O'zgaruvchan     — elementlarni qo'shish, o'chirish, o'zgartirish mumkin
  ✔️ Takrorlanuvchi   — bir xil qiymat bir necha marta bo'lishi mumkin
  ✔️ Har xil turlar   — str, int, float, bool aralash bo'lishi mumkin
"""

# ── List yaratish ────────────────────────────────────────────
bo_sh      = []                          # bo'sh list
sonlar     = [1, 2, 3, 4, 5]
ismlar     = ["Ali", "Vali", "Jasur"]
aralash    = [1, "Python", 3.14, True]   # har xil turlar
ichma_ich  = [1, [2, 3], [4, 5]]         # list ichida list

print(sonlar)     # [1, 2, 3, 4, 5]
print(ismlar)     # ['Ali', 'Vali', 'Jasur']
print(aralash)    # [1, 'Python', 3.14, True]
print(type(sonlar))   # <class 'list'>


# ============================================================
# ELEMENTLARGA MUROJAAT — INDEKSLASH
# ============================================================

"""
List indeksi 0 dan boshlanadi.
Manfiy indeks ham ishlaydi (-1 = oxirgi element).
"""

mevalar = ["olma", "banan", "uzum", "shaftoli", "nok"]
#            0        1       2        3           4
#           -5       -4      -3       -2          -1

print(mevalar[0])    # olma     — birinchi
print(mevalar[2])    # uzum     — uchinchi
print(mevalar[-1])   # nok      — oxirgi
print(mevalar[-2])   # shaftoli — oxiridan ikkinchi

# ── Slicing — qism olish ─────────────────────────────────────
print(mevalar[1:3])    # ['banan', 'uzum']
print(mevalar[:3])     # ['olma', 'banan', 'uzum']
print(mevalar[2:])     # ['uzum', 'shaftoli', 'nok']
print(mevalar[::-1])   # ['nok', 'shaftoli', 'uzum', 'banan', 'olma']


# ============================================================
# len() va type()
# ============================================================

print(len(mevalar))       # 5  — elementlar soni
print(type(mevalar))      # <class 'list'>

# Bo'sh list tekshirish
ro_yxat = []
if len(ro_yxat) == 0:
    print("Ro'yxat bo'sh!")


# ============================================================
# ELEMENTNI O'ZGARTIRISH
# ============================================================

"""
List o'zgaruvchan (mutable) — elementni to'g'ridan-to'g'ri o'zgartirish mumkin.
"""

baholar = [85, 90, 78, 92, 70]
print(baholar)       # [85, 90, 78, 92, 70]

baholar[2] = 88      # 3-elementni o'zgartirish
print(baholar)       # [85, 90, 88, 92, 70]

baholar[-1] = 95     # oxirgi elementni o'zgartirish
print(baholar)       # [85, 90, 88, 92, 95]

# Bir nechta elementni birdan o'zgartirish (slicing bilan)
baholar[1:3] = [100, 100]
print(baholar)       # [85, 100, 100, 92, 95]


# ============================================================
# MAVJUDLIGINI TEKSHIRISH — in operatori
# ============================================================

mevalar = ["olma", "banan", "uzum"]

print("banan" in mevalar)      # True
print("anor" in mevalar)       # False
print("anor" not in mevalar)   # True

# if bilan birga:
if "olma" in mevalar:
    print("Olma ro'yxatda bor!")

meeva = input("Qaysi mevani qidirasiz? ")
if meeva in mevalar:
    print(f"'{meeva}' ro'yxatda mavjud!")
else:
    print(f"'{meeva}' ro'yxatda yo'q.")


# ============================================================
# LIST METODLARI
# ============================================================

# ── append() — Oxiriga element qo'shish ──────────────────────
"""
append(element)  — listning OXIRIGA bitta element qo'shadi
"""
ro_yxat = [1, 2, 3]
ro_yxat.append(4)
ro_yxat.append(5)
print(ro_yxat)    # [1, 2, 3, 4, 5]

ismlar = ["Ali", "Vali"]
ismlar.append("Jasur")
print(ismlar)     # ['Ali', 'Vali', 'Jasur']

# ── insert() — Belgilangan joyga qo'shish ────────────────────
"""
insert(indeks, element)  — ko'rsatilgan indeksga element qo'shadi
"""
ro_yxat = [1, 2, 4, 5]
ro_yxat.insert(2, 3)     # 2-indeksga 3 ni qo'sh
print(ro_yxat)    # [1, 2, 3, 4, 5]

ismlar = ["Ali", "Jasur"]
ismlar.insert(1, "Vali")  # o'rtaga qo'sh
print(ismlar)     # ['Ali', 'Vali', 'Jasur']

# ── extend() — Boshqa listni qo'shish ────────────────────────
"""
extend(boshqa_list)  — boshqa listning barcha elementlarini qo'shadi
append([1,2]) vs extend([1,2]):
  append → [[1, 2]]   (list ichida list)
  extend → [1, 2]     (elementlar qo'shiladi)
"""
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)    # [1, 2, 3, 4, 5, 6]

# + operatori bilan ham birlashtirish mumkin:
x = [1, 2] + [3, 4]
print(x)    # [1, 2, 3, 4]

# ── remove() — Qiymat bo'yicha o'chirish ─────────────────────
"""
remove(element)  — ko'rsatilgan QIYMATNI birinchi uchraganini o'chiradi
Topilmasa — XATO! (ValueError)
"""
ro_yxat = [1, 2, 3, 2, 4]
ro_yxat.remove(2)        # birinchi 2 ni o'chiradi
print(ro_yxat)    # [1, 3, 2, 4]

mevalar = ["olma", "banan", "uzum"]
mevalar.remove("banan")
print(mevalar)    # ['olma', 'uzum']

# ── pop() — Indeks bo'yicha o'chirish ────────────────────────
"""
pop()       — OXIRGI elementni o'chirib, uni qaytaradi
pop(indeks) — ko'rsatilgan indeksdagi elementni o'chirib qaytaradi
"""
ro_yxat = [1, 2, 3, 4, 5]
oxirgi = ro_yxat.pop()      # oxirgi elementni o'chiradi
print(oxirgi)    # 5
print(ro_yxat)   # [1, 2, 3, 4]

birinchi = ro_yxat.pop(0)   # 0-indeksdagi elementni o'chiradi
print(birinchi)  # 1
print(ro_yxat)   # [2, 3, 4]

# ── del — O'chirish ───────────────────────────────────────────
"""
del list[indeks]       — indeks bo'yicha o'chiradi
del list[boshlash:tugash] — qism o'chiradi
del list               — butun listni o'chiradi
"""
ro_yxat = [1, 2, 3, 4, 5]
del ro_yxat[2]        # 3 ni o'chiradi
print(ro_yxat)    # [1, 2, 4, 5]

del ro_yxat[1:3]      # 2 va 4 ni o'chiradi
print(ro_yxat)    # [1, 5]

# ── clear() — Barchasini tozalash ────────────────────────────
ro_yxat = [1, 2, 3, 4, 5]
ro_yxat.clear()
print(ro_yxat)    # []

# ── copy() — Nusxa olish ──────────────────────────────────────
"""
DIQQAT: a = b deb yozsangiz — bu nusxa emas, bir xil obyekt!
        b da o'zgarish a ni ham o'zgartiradi!
        Haqiqiy nusxa uchun copy() ishlating.
"""
asl    = [1, 2, 3]
nusxa  = asl.copy()
nusxa.append(4)
print(asl)     # [1, 2, 3]   — o'zgarmadi
print(nusxa)   # [1, 2, 3, 4]

# Xato usul:
a = [1, 2, 3]
b = a             # bu nusxa EMAS!
b.append(4)
print(a)    # [1, 2, 3, 4]  — a ham o'zgardi!

# ── count() — Elementni sanash ────────────────────────────────
ro_yxat = [1, 2, 2, 3, 2, 4]
print(ro_yxat.count(2))    # 3  — 2 uchta bor
print(ro_yxat.count(5))    # 0  — 5 yo'q

# ── index() — Elementning indeksini topish ────────────────────
ro_yxat = ["Ali", "Vali", "Jasur"]
print(ro_yxat.index("Vali"))    # 1
# print(ro_yxat.index("Nodir")) → XATO! ValueError


# ============================================================
# SARALASH — sort() va reverse()
# ============================================================

# ── sort() — Tartiblash ───────────────────────────────────────
"""
sort()              — o'sish tartibida (kichikdan kattaga)
sort(reverse=True)  — kamayish tartibida (kattadan kichikka)
"""
sonlar = [3, 1, 4, 1, 5, 9, 2, 6]
sonlar.sort()
print(sonlar)    # [1, 1, 2, 3, 4, 5, 6, 9]

sonlar.sort(reverse=True)
print(sonlar)    # [9, 6, 5, 4, 3, 2, 1, 1]

ismlar = ["Jasur", "Ali", "Vali", "Bobur"]
ismlar.sort()
print(ismlar)    # ['Ali', 'Bobur', 'Jasur', 'Vali']  — alifbo tartibida

# ── sorted() — Yangi tartiblangan list qaytaradi ─────────────
"""
sort()   — listning O'ZINI o'zgartiradi
sorted() — YANGI tartiblangan list qaytaradi (asl o'zgarmaydi)
"""
asl    = [3, 1, 4, 1, 5]
yangi  = sorted(asl)
print(asl)     # [3, 1, 4, 1, 5]  — o'zgarmadi
print(yangi)   # [1, 1, 3, 4, 5]

# ── reverse() — Teskari aylantirish ──────────────────────────
ro_yxat = [1, 2, 3, 4, 5]
ro_yxat.reverse()
print(ro_yxat)    # [5, 4, 3, 2, 1]


# ============================================================
# list() va range() BILAN LIST YARATISH
# ============================================================

"""
list(range(...))  — range dan list yaratish
"""
ro_yxat = list(range(1, 11))
print(ro_yxat)    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

juftlar = list(range(0, 20, 2))
print(juftlar)    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# ── List Comprehension — qisqa list yaratish ─────────────────
"""
[ifoda for element in range]  — bir qatorda list yaratish
"""
kvadratlar = [x ** 2 for x in range(1, 6)]
print(kvadratlar)   # [1, 4, 9, 16, 25]

juftlar = [x for x in range(20) if x % 2 == 0]
print(juftlar)      # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# ============================================================
# FOR SIKLI BILAN LIST
# ============================================================

ismlar = ["Ali", "Vali", "Jasur", "Bobur"]

# Oddiy ko'rib chiqish:
for ism in ismlar:
    print(f"Salom, {ism}!")

# enumerate() bilan indeks ham olish:
for i, ism in enumerate(ismlar):
    print(f"{i + 1}. {ism}")

# Natija:
# 1. Ali
# 2. Vali
# 3. Jasur
# 4. Bobur


# ============================================================
# AMALIY DASTUR — Baholar tahlilchisi
# ============================================================

print("\n=== Baholar tahlilchisi ===")
baholar = []
n = int(input("Nechta baho kiritasiz? "))

for i in range(n):
    baho = int(input(f"{i + 1}-baho: "))
    baholar.append(baho)

print(f"\nBaholar  : {baholar}")
print(f"Eng yuqori: {max(baholar)}")
print(f"Eng past  : {min(baholar)}")
print(f"O'rtacha  : {round(sum(baholar) / len(baholar), 1)}")

baholar.sort(reverse=True)
print(f"Tartiblangan: {baholar}")


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Asosiy (Oson):
  5 ta shahar nomini o'z ichiga olgan list yarating.
  a) Birinchi va oxirgi shaharni chiqaring
  b) Listni alifbo tartibida tartiblang va chiqaring
  c) Yangi shahar qo'shing (append)
  d) Ro'yxatdagi shaharlar sonini chiqaring (len)

TOPSHIRIQ 2 — O'rta:
  Foydalanuvchidan 5 ta son olib listga qo'shing.
  Quyidagilarni chiqaring:
    - Yig'indi (sum)
    - O'rtacha qiymat
    - Eng katta va eng kichik son
    - Saralangan holda

TOPSHIRIQ 3 — Qiyin:
  Do'kon ro'yxati dasturi:
    - Boshlang'ich ro'yxat: ["non", "sut", "tuxum"]
    - Foydalanuvchi "qo'sh" desa — yangi mahsulot qo'shsin
    - "o'chir" desa — mahsulot o'chirsin
    - "ko'rsat" desa — ro'yxatni chiqarsin
    - "chiq" desa — dastur tugasin

TOPSHIRIQ 4 — Ijodiy:
  1 dan 50 gacha bo'lgan toq sonlar listini
  list comprehension bilan yarating va chiqaring.
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ List nima va yaratish usullari []
✔️ Indekslash va slicing — list[0], list[-1], list[1:3]
✔️ len(), type()
✔️ Elementni o'zgartirish — list[i] = yangi_qiymat
✔️ "element" in list — mavjudligini tekshirish
✔️ List metodlari:
    append()  — oxiriga qo'shish
    insert()  — belgilangan joyga qo'shish
    extend()  — boshqa listni biriktirish
    remove()  — qiymat bo'yicha o'chirish
    pop()     — indeks bo'yicha o'chirib qaytarish
    del       — o'chirish
    clear()   — tozalash
    copy()    — nusxa olish
    count()   — elementni sanash
    index()   — elementning indeksini topish
✔️ sort(), sorted(), reverse()
✔️ list(range(...)) bilan list yaratish
✔️ List Comprehension — [x**2 for x in range(5)]
✔️ for sikli bilan listni ko'rib chiqish
✔️ enumerate() — indeks va qiymat birga
"""