# ============================================================
#   DARS 22: Pythonda JSON va RegEx modullar
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# DARS HAQIDA
# ------------------------------------------------------------

"""
Bu darsda ikki muhim modul o'rganamiz:

  1️⃣  JSON   — ma'lumotlarni saqlash va almashish formati
  2️⃣  RegEx  — matndan naqsh bo'yicha qidirish

Qayerda ishlatiladi:
  JSON  → API, konfiguratsiya fayllari, ma'lumotlar bazasi
  RegEx → email tekshirish, telefon raqam, parol validatsiya
"""


# ============================================================
#   QISM 1: JSON (JavaScript Object Notation)
# ============================================================

# ------------------------------------------------------------
# JSON NIMA?
# ------------------------------------------------------------

"""
JSON — ma'lumotlarni matn shaklida saqlash va uzatish formati.
Python dict ga juda o'xshash ko'rinish:

  Python dict:                JSON:
  {"ism": "Ali",     →       {"ism": "Ali",
   "yosh": 15,                "yosh": 15,
   "talaba": True}            "talaba": true}

Farqlari:
  Python       JSON
  True    →    true
  False   →    false
  None    →    null
  tuple   →    array (list kabi)

JSON faylda odatda .json kengaytmasi ishlatiladi.
"""

import json

# ── Python → JSON turlari ─────────────────────────────────────
"""
Python       → JSON
dict         → object  {}
list, tuple  → array   []
str          → string  ""
int, float   → number
True/False   → true/false
None         → null
"""


# ============================================================
# JSON BILAN ISHLASH: dumps() va loads()
# ============================================================

print("=" * 50)
print("  1. dumps() va loads()  ")
print("=" * 50)

# ── dumps() — Python → JSON string ───────────────────────────
"""
json.dumps(ob'ekt)          — JSON stringga aylantiradi
json.dumps(ob'ekt, indent=4)— chiroyli formatlaydi
"""

talaba = {
    "ism"    : "Ali",
    "yosh"   : 15,
    "sinf"   : "9-A",
    "talaba" : True,
    "baholar": [90, 85, 92, 88],
    "manzil" : None
}

json_string = json.dumps(talaba)
print(type(json_string))   # <class 'str'>
print(json_string)

# Chiroyli formatlash (indent):
chiroyli = json.dumps(talaba, indent=4)
print("\nChiroyli ko'rinish:")
print(chiroyli)

# ensure_ascii=False — unicode harflarni saqlash:
matn = {"salom": "Привет", "uzbek": "O'zbek"}
print(json.dumps(matn, ensure_ascii=False, indent=2))


# ── loads() — JSON string → Python ───────────────────────────
"""
json.loads(json_string) — JSON stringni Python ob'ektga aylantiradi
"""

json_matn = '{"ism": "Vali", "yosh": 16, "talaba": true}'
python_ob = json.loads(json_matn)

print(type(python_ob))     # <class 'dict'>
print(python_ob["ism"])    # Vali
print(python_ob["talaba"]) # True  (json true → Python True)


# ============================================================
# JSON FAYL BILAN ISHLASH: dump() va load()
# ============================================================

print("\n" + "=" * 50)
print("  2. dump() va load() — Fayl bilan  ")
print("=" * 50)

# ── dump() — Python → JSON fayl ──────────────────────────────
"""
json.dump(ob'ekt, fayl)  — faylga yozadi
"""

maktab = {
    "nomi"     : "15-sonli maktab",
    "shahar"   : "Toshkent",
    "sinf_soni": 30,
    "talabalar": [
        {"ism": "Ali",   "ball": 90},
        {"ism": "Vali",  "ball": 85},
        {"ism": "Jasur", "ball": 92}
    ]
}

with open("maktab.json", "w", encoding="utf-8") as f:
    json.dump(maktab, f, indent=4, ensure_ascii=False)
print("✓ maktab.json fayli yaratildi")

# ── load() — JSON fayl → Python ──────────────────────────────
"""
json.load(fayl) — fayldan o'qiydi
"""

with open("maktab.json", "r", encoding="utf-8") as f:
    o_qilgan = json.load(f)

