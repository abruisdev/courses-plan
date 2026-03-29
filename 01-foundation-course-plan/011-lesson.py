# ============================================================
#   DARS 11: Pythonda Dictionary (Lug'at)
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# DICTIONARY NIMA?
# ------------------------------------------------------------

"""
Dictionary — bu "kalit: qiymat" (key: value) juftlarini saqlaydi.
Jingalak qavs {} ichida, kalit va qiymat ikki nuqta (:) bilan ajratiladi.

Kundalik hayotda:
  - Telefon kitobi: {"Ali": "93-123-45-67", "Vali": "90-987-65-43"}
  - Mahsulot narxlari: {"non": 3000, "sut": 8000, "tuxum": 15000}
  - O'quvchi ma'lumoti: {"ism": "Ali", "yosh": 15, "sinf": "9-A"}

Xususiyatlari:
  ✔️ Kalit (key) — YAGONA va O'ZGARMAS bo'lishi kerak (str, int, tuple)
  ✔️ Qiymat (value) — istalgan tur bo'lishi mumkin
  ✔️ O'zgaruvchan — qo'shish, o'chirish, o'zgartirish mumkin
  ✔️ Python 3.7+ da TARTIBLI (kiritilgan tartibda saqlaydi)
"""

# ── Dictionary yaratish ───────────────────────────────────────
bo_sh     = {}
talaba    = {"ism": "Ali", "yosh": 15, "sinf": "9-A"}
narxlar   = {"non": 3000, "sut": 8000, "tuxum": 15000}
aralash   = {1: "bir", 2: "ikki", 3: "uch"}

print(talaba)        # {'ism': 'Ali', 'yosh': 15, 'sinf': '9-A'}
print(type(talaba))  # <class 'dict'>


# ============================================================
# QIYMATGA MUROJAAT — KEY ORQALI
# ============================================================

"""
dict[kalit]    — qiymatni oladi (topilmasa XATO!)
dict.get(kalit)— qiymatni oladi (topilmasa None yoki default)
"""

talaba = {"ism": "Ali", "yosh": 15, "sinf": "9-A", "ball": 87.5}

# ── [] bilan murojaat ─────────────────────────────────────────
print(talaba["ism"])    # Ali
print(talaba["yosh"])   # 15
print(talaba["ball"])   # 87.5

# Mavjud bo'lmagan kalit — XATO!
# print(talaba["manzil"])  →  KeyError: 'manzil'

# ── get() bilan murojaat — xavfsiz usul ──────────────────────
print(talaba.get("ism"))       # Ali
print(talaba.get("manzil"))    # None  (XATO yo'q!)
print(talaba.get("manzil", "Noma'lum"))   # Noma'lum  (default qiymat)

# ── Kalit mavjudligini tekshirish ─────────────────────────────
print("ism" in talaba)        # True
print("manzil" in talaba)     # False

if "ball" in talaba:
    print(f"Ball: {talaba['ball']}")


# ============================================================
# QIYMATNI O'ZGARTIRISH VA QO'SHISH
# ============================================================

talaba = {"ism": "Ali", "yosh": 15}

# ── Mavjud kalitni yangilash ──────────────────────────────────
talaba["yosh"] = 16
print(talaba)    # {'ism': 'Ali', 'yosh': 16}

# ── Yangi kalit qo'shish ──────────────────────────────────────
talaba["sinf"]  = "10-A"
talaba["ball"]  = 92
print(talaba)    # {'ism': 'Ali', 'yosh': 16, 'sinf': '10-A', 'ball': 92}


# ============================================================
# DICTIONARY METODLARI
# ============================================================

ma_lumot = {
    "ism"   : "Jasur",
    "yosh"  : 22,
    "kasb"  : "Dasturchi",
    "shahar": "Toshkent"
}

# ── keys() — Barcha kalitlar ──────────────────────────────────
print(ma_lumot.keys())
# dict_keys(['ism', 'yosh', 'kasb', 'shahar'])

# Listga aylantirish:
kalitlar = list(ma_lumot.keys())
print(kalitlar)   # ['ism', 'yosh', 'kasb', 'shahar']

# ── values() — Barcha qiymatlar ───────────────────────────────
print(ma_lumot.values())
# dict_values(['Jasur', 22, 'Dasturchi', 'Toshkent'])

# ── items() — Kalit-qiymat juftlari ──────────────────────────
print(ma_lumot.items())
# dict_items([('ism', 'Jasur'), ('yosh', 22), ('kasb', 'Dasturchi'), ('shahar', 'Toshkent')])

# ── get() — Xavfsiz qiymat olish (yuqorida ko'rdik) ──────────

