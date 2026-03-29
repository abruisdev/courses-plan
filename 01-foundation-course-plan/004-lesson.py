# ============================================================
#   DARS 4: While Sikl Operatori
#           break, continue, end=" "
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# SIKL (LOOP) NIMA?
# ------------------------------------------------------------

"""
Tasavvur qiling: 10 ta o'quvchiga "Salom!" deb yozishingiz kerak.

  print("Salom!")
  print("Salom!")
  print("Salom!")
  ... (10 marta)

Bu juda zerikarli va noqulay.

Sikl — bu bir xil kodni qayta-qayta bajarish imkonini beradi.
Bir marta yozasiz, Python uni kerakli marta takrorlaydi.

Python'da 2 xil sikl bor:
  while  — shart True bo'lguncha takrorlaydi   (bu darsda)
  for    — ro'yxat yoki ketma-ketlik bo'ylab   (keyingi darsda)
"""


# ============================================================
# WHILE SIKLI — ASOSIY TUSHUNCHA
# ============================================================

"""
while — "shart bajarilguncha davom et" degani.

Sintaksis:
  while shart:
      bajariladigan_kod

ISHLASH TARTIBI:
  1. Shart tekshiriladi
  2. Agar True  → kod bajariladi, 1-qadamga qaytiladi
  3. Agar False → sikl to'xtaydi, keyingi qatorga o'tiladi

  ┌─────────────────────────────────────────┐
  │  while shart:                           │
  │      ┌──────────────────────────────┐   │
  │      │  True bo'lsa: kod bajariladi │◄──┤
  │      │  keyin shart qayta tekshir   │   │
  │      └──────────────────────────────┘   │
  │  False bo'lsa: sikldan chiqiladi        │
  └─────────────────────────────────────────┘

MUHIM:
  Shart biror vaqt False bo'lishi kerak!
  Aks holda sikl CHEKSIZ ishlaydi (bu xato!).
"""

# ── ENG ODDIY MISOL ──────────────────────────────────────────
# 1 dan 5 gacha sonlarni chiqarish

i = 1               # boshlang'ich qiymat — "hisoblagich"
while i <= 5:       # shart: i 5 dan kichik yoki teng bo'lsa
    print(i)        # i ni chiqar
    i = i + 1       # i ni 1 ga oshir (SHART O'ZGARISHI)

# Natija:
# 1
# 2
# 3
# 4
# 5

# ── NIMA SODIR BO'LADI — QADAMLAB ────────────────────────────
"""
  i=1  →  1 <= 5? True  →  print(1)  →  i=2
  i=2  →  2 <= 5? True  →  print(2)  →  i=3
  i=3  →  3 <= 5? True  →  print(3)  →  i=4
  i=4  →  4 <= 5? True  →  print(4)  →  i=5
  i=5  →  5 <= 5? True  →  print(5)  →  i=6
  i=6  →  6 <= 5? False →  SIKL TUGADI
"""

print("---")

# ── i += 1 — QISQA YOZUV ─────────────────────────────────────
"""
  i = i + 1   →  i += 1    (bir xil ma'no, qisqaroq yozish)
  i = i - 1   →  i -= 1
  i = i * 2   →  i *= 2
  i = i / 2   →  i /= 2
"""
i = 1
while i <= 5:
    print(i)
    i += 1       # i = i + 1 bilan bir xil


# ============================================================
# WHILE SIKLI — KO'PROQ MISOLLAR
# ============================================================

print("\n=== 5 marta Salom ===")
# MISOL 1 — 5 marta "Salom!" chiqarish
n = 1
while n <= 5:
    print(n, "- Salom!")
    n += 1

print("\n=== Juft sonlar ===")
# MISOL 2 — 1 dan 20 gacha juft sonlar
i = 2
while i <= 20:
    print(i)
    i += 2      # har safar 2 ga oshirib ketamiz

print("\n=== Ortga hisoblash ===")
# MISOL 3 — 10 dan 1 gacha ortga sanash
hisoblagich = 10
while hisoblagich >= 1:
    print(hisoblagich)
    hisoblagich -= 1    # har safar 1 ga kamaytiramiz
print("Start!")

print("\n=== Yig'indi ===")
# MISOL 4 — 1 dan 100 gacha sonlar yig'indisi
yigindi = 0
i = 1
while i <= 100:
    yigindi += i    # yigindi = yigindi + i
    i += 1
print("1 dan 100 gacha yig'indi:", yigindi)   # Natija: 5050

print("\n=== Ko'paytma ===")
# MISOL 5 — 5 ning ko'paytma jadvali
i = 1
while i <= 10:
    print("5 x", i, "=", 5 * i)
    i += 1


# ============================================================
# CHEKSIZ SIKL VA TRUE
# ============================================================

"""
Ba'zan sikl shartini oldindan bilmaymiz.
Masalan, foydalanuvchi "chiq" deguncha dastur ishlaydi.

Buning uchun:  while True:  ishlatiladi.

  while True:
      kod...
      # sikldan chiqish uchun break ishlatiladi (keyingi bo'limda)

DIQQAT:
  while True  →  cheksiz sikl!
  Faqat break bilan to'xtatish mumkin.
  break bo'lmasa, dastur hech qachon to'xtamaydi!
"""

# MISOL — Parol so'rash
while True:
    parol = input("Parolni kiriting: ")
    if parol == "python123":
        print("Xush kelibsiz!")
        break           # to'g'ri parol → sikldan chiq
    else:
        print("Xato parol, qayta urinib ko'ring...")


# ============================================================
# break — SIKLNI TO'XTATISH
# ============================================================

"""
break — siklni darhol to'xtatadi va sikldan chiqadi.

  while shart:
      if boshqa_shart:
          break       ← shu yerga yetganda sikl tugaydi
      kod...

Qachon ishlatiladi?
  - Kerakli narsani topganda davom etish shart emas
  - Foydalanuvchi "chiq" deb yozganda
  - Xato yuz berganda siklni to'xtatish kerakda
"""

print("\n=== break misoli 1 ===")
# MISOL 1 — 7 ga yetganda to'xtat
i = 1
while i <= 20:
    if i == 7:
        print("7 ga yetdik, to'xtatamiz!")
        break       # sikldan chiq
    print(i)
    i += 1
# Natija: 1 2 3 4 5 6 → keyin to'xtaydi

print("\n=== break misoli 2 ===")
# MISOL 2 — Birinchi juft sonni topib to'xtat
i = 1
while i <= 100:
    if i % 2 == 0:
        print("Birinchi juft son:", i)
        break
    i += 1
# Natija: Birinchi juft son: 2

print("\n=== break misoli 3: Taxmin o'yini ===")
# MISOL 3 — Taxmin o'yini: 3 ta urinish
maxfiy = 42
urinish = 0

while True:
    urinish += 1
    taxmin = int(input(f"{urinish}-urinish: Son nechta? "))

    if taxmin == maxfiy:
        print(f"Barakalla! {urinish}-urinishda topdingiz!")
        break
    elif taxmin < maxfiy:
        print("Kattaroq son!")
    else:
        print("Kichikroq son!")

    if urinish == 3:
        print(f"Urinishlar tugadi. Javob: {maxfiy}")
        break


# ============================================================
# continue — KEYINGI QADAMGA O'TISH
# ============================================================

"""
continue — joriy qadamni o'tkazib yuboradi va
           siklning boshiga qaytadi (shart qayta tekshiriladi).

  while shart:
      if boshqa_shart:
          continue    ← bu qatordan pastdagi kod bajarilmaydi,
                         to'g'ridan-to'g'ri shart tekshirishga qaytadi
      kod...

break  vs  continue farqi:
  break    →  siklni BUTUNLAY to'xtatadi
  continue →  faqat JORIY QADAMNI o'tkazadi, sikl davom etadi
"""

print("\n=== continue misoli 1 ===")
# MISOL 1 — 5 ni o'tkazib, qolganlarini chiqar
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue    # 5 ni chiqarma, keyingisiga o't
    print(i)
# Natija: 1 2 3 4  6 7 8 9 10  (5 yo'q!)

print("\n=== continue misoli 2 ===")
# MISOL 2 — Faqat toq sonlarni chiqar (juftlarni o'tkazib yubor)
i = 0
while i < 15:
    i += 1
    if i % 2 == 0:
        continue    # juft son → o'tkazib yubor
    print(i)        # faqat toq sonlar chiqadi
# Natija: 1 3 5 7 9 11 13 15

# ── break va continue birga ───────────────────────────────────
print("\n=== break va continue birga ===")
# 1 dan 20 gacha: 3 ga bo'linadiganlarni chiqar, 15 ga yetsa to'xtat
i = 0
while i < 20:
    i += 1
    if i == 15:
        print("15 ga yetdik, to'xtatamiz!")
        break
    if i % 3 != 0:
        continue    # 3 ga bo'linmaydigan → o'tkazib yubor
    print(i)        # faqat 3 ga bo'linadiganlar
# Natija: 3 6 9 12  → keyin to'xtaydi


# ============================================================
# end=" " — CHIQARISH FORMATINI O'ZGARTIRISH
# ============================================================

"""
Odatda print() har chiqarishdan keyin yangi qatorga o'tadi.
Lekin ba'zan barcha chiqishlarni BIR QATORDA ko'rsatish kerak.

print() funksiyasining end parametri shuni boshqaradi.

  print("narsa", end="...")
                      ^^^
                      yangi qator o'rniga shu yoziladi

Standart holat:  end="\\n"   (yangi qator belgisi)
Biz o'zgartirsak: end=" "   (bo'sh joy)
                  end=", "  (vergul va bo'sh joy)
                  end=""    (hech narsa — to'g'ridan-to'g'ri yopishadi)
"""

print("\n=== end misoli 1: yangi qator (odatiy) ===")
# Odatiy — har biri yangi qatorda
print("olma")
print("nok")
print("uzum")
# Natija:
# olma
# nok
# uzum

print("\n=== end misoli 2: end=\" \" bilan ===")
# end=" " — barchasi bir qatorda, orasida bo'sh joy
print("olma", end=" ")
print("nok", end=" ")
print("uzum", end=" ")
print()   # oxirida yangi qatorga o'tish uchun bo'sh print
# Natija: olma nok uzum

print("\n=== end misoli 3: while + end=\" \" ===")
# While sikli bilan bir qatorda chiqarish
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()   # natija yangi qatordan boshlansin
# Natija: 1 2 3 4 5 6 7 8 9 10

print("\n=== end misoli 4: end=\", \" ===")
# Vergul bilan ajratib chiqarish
i = 1
while i <= 5:
    print(i, end=", ")
    i += 1
print()
# Natija: 1, 2, 3, 4, 5,

print("\n=== end misoli 5: end=\"\" ===")
# Hech narsa qo'shmasdan — to'g'ridan-to'g'ri yopishadi
print("Py", end="")
print("thon", end="")
print("!")
# Natija: Python!

print("\n=== end misoli 6: Ko'paytma jadvali ===")
# Ko'paytma jadvali — 3 ning jadvali bir qatorda
i = 1
while i <= 10:
    print(f"3x{i}={3*i}", end="  ")
    i += 1
print()
# Natija: 3x1=3  3x2=6  3x3=9  ...  3x10=30

print("\n=== end misoli 7: Yulduzlar ===")
# Har safar bitta yulduz qo'shib chiqarish
i = 1
while i <= 8:
    print("*", end="")
    i += 1
print()
# Natija: ********


# ============================================================
# WHILE + INPUT() — FOYDALANUVCHI BILAN ISHLASH
# ============================================================

"""
while va input() birgalikda juda kuchli.
Foydalanuvchi nimadir kiritmaguncha dastur ishlaydi.
"""

# MISOL 1 — Foydalanuvchi "chiq" yozmaguncha davom et
while True:
    xabar = input("Xabar yozing ('chiq' — tugatish): ")
    if xabar == "chiq":
        print("Dasturdan chiqdingiz. Xayr!")
        break
    print("Siz yozdingiz:", xabar)

# MISOL 2 — To'g'ri javob topguncha so'ra
togri_javob = "python" or "Python" or "PYTHON"
while True:
    javob = input("Eng mashhur dasturlash tili? ").lower()
    if javob == togri_javob:
        print("To'g'ri! Barakalla!")
        break
    else:
        print("Noto'g'ri, qayta urinib ko'ring...")

# MISOL 3 — Sonlar kiritib yig'indi hisoblash
yigindi = 0
soni = 0
print("Sonlarni kiriting. Tugatish uchun 0 kiriting.")
while True:
    son = int(input("Son: "))
    if son == 0:
        break
    yigindi += son
    soni += 1
print(f"\n{soni} ta son kiritildi.")
print(f"Yig'indi: {yigindi}")
if soni > 0:
    print(f"O'rtacha: {round(yigindi / soni, 2)}")


# ============================================================
# ELSE — WHILE BILAN BIRGA
# ============================================================

"""
while siklida else ham ishlatish mumkin.
else bloki sikl ODATIY tugaganda (break bo'lmasa) bajariladi.

  while shart:
      kod...
  else:
      # shart False bo'lib tugasa — bu bajariladi
      # break bilan tugasa — bu BAJARILMAYDI

Qachon foydali?
  Biror narsani qidirgan bo'lib, topa olmasangiz — xabar berish uchun.
"""

print("\n=== while-else misoli ===")
# 1 dan 10 gacha sonlar ichida 7 ni qidirish
i = 1
qidirilayotgan = 7

while i <= 10:
    if i == qidirilayotgan:
        print(f"{qidirilayotgan} topildi!")
        break
    i += 1
else:
    print(f"{qidirilayotgan} topilmadi")   # break bo'lmasa ishlaydi
# Natija: 7 topildi!

# ── Agar bo'lmagan son qidirilsa ─────────────────────────────
i = 1
qidirilayotgan = 15

while i <= 10:
    if i == qidirilayotgan:
        print(f"{qidirilayotgan} topildi!")
        break
    i += 1
else:
    print(f"{qidirilayotgan} 1-10 oralig'ida yo'q")
# Natija: 15 1-10 oralig'ida yo'q


# ============================================================
# TO'LIQ AMALIY DASTUR
# ============================================================

"""
Quyidagi dastur hamma narsani birga ishlatadi.
"""

# --- Oddiy ATM Dasturi ---

balans = 500_000     # so'm
parol  = "1234"

print("=" * 30)
print("   VIRTUAL ATM   ")
print("=" * 30)

# # Parol tekshiruvi — 3 ta urinish
urinish = 0
kirish = False

while urinish < 3:
    kiritilgan = input("Parolni kiriting: ")
    urinish += 1
    if kiritilgan == parol:
        kirish = True
        break
    else:
        qolgan = 3 - urinish
        if qolgan > 0:
            print(f"Xato parol! {qolgan} ta urinish qoldi.")

if not kirish:
    print("Karta bloklanди! Bankka murojaat qiling.")
else:
    print(f"\nXush kelibsiz! Balansingiz: {balans:,} so'm")

    while True:
        print("\n--- MENYU ---")
        print("1 - Balansni ko'rish")
        print("2 - Pul yechish")
        print("3 - Chiqish")

        tanlov = input("Tanlang (1/2/3): ")

        if tanlov == "1":
            print(f"Balansingiz: {balans:,} so'm")

        elif tanlov == "2":
            miqdor = int(input("Qancha yechmoqchisiz? "))
            if miqdor <= 0:
                print("Noto'g'ri miqdor!")
                continue
            if miqdor > balans:
                print("Mablag' yetarli emas!")
            else:
                balans -= miqdor
                print(f"{miqdor:,} so'm yechildi.")
                print(f"Qoldiq: {balans:,} so'm")

        elif tanlov == "3":
            print("Xayr! Kartangizni unutmang!")
            break

        else:
            print("Noto'g'ri tanlov, qayta urinib ko'ring.")


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Oddiy while:
  1 dan 50 gacha sonlarni ekranga chiqaring.
  Barchasi BIR QATORDA bo'lsin (end=" " ishlating).

TOPSHIRIQ 2 — Yig'indi:
  1 dan 10 gacha sonlarning yig'indisini while sikli bilan hisoblang.
  Natijani "1+2+3+...+10 = 55" formatida chiqaring.

TOPSHIRIQ 3 — break:
  Foydalanuvchidan ketma-ket sonlar oling.
  Agar manfiy son kiritilsa — sikl to'xtatilsin va
  "Manfiy son kiritildi, dastur to'xtatildi" deb yozilsin.

TOPSHIRIQ 4 — continue:
  1 dan 30 gacha sonlar ichida faqat 3 ga ham, 5 ga ham
  bo'linadiganlarni (ya'ni 15 ga bo'linadiganlarni) chiqaring.
  (Qolganlarini continue bilan o'tkazing)

TOPSHIRIQ 5 — end=" ":
  Ko'paytma jadvali: Foydalanuvchidan son oling (1-10 orasida),
  o'sha sonning ko'paytma jadvalini chiqaring:
    Misol: son = 7
    7 x 1 = 7
    7 x 2 = 14
    ...
    7 x 10 = 70

TOPSHIRIQ 6 (Qo'shimcha) — Login tizimi:
  Foydalanuvchiga 3 ta urinish bering:
    - To'g'ri login: "user", to'g'ri parol: "pass123"
    - Har xato urinishda: "Xato! X ta urinish qoldi." chiqaring
    - 3 ta urinish tugasa: "Hisob vaqtincha bloklanди!"
    - To'g'ri kirsа:       "Tizimga xush kelibsiz!"
"""


# ------------------------------------------------------------
# QUSHIMCHA RESURSLAR (Uyga vazifa uchun)
# ------------------------------------------------------------

"""
📚 RASMIY HUJJATLAR:
   https://docs.python.org/3/tutorial/controlflow.html#the-while-statement
   — while sikli haqida rasmiy ma'lumot

🌐 W3SCHOOLS:
   https://www.w3schools.com/python/python_while_loops.asp
   — while sikli, break, continue
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ Sikl nima va nima uchun kerak
✔️ while sikli — sintaksis va ishlash tartibi
✔️ Hisoblagich (i = 0, i += 1) bilan ishlash
✔️ break    — siklni butunlay to'xtatish
✔️ continue — joriy qadamni o'tkazib, siklni davom ettirish
✔️ end=" "  — print() da yangi qator o'rniga boshqa belgi
✔️ while True — cheksiz sikl (break bilan to'xtatiladi)
✔️ while + input() — foydalanuvchi bilan interaktiv ishlash
✔️ while + else — odatiy tugashda qo'shimcha amal

  break    →  ■ STOP — sikldan chiqadi
  continue →  ↩ SKIP — joriy qadamni o'tkazadi, davom etadi
  end=" "  →  yangi qator o'rniga bo'sh joy (yoki boshqa belgi)
"""