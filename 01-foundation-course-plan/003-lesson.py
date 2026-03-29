# ============================================================
#   DARS 3: Tarmoqlanuvchi Operatorlar — if, elif, else
#           Solishtirish va Mantiq Operatorlari
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# TARMOQLANISH NIMA?
# ------------------------------------------------------------

"""
Kundalik hayotda ko'p qarorlar shart asosida qabul qilinadi:

  "Agar yomg'ir yog'sa  →  soyabon ol"
  "Agar ball 90+ bo'lsa →  'A' baho"
  "Agar pul yetarli bo'lsa → sotib ol, aks holda → kut"

Dasturlashda ham xuddi shunday.
Tarmoqlanish — bu shartga qarab, turli yo'llardan birini tanlash.

Python'da buning uchun:  if, elif, else  kalit so'zlari ishlatiladi.
"""


# ============================================================
# SOLISHTIRISH OPERATORLARI
# ============================================================

"""
Solishtirish operatorlari ikki qiymatni taqqoslaydi
va natija sifatida Boolean (True yoki False) qaytaradi.

  Operator   Nomi                    Misol         Natija
  ─────────  ──────────────────────  ────────────  ──────
  ==         Teng                    5 == 5        True
  !=         Teng emas               5 != 3        True
  >          Katta                   7 > 4         True
  <          Kichik                  3 < 1         False
  >=         Katta yoki teng         5 >= 5        True
  <=         Kichik yoki teng        4 <= 3        False

DIQQAT:
  =   →  qiymat berish (o'zlashtirish):   x = 5
  ==  →  teng ekanini tekshirish:         x == 5
  Bu IKKI XIL narsa! Adashtirmang!
"""

# ── == Teng ─────────────────────────────────────────────────
print(5 == 5)          # True
print(5 == 3)          # False
print("Ali" == "Ali")  # True
print("ali" == "Ali")  # False  (katta-kichik harf farq qiladi!)

# ── != Teng emas ─────────────────────────────────────────────
print(5 != 3)          # True   (5 va 3 teng emas)
print(5 != 5)          # False  (5 va 5 teng — farq yo'q)

# ── > Katta ─────────────────────────────────────────────────
print(7 > 4)           # True
print(4 > 7)           # False
print(5 > 5)           # False  (teng, lekin katta emas)

# ── < Kichik ─────────────────────────────────────────────────
print(3 < 8)           # True
print(8 < 3)           # False
print(5 < 5)           # False  (teng, lekin kichik emas)

# ── >= Katta yoki teng ───────────────────────────────────────
print(5 >= 5)          # True   (aynan teng)
print(6 >= 5)          # True   (katta)
print(4 >= 5)          # False

# ── <= Kichik yoki teng ──────────────────────────────────────
print(3 <= 5)          # True   (kichik)
print(5 <= 5)          # True   (aynan teng)
print(6 <= 5)          # False


# ============================================================
# MANTIQ OPERATORLARI (and, or, not)
# ============================================================

"""
Ba'zan bir nechta shartni birga tekshirish kerak bo'ladi.
Buning uchun mantiq operatorlari ishlatiladi:

  Operator   Nomi     Ma'nosi
  ─────────  ───────  ─────────────────────────────────────────────────
  and        VA       Ikkala shart ham True bo'lsagina natija True
  or         YOKI     Kamida bitta shart True bo'lsa natija True
  not        EMAS     True ni False ga, False ni True ga aylantiradi
"""

# ── and (VA) — Ikkala shart bajarilishi shart ────────────────
"""
  True  and True   →  True    (ikkalasi ham to'g'ri)
  True  and False  →  False   (biri noto'g'ri)
  False and True   →  False   (biri noto'g'ri)
  False and False  →  False   (ikkalasi ham noto'g'ri)

  Misol: "Agar YOSH ≥ 18 VA FUQARO bo'lsa → ovoz berishi mumkin"
"""
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

# Amaliy misol:
yosh = 20
fuqaro = True
print(yosh >= 18 and fuqaro == True)   # True  (ikkalasi bajarildi)

yosh = 16
print(yosh >= 18 and fuqaro == True)   # False (yosh sharti bajarilmadi)

# ── or (YOKI) — Kamida bitta shart bajarilsa yetarli ─────────
"""
  True  or True   →  True    (ikkalasi ham to'g'ri)
  True  or False  →  True    (biri to'g'ri — yetarli)
  False or True   →  True    (biri to'g'ri — yetarli)
  False or False  →  False   (ikkalasi ham noto'g'ri)

  Misol: "Agar TALABA YOKI PENSIONER bo'lsa → chegirma oladi"
"""
print(True or False)    # True
print(False or False)   # False