print(type(o_qilgan))                    # <class 'dict'>
print(o_qilgan["nomi"])                  # 15-sonli maktab
print(o_qilgan["talabalar"][0]["ism"])   # Ali

# Barcha talabalarni chiqarish:
for t in o_qilgan["talabalar"]:
    print(f"  {t['ism']}: {t['ball']} ball")


# ============================================================
# AMALIY DASTUR — JSON bilan Kontaktlar kitobi
# ============================================================

print("\n=== JSON KONTAKTLAR KITOBI ===")

FAYL = "kontaktlar.json"

def kontaktlarni_o_qi():
    """JSON fayldan kontaktlarni yuklash"""
    try:
        with open(FAYL, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def kontaktlarni_saqlash(kontaktlar):
    """Kontaktlarni JSON faylga saqlash"""
    with open(FAYL, "w", encoding="utf-8") as f:
        json.dump(kontaktlar, f, indent=4, ensure_ascii=False)

def kontakt_qo_sh(ism, telefon, email=""):
    kontaktlar = kontaktlarni_o_qi()
    kontaktlar[ism] = {"telefon": telefon, "email": email}
    kontaktlarni_saqlash(kontaktlar)
    print(f"✓ {ism} qo'shildi")

def kontakt_ko_r():
    kontaktlar = kontaktlarni_o_qi()
    if not kontaktlar:
        print("Kontaktlar yo'q.")
        return
    print(f"\n{'Ism':<15} {'Telefon':<15} {'Email'}")
    print("─" * 45)
    for ism, ma_lumot in sorted(kontaktlar.items()):
        print(f"{ism:<15} {ma_lumot['telefon']:<15} {ma_lumot.get('email', '')}")

# Demo:
kontakt_qo_sh("Ali Karimov",  "+998901234567", "ali@mail.ru")
kontakt_qo_sh("Vali Rahimov", "+998935556677", "vali@gmail.com")
kontakt_qo_sh("Jasur Toshev", "+998990001122")
kontakt_ko_r()


# ============================================================
#   QISM 2: RegEx (Regular Expressions — Muntazam iboralar)
# ============================================================

import re

# ------------------------------------------------------------
# REGEX NIMA?
# ------------------------------------------------------------

"""
RegEx — matndagi naqshlarni (pattern) qidirish usuli.

Misol:
  "email@domain.com" → email formatini tekshirish
  "+998901234567"    → telefon raqam formatini tekshirish
  "Parol123!"        → parol kuchliligini tekshirish

Python da: import re
"""

print("\n" + "=" * 50)
print("  REGEX — Asosiy naqshlar  ")
print("=" * 50)

# ── Asosiy belgilar ───────────────────────────────────────────
"""
Naqsh   Ma'nosi                   Misol
─────────────────────────────────────────────────
.       Istalgan bitta belgi       a.c → abc, a1c
\d      Raqam [0-9]               \d+ → 123
\D      Raqam EMAS                \D+ → abc
\w      Harf, raqam, _ [a-zA-Z0-9_] \w+ → hello_1
\W      \w EMAS (bo'sh joy va h.)
\s      Bo'sh joy (space, tab)    \s+ → " "
\S      Bo'sh joy EMAS
^       Boshlanishi               ^Salom → "Salom..."
$       Tugashi                   .txt$ → "fayl.txt"
*       0 va undan ko'p           ab* → a, ab, abb
+       1 va undan ko'p           ab+ → ab, abb (a emas)
?       0 yoki 1 marta            colou?r → color, colour
{n}     Aniq n marta              \d{4} → 2024
{n,m}   n dan m gacha             \d{2,4} → 12, 123, 1234
[]      Belgilar to'plami         [abc] → a yoki b yoki c
[^]     Inkor                     [^0-9] → raqam emas
|       YOKI                      cat|dog → cat yoki dog
()      Guruh                     (ab)+ → ab, abab
"""

# ============================================================
# ASOSIY FUNKSIYALAR
# ============================================================

# ── re.match() — BOSHIDAN moslik qidiradi ────────────────────
print("\n--- re.match() ---")
natija = re.match(r"\d+", "123abc")
if natija:
    print(natija.group())   # 123

natija = re.match(r"\d+", "abc123")
print(natija)               # None — boshida raqam yo'q

# ── re.search() — ISTALGAN joydan moslik qidiradi ─────────────
print("\n--- re.search() ---")
natija = re.search(r"\d+", "abc 456 xyz")
if natija:
    print(natija.group())   # 456

# ── re.findall() — BARCHA mosliklarni LIST da qaytaradi ───────
print("\n--- re.findall() ---")
matn = "Toshkent 2024, Samarqand 2023, Buxoro 2022"
sonlar = re.findall(r"\d+", matn)
print(sonlar)   # ['2024', '2023', '2022']

so_zlar = re.findall(r"[A-Z][a-z]+", matn)
print(so_zlar)  # ['Toshkent', 'Samarqand', 'Buxoro']

# ── re.sub() — ALMASHTIRISH ───────────────────────────────────
print("\n--- re.sub() ---")
matn = "Telefon: 998-90-123-45-67"
yangi = re.sub(r"[-\s]", "", matn)
print(yangi)    # Telefon: 99890123456

# Hamma sonni X bilan almashtirish:
matn2 = "Ali 15 yoshda, Vali 17 yoshda"
print(re.sub(r"\d+", "XX", matn2))   # Ali XX yoshda, Vali XX yoshda

# ── re.split() — NAQSH BO'YICHA BO'LISH ──────────────────────
print("\n--- re.split() ---")
matn = "ali;vali,jasur bobur"
qismlar = re.split(r"[;,\s]+", matn)
print(qismlar)   # ['ali', 'vali', 'jasur', 'bobur']

# ── re.compile() — NAQSHNI BIR MARTA TAYYORLASH ──────────────
print("\n--- re.compile() ---")
# Ko'p marta ishlatilsa tezroq ishlaydi:
raqam_naqsh = re.compile(r"\d+")
print(raqam_naqsh.findall("1 ta olma, 5 ta nok, 12 ta uzum"))
# ['1', '5', '12']

# ── Flags ─────────────────────────────────────────────────────
"""
re.IGNORECASE (re.I) — katta/kichik harfga e'tibor bermaydi
re.MULTILINE  (re.M) — ^ va $ har qator uchun ishlaydi
re.DOTALL     (re.S) — . yangi qatorni ham qamrab oladi
"""
matn = "Python juda zo'r. python oson o'rganiladi."
print(re.findall(r"python", matn, re.IGNORECASE))
# ['Python', 'python']


# ============================================================
# AMALIY MISOLLAR — VALIDATSIYA
# ============================================================

print("\n" + "=" * 50)
print("  AMALIY VALIDATSIYA  ")
print("=" * 50)

# ── Email tekshirish ──────────────────────────────────────────
def email_tekshir(email):
    """Email formatini tekshiradi"""
    naqsh = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(naqsh, email):
        print(f"✓ '{email}' — to'g'ri email")
        return True
    else:
        print(f"✗ '{email}' — noto'g'ri email")
        return False

print("\n--- Email tekshirish ---")
email_tekshir("ali@gmail.com")       # ✓
email_tekshir("vali.karimov@mail.ru")# ✓
email_tekshir("jasur@")              # ✗
email_tekshir("@domain.com")         # ✗
email_tekshir("noto'g'ri")           # ✗

# ── Telefon raqam tekshirish ──────────────────────────────────
def telefon_tekshir(tel):
    """O'zbekiston telefon raqamini tekshiradi"""
    naqsh = r"^(\+998|998|0)(90|91|93|94|95|97|98|99|33|88|77)\d{7}$"
    tel_toza = re.sub(r"[\s\-()]", "", tel)   # bo'shliq va tire olib tashlash
    if re.match(naqsh, tel_toza):
        print(f"✓ '{tel}' — to'g'ri raqam")
        return True
    else:
        print(f"✗ '{tel}' — noto'g'ri raqam")
        return False

print("\n--- Telefon tekshirish ---")
telefon_tekshir("+998901234567")  # ✓
telefon_tekshir("998935556677")   # ✓
telefon_tekshir("0991112233")     # ✓
telefon_tekshir("+7901234567")    # ✗
telefon_tekshir("123")            # ✗

# ── Parol kuchliligi ──────────────────────────────────────────
def parol_tekshir(parol):
    """Parol kuchliligini tekshiradi"""
    xatolar = []
    if len(parol) < 8:
        xatolar.append("✗ Kamida 8 ta belgi kerak")
    if not re.search(r"[A-Z]", parol):
        xatolar.append("✗ Kamida 1 ta katta harf kerak")
    if not re.search(r"[a-z]", parol):
        xatolar.append("✗ Kamida 1 ta kichik harf kerak")
    if not re.search(r"\d", parol):
        xatolar.append("✗ Kamida 1 ta raqam kerak")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", parol):
        xatolar.append("✗ Kamida 1 ta maxsus belgi kerak")

    if xatolar:
        print(f"Parol '{parol}' zaif:")
        for x in xatolar:
            print(f"  {x}")
    else:
        print(f"✓ Parol '{parol}' kuchli!")

print("\n--- Parol tekshirish ---")
parol_tekshir("123")            # zaif
parol_tekshir("parol123")       # zaif
parol_tekshir("Parol123!")      # kuchli ✓

# ── Matndan ma'lumot ajratish ─────────────────────────────────
print("\n--- Matndan ma'lumot ajratish ---")
matn = """
  Ali Karimov: ali.karimov@gmail.com, +998901234567
  Vali Rahimov: vali@mail.ru, +998935556677
  Jasur Toshev: jasur123@yandex.com, 998991112233
"""

# Emaillarni ajratib olish:
emaillar = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", matn)
print("Emaillar:", emaillar)

# Telefon raqamlarni ajratib olish:
telefonlar = re.findall(r"(\+?998\d{9})", matn)
print("Telefonlar:", telefonlar)


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — JSON (Oson):
  Sevimli filmlaringiz haqida JSON fayil yarating:
    [
      {"nomi": "Film nomi", "yil": 2020, "janr": "drama", "baho": 9.0},
      ...
    ]
  a) Faylga 5 ta film yozing
  b) Eng yuqori baholi filmni toping
  c) 2020-yildan keyin chiqgan filmlarni filtrlang

