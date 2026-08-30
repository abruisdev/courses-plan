# ============================================================
#   DARS 3: Pythonda Tarmoqlanuvchi Operatorlar
#            if, elif, else
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================


# ------------------------------------------------------------
# DARSNING MAQSADI
# ------------------------------------------------------------

"""
Bugungi darsda:

  ✔️ Shart nima ekanini bilib olamiz
  ✔️ Solishtirish operatorlari bilan ishlaymiz
  ✔️ Mantiq operatorlarini o‘rganamiz
  ✔️ if operatorini ishlatamiz
  ✔️ if-else operatorini ishlatamiz
  ✔️ if-elif-else bilan bir nechta shart yozamiz
  ✔️ Ichma-ich if bilan ishlaymiz
  ✔️ Qisqa if (ternary operator) yozamiz
  ✔️ Yosh, baho, parol va kalkulyator misollarini qilamiz
"""


# ------------------------------------------------------------
# TARMOQLANISH NIMA?
# ------------------------------------------------------------

"""
Dastur har doim ham bir xil yo‘l bilan ishlamaydi.

Ba’zan ma’lum bir shart bajarilsa, bir kod ishlashi,
aks holda boshqa kod ishlashi kerak bo‘ladi.

Masalan:

  Agar yosh 18 dan katta yoki teng bo‘lsa:
      "Siz voyaga yetgansiz" deb chiqarish.

  Aks holda:
      "Siz voyaga yetmagansiz" deb chiqarish.

Bunday holatlarda if, elif va else ishlatiladi.
"""


# ------------------------------------------------------------
# SOLISHTIRISH OPERATORLARI
# ------------------------------------------------------------

"""
Solishtirish operatorlari 2 ta qiymatni solishtiradi.

Natija doim bool bo‘ladi:

    True    — shart rost bo‘lsa
    False   — shart yolg‘on bo‘lsa

  Operator   Nomi                    Misol       Natija
  ────────   ──────────────────────  ─────────   ──────
  ==         Teng                    5 == 5      True
  !=         Teng emas               5 != 3      True
  >          Katta                   10 > 5      True
  <          Kichik                  3 < 8       True
  >=         Katta yoki teng         10 >= 10    True
  <=         Kichik yoki teng        5 <= 10     True
"""


# ── == Teng ─────────────────────────────────────────────────

print(5 == 5)           # Natija: True
print(5 == 10)          # Natija: False
print("Ali" == "Ali")   # Natija: True
print("Ali" == "Vali")  # Natija: False


# ── != Teng emas ─────────────────────────────────────────────

print(5 != 3)           # Natija: True
print(10 != 10)         # Natija: False
print("admin" != "user")  # Natija: True


# ── > Katta ──────────────────────────────────────────────────

print(10 > 5)           # Natija: True
print(5 > 10)           # Natija: False
print(18 > 18)          # Natija: False


# ── < Kichik ─────────────────────────────────────────────────

print(3 < 8)            # Natija: True
print(10 < 2)           # Natija: False
print(18 < 18)          # Natija: False


# ── >= Katta yoki teng ───────────────────────────────────────

print(10 >= 10)         # Natija: True
print(15 >= 10)         # Natija: True
print(5 >= 10)          # Natija: False


# ── <= Kichik yoki teng ──────────────────────────────────────

print(5 <= 10)          # Natija: True
print(10 <= 10)         # Natija: True
print(15 <= 10)         # Natija: False


# ------------------------------------------------------------
# = VA == FARQI
# ------------------------------------------------------------

"""
=   → qiymat berish uchun ishlatiladi
==  → solishtirish uchun ishlatiladi
"""

yosh = 18           # yosh o‘zgaruvchisiga 18 qiymati berildi

print(yosh == 18)   # yosh 18 ga tengmi? → True

# NOTO‘G‘RI:
# if yosh = 18:
#     print("Siz 18 yoshdasiz")

# TO‘G‘RI:
if yosh == 18:
    print("Siz 18 yoshdasiz")


# ------------------------------------------------------------
# if OPERATORI
# ------------------------------------------------------------

