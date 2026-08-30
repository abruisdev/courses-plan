# ============================================================
#   DARS 11: Xatolar bilan Ishlash va Debugging
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ SyntaxError, TypeError, ValueError, KeyError
  ✔️ Xato matnini o‘qish
  ✔️ try / except / else / finally
  ✔️ raise bilan o‘zimiz xato chiqarish
  ✔️ print() va Debugger bilan xato topish
"""


# ------------------------------------------------------------
# XATO (ERROR) NIMA?
# ------------------------------------------------------------

"""
Xato — dastur ishlashiga to‘sqinlik qiladigan muammo.

Traceback matnini pastdan yuqoriga qarab o‘qing:
  1. Oxirgi qatorda xato turi va sababi yoziladi.
  2. Undan yuqorida xato qaysi fayl va qatorda bo‘lgani ko‘rsatiladi.
"""


# ------------------------------------------------------------
# ASOSIY XATO TURLARI
# ------------------------------------------------------------

"""
SyntaxError — kod yozish qoidasi buzilgan.
  Misol: if dan keyin : qo‘ymaslik.

TypeError — noto‘g‘ri turdagi qiymatlar bilan amal qilish.
  Misol: "5" + 3.

ValueError — turi to‘g‘ri, lekin qiymati noto‘g‘ri.
  Misol: int("salom").

KeyError — dictionary’da yo‘q kalitga murojaat qilish.
  Misol: talaba["telefon"].

IndexError — listdagi mavjud bo‘lmagan indeksga murojaat qilish.
  Misol: [1, 2][5].
"""

# Quyidagi qatorlar xato berishi mumkin, shuning uchun commentda:
# print("Yosh: " + 18)        # TypeError
# print(int("o‘n"))           # ValueError
# print({"ism": "Ali"}["yosh"])  # KeyError
# print([10, 20][5])           # IndexError


# ------------------------------------------------------------
# try VA except
# ------------------------------------------------------------

"""
try ichiga xato bo‘lishi mumkin bo‘lgan kod yoziladi.
except ichiga xatoni boshqaradigan kod yoziladi.
"""

try:
    son = int(input("Butun son kiriting: "))
    print("Siz kiritgan son:", son)
except ValueError:
    print("Xato: butun son kiritishingiz kerak")


# Bir nechta xato turini ushlash
try:
    son1 = int(input("Birinchi son: "))
    son2 = int(input("Ikkinchi son: "))
    print("Natija:", son1 / son2)
except ValueError:
    print("Xato: son kiritishingiz kerak")
except ZeroDivisionError:
    print("Xato: 0 ga bo‘lish mumkin emas")


# Exception as error — xato matnini olish
try:
    fayl = open("mavjud_emas.txt", "r", encoding="utf-8")
except FileNotFoundError as error:
    print("Fayl topilmadi:", error)


# ------------------------------------------------------------
# else VA finally
# ------------------------------------------------------------

"""
else — try ichida xato bo‘lmasa ishlaydi.
finally — xato bo‘lsa ham, bo‘lmasa ham doim ishlaydi.
"""

try:
    yosh = int(input("Yoshingizni kiriting: "))
except ValueError:
    print("Yosh son bo‘lishi kerak")
else:
    print("Siz", yosh, "yoshdasiz")
finally:
    print("Dastur yakunlandi")


# ------------------------------------------------------------
# raise — O‘ZIMIZ XATO CHIQARISH
# ------------------------------------------------------------

"""
raise — dasturchi belgilagan qoida buzilganda xato chiqaradi.
"""


def yoshni_tekshir(yosh):
    if yosh < 0:
        raise ValueError("Yosh manfiy bo‘lishi mumkin emas")

    return "Yosh qabul qilindi"


try:
    print(yoshni_tekshir(18))
    # print(yoshni_tekshir(-5))
except ValueError as error:
    print("Xato:", error)


# ------------------------------------------------------------
# print() BILAN DEBUGGING
# ------------------------------------------------------------

"""
Debugging — xatoni qidirish va tuzatish jarayoni.
O‘zgaruvchi ichidagi qiymatni ko‘rish uchun vaqtincha print() yozish
mumkin.
"""


def chegirma_hisobla(narx, foiz):
    print("DEBUG → narx:", narx)
    print("DEBUG → foiz:", foiz)

    chegirma = narx * foiz / 100
    print("DEBUG → chegirma:", chegirma)

    return narx - chegirma


print(chegirma_hisobla(100_000, 10))


# ------------------------------------------------------------
# PYCHARM DEBUGGER
# ------------------------------------------------------------

"""
PyCharm’da Debugger ishlatish:

  1. Kod qatori chapiga bosing — qizil nuqta (breakpoint) chiqadi.
  2. Run o‘rniga Debug tugmasini bosing.
  3. Dastur breakpointga kelganda to‘xtaydi.
  4. Variables oynasidan o‘zgaruvchilar qiymatini ko‘ring.
  5. Step Over bilan keyingi qatorga o‘ting.

Debugger murakkab koddagi xatoni topishning eng yaxshi usullaridan biri.
"""


# ------------------------------------------------------------
# AMALIY MISOL 1 — XAVFSIZ SON KIRITISH
# ------------------------------------------------------------


def xavfsiz_son_olish(xabar):
    while True:
        try:
            return int(input(xabar))
        except ValueError:
            print("Iltimos, butun son kiriting")


# yosh = xavfsiz_son_olish("Yoshingiz: ")
# print(yosh)


# ------------------------------------------------------------
# AMALIY MISOL 2 — LOGIN TIZIMI
# ------------------------------------------------------------

foydalanuvchilar = {
    "admin": "python123",
    "ali": "12345",
}

login = input("Login: ")
parol = input("Parol: ")

if login not in foydalanuvchilar:
    print("Bunday foydalanuvchi mavjud emas")
elif foydalanuvchilar[login] != parol:
    print("Parol noto‘g‘ri")
else:
    print("Tizimga xush kelibsiz")


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. 2 ta sonni bo‘luvchi dastur yozing. ValueError va
   ZeroDivisionError holatlarini boshqaring.
2. Dictionary’dan foydalanuvchi ismini xavfsiz get() bilan oling.
3. Foydalanuvchidan 0–100 oralig‘ida baho oling.
   Oraliqdan tashqarida raise ValueError ishlating.
4. xavfsiz_float_olish(xabar) funksiyasini yarating.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ Asosiy xato turlarini
✔️ Traceback matnini o‘qishni
✔️ try / except / else / finally
✔️ raise ishlatishni
✔️ print() va debugger bilan xatoni topishni
"""