talaba = False
pensioner = True
print(talaba or pensioner)   # True  (pensioner shart bajarildi)

talaba = False
pensioner = False
print(talaba or pensioner)   # False (ikkalasi ham False)

# ── not (EMAS) — Qiymatni teskari aylantiradi ────────────────
"""
  not True   →  False
  not False  →  True

  Misol: "Agar foydalanuvchi LOGIN qilmagan bo'lsa → kirish sahifasiga yo'nalt"
"""
print(not True)         # False
print(not False)        # True

login_qilgan = False
print(not login_qilgan) # True  (qilmagan — demak kirishiga ruxsat)

# ── Kombinatsiya: and, or, not birga ─────────────────────────
yosh = 25
talaba = True
pensioner = False

# 18 dan katta VA (talaba YOKI pensioner) bo'lsa
print(yosh >= 18 and (talaba or pensioner))   # True
# 18 dan katta VA talaba EMAS bo'lsa
print(yosh >= 18 and not talaba)              # False


# ============================================================
# if — ENG ODDIY SHART
# ============================================================

"""
if — agar shart True bo'lsa, ichidagi kod bajariladi.

Sintaksis:
  if shart:
      # shart True bo'lsa shu yerga keladi
      bajariladigan_kod

MUHIM QOIDALAR:
  1. if dan keyin ikki nuqta (:) qo'yiladi
  2. Ichki kod 4 ta bo'sh joy (INDENT) bilan yoziladi
  3. Indent noto'g'ri bo'lsa — dastur XATO beradi
"""

# MISOL 1 — Son musbatmi?
son = 10
if son > 0:
    print("Son musbat!")       # Natija: Son musbat!

# MISOL 2 — Shart bajarilmasa, hech narsa bo'lmaydi
son = -5
if son > 0:
    print("Bu chiqmaydi")      # Shart False → kod bajarilamaydi

# MISOL 3 — Sinf ichida bir nechta qator
ball = 85
if ball >= 50:
    print("Siz o'tdingiz!")
    print("Tabriklaymiz!")
    print("Balingiz:", ball)


# ============================================================
# if — else
# ============================================================

"""
else — shart False bo'lganda nima qilishni belgilaydi.

Sintaksis:
  if shart:
      # True bo'lsa
      birinchi_kod
  else:
      # False bo'lsa
      ikkinchi_kod

Faqat ikkita yo'l: YO if, YO else. Ikkalasi birga bajarilamaydi.
"""

# MISOL 1 — Musbat yoki manfiy
son = -3
if son > 0:
    print("Musbat son")
else:
    print("Manfiy son yoki nol")   # Natija: Manfiy son yoki nol

# MISOL 2 — O'tdi yoki o'tmadi
ball = 45
if ball >= 50:
    print("O'tdingiz!")
else:
    print("O'tmadingi. Qayta urinib ko'ring.")   # Natija shu

# MISOL 3 — Juft yoki toq
son = 17
if son % 2 == 0:
    print(son, "— juft son")
else:
    print(son, "— toq son")   # Natija: 17 — toq son

# MISOL 4 — input() bilan
# ism = input("Ismingizni kiriting: ")
# if ism == "Admin":
#     print("Xush kelibsiz, Admin!")
# else:
#     print("Salom,", ism)


# ============================================================
# if — elif — else
# ============================================================

"""
elif — "else if" ning qisqartmasi.
Bir nechta shart ketma-ket tekshirilganda ishlatiladi.

Sintaksis:
  if birinchi_shart:
      birinchi_kod
  elif ikkinchi_shart:
      ikkinchi_kod
  elif uchinchi_shart:
      uchinchi_kod
  else:
      oxirgi_kod   # hech biri bajarilmasa

ISHLASH TARTIBI:
  Python yuqoridan pastga qarab tekshiradi.
  Birinchi True bo'lgan shart bajariladi va qolganlar o'tkazib yuboriladi.
  Hech biri True bo'lmasa — else bajariladi.
"""

# MISOL 1 — Baho tizimi
ball = 78

if ball >= 90:
    print("Baho: A — Mukammal!")
elif ball >= 80:
    print("Baho: B — Yaxshi!")
elif ball >= 70:
    print("Baho: C — Qoniqarli")    # Natija: Baho: C — Qoniqarli
elif ball >= 50:
    print("Baho: D — O'rtacha")
else:
    print("Baho: F — O'tmadi")

# MISOL 2 — Kun vaqti
soat = 14

if soat < 12:
    print("Xayrli tong!")
elif soat < 17:
    print("Xayrli kun!")          # Natija: Xayrli kun!
elif soat < 21:
    print("Xayrli kech!")
else:
    print("Xayrli tun!")

# MISOL 3 — Harorat tavsifi
harorat = -5