"""
if — agar degani.

Sintaksisi:

    if shart:
        bajariladigan_kod

Muhim qoidalar:

  ✔️ Shartdan keyin : belgisi qo‘yiladi
  ✔️ if ichidagi kod 4 ta bo‘sh joy bilan yoziladi
  ✔️ Shart True bo‘lsa, kod ishlaydi
  ✔️ Shart False bo‘lsa, kod ishlamaydi
"""


# MISOL 1 — Yoshni tekshirish
yosh = 20

if yosh >= 18:
    print("Siz voyaga yetgansiz")


# MISOL 2 — Baho tekshirish
baho = 90

if baho >= 86:
    print("Sizning bahoyingiz a’lo")


# MISOL 3 — Parol tekshirish
parol = "python123"

if parol == "python123":
    print("Parol to‘g‘ri")


# MISOL 4 — Juft sonni aniqlash
son = 14

if son % 2 == 0:
    print("Bu juft son")


# ------------------------------------------------------------
# INDENTATION — JOY TASHLASH
# ------------------------------------------------------------

"""
Python’da if ichidagi kod albatta joy tashlab yoziladi.

Bu indentation deyiladi.

Ko‘pincha 4 ta bo‘sh joy ishlatiladi.
"""

yosh = 19

if yosh >= 18:
    print("Siz ovoz berishingiz mumkin")
    print("Siz voyaga yetgansiz")

print("Bu qator if’dan tashqarida")


# NOTO‘G‘RI:
# if yosh >= 18:
# print("Siz voyaga yetgansiz")

# TO‘G‘RI:
# if yosh >= 18:
#     print("Siz voyaga yetgansiz")


# ------------------------------------------------------------
# if-else OPERATORI
# ------------------------------------------------------------

"""
if-else — agar shart rost bo‘lsa bir kod,
aks holda boshqa kod ishlaydi.

Sintaksisi:

    if shart:
        birinchi_kod
    else:
        ikkinchi_kod
"""


# MISOL 1 — Yosh aniqlash
yosh = 16

if yosh >= 18:
    print("Siz voyaga yetgansiz")
else:
    print("Siz voyaga yetmagansiz")


# MISOL 2 — Juft yoki toq son
son = 17

if son % 2 == 0:
    print("Bu juft son")
else:
    print("Bu toq son")


# MISOL 3 — Login tekshirish
login = "admin"

if login == "admin":
    print("Xush kelibsiz, admin!")
else:
    print("Login noto‘g‘ri")


# MISOL 4 — Omborda mahsulot bor yoki yo‘qligi
omborda_bor = False

if omborda_bor:
    print("Mahsulot mavjud")
else:
    print("Mahsulot hozirda mavjud emas")


# ------------------------------------------------------------
# if-elif-else OPERATORI
# ------------------------------------------------------------

"""
elif — "aks holda agar" degani.

Bir nechta shart tekshirish kerak bo‘lganda ishlatiladi.

Sintaksisi:

    if birinchi_shart:
        kod
    elif ikkinchi_shart:
        kod
    elif uchinchi_shart:
        kod
    else:
        kod

Python shartlarni yuqoridan pastga qarab tekshiradi.
Birinchi True bo‘lgan shartning kodi ishlaydi.
"""


# MISOL 1 — Baho hisoblash
baho = 78

if baho >= 86:
    print("Bahoingiz: 5")
elif baho >= 71:
    print("Bahoingiz: 4")
elif baho >= 56:
    print("Bahoingiz: 3")
else:
    print("Bahoingiz: 2")


# MISOL 2 — Yosh toifalari
yosh = 25

if yosh < 7:
    print("Maktabgacha yosh")
elif yosh < 18:
    print("O‘quvchi")
elif yosh < 23:
    print("Talaba yoshidagi foydalanuvchi")
elif yosh < 60:
    print("Katta yoshdagi foydalanuvchi")
else:
    print("Nafaqa yoshidagi foydalanuvchi")


# MISOL 3 — Ob-havo haroratini aniqlash
harorat = 18

if harorat >= 35:
    print("Juda issiq")
elif harorat >= 25:
    print("Issiq")
elif harorat >= 15:
    print("Iliq")
elif harorat >= 0:
    print("Sovuq")
else:
    print("Juda sovuq")


# ------------------------------------------------------------
# MANTIQ OPERATORLARI
# ------------------------------------------------------------

"""
Mantiq operatorlari bir nechta shartni birlashtirish uchun ishlatiladi.

  and     → barcha shart True bo‘lsa True
  or      → kamida bitta shart True bo‘lsa True
  not     → True’ni False, False’ni True qiladi
"""


# ------------------------------------------------------------
# and OPERATORI
# ------------------------------------------------------------

"""
and — ikkala shart ham True bo‘lishi kerak.

  True  and True   → True
  True  and False  → False
  False and True   → False
  False and False  → False
"""

yosh = 20
pasport_bor = True

if yosh >= 18 and pasport_bor:
    print("Siz ro‘yxatdan o‘tishingiz mumkin")


# MISOL — Imtihondan o‘tish
baho = 75
davomat = 85

if baho >= 56 and davomat >= 80:
    print("Talaba imtihondan o‘tdi")
else:
    print("Talaba imtihondan o‘tmadi")


# ------------------------------------------------------------
# or OPERATORI
# ------------------------------------------------------------

"""
or — kamida bitta shart True bo‘lsa, natija True bo‘ladi.

  True  or True    → True
  True  or False   → True
  False or True    → True
  False or False   → False
"""

kun = "shanba"

if kun == "shanba" or kun == "yakshanba":
    print("Bugun dam olish kuni")
else:
    print("Bugun ish yoki o‘qish kuni")


# MISOL — Chegirma
vip_mijoz = False
promo_kod_bor = True

if vip_mijoz or promo_kod_bor:
    print("Siz chegirma olasiz")
else:
    print("Chegirma mavjud emas")


# ------------------------------------------------------------
# not OPERATORI
# ------------------------------------------------------------

"""
not — qiymatni teskarisiga o‘zgartiradi.

  not True   → False
  not False  → True
"""

tizim_yopiq = False

if not tizim_yopiq:
    print("Tizim ochiq")

# Yoki:
tizim_ochiq = True

if not tizim_ochiq:
    print("Tizim yopiq")
else:
    print("Tizim ochiq")


# ------------------------------------------------------------
# ICHMA-ICH if (NESTED if)
# ------------------------------------------------------------

"""
Ichma-ich if — if ichida yana if ishlatish.

Avval bitta shart tekshiriladi.
Agar u True bo‘lsa, ichidagi keyingi shart tekshiriladi.
"""

yosh = 20
pasport_bor = True

if yosh >= 18:
    if pasport_bor:
        print("Siz ro‘yxatdan o‘tishingiz mumkin")
    else:
        print("Sizda pasport yo‘q")
else:
    print("Sizning yoshingiz yetarli emas")


# MISOL — Login va parol
login = input("Loginni kiriting: ")
parol = input("Parolni kiriting: ")

if login == "admin":
    if parol == "python123":
        print("Xush kelibsiz, admin!")
    else:
        print("Parol noto‘g‘ri")
else:
    print("Bunday login mavjud emas")


# ------------------------------------------------------------
# QISQA if — TERNARY OPERATOR
# ------------------------------------------------------------

"""
Qisqa if bitta qatorga yoziladi.

Sintaksisi:

    qiymat = agar_true_bo‘lsa if shart else agar_false_bo‘lsa
"""

yosh = 20

natija = "Voyaga yetgan" if yosh >= 18 else "Voyaga yetmagan"

print(natija)


# MISOL — Juft yoki toq son
son = 15

natija = "Juft son" if son % 2 == 0 else "Toq son"

print(natija)


# MISOL — Baho natijasi
baho = 60

natija = "O‘tdingiz" if baho >= 56 else "Yiqildingiz"

print(natija)


# ------------------------------------------------------------
# AMALIY MISOLLAR
# ------------------------------------------------------------

# MISOL 1 — Foydalanuvchi yoshini aniqlash
yosh = int(input("Yoshingizni kiriting: "))

if yosh < 0:
    print("Yosh manfiy son bo‘lishi mumkin emas")
elif yosh < 18:
    print("Siz voyaga yetmagansiz")
else:
    print("Siz voyaga yetgansiz")


# MISOL 2 — Parol tekshirish
togri_parol = "python123"
parol = input("Parolni kiriting: ")

if parol == togri_parol:
    print("Tizimga muvaffaqiyatli kirdingiz")
else:
    print("Parol noto‘g‘ri")


# MISOL 3 — Baho hisoblash
baho = int(input("Bahongizni kiriting (0-100): "))

if baho < 0 or baho > 100:
    print("Baho 0 dan 100 gacha bo‘lishi kerak")
elif baho >= 86:
    print("Sizning bahoyingiz: 5")
elif baho >= 71:
    print("Sizning bahoyingiz: 4")
elif baho >= 56:
    print("Sizning bahoyingiz: 3")
else:
    print("Sizning bahoyingiz: 2")


# MISOL 4 — Oddiy kalkulyator
son1 = float(input("Birinchi sonni kiriting: "))
amal = input("Amalni kiriting (+, -, *, /): ")
son2 = float(input("Ikkinchi sonni kiriting: "))

if amal == "+":
    print("Natija:", son1 + son2)
elif amal == "-":
    print("Natija:", son1 - son2)
elif amal == "*":
    print("Natija:", son1 * son2)
elif amal == "/":
    if son2 != 0:
        print("Natija:", son1 / son2)
    else:
        print("0 ga bo‘lish mumkin emas")
else:
    print("Noto‘g‘ri amal kiritildi")


# MISOL 5 — Kirish chiptasi narxi
yosh = int(input("Yoshingizni kiriting: "))

if yosh < 7:
    print("Siz uchun kirish bepul")
elif yosh < 18:
    print("Chipta narxi: 10 000 so‘m")
elif yosh < 60:
    print("Chipta narxi: 20 000 so‘m")
else:
    print("Chipta narxi: 10 000 so‘m")


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Oson:

  Foydalanuvchidan son oling.

  Agar son musbat bo‘lsa:
      "Musbat son" deb chiqaring.

  Aks holda:
      "Manfiy yoki 0" deb chiqaring.


TOPSHIRIQ 2 — Juft yoki toq:

  Foydalanuvchidan son oling.

  Agar son juft bo‘lsa:
      "Juft son"

  Aks holda:
      "Toq son"

  deb chiqaring.


TOPSHIRIQ 3 — Kirish tizimi:

  Foydalanuvchidan login va parol so‘rang.

  To‘g‘ri login: admin
  To‘g‘ri parol: 12345

  Agar ikkalasi ham to‘g‘ri bo‘lsa:
      "Xush kelibsiz!"

  Aks holda:
      "Login yoki parol noto‘g‘ri"


TOPSHIRIQ 4 — Baho aniqlash:

  Foydalanuvchidan 0 dan 100 gacha baho oling.

  86 - 100  → 5
  71 - 85   → 4
  56 - 70   → 3
  0 - 55    → 2

  Agar foydalanuvchi 0 dan kichik yoki 100 dan katta
  son kiritsa, xato xabari chiqsin.


TOPSHIRIQ 5 — Uchta sondan kattasini topish:

  Foydalanuvchidan 3 ta son oling.

  if, elif va else yordamida eng katta sonni aniqlang.

  max() funksiyasini ishlatmang.


TOPSHIRIQ 6 — Mini kalkulyator:

  Foydalanuvchidan 2 ta son va amal oling.

  Quyidagi amallar ishlashi kerak:

    +
    -
    *
    /

  Agar foydalanuvchi 0 ga bo‘lishga urinsa,
  "0 ga bo‘lish mumkin emas" deb chiqaring.
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O‘RGANDIK?
# ------------------------------------------------------------

"""
✔️ Tarmoqlanish nima ekanini
✔️ Solishtirish operatorlarini:
    ==   teng
    !=   teng emas
    >    katta
    <    kichik
    >=   katta yoki teng
    <=   kichik yoki teng
✔️ = va == farqini
✔️ if operatorini
✔️ if-else operatorini
✔️ if-elif-else operatorini
✔️ and, or, not mantiq operatorlarini
✔️ Ichma-ich if yozishni
✔️ Qisqa if (ternary operator) yozishni
✔️ Yosh, baho, parol va kalkulyator dasturlarini
"""
