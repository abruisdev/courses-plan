# ============================================================
#   IMTIHON: 1—5 Mavzular
#   Vaqt: 2 soat  |  Jami: 100 ball
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# O'QUVCHI MA'LUMOTLARI
# ------------------------------------------------------------
# Ism-familiya : ________________________________
# Sana         : ________________________________
# Sinf / Guruh : ________________________________
# ------------------------------------------------------------

"""
IMTIHON QOIDALARI:
  ✔️ Har bir savolni diqqat bilan o'qing
  ✔️ Kod yozadigan savollarda faqat shu faylda ishlang
  ✔️ Vaqt: 2 soat (120 daqiqa)
  ✔️ Jami: 100 ball

BALL TAQSIMOTI:
  1-Bo'lim  — Test savollari         (20 savol × 1 ball  = 20 ball)
  2-Bo'lim  — Kod o'qish             (10 savol × 2 ball  = 20 ball)
  3-Bo'lim  — Xatoni toping          ( 5 savol × 2 ball  = 10 ball)
  4-Bo'lim  — Kod yozish (kichik)    ( 5 savol × 4 ball  = 20 ball)
  5-Bo'lim  — Kod yozish (o'rta)     ( 3 savol × 6 ball  = 18 ball)
  6-Bo'lim  — Kod yozish (katta)     ( 2 savol × 6 ball  = 12 ball)
  ─────────────────────────────────────────────────────────
  JAMI:                                               100 ball

BAHO MEZONI:
  90 — 100  →  A  (Mukammal)
  80 —  89  →  B  (Yaxshi)
  70 —  79  →  C  (Qoniqarli)
  50 —  69  →  D  (O'rtacha)
   0 —  49  →  F  (O'tmadi)
"""


# ============================================================
#   1-BO'LIM: TEST SAVOLLARI
#   20 savol × 1 ball = 20 ball
#   Ko'rsatma: To'g'ri javobni ( ) ichiga X qo'yib belgilang.
# ============================================================

"""
──────────────────────────────────────────────────────────────
SAVOL 1. Quyidagi kod nima chiqaradi?
         print(10 // 3)

  ( ) 3.33
  ( ) 3.0
  ( ) 3           ← TO'G'RI (TEACHER)
  ( ) 1

──────────────────────────────────────────────────────────────
SAVOL 2. Pythonda izoh qanday yoziladi?

  ( ) // Bu izoh
  ( ) /* Bu izoh */
  ( ) # Bu izoh    ← TO'G'RI (TEACHER)
  ( ) -- Bu izoh

──────────────────────────────────────────────────────────────
SAVOL 3. input() funksiyasi qaysi turni qaytaradi?

  ( ) int
  ( ) float
  ( ) bool
  ( ) str           ← TO'G'RI (TEACHER)

──────────────────────────────────────────────────────────────
SAVOL 4. Quyidagining natijasi qanday?
         print(2 ** 10)

  ( ) 20
  ( ) 1024          ← TO'G'RI (TEACHER)
  ( ) 210
  ( ) 512

──────────────────────────────────────────────────────────────
SAVOL 5. bool("") qanday natija beradi?

  ( ) True
  ( ) False         ← TO'G'RI (TEACHER)
  ( ) None
  ( ) Xato chiqadi

──────────────────────────────────────────────────────────────
SAVOL 6. Quyidagi kod nima chiqaradi?
         x = 7
         print(x % 3)

  ( ) 2             ← TO'G'RI (TEACHER)
  ( ) 3
  ( ) 1
  ( ) 0

──────────────────────────────────────────────────────────────
SAVOL 7. range(2, 10, 3) qanday sonlarni beradi?

  ( ) 2, 5, 8       ← TO'G'RI (TEACHER)
  ( ) 2, 4, 6, 8
  ( ) 3, 6, 9
  ( ) 2, 5, 8, 11

──────────────────────────────────────────────────────────────
SAVOL 8. while siklidagi break buyrug'i nima qiladi?

  ( ) Joriy qadamni o'tkazib yuboradi
  ( ) Siklni butunlay to'xtatadi      ← TO'G'RI (TEACHER)
  ( ) Siklni boshidan qaytaradi
  ( ) Yangi shart qo'shadi

──────────────────────────────────────────────────────────────
SAVOL 9. Quyidagi ifoda qanday natija beradi?
         print(5 > 3 and 2 < 1)

  ( ) True
  ( ) False         ← TO'G'RI (TEACHER)
  ( ) None
  ( ) Xato chiqadi

──────────────────────────────────────────────────────────────
SAVOL 10. int(3.99) qanday natija beradi?

  ( ) 4   (yaxlitlaydi)
  ( ) 3   (kasr qismini tashlab yuboradi)   ← TO'G'RI (TEACHER)
  ( ) 3.99
  ( ) Xato chiqadi

──────────────────────────────────────────────────────────────
SAVOL 11. Quyidagi kod necha marta "Salom" chiqaradi?
          for i in range(3):
              print("Salom")

  ( ) 2
  ( ) 4
  ( ) 3             ← TO'G'RI (TEACHER)
  ( ) 0

──────────────────────────────────────────────────────────────
SAVOL 12. continue buyrug'i nima qiladi?

  ( ) Siklni to'xtatadi
  ( ) Siklni boshiga qaytaradi
  ( ) Joriy qadamni o'tkazib, siklni davom ettiradi   ← TO'G'RI (TEACHER)
  ( ) Yangi o'zgaruvchi yaratadi

──────────────────────────────────────────────────────────────
SAVOL 13. O'zgaruvchi nomida quyidagilardan qaysi biri
          ishlatilishi MUMKIN EMAS?

  ( ) pastki chiziq (_)
  ( ) harf (a-z)
  ( ) raqam (boshida)    ← TO'G'RI (TEACHER)
  ( ) katta harf (A-Z)

──────────────────────────────────────────────────────────────
SAVOL 14. Quyidagi kodda i necha marta oshadi?
          i = 0
          while i < 5:
              i += 1

  ( ) 4
  ( ) 6
  ( ) 5             ← TO'G'RI (TEACHER)
  ( ) 0

──────────────────────────────────────────────────────────────
SAVOL 15. Tashqi sikl 4 marta, ichki sikl 3 marta ishlasa,
          ichki sikldagi kod jami necha marta bajariladi?

  ( ) 7
  ( ) 4
  ( ) 3
  ( ) 12            ← TO'G'RI (TEACHER)

──────────────────────────────────────────────────────────────
SAVOL 16. Quyidagi ifoda qanday natija beradi?
          print(not (5 > 10))

  ( ) False
  ( ) True          ← TO'G'RI (TEACHER)
  ( ) None
  ( ) 5

──────────────────────────────────────────────────────────────
SAVOL 17. Quyidagi kodda xato bormi?
          if x = 5:
              print("Besh")

  ( ) Xato yo'q
  ( ) Xato bor, = o'rniga == ishlatilishi kerak  ← TO'G'RI (TEACHER)
  ( ) Xato bor, print yozilmagan
  ( ) Xato bor, if katta harf bilan yozilishi kerak

──────────────────────────────────────────────────────────────
SAVOL 18. abs(-99) qanday natija beradi?

  ( ) -99
  ( ) 99            ← TO'G'RI (TEACHER)
  ( ) 0
  ( ) Xato chiqadi

──────────────────────────────────────────────────────────────
SAVOL 19. Quyidagi kodda necha ta o'zgaruvchi yaratildi?
          a = b = c = 10

  ( ) 1
  ( ) 2
  ( ) 3             ← TO'G'RI (TEACHER)
  ( ) 10

──────────────────────────────────────────────────────────────
SAVOL 20. for sikli for + else da else qachon bajariladi?

  ( ) Har doim
  ( ) Hech qachon
  ( ) break bilan to'xtasa
  ( ) break bo'lmay odatiy tugasa    ← TO'G'RI (TEACHER)
──────────────────────────────────────────────────────────────
"""


# ============================================================
#   2-BO'LIM: KOD O'QISH
#   10 savol × 2 ball = 20 ball
#   Ko'rsatma: Har bir kod nima chiqarishini yozing.
# ============================================================

"""
──────────────────────────────────────────────────────────────
SAVOL 21. Natija: ___________________

    print(3 + 4 * 2)

Javob: 11

──────────────────────────────────────────────────────────────
SAVOL 22. Natija: ___________________

    x = 10
    x += 5
    x *= 2
    print(x)

Javob: 30

──────────────────────────────────────────────────────────────
SAVOL 23. Natija: ___________________

    for i in range(1, 6):
        print(i, end=" ")

Javob: 1 2 3 4 5

──────────────────────────────────────────────────────────────
SAVOL 24. Natija: ___________________

    ball = 65
    if ball >= 90:
        print("A")
    elif ball >= 70:
        print("C")
    elif ball >= 50:
        print("D")
    else:
        print("F")

Javob: D

──────────────────────────────────────────────────────────────
SAVOL 25. Natija: ___________________

    i = 1
    yigindi = 0
    while i <= 4:
        yigindi += i
        i += 1
    print(yigindi)

Javob: 10

──────────────────────────────────────────────────────────────
SAVOL 26. Natija: ___________________

    for harf in "Kod":
        print(harf, end=".")

Javob: K.o.d.

──────────────────────────────────────────────────────────────
SAVOL 27. Natija: ___________________

    for i in range(1, 10):
        if i == 5:
            break
        if i % 2 == 0:
            continue
        print(i, end=" ")

Javob: 1 3

──────────────────────────────────────────────────────────────
SAVOL 28. Natija (necha qator, necha yulduz): ___________________

    for i in range(1, 4):
        for j in range(i):
            print("*", end="")
        print()

Javob:
*
**
***

──────────────────────────────────────────────────────────────
SAVOL 29. Natija: ___________________

    x = 15
    natija = "juft" if x % 2 == 0 else "toq"
    print(natija)

Javob: toq

──────────────────────────────────────────────────────────────
SAVOL 30. Natija: ___________________

    son = -8
    print(abs(son) > 5 and son < 0)

Javob: True
──────────────────────────────────────────────────────────────
"""


# ============================================================
#   3-BO'LIM: XATONI TOPING VA TO'G'RILANG
#   5 savol × 2 ball = 10 ball
#   Ko'rsatma: Kodda xatoni toping va to'g'ri variantini yozing.
# ============================================================

"""
──────────────────────────────────────────────────────────────
SAVOL 31. Xatoni toping va to'g'rilang:

    yosh = input("Yoshingiz: ")
    yangi_yosh = yosh + 1
    print(yangi_yosh)

Xato: input() string qaytaradi, int + string bo'lmaydi.
To'g'risi:
    yosh = int(input("Yoshingiz: "))
    yangi_yosh = yosh + 1
    print(yangi_yosh)

──────────────────────────────────────────────────────────────
SAVOL 32. Xatoni toping va to'g'rilang:

    i = 1
    while i <= 5
        print(i)
        i += 1

Xato: while qatorida ikki nuqta (:) yetishmayapti.
To'g'risi:
    i = 1
    while i <= 5:
        print(i)
        i += 1

──────────────────────────────────────────────────────────────
SAVOL 33. Xatoni toping va to'g'rilang:

    ball = 80
    if ball = 80:
        print("Saksonga teng")

Xato: = (o'zlashtirish) o'rniga == (taqqoslash) ishlatilishi kerak.
To'g'risi:
    ball = 80
    if ball == 80:
        print("Saksonga teng")

──────────────────────────────────────────────────────────────
SAVOL 34. Xatoni toping va to'g'rilang:

    for i in range(1, 6):
    print(i)

Xato: print(i) indentlanmagan (4 bo'sh joy kerak).
To'g'risi:
    for i in range(1, 6):
        print(i)

──────────────────────────────────────────────────────────────
SAVOL 35. Xatoni toping va to'g'rilang:

    print("Mening yoshim: " + 15)

Xato: str + int bo'lmaydi, int ni str ga aylantirish kerak.
To'g'risi:
    print("Mening yoshim: " + str(15))
    # Yoki:
    print("Mening yoshim:", 15)
──────────────────────────────────────────────────────────────
"""