# ── update() — Bir nechta qiymat yangilash/qo'shish ──────────
"""
update({kalit: qiymat})  — mavjudni yangilaydi, yo'qni qo'shadi
"""
ma_lumot.update({"yosh": 23, "email": "jasur@gmail.com"})
print(ma_lumot)
# {'ism': 'Jasur', 'yosh': 23, 'kasb': 'Dasturchi', 'shahar': 'Toshkent', 'email': 'jasur@gmail.com'}

# ── pop() — Kalit bo'yicha o'chirish va qaytarish ────────────
kasb = ma_lumot.pop("kasb")
print(kasb)       # Dasturchi
print(ma_lumot)   # kasb o'chirildi

# ── popitem() — Oxirgi kalit-qiymatni o'chirish ──────────────
oxirgi = ma_lumot.popitem()
print(oxirgi)     # ('email', 'jasur@gmail.com')  — tuple holida
print(ma_lumot)

# ── del — O'chirish ───────────────────────────────────────────
ma_lumot = {"a": 1, "b": 2, "c": 3}
del ma_lumot["b"]
print(ma_lumot)   # {'a': 1, 'c': 3}
# del ma_lumot    — butun dict ni o'chiradi

# ── clear() — Tozalash ───────────────────────────────────────
ma_lumot.clear()
print(ma_lumot)   # {}

# ── copy() — Nusxa ───────────────────────────────────────────
asl   = {"a": 1, "b": 2}
nusxa = asl.copy()
nusxa["c"] = 3
print(asl)    # {'a': 1, 'b': 2}   — o'zgarmadi
print(nusxa)  # {'a': 1, 'b': 2, 'c': 3}

# ── dict() — Konstruktor bilan yaratish ──────────────────────
yangi = dict(ism="Ali", yosh=15, sinf="9-A")
print(yangi)   # {'ism': 'Ali', 'yosh': 15, 'sinf': '9-A'}

# ── len() — Elementlar soni ───────────────────────────────────
d = {"a": 1, "b": 2, "c": 3}
print(len(d))   # 3


# ============================================================
# FOR SIKLI BILAN DICTIONARY
# ============================================================

talaba = {"ism": "Ali", "yosh": 15, "sinf": "9-A", "ball": 87}

# ── Faqat kalitlarni ko'rish ──────────────────────────────────
for kalit in talaba:
    print(kalit)
# ism  yosh  sinf  ball

# ── Faqat qiymatlarni ko'rish ─────────────────────────────────
for qiymat in talaba.values():
    print(qiymat)
# Ali  15  9-A  87

# ── Kalit va qiymatni birga ko'rish — items() ────────────────
for kalit, qiymat in talaba.items():
    print(f"{kalit:10} : {qiymat}")
# ism        : Ali
# yosh       : 15
# sinf       : 9-A
# ball       : 87


# ============================================================
# ICHMA-ICH DICTIONARY (Nested Dictionary)
# ============================================================

"""
Dictionary qiymatining o'zi ham dictionary bo'lishi mumkin.
Bu murakkab ma'lumotlarni saqlashda juda qulay.
"""

maktab = {
    "9-A": {
        "o'quvchilar": ["Ali", "Vali", "Jasur"],
        "o'qituvchi" : "Karimov A.",
        "o'quvchi_soni": 30
    },
    "9-B": {
        "o'quvchilar": ["Bobur", "Nodir", "Sanjar"],
        "o'qituvchi" : "Rahimov B.",
        "o'quvchi_soni": 28
    }
}

# Ichma-ich ga murojaat:
print(maktab["9-A"]["o'qituvchi"])          # Karimov A.
print(maktab["9-B"]["o'quvchi_soni"])       # 28
print(maktab["9-A"]["o'quvchilar"][0])      # Ali

# Ko'rib chiqish:
for sinf, ma_lumot in maktab.items():
    print(f"\n{sinf} sinfi:")
    print(f"  O'qituvchi    : {ma_lumot['o\'qituvchi']}")
    print(f"  O'quvchilar   : {', '.join(ma_lumot['o\'quvchilar'])}")
    print(f"  O'quvchi soni : {ma_lumot['o\'quvchi_soni']}")

# ── Ro'yxat ichida dictionary ─────────────────────────────────
talabalar = [
    {"ism": "Ali",   "ball": 87},
    {"ism": "Vali",  "ball": 92},
    {"ism": "Jasur", "ball": 78}
]

for t in talabalar:
    print(f"{t['ism']}: {t['ball']} ball")

# Eng yuqori ball:
eng_yaxshi = max(talabalar, key=lambda x: x["ball"])
print(f"Eng yaxshi: {eng_yaxshi['ism']} — {eng_yaxshi['ball']}")