TOPSHIRIQ 2 — JSON (O'rta):
  Kundalik xarajatlar daftari:
  - Xarajat qo'shish: {"sana": "2024-01-15", "tur": "oziq-ovqat", "summa": 50000}
  - Barcha xarajatlarni ko'rish
  - Tur bo'yicha jami hisoblash
  - Kunlik o'rtachani hisoblash

TOPSHIRIQ 3 — RegEx (Oson):
  Quyidagi naqshlarni yozing va test qiling:
  a) Faqat katta harflardan iborat so'z:  [A-Z]+
  b) Veb-sayt URL:  https?://www\.\S+
  c) IP manzil (soddalashtirilgan):  \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}

TOPSHIRIQ 4 — RegEx (Qiyin):
  Matn tahlil qiluvchi dastur:
  - Foydalanuvchidan paragraf oling
  - Barcha email adreslarni ajrating
  - Barcha sonlarni ajrating va yig'indisini hisoblang
  - Nechta so'z borligini sanang
  - Eng uzun so'zni toping
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
JSON:
  ✔️ json.dumps()  — Python ob'ekt → JSON string
  ✔️ json.loads()  — JSON string → Python ob'ekt
  ✔️ json.dump()   — Python ob'ekt → JSON fayl
  ✔️ json.load()   — JSON fayl → Python ob'ekt
  ✔️ indent=4      — chiroyli formatlash
  ✔️ ensure_ascii=False — unicode harflar

RegEx:
  ✔️ re.match()    — boshidan moslik
  ✔️ re.search()   — istalgan joydan
  ✔️ re.findall()  — barcha mosliklar → list
  ✔️ re.sub()      — almashtirish
  ✔️ re.split()    — bo'lish
  ✔️ re.compile()  — naqshni oldindan tayyorlash
  ✔️ Asosiy belgilar: \d \w \s . * + ? {n} [] ^ $
  ✔️ Amaliy: email, telefon, parol validatsiyasi
"""