# ============================================================
#   4-BO'LIM: KOD YOZISH — KICHIK
#   5 savol × 4 ball = 20 ball
#   Ko'rsatma: Har bir topshiriq uchun kod yozing.
# ============================================================

# ── SAVOL 36 — (4 ball) ──────────────────────────────────────
"""
Foydalanuvchidan ikkita son oling (int sifatida).
Quyidagilarni chiqaring:
  - Yig'indi
  - Ayirma
  - Ko'paytma
  - Bo'linma (float)
  - Kattarog'i

Kutilayotgan natija (masalan: a=12, b=4):
  Yig'indi   : 16
  Ayirma     : 8
  Ko'paytma  : 48
  Bo'linma   : 3.0
  Kattarog'i : 12
"""
# JAVOBINGIZNI SHU YERGA YOZING:


# ── SAVOL 37 — (4 ball) ──────────────────────────────────────
"""
Foydalanuvchidan yosh oling.
Quyidagi shartga ko'ra xabar chiqaring:
  0—5   → "Bog'cha yoshi"
  6—11  → "Boshlang'ich sinf"
  12—17 → "O'rta maktab"
  18—22 → "Talaba yoshi"
  23+   → "Kattalar"
"""
# JAVOBINGIZNI SHU YERGA YOZING:


# ── SAVOL 38 — (4 ball) ──────────────────────────────────────
"""
while sikli yordamida 1 dan 50 gacha bo'lgan
barcha 7 ga bo'linadigan sonlarni bir qatorda chiqaring.

Kutilayotgan natija:
  7 14 21 28 35 42 49
"""
# JAVOBINGIZNI SHU YERGA YOZING:


# ── SAVOL 39 — (4 ball) ──────────────────────────────────────
"""
for sikli yordamida quyidagi shaklni chiqaring:
  *
  **
  ***
  ****
  *****
  ****
  ***
  **
  *
(Avval o'sadi, keyin kamayadi — 2 ta alohida for ishlating)
"""
# JAVOBINGIZNI SHU YERGA YOZING:


# ── SAVOL 40 — (4 ball) ──────────────────────────────────────
"""
Foydalanuvchidan matn oling.
For sikli yordamida:
  a) Matndagi harflar sonini hisoblang (len() ishlatmasdan)
  b) Matndagi 'a' va 'A' harflari necha marta uchrashini toping

Kutilayotgan natija (masalan: "Assalomu alaykum"):
  Jami harf soni: 16
  'a' harfi soni: 4
"""
# JAVOBINGIZNI SHU YERGA YOZING:


# ============================================================
#   5-BO'LIM: KOD YOZISH — O'RTA
#   3 savol × 6 ball = 18 ball
# ============================================================

# ── SAVOL 41 — (6 ball) ──────────────────────────────────────
"""
Foydalanuvchidan 5 ta son oling (while sikli bilan).
Kiritilgan sonlar ichidan:
  - Eng katta sonni toping (max() ishlatmasdan)
  - Eng kichik sonni toping (min() ishlatmasdan)
  - Barcha musbat sonlar yig'indisini hisoblang

Kutilayotgan natija (masalan: 3, -1, 7, 2, -4):
  Eng katta : 7
  Eng kichik: -4
  Musbat yig'indisi: 12
"""
# JAVOBINGIZNI SHU YERGA YOZING:


# ── SAVOL 42 — (6 ball) ──────────────────────────────────────
"""
Quyidagi ko'paytma jadvalini for + ichma-ich for bilan chiqaring.
Faqat 1 dan 5 gacha bo'lgan sonlar uchun, lekin
ikkala son ham toq bo'lgan juftlarni o'tkazib yuboring (continue).

Kutilayotgan natija (qisman):
  1x2=2  1x4=4
  2x1=2  2x2=4  2x3=6  2x4=8  2x5=10
  3x2=6  3x4=12
  ... va hokazo
"""
# JAVOBINGIZNI SHU YERGA YOZING:


# ── SAVOL 43 — (6 ball) ──────────────────────────────────────
"""
Oddiy login tizimi yarating:

  To'g'ri login: "admin"
  To'g'ri parol: "python2025"

  - Foydalanuvchiga 3 ta urinish bering
  - Har xato urinishdan keyin nechta urinish qolganini ko'rsating
  - 3 ta urinish tugasa: "Hisob vaqtincha bloklandi!"
  - To'g'ri kirganda: "Tizimga xush kelibsiz, [login]!"

Kutilayotgan natija (ikki xato, keyin to'g'ri):
  Login: user   → Xato! 2 ta urinish qoldi.
  Login: admin  → Parol: abc → Xato! 1 ta urinish qoldi.
  Login: admin  → Parol: python2025 → Tizimga xush kelibsiz, admin!
"""
# JAVOBINGIZNI SHU YERGA YOZING:


# ============================================================
#   6-BO'LIM: KOD YOZISH — KATTA
#   2 savol × 6 ball = 12 ball
# ============================================================

# ── SAVOL 44 — (6 ball) ──────────────────────────────────────
"""
Foydalanuvchidan n ta talabaning ismini va ballini oling.
(n ni ham foydalanuvchi kiritsin)

Dastur quyidagilarni chiqarsin:
  1. Barcha talabalar ro'yxati (ism: ball  |  baho)
     (A: 90+, B: 80-89, C: 70-79, D: 50-69, F: <50)
  2. Sinfning o'rtacha bali
  3. Eng yuqori ball olgan talabaning ismi va bali
  4. "A" baho olganlar soni

Kutilayotgan natija (3 talaba: Ali=92, Vali=75, Jasur=48):
  ─────────────────────────
  Ali   : 92 | A
  Vali  : 75 | C
  Jasur : 48 | F
  ─────────────────────────
  O'rtacha ball    : 71.7
  Eng yaxshi talaba: Ali (92)
  "A" olganlar     : 1 ta
"""
# JAVOBINGIZNI SHU YERGA YOZING:


# ── SAVOL 45 — (6 ball) ──────────────────────────────────────
"""
Sonni taxmin qilish o'yini yarating:

  - Dastur 1 dan 50 gacha maxfiy son o'ylasin
    (maxfiy_son = 37  deb qo'yib qo'ying)
  - Foydalanuvchiga 7 ta urinish bering
  - Har urinishdan so'ng maslahat bering:
      "Kattaroq son!" yoki "Kichikroq son!"
  - To'g'ri topsa:  "Barakalla! X-urinishda topdingiz!"
  - 7 urinishda topa olmasa: "Yutqazdingiz! Javob: 37"
  - Har urinishda nechta urinish qolganini ham ko'rsating

Kutilayotgan natija (qisman):
  1-urinish (6 ta qoldi): 25
  Kattaroq son!
  2-urinish (5 ta qoldi): 40
  Kichikroq son!
  3-urinish (4 ta qoldi): 37
  Barakalla! 3-urinishda topdingiz!
"""
# JAVOBINGIZNI SHU YERGA YOZING:


# ============================================================
#   IMTIHON TUGADI
# ============================================================

"""
Ish tugagach, faylni saqlang va o'qituvchiga topshiring.

BALL JADVALI:
  ┌──────────────┬───────────┬───────────┐
  │ Bo'lim       │ Max ball  │ Sizning   │
  │              │           │ balingiz  │
  ├──────────────┼───────────┼───────────┤
  │ 1. Test      │   20      │           │
  │ 2. Kod o'qi  │   20      │           │
  │ 3. Xato top  │   10      │           │
  │ 4. Kichik    │   20      │           │
  │ 5. O'rta     │   18      │           │
  │ 6. Katta     │   12      │           │
  ├──────────────┼───────────┼───────────┤
  │ JAMI         │  100      │           │
  └──────────────┴───────────┴───────────┘

Omad!
"""