# ============================================================
# DICTIONARY COMPREHENSION
# ============================================================

"""
{kalit: qiymat for element in ketma_ketlik}
"""

# Sonlarning kvadratlari:
kvadratlar = {x: x**2 for x in range(1, 6)}
print(kvadratlar)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Faqat juft sonlar:
juft_kv = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(juft_kv)
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# So'z uzunliklari:
so_zlar = ["Python", "Java", "C++", "Kotlin"]
uzunliklar = {so_z: len(so_z) for so_z in so_zlar}
print(uzunliklar)
# {'Python': 6, 'Java': 4, 'C++': 3, 'Kotlin': 6}


# ============================================================
# AMALIY DASTUR — Telefon kitobi
# ============================================================

print("\n=== TELEFON KITOBI ===")

telefon_kitob = {}

while True:
    print("\n1 — Qo'shish")
    print("2 — Qidirish")
    print("3 — O'chirish")
    print("4 — Hammasini ko'rish")
    print("5 — Chiqish")

    tanlov = input("\nTanlov: ")

    if tanlov == "1":
        ism = input("Ism: ").strip().title()
        tel = input("Tel: ").strip()
        telefon_kitob[ism] = tel
        print(f"✓ {ism} qo'shildi!")

    elif tanlov == "2":
        ism = input("Qidirish (ism): ").strip().title()
        if ism in telefon_kitob:
            print(f"{ism}: {telefon_kitob[ism]}")
        else:
            print(f"'{ism}' topilmadi!")

    elif tanlov == "3":
        ism = input("O'chirish (ism): ").strip().title()
        if ism in telefon_kitob:
            del telefon_kitob[ism]
            print(f"✓ {ism} o'chirildi!")
        else:
            print(f"'{ism}' topilmadi!")

    elif tanlov == "4":
        if telefon_kitob:
            print("\n--- Kontaktlar ---")
            for ism, tel in sorted(telefon_kitob.items()):
                print(f"  {ism:15} : {tel}")
        else:
            print("Telefon kitobi bo'sh!")

    elif tanlov == "5":
        print("Xayr!")
        break

    else:
        print("Noto'g'ri tanlov!")


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Asosiy (Oson):
  O'zingiz haqingizda dictionary yarating:
    ism, familya, yosh, shahar, sevimli_rang
  a) Har bir kalit-qiymatni items() bilan chiqaring
  b) "telefon" kalitini qo'shing
  c) "yosh" ni yangilang

TOPSHIRIQ 2 — O'rta:
  Mahsulotlar narxlari dictionary:
    {"non": 3000, "sut": 8000, "tuxum": 15000, "yog": 35000}
  a) Eng qimmat va eng arzon mahsulotni toping
  b) Barcha narxlarni 10% oshiring
  c) Yangi mahsulot qo'shing
  d) Jami qiymatni hisoblang (sum(dict.values()))

TOPSHIRIQ 3 — Qiyin (Ichma-ich):
  Quyidagi tuzilmani yarating:
    {
      "Ali":   {"matematika": 90, "fizika": 85, "ingliz": 88},
      "Vali":  {"matematika": 78, "fizika": 92, "ingliz": 80},
      "Jasur": {"matematika": 95, "fizika": 88, "ingliz": 91}
    }
  a) Har bir o'quvchining o'rtacha bahosini chiqaring
  b) Matematikadan eng yuqori baho olgan o'quvchini toping
  c) Har bir fan bo'yicha sinfning o'rtachasini hisoblang

TOPSHIRIQ 4 — So'z sanagich (Ijodiy):
  Foydalanuvchidan jumla oling.
  Har bir so'z necha marta uchraganini dictionary yordamida hisoblang.
  Natijani chiqaring.
  Masalan: "ali vali ali jasur vali ali"
  → {'ali': 3, 'vali': 2, 'jasur': 1}
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ Dictionary nima — {kalit: qiymat} to'plam
✔️ Qiymatga murojaat: dict[kalit] va dict.get(kalit)
✔️ Kalit mavjudligi: "kalit" in dict
✔️ Qiymat qo'shish/yangilash: dict[kalit] = qiymat
✔️ Dictionary metodlari:
    keys()      — barcha kalitlar
    values()    — barcha qiymatlar
    items()     — kalit-qiymat juftlari
    get()       — xavfsiz qiymat olish
    update()    — yangilash/qo'shish
    pop()       — kalit bo'yicha o'chirish
    popitem()   — oxirgi elementni o'chirish
    del         — o'chirish
    clear()     — tozalash
    copy()      — nusxa
    dict()      — konstruktor
    len()       — uzunlik
✔️ for sikli bilan dictionary
✔️ Ichma-ich dictionary
✔️ Dictionary comprehension
"""