if harorat > 30:
    print("Juda issiq — suv iching!")
elif harorat > 20:
    print("Issiq — yengil kiyining")
elif harorat > 10:
    print("Iliq — oddiy kiyim yetarli")
elif harorat > 0:
    print("Salqin — kofta kiyib oling")
else:
    print("Sovuq — issiq kiyining!")   # Natija: Sovuq — issiq kiyining!

# MISOL 4 — Tramvay narxi (chegirmalar bilan)
yosh = int(input("Yoshingizni kiriting: "))

if yosh < 7:
    print("Bepul — bolalar uchun")
elif yosh <= 14:
    print("Narx: 500 so'm — o'quvchilar uchun")
elif yosh >= 65:
    print("Narx: 500 so'm — pensionerlar uchun")
else:
    print("Narx: 1500 so'm — oddiy narx")


# ============================================================
# MANTIQ OPERATORLARI if BILAN BIRGA
# ============================================================

# ── and bilan ────────────────────────────────────────────────

# MISOL 1 — Kirish huquqi
yosh = 20
parol_togri = True

if yosh >= 18 and parol_togri:
    print("Tizimga kirildi!")
else:
    print("Kirish rad etildi")   # Natija: Tizimga kirildi!

# MISOL 2 — Oraliq tekshirish (1 dan 100 gacha)
son = 45
if son >= 1 and son <= 100:
    print("Son to'g'ri oraliqda")   # Natija: Son to'g'ri oraliqda

# Yoki qisqaroq yozish mumkin:
if 1 <= son <= 100:
    print("To'g'ri oraliq!")        # Python bu sintaksisni qabul qiladi

# ── or bilan ─────────────────────────────────────────────────

# MISOL 3 — Dam olish kuni
kun = "Shanba"

if kun == "Shanba" or kun == "Yakshanba":
    print("Bugun dam olish kuni!")
else:
    print("Ish kuni, ishga boring!")   # Natija: Dam olish kuni!

# MISOL 4 — Maxsus foydalanuvchi
foydalanuvchi = "admin"

if foydalanuvchi == "admin" or foydalanuvchi == "moderator":
    print("Keng huquqlar berildi")
else:
    print("Oddiy foydalanuvchi")

# ── not bilan ────────────────────────────────────────────────

# MISOL 5 — Kirmagan foydalanuvchi
kirgan = False

if not kirgan:
    print("Iltimos, avval tizimga kiring!")
else:
    print("Xush kelibsiz!")   # Natija: Iltimos, avval tizimga kiring!

# MISOL 6 — Xavfsiz parol tekshiruvi
parol = "1234"
xavfsiz_parollar = ["admin", "1234", "qwerty", "password"]

if parol not in xavfsiz_parollar:
    print("Parol xavfsiz!")
else:
    print("Parol juda oddiy, o'zgartiring!")  # Natija: Parol juda oddiy


# ============================================================
# ICHMA-ICH if (Nested if)
# ============================================================

"""
if ichida yana if yozish mumkin.
Bu "ichma-ich shart" deyiladi.

Qachon ishlatiladi?
  Birinchi shart bajarilgandan KEYIN,
  ikkinchi, yanada aniqroq shartni tekshirish kerak bo'lganda.
"""

# MISOL 1 — Bank kartasi tekshiruvi
karta_mavjud = True
balans = 50000
to_lov = 30000

if karta_mavjud:
    print("Karta topildi")
    if balans >= to_lov:
        print("To'lov amalga oshirildi!")
        print("Qoldiq:", balans - to_lov, "so'm")
    else:
        print("Mablag' yetarli emas!")
else:
    print("Karta topilmadi!")

# MISOL 2 — O'yin kirish tizimi
yosh = int(input("Yoshingiz: "))
obuna = input("Obunangiz bormi? (ha/yo'q): ")

if yosh >= 18:
    if obuna == "ha":
        print("Barcha o'yinlarga kirish ochiq!")
    else:
        print("Obuna oling — narx: 50 000 so'm/oy")
else:
    print("Kechirasiz, bu platforma 18+ uchun")


# ============================================================
# QISQA if (Ternary Operator)
# ============================================================

"""
Oddiy if-else ni bir qatorda yozish mumkin.
Bu "ternary" yoki "inline if" deyiladi.

Sintaksis:
  qiymat = true_qiymat  if  shart  else  false_qiymat

Qachon ishlatiladi?
  Qisqa, oddiy shartlarda kod qisqaroq bo'lishi uchun.
"""

# Oddiy usul (3 qator):
son = 7
if son > 0:
    natija = "musbat"
else:
    natija = "manfiy"
print(natija)   # musbat

# Qisqa usul (1 qator):
natija = "musbat" if son > 0 else "manfiy"
print(natija)   # musbat

