# ============================================================
#   DARS 7: Takrorlash va EXAM
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BU DARSNING MAQSADI:
  ✔️ 1–6-darslarni takrorlash
  ✔️ Mustaqil masalalar ishlash
  ✔️ Mini loyiha yozish
  ✔️ Nazariy va amaliy imtihon topshirish

Bugun yangi mavzu o‘rganilmaydi. Oldingi bilimlar mustahkamlanadi.
"""


# ------------------------------------------------------------
# TAKRORLASH SAVOLLARI
# ------------------------------------------------------------

"""
1. Python nima uchun ishlatiladi?
2. print() va input() farqi nima?
3. str, int, float va bool nima?
4. = va == farqi nima?
5. if qachon ishlatiladi?
6. while va for farqi nima?
7. break va continue nima qiladi?
8. Funksiya nima uchun kerak?
9. Parametr va argument farqi nima?
10. print() va return farqi nima?
"""


# ------------------------------------------------------------
# MINI LOYIHA 1 — KONSOL KALKULYATORI
# ------------------------------------------------------------


def kalkulyator():
    while True:
        print("\n--- KALKULYATOR ---")
        print("1. Qo‘shish")
        print("2. Ayirish")
        print("3. Ko‘paytirish")
        print("4. Bo‘lish")
        print("0. Chiqish")

        tanlov = input("Tanlovingiz: ")

        if tanlov == "0":
            print("Kalkulyator tugadi")
            break

        if tanlov not in ["1", "2", "3", "4"]:
            print("Noto‘g‘ri tanlov")
            continue

        son1 = float(input("Birinchi son: "))
        son2 = float(input("Ikkinchi son: "))

        if tanlov == "1":
            print("Natija:", son1 + son2)
        elif tanlov == "2":
            print("Natija:", son1 - son2)
        elif tanlov == "3":
            print("Natija:", son1 * son2)
        elif son2 == 0:
            print("0 ga bo‘lish mumkin emas")
        else:
            print("Natija:", son1 / son2)


# kalkulyator()


# ------------------------------------------------------------
# MINI LOYIHA 2 — QUIZ DASTURI
# ------------------------------------------------------------


def quiz():
    ball = 0

    savollar = [
        ("Python qanday dasturlash tili?", "yuqori"),
        ("2 + 2 nechiga teng?", "4"),
        ("Python’da ekranga chiqarish funksiyasi?", "print"),
    ]

    for savol, togri_javob in savollar:
        javob = input(savol + " ").lower()

        if javob == togri_javob:
            print("To‘g‘ri javob!")
            ball += 1
        else:
            print("Noto‘g‘ri. To‘g‘ri javob:", togri_javob)

    print("\nSizning ballingiz:", ball, "/", len(savollar))


# quiz()


# ------------------------------------------------------------
# MINI LOYIHA 3 — ATM DASTURI
# ------------------------------------------------------------


def atm():
    balans = 1_000_000

    while True:
        print("\n--- ATM ---")
        print("1. Balansni ko‘rish")
        print("2. Pul qo‘shish")
        print("3. Pul yechish")
        print("0. Chiqish")

        tanlov = input("Tanlovingiz: ")

        if tanlov == "1":
            print("Balansingiz:", balans, "so‘m")
        elif tanlov == "2":
            summa = int(input("Summa: "))
            balans += summa
            print("Pul qo‘shildi")
        elif tanlov == "3":
            summa = int(input("Summa: "))

            if summa <= balans:
                balans -= summa
                print("Pul berildi")
            else:
                print("Balans yetarli emas")
        elif tanlov == "0":
            print("Xayr!")
            break
        else:
            print("Noto‘g‘ri tanlov")


# atm()


# ------------------------------------------------------------
# AMALIY EXAM
# ------------------------------------------------------------

"""
EXAM 1 — BAHO TIZIMI:
  Foydalanuvchidan 5 ta baho oling.
  O‘rtacha bahoni, eng katta va eng kichik bahoni chiqaring.

EXAM 2 — PAROL TIZIMI:
  Foydalanuvchiga 3 ta urinish bering.
  To‘g‘ri parol: python123.

EXAM 3 — SON TOPISH:
  Sirli sonni belgilang.
  Foydalanuvchi topmaguncha taxmin so‘rang.

EXAM 4 — MENYU:
  while True va funksiyalar yordamida o‘zingiz haqingizda
  ma’lumot chiqaradigan konsol menyu yarating.

BAHOLASH:
  0–55   — qayta ishlash kerak
  56–70  — qoniqarli
  71–85  — yaxshi
  86–100 — a’lo
"""
