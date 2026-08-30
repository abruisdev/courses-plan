# ============================================================
#   DARS 5: Pythonda For Sikl Operatori
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================


# ------------------------------------------------------------
# DARSNING MAQSADI
# ------------------------------------------------------------

"""
Bugungi darsda:

  ✔️ for sikli nima ekanini bilib olamiz
  ✔️ range() funksiyasi bilan ishlaymiz
  ✔️ range(stop), range(start, stop), range(start, stop, step)
     ko‘rinishlarini o‘rganamiz
  ✔️ for + string bilan ishlaymiz
  ✔️ for + list bilan ishlaymiz
  ✔️ break va continue operatorlarini for’da ishlatamiz
  ✔️ Ichma-ich sikllar yozamiz
  ✔️ Ko‘paytma jadvali tuzamiz
  ✔️ Tub sonni aniqlaymiz
  ✔️ Baholar tahlilini qilamiz
  ✔️ Shakllar chizamiz
  ✔️ for va while farqini bilib olamiz
"""


# ------------------------------------------------------------
# for SIKLI NIMA?
# ------------------------------------------------------------

"""
for sikli — ketma-ketlik ichidagi elementlarni
birma-bir ko‘rib chiqish uchun ishlatiladi.

Ketma-ketliklar:

  - range()
  - string
  - list
  - tuple
  - set
  - dictionary

Sintaksisi:

    for o_zgaruvchi in ketma_ketlik:
        bajariladigan_kod
"""


# ------------------------------------------------------------
# ODDIY for SIKLI
# ------------------------------------------------------------

"""
for sikli bilan biror matnni bir necha marta chiqarish mumkin.
"""

for i in range(5):
    print("Assalomu alaykum!")

# Natija:
# Assalomu alaykum!
# Assalomu alaykum!
# Assalomu alaykum!
# Assalomu alaykum!
# Assalomu alaykum!


# ------------------------------------------------------------
# range() FUNKSIYASI
# ------------------------------------------------------------

"""
range() — sonlar ketma-ketligini yaratadi.

range() 3 xil usulda ishlatiladi:

    range(stop)
    range(start, stop)
    range(start, stop, step)

Muhim qoida:

  range()dagi stop qiymati NATIJAGA KIRMAYDI.
"""


# ------------------------------------------------------------
# range(stop)
# ------------------------------------------------------------

"""
range(stop) — 0 dan stop - 1 gacha sonlar yaratadi.
"""

for son in range(5):
    print(son)

# Natija:
# 0
# 1
# 2
# 3
# 4


# ------------------------------------------------------------
# range(start, stop)
# ------------------------------------------------------------

"""
range(start, stop) — start dan boshlanadi,
stop - 1 gacha davom etadi.
"""

for son in range(1, 6):
    print(son)

# Natija:
# 1
# 2
# 3
# 4
# 5


# ------------------------------------------------------------
# range(start, stop, step)
# ------------------------------------------------------------

"""
step — qadam miqdorini belgilaydi.

Masalan, 2 qadam bilan yurish:
"""

for son in range(0, 11, 2):
    print(son)

# Natija:
# 0
# 2
# 4
# 6
# 8
# 10


# Toq sonlarni chiqarish
for son in range(1, 11, 2):
    print(son)

# Natija:
# 1
# 3
# 5
# 7
# 9


# ------------------------------------------------------------
# TESKARI range()
# ------------------------------------------------------------

"""
Teskari sanash uchun step manfiy bo‘ladi.

Masalan:

    range(10, 0, -1)

10 dan boshlanadi va 1 gacha tushadi.
"""

for son in range(10, 0, -1):
    print(son)

print("Uchirish!")


# ------------------------------------------------------------
# for + STRING
# ------------------------------------------------------------

"""
String — belgilar ketma-ketligi.

for yordamida string ichidagi har bir harfni
alohida ko‘rib chiqish mumkin.
"""

ism = "Ali"

for harf in ism:
    print(harf)

# Natija:
# A
# l
# i


# So‘zdagi harflarni tartib raqami bilan chiqarish
soz = "Python"
raqam = 1

for harf in soz:
    print(raqam, "-", harf)
    raqam += 1


# Unli harflarni aniqlash
matn = "Abruisdev"
unlilar = "aeiouAEIOU"

for harf in matn:
    if harf in unlilar:
        print(harf, "- unli harf")


# ------------------------------------------------------------
# for + LIST
# ------------------------------------------------------------

"""
List — bir nechta ma’lumotni bitta joyda saqlash usuli.

List mavzusini keyin batafsil o‘rganamiz.
Hozircha for bilan list ichidagi elementlarni ko‘rib chiqamiz.
"""

ismlar = ["Ali", "Vali", "Hasan", "Husan"]

for ism in ismlar:
    print("Assalomu alaykum,", ism)


# Sonlardan iborat list
sonlar = [10, 25, 30, 45, 50]

for son in sonlar:
    print(son)


# List ichidagi sonlarning kvadratini chiqarish
sonlar = [1, 2, 3, 4, 5]

for son in sonlar:
    print(son, "ning kvadrati:", son ** 2)


# ------------------------------------------------------------
# break — SIKLDAN CHIQISH
# ------------------------------------------------------------

"""
break — siklni darhol to‘xtatadi.

Kerakli qiymat topilganda yoki biror shart bajarilganda
sikldan chiqish uchun ishlatiladi.
"""

for son in range(1, 11):
    print(son)

    if son == 5:
        break

# Natija:
# 1
# 2
# 3
# 4
# 5


# List ichidan ism qidirish
ismlar = ["Ali", "Vali", "Hasan", "Husan"]
qidirilayotgan_ism = "Hasan"

for ism in ismlar:
    if ism == qidirilayotgan_ism:
        print("Ism topildi:", ism)
        break


# ------------------------------------------------------------
# continue — JORIY QADAMNI O‘TKAZIB YUBORISH
# ------------------------------------------------------------

"""
continue — joriy qadamdagi qolgan kodni o‘tkazib yuboradi.

Sikl keyingi aylanishga o‘tadi.
"""

for son in range(1, 11):
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


# Juft sonlarni o‘tkazib yuborish
for son in range(1, 11):
    if son % 2 == 0:
        continue

    print(son)

# Natija:
# 1
# 3
# 5
# 7
# 9


# Manfiy sonlarni o‘tkazib yuborish
sonlar = [10, -5, 20, -8, 15, 0]

for son in sonlar:
    if son < 0:
        continue

    print(son)


# ------------------------------------------------------------
# ICHMA-ICH SIKLLAR (NESTED LOOPS)
# ------------------------------------------------------------

"""
Ichma-ich sikl — for ichida yana for ishlatish.

Tashqi sikl 1 marta aylanganda,
ichki sikl to‘liq aylanib chiqadi.

Masalan:

    tashqi sikl: 3 marta
    ichki sikl: 2 marta

    jami: 3 * 2 = 6 marta ishlaydi
"""

for tashqi in range(1, 4):
    print("Tashqi sikl:", tashqi)

    for ichki in range(1, 3):
        print("   Ichki sikl:", ichki)


# ------------------------------------------------------------
# AMALIY MISOL 1 — KO‘PAYTMA JADVALI
# ------------------------------------------------------------

son = int(input("Ko‘paytma jadvali uchun son kiriting: "))

for i in range(1, 11):
    print(son, "x", i, "=", son * i)


# 1 dan 10 gacha barcha ko‘paytma jadvali
for son in range(1, 11):
    print("\n---", son, "karra jadvali ---")

    for i in range(1, 11):
        print(son, "x", i, "=", son * i)


# ------------------------------------------------------------
# AMALIY MISOL 2 — TUB SONNI ANIQLASH
# ------------------------------------------------------------

"""
Tub son — faqat 1 ga va o‘ziga bo‘linadigan son.

Masalan:

  Tub sonlar:
      2, 3, 5, 7, 11, 13

  Tub bo‘lmagan sonlar:
      1, 4, 6, 8, 9, 10
"""

son = int(input("Son kiriting: "))

if son < 2:
    print(son, "tub son emas")
else:
    tub_son = True

    for boluvchi in range(2, son):
        if son % boluvchi == 0:
            tub_son = False
            break

    if tub_son:
        print(son, "tub son")
    else:
        print(son, "tub son emas")


# ------------------------------------------------------------
# AMALIY MISOL 3 — BAHOLAR TAHLILI
# ------------------------------------------------------------

baholar = [85, 72, 90, 55, 68, 100, 43]

yigindi = 0

for baho in baholar:
    print("Baho:", baho)
    yigindi += baho

orta_baho = yigindi / len(baholar)

print("Baholar yig‘indisi:", yigindi)
print("O‘rtacha baho:", orta_baho)
print("Eng katta baho:", max(baholar))
print("Eng kichik baho:", min(baholar))


# O‘tgan va o‘tmagan o‘quvchilar soni
otganlar = 0
otmaganlar = 0

for baho in baholar:
    if baho >= 56:
        otganlar += 1
    else:
        otmaganlar += 1

print("O‘tganlar soni:", otganlar)
print("O‘tmaganlar soni:", otmaganlar)


# ------------------------------------------------------------
# AMALIY MISOL 4 — TO‘G‘RI TO‘RTBURCHAK CHIZISH
# ------------------------------------------------------------

qatorlar = 4
ustunlar = 6

for qator in range(qatorlar):
    for ustun in range(ustunlar):
        print("*", end=" ")

    print()

# Natija:
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *


# ------------------------------------------------------------
# AMALIY MISOL 5 — UCHBURCHAK CHIZISH
# ------------------------------------------------------------

qatorlar = 5

for qator in range(1, qatorlar + 1):
    print("*" * qator)

# Natija:
# *
# **
# ***
# ****
# *****


# ------------------------------------------------------------
# AMALIY MISOL 6 — TESKARI UCHBURCHAK
# ------------------------------------------------------------

qatorlar = 5

for qator in range(qatorlar, 0, -1):
    print("*" * qator)

# Natija:
# *****
# ****
# ***
# **
# *


# ------------------------------------------------------------
# AMALIY MISOL 7 — PIRAMIDA
# ------------------------------------------------------------

qatorlar = 5

for qator in range(1, qatorlar + 1):
    bosh_joy = " " * (qatorlar - qator)
    yulduzlar = "*" * (2 * qator - 1)

    print(bosh_joy + yulduzlar)

# Natija:
#     *
#    ***
#   *****
#  *******
# *********


# ------------------------------------------------------------
# for VA while FARQI
# ------------------------------------------------------------

"""
for va while ikkalasi ham sikl, lekin ishlatilish holati farq qiladi.

for ishlatiladi:

  ✔️ Takrorlanish soni oldindan ma’lum bo‘lsa
  ✔️ range() bilan ishlaganda
  ✔️ String yoki list ichidagi elementlarni ko‘rganda

while ishlatiladi:

  ✔️ Takrorlanish soni oldindan noma’lum bo‘lsa
  ✔️ Foydalanuvchi "exit" yozmaguncha ishlaydigan dasturda
  ✔️ To‘g‘ri parol kiritilmaguncha ishlaydigan dasturda
  ✔️ Menyu tizimida

Misol:

  1 dan 10 gacha sonlarni chiqarish:
      for qulayroq

  Parol to‘g‘ri kiritilmaguncha so‘rash:
      while qulayroq
"""


# for misoli
for son in range(1, 6):
    print(son)

# while misoli
son = 1

while son <= 5:
    print(son)
    son += 1


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Sonlarni chiqarish:

  for va range() yordamida 1 dan 100 gacha
  bo‘lgan sonlarni ekranga chiqaring.


TOPSHIRIQ 2 — Juft sonlar:

  1 dan 50 gacha bo‘lgan faqat juft sonlarni chiqaring.


TOPSHIRIQ 3 — Teskari sanash:

  20 dan 1 gacha teskari sanang.

  Oxirida:

      "Uchirish!"

  deb chiqaring.


TOPSHIRIQ 4 — Ismdagi harflar:

  Foydalanuvchidan ism oling.

  for yordamida ismdagi har bir harfni alohida qatorga chiqaring.


TOPSHIRIQ 5 — Unli harflar:

  Foydalanuvchidan so‘z oling.

  Ushbu so‘zdagi unli harflar sonini aniqlang.

  Unli harflar:

      a, e, i, o, u


TOPSHIRIQ 6 — Ko‘paytma jadvali:

  Foydalanuvchidan son oling.

  Shu sonning 1 dan 10 gacha ko‘paytma jadvalini chiqaring.


TOPSHIRIQ 7 — Tub son:

  Foydalanuvchidan son oling.

  for yordamida ushbu son tub yoki tub emasligini aniqlang.


TOPSHIRIQ 8 — Shakl chizish:

  Quyidagi shaklni for yordamida chiqaring:

      *
      **
      ***
      ****
      *****


TOPSHIRIQ 9 — Baholar:

  Quyidagi baholar listi berilgan:

      baholar = [65, 80, 45, 90, 55, 100, 72]

  for yordamida:

    - O‘rtacha bahoni aniqlang
    - Nechta o‘quvchi o‘tganini aniqlang
    - Nechta o‘quvchi o‘tmaganini aniqlang
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O‘RGANDIK?
# ------------------------------------------------------------

"""
✔️ for sikli nima ekanini
✔️ range(stop) ishlatishni
✔️ range(start, stop) ishlatishni
✔️ range(start, stop, step) ishlatishni
✔️ Teskari range() yozishni
✔️ for + string bilan ishlashni
✔️ for + list bilan ishlashni
✔️ break bilan sikldan chiqishni
✔️ continue bilan joriy qadamni o‘tkazib yuborishni
✔️ Ichma-ich sikllarni
✔️ Ko‘paytma jadvalini yozishni
✔️ Tub sonni aniqlashni
✔️ Baholarni tahlil qilishni
✔️ Shakllar chizishni
✔️ for va while farqini
"""