# Boshqa misollar:
ball = 75
xulosa = "O'tdi" if ball >= 50 else "O'tmadi"
print(xulosa)   # O'tdi

yosh = 20
toifa = "kattalar" if yosh >= 18 else "yoshlar"
print(toifa)    # kattalar


# ============================================================
# TO'LIQ AMALIY DASTUR
# ============================================================

"""
Quyidagi dastur hamma narsani birga ishlatadi.
"""

# --- BMI (Tana Massa Indeksi) Kalkulyatori ---

ism    = input("Ismingiz: ")
vazn   = float(input("Vazningiz (kg): "))
boy    = float(input("Bo'yingiz (metr): "))

bmi = vazn / (boy ** 2)
bmi = round(bmi, 1)

print()
print(f"{ism}, sizning BMI: {bmi}")

if bmi < 18.5:
    print("Holat: Tana vazni kam")
    print("Maslahat: Ko'proq kaloriya iste'mol qiling")
elif bmi < 25:
    print("Holat: Normal vazn — Zo'r!")
elif bmi < 30:
    print("Holat: Ortiqcha vazn")
    print("Maslahat: Sport va parhez foydali")
else:
    print("Holat: Semizlik")
    print("Maslahat: Shifokorga murojaat qiling")


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Solishtirish:
  a = 15, b = 20 o'zgaruvchilarni yarating.
  Quyidagilarni chiqaring (True/False):
    - a == b
    - a != b
    - a < b
    - a >= b

TOPSHIRIQ 2 — Oddiy if-else:
  Foydalanuvchidan son oling.
  Agar musbat bo'lsa — "Musbat son"
  Agar manfiy bo'lsa — "Manfiy son"
  Agar nol bo'lsa    — "Nol"  chiqaring.

TOPSHIRIQ 3 — Baho tizimi:
  Foydalanuvchidan ball oling (0—100).
  if-elif-else bilan baho chiqaring:
    90-100 → "A (Mukammal)"
    80-89  → "B (Yaxshi)"
    70-79  → "C (Qoniqarli)"
    50-69  → "D (O'rtacha)"
    0-49   → "F (O'tmadi)"

TOPSHIRIQ 4 — and/or/not:
  Foydalanuvchidan yosh oling.
    - Agar 6 va undan katta VA 18 dan kichik bo'lsa → "Maktab o'quvchisi"
    - Agar 18 va undan katta VA 65 dan kichik bo'lsa → "Ishchi yoshdagi kishi"
    - Agar 65 va undan katta bo'lsa → "Pensioner"
    - Agar 6 dan kichik bo'lsa → "Maktabgacha yoshdagi bola"

TOPSHIRIQ 5 — Kalit so'z o'yini:
  Maxfiy so'z = "python" deb belgilang.
  Foydalanuvchidan so'z oling.
  Agar to'g'ri taxmin qilsa → "Tabriklaymiz! To'g'ri!"
  Agar noto'g'ri bo'lsa     → "Noto'g'ri taxmin :("

TOPSHIRIQ 6 (Qo'shimcha) — Ichma-ich shart:
  Foydalanuvchidan ikkita son oling.
  Birinchi son musbat bo'lsagina ikkinchi shart tekshirilsin:
    - Agar ikkinchi son ham musbat bo'lsa → "Ikkalasi musbat"
    - Agar ikkinchi son manfiy bo'lsa    → "Faqat birinchisi musbat"
  Agar birinchi son manfiy bo'lsa → "Birinchi son manfiy"
"""


# ------------------------------------------------------------
# QUSHIMCHA RESURSLAR (Uyga vazifa uchun)
# ------------------------------------------------------------

"""
📚 RASMIY HUJJATLAR:
   https://docs.python.org/3/tutorial/controlflow.html
   — if, elif, else haqida rasmiy ma'lumot

🌐 W3SCHOOLS:
   https://www.w3schools.com/python/python_conditions.asp
   — if, elif, else

   https://www.w3schools.com/python/python_operators.asp
   — Barcha operatorlar (solishtirish va mantiq)
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ Solishtirish operatorlari:
    ==   teng
    !=   teng emas
    >    katta
    <    kichik
    >=   katta yoki teng
    <=   kichik yoki teng

✔️ Mantiq operatorlari:
    and  —  ikkalasi ham True bo'lsa → True
    or   —  kamida biri True bo'lsa → True
    not  —  True → False, False → True

✔️ if       — shart to'g'ri bo'lsa bajara
✔️ if-else  — aks holda boshqa narsa bajara
✔️ if-elif-else — bir nechta shart ketma-ket
✔️ Ichma-ich if (nested if)
✔️ Qisqa if (ternary): natija = "a" if shart else "b"
"""