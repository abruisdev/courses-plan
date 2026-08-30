# ============================================================
#   DARS 4: Pythonda While Sikl Operatori
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================


# ------------------------------------------------------------
# DARSNING MAQSADI
# ------------------------------------------------------------

"""
Bugungi darsda:

  ✔️ Sikl nima va nima uchun kerakligini bilib olamiz
  ✔️ while sikli bilan ishlaymiz
  ✔️ Hisoblagich (counter) ishlatamiz
  ✔️ break bilan sikldan chiqamiz
  ✔️ continue bilan qadamni o‘tkazib yuboramiz
  ✔️ while True bilan cheksiz sikl yaratamiz
  ✔️ while + input() bilan interaktiv dastur tuzamiz
  ✔️ while + else bilan ishlaymiz
  ✔️ Parol tekshirish, menyu va son topish dasturlarini qilamiz
"""


# ------------------------------------------------------------
# SIKL NIMA?
# ------------------------------------------------------------

"""
Sikl — bir xil kodni bir necha marta takrorlash usuli.

Masalan, "Salom" so‘zini 5 marta chiqarish uchun
print()ni 5 marta yozish mumkin:

    print("Salom")
    print("Salom")
    print("Salom")
    print("Salom")
    print("Salom")

Lekin bu qulay emas.

Sikl bilan buni qisqa qilib yozamiz:

    5 marta "Salom" chiqarish
"""


# ------------------------------------------------------------
# while SIKLI
# ------------------------------------------------------------

"""
while — "shart rost bo‘lib turgan paytda" degani.

Sintaksisi:

    while shart:
        bajariladigan_kod

while sikli shart True bo‘lib turgan vaqt davomida ishlaydi.

Muhim qoida:

  ✔️ Shartdan keyin : belgisi qo‘yiladi
  ✔️ Sikl ichidagi kod 4 ta bo‘sh joy bilan yoziladi
  ✔️ Sikldagi shart bir payt False bo‘lishi kerak
  ✔️ Aks holda cheksiz sikl hosil bo‘ladi
"""


# ------------------------------------------------------------
# HISOBLAGICH (COUNTER) BILAN ISHLASH
# ------------------------------------------------------------

"""
Hisoblagich — sikl necha marta ishlaganini hisoblaydigan
o‘zgaruvchi.

Ko‘pincha i, count, son yoki sanoq kabi nomlar ishlatiladi.
"""

i = 1

while i <= 5:
    print(i)
    i = i + 1

# Natija:
# 1
# 2
# 3
# 4
# 5


# ------------------------------------------------------------
# i = i + 1 VA i += 1 FARQI
# ------------------------------------------------------------

"""
Quyidagi 2 ta yozuv bir xil ishlaydi:

    i = i + 1
    i += 1

i += 1 — qisqaroq va ko‘proq ishlatiladigan usul.
"""

i = 1

while i <= 5:
    print(i)
    i += 1


# ------------------------------------------------------------
# 1 DAN 10 GACHA SONLARNI CHIQARISH
# ------------------------------------------------------------

son = 1

while son <= 10:
    print(son)
    son += 1


# ------------------------------------------------------------
# KAMAYIB BORUVCHI SIKL
# ------------------------------------------------------------

"""
Hisoblagich faqat oshib borishi shart emas.
U kamayib ham borishi mumkin.
"""

son = 10

while son >= 1:
    print(son)
    son -= 1

print("Uchirish!")


# ------------------------------------------------------------
# CHEKSIZ SIKL (INFINITE LOOP)
# ------------------------------------------------------------

"""
Agar sikl ichida shartni o‘zgartirmasak,
sikl cheksiz ishlashi mumkin.

Masalan:
"""

# XAVFLI KOD — ISHGA TUSHIRMANG!
#
# i = 1
#
# while i <= 5:
#     print(i)
#
# Bu yerda i o‘zgarmaydi.
# i doim 1 bo‘lib qoladi.
# Shuning uchun sikl cheksiz ishlaydi.


# TO‘G‘RI KOD:
i = 1

while i <= 5:
    print(i)
    i += 1


# ------------------------------------------------------------
# while VA if FARQI
# ------------------------------------------------------------

"""
if — shartni faqat 1 marta tekshiradi.

while — shartni qayta-qayta tekshiradi.

Misol:
"""

yosh = 18

if yosh >= 18:
    print("Siz voyaga yetgansiz")

# while bilan:
son = 1

while son <= 3:
    print("Bu qator 3 marta chiqadi")
    son += 1


# ------------------------------------------------------------
# break — SIKLDAN CHIQISH
# ------------------------------------------------------------

"""
break — siklni darhol to‘xtatadi.

break ishlaganda siklning qolgan qismi bajarilmaydi.
"""

son = 1

while son <= 10:
    print(son)

    if son == 5:
        break

    son += 1

# Natija:
# 1
# 2
# 3
# 4
# 5


# ------------------------------------------------------------
# break BILAN QIDIRISH
# ------------------------------------------------------------

"""
Kerakli qiymat topilganda siklni to‘xtatish mumkin.
"""

qidirilayotgan_son = 7
son = 1

while son <= 10:
    if son == qidirilayotgan_son:
        print("Son topildi:", son)
        break

    print(son, "qidirilmoqda...")
    son += 1


# ------------------------------------------------------------
# continue — JORIY QADAMNI O‘TKAZIB YUBORISH
# ------------------------------------------------------------

"""
continue — siklning joriy qadamini o‘tkazib yuboradi.

continue’dan keyingi kod ishlamaydi.
Sikl keyingi aylanishga o‘tadi.
"""

son = 0

while son < 10:
    son += 1

    if son == 5:
        continue

    print(son)

# Natija:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10


# ------------------------------------------------------------
# continue BILAN JUFT SONLARNI O‘TKAZIB YUBORISH
# ------------------------------------------------------------

son = 0

while son < 10:
    son += 1

    if son % 2 == 0:
        continue

    print(son)

# Natija:
# 1
# 3
# 5
# 7
# 9


# ------------------------------------------------------------
# while True — CHEKSIZ SIKL
# ------------------------------------------------------------

"""
while True doim ishlaydi.

Undan chiqish uchun odatda break ishlatiladi.

Bu usul menyu, bot va foydalanuvchi bilan doimiy
ishlaydigan dasturlarda ko‘p ishlatiladi.
"""

son = 1

while True:
    print(son)

    if son == 5:
        break

    son += 1


# ------------------------------------------------------------
# while + input()
# ------------------------------------------------------------

"""
while + input() yordamida foydalanuvchidan qayta-qayta
ma’lumot olish mumkin.
"""

while True:
    ism = input("Ismingizni kiriting ('exit' chiqish uchun): ")

    if ism == "exit":
        print("Dastur tugadi")
        break

    print("Assalomu alaykum,", ism)


# ------------------------------------------------------------
# PAROLNI TEKSHIRISH
# ------------------------------------------------------------

"""
Foydalanuvchi to‘g‘ri parol kiritmaguncha,
dastur qayta so‘raydi.
"""

togri_parol = "python123"

while True:
    parol = input("Parolni kiriting: ")

    if parol == togri_parol:
        print("Tizimga muvaffaqiyatli kirdingiz")
        break

    print("Parol noto‘g‘ri. Qaytadan urinib ko‘ring.")


# ------------------------------------------------------------
# CHEKLANGAN URINISHLAR BILAN PAROL
# ------------------------------------------------------------

"""
Foydalanuvchiga 3 ta urinish beramiz.
"""

togri_parol = "python123"
urinishlar = 3

while urinishlar > 0:
    parol = input("Parolni kiriting: ")

    if parol == togri_parol:
        print("Tizimga muvaffaqiyatli kirdingiz")
        break

    urinishlar -= 1
    print("Parol noto‘g‘ri.")
    print("Qolgan urinishlar soni:", urinishlar)

else:
    print("Urinishlar soni tugadi. Tizim bloklandi.")


# ------------------------------------------------------------
# while + else
# ------------------------------------------------------------

"""
while siklining else qismi ham bo‘lishi mumkin.

else faqat sikl tabiiy tugasa ishlaydi.

Agar sikl break orqali tugasa, else ishlamaydi.
"""

son = 1

while son <= 3:
    print(son)
    son += 1
else:
    print("Sikl muvaffaqiyatli tugadi")


# break bo‘lsa else ishlamaydi:
son = 1

while son <= 5:
    print(son)

    if son == 3:
        break

    son += 1
else:
    print("Bu qator chiqmaydi")


# ------------------------------------------------------------
# while + else BILAN SON QIDIRISH
# ------------------------------------------------------------

"""
Agar son topilsa break ishlaydi.
Agar son topilmasa, else ishlaydi.
"""

qidirilayotgan_son = 8
son = 1

while son <= 5:
    if son == qidirilayotgan_son:
        print("Son topildi:", son)
        break

    son += 1
else:
    print("Qidirilgan son topilmadi")


# ------------------------------------------------------------
# AMALIY MISOL 1 — MENYU TIZIMI
# ------------------------------------------------------------

"""
Foydalanuvchi 0 ni tanlamaguncha dastur ishlaydi.
"""

while True:
    print("\n--- MENU ---")
    print("1. Salomlashish")
    print("2. Bugungi dars")
    print("3. Kurs haqida")
    print("0. Chiqish")

    tanlov = input("Tanlovingizni kiriting: ")

    if tanlov == "1":
        print("Assalomu alaykum!")
    elif tanlov == "2":
        print("Bugungi mavzu: While sikli")
    elif tanlov == "3":
        print("Python Foundation kursiga xush kelibsiz")
    elif tanlov == "0":
        print("Dastur tugadi. Xayr!")
        break
    else:
        print("Noto‘g‘ri tanlov. Qaytadan urinib ko‘ring.")


# ------------------------------------------------------------
# AMALIY MISOL 2 — SON TOPISH O‘YINI
# ------------------------------------------------------------

"""
Hozircha sirli sonni o‘zimiz belgilaymiz.

Keyingi darslarda random moduli bilan sirli sonni
avtomatik tanlashni ham o‘rganamiz.
"""

sirli_son = 7

while True:
    taxmin = int(input("1 dan 10 gacha son kiriting: "))

    if taxmin == sirli_son:
        print("Tabriklaymiz! Siz sonni topdingiz!")
        break
    elif taxmin < sirli_son:
        print("Sirli son kattaroq")
    else:
        print("Sirli son kichikroq")


# ------------------------------------------------------------
# AMALIY MISOL 3 — YIG‘INDI HISOBLASH
# ------------------------------------------------------------

"""
Foydalanuvchi 0 kiritsa, dastur to‘xtaydi.
Kiritilgan sonlarning yig‘indisi chiqariladi.
"""

yigindi = 0

while True:
    son = int(input("Son kiriting (0 - tugatish): "))

    if son == 0:
        break

    yigindi += son

print("Kiritilgan sonlar yig‘indisi:", yigindi)


# ------------------------------------------------------------
# AMALIY MISOL 4 — FAQAT MUSBAT SONLARNI HISOBLASH
# ------------------------------------------------------------

"""
Foydalanuvchi 0 kiritsa dastur tugaydi.

Manfiy sonlar hisobga olinmaydi.
"""

yigindi = 0

while True:
    son = int(input("Son kiriting (0 - tugatish): "))

    if son == 0:
        break

    if son < 0:
        print("Manfiy son hisobga olinmadi")
        continue

    yigindi += son

print("Musbat sonlar yig‘indisi:", yigindi)


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — 1 dan 20 gacha:

  while yordamida 1 dan 20 gacha bo‘lgan sonlarni chiqaring.


TOPSHIRIQ 2 — Juft sonlar:

  while yordamida 1 dan 50 gacha bo‘lgan faqat juft
  sonlarni ekranga chiqaring.


TOPSHIRIQ 3 — Teskari sanash:

  10 dan 1 gacha teskari sanang.

  Oxirida:

      "Uchirish!"

  deb chiqaring.


TOPSHIRIQ 4 — Parol:

  To‘g‘ri parolni belgilang:

      12345

  Foydalanuvchi to‘g‘ri parolni kiritmaguncha,
  parolni qayta-qayta so‘rang.


TOPSHIRIQ 5 — 3 ta urinish:

  Foydalanuvchiga 3 ta urinish bering.

  Agar u 3 marta noto‘g‘ri parol kiritsa:

      "Tizim bloklandi"

  deb chiqaring.


TOPSHIRIQ 6 — Sonlar yig‘indisi:

  Foydalanuvchi 0 kiritmaguncha son so‘rang.

  Kiritilgan barcha sonlarning yig‘indisini chiqaring.


TOPSHIRIQ 7 — Mini menyu:

  Quyidagi menyuni while True yordamida yarating:

      1. Ismni chiqarish
      2. Yoshni chiqarish
      3. Kurs haqida
      0. Chiqish

  Foydalanuvchi 0 ni tanlaganda dastur tugasin.
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O‘RGANDIK?
# ------------------------------------------------------------

"""
✔️ Sikl nima va nima uchun kerakligini
✔️ while sikli sintaksisini
✔️ Hisoblagich bilan ishlashni
✔️ i += 1 va i -= 1 ishlatishni
✔️ Cheksiz sikl nima ekanini
✔️ break bilan sikldan chiqishni
✔️ continue bilan joriy qadamni o‘tkazib yuborishni
✔️ while True bilan ishlashni
✔️ while + input() bilan interaktiv dastur yozishni
✔️ while + else ishlashini
✔️ Parol tekshirish dasturini
✔️ Menyu tizimini
✔️ Son topish o‘yinini
"""
