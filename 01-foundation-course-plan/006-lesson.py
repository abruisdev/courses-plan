# ============================================================
#   DARS 6: Pythonda Funksiyalar
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ Funksiya nima va nima uchun kerakligi
  ✔️ def bilan funksiya yaratish
  ✔️ Parametr va argument farqi
  ✔️ return bilan qiymat qaytarish
  ✔️ Default va keyword argumentlar
  ✔️ *args va **kwargs
  ✔️ Local va global o‘zgaruvchilar
  ✔️ Lambda funksiya
"""

# ------------------------------------------------------------
# FUNKSIYA NIMA?
# ------------------------------------------------------------

"""
Funksiya — ma’lum bir vazifani bajaradigan, kerak bo‘lganda
qayta chaqiriladigan kod bo‘lagi.

Funksiya yozishning foydasi:
  ✔️ Bir xil kodni qayta-qayta yozmaymiz
  ✔️ Kod tartibli va tushunarli bo‘ladi
  ✔️ Katta dasturni kichik vazifalarga bo‘lamiz

Sintaksisi:

    def funksiya_nomi():
        bajariladigan_kod
"""


# Parametrsiz funksiya
def salomlash():
    print("Assalomu alaykum!")
    print("Python Foundation kursiga xush kelibsiz!")


# Funksiya faqat chaqirilganda ishlaydi
salomlash()
salomlash()


# ------------------------------------------------------------
# PARAMETR VA ARGUMENT
# ------------------------------------------------------------

"""
Parametr — funksiya yaratilgandagi o‘zgaruvchi.
Argument — funksiyani chaqirganda beriladigan haqiqiy qiymat.

    def salom_ber(ism):     # ism — parametr
        print("Salom", ism)

    salom_ber("Ali")       # "Ali" — argument
"""


def salom_ber(ism):
    print("Assalomu alaykum,", ism)


salom_ber("Ali")
salom_ber("Madina")


def ikki_sonni_qosh(a, b):
    print(a + b)


ikki_sonni_qosh(5, 3)
ikki_sonni_qosh(100, 250)


# ------------------------------------------------------------
# return — QIYMAT QAYTARISH
# ------------------------------------------------------------

"""
print() natijani ekranga chiqaradi.
return esa natijani funksiya tashqarisiga qaytaradi.

return qilingan qiymatni o‘zgaruvchiga saqlash, hisoblash yoki
boshqa funksiyaga berish mumkin.
"""


def qoshish(a, b):
    return a + b


natija = qoshish(10, 20)
print("Natija:", natija)
print(qoshish(7, 8) * 2)


def kvadrat(son):
    return son ** 2


print(kvadrat(5))


def yoshni_aniqla(tugilgan_yil, joriy_yil):
    return joriy_yil - tugilgan_yil


yosh = yoshni_aniqla(2005, 2026)
print("Yosh:", yosh)


# return dan keyingi kod ishlamaydi
def tekshir(son):
    if son > 0:
        return "Musbat son"

    return "0 yoki manfiy son"


print(tekshir(10))
print(tekshir(-5))


# ------------------------------------------------------------
# DEFAULT PARAMETR
# ------------------------------------------------------------

"""
Default parametr — parametrga oldindan qiymat berish.
Argument berilmasa, shu qiymat ishlatiladi.
"""


def salomlash(ism, til="uz"):
    if til == "uz":
        print("Assalomu alaykum,", ism)
    elif til == "en":
        print("Hello,", ism)
    else:
        print("Til topilmadi")


salomlash("Ali")
salomlash("John", "en")


def daraja(son, daraja_soni=2):
    return son ** daraja_soni


print(daraja(5))
print(daraja(2, 8))


# ------------------------------------------------------------
# KEYWORD ARGUMENTLAR
# ------------------------------------------------------------

"""
Keyword argumentda parametr nomi bilan qiymat beriladi.
Bu kodni tushunarliroq qiladi va argumentlar tartibini o‘zgartirishga
imkon beradi.
"""


def talaba_haqida(ism, yosh, shahar):
    print("Ism:", ism)
    print("Yosh:", yosh)
    print("Shahar:", shahar)


talaba_haqida(ism="Madina", yosh=20, shahar="Toshkent")
talaba_haqida(shahar="Samarqand", ism="Ali", yosh=18)


# ------------------------------------------------------------
# *args — KO‘P SONLI ARGUMENTLAR
# ------------------------------------------------------------

"""
*args — argumentlar soni oldindan noma’lum bo‘lsa ishlatiladi.
Funksiya ichida args tuple ko‘rinishida bo‘ladi.
"""


def yigindi_top(*sonlar):
    yigindi = 0

    for son in sonlar:
        yigindi += son

    return yigindi


print(yigindi_top(1, 2, 3))
print(yigindi_top(10, 20, 30, 40, 50))


def ismlarni_chiqar(*ismlar):
    for ism in ismlar:
        print("Salom,", ism)


ismlarni_chiqar("Ali", "Vali", "Madina")


# ------------------------------------------------------------
# **kwargs — KALIT-QIYMAT ARGUMENTLARI
# ------------------------------------------------------------

"""
**kwargs — kalit=qiymat ko‘rinishidagi argumentlar soni
oldindan noma’lum bo‘lsa ishlatiladi.
Funksiya ichida kwargs dictionary ko‘rinishida bo‘ladi.
"""


def foydalanuvchi_haqida(**malumotlar):
    for kalit, qiymat in malumotlar.items():
        print(kalit + ":", qiymat)


foydalanuvchi_haqida(
    ism="Ali",
    yosh=18,
    shahar="Toshkent"
)


# ------------------------------------------------------------
# LOCAL VA GLOBAL O‘ZGARUVCHILAR
# ------------------------------------------------------------

"""
Local o‘zgaruvchi — faqat funksiya ichida ishlaydi.
Global o‘zgaruvchi — funksiya tashqarisida yaratiladi.

global kalit so‘zini kam ishlating. Qiymatni parametr orqali olib,
return bilan qaytarish odatda xavfsizroq va tushunarliroq bo‘ladi.
"""

kurs_nomi = "Python Foundation"  # Global o‘zgaruvchi


def dars_haqida():
    dars_nomi = "Funksiyalar"  # Local o‘zgaruvchi
    print(kurs_nomi)
    print(dars_nomi)


dars_haqida()
# print(dars_nomi)  # Xato: dars_nomi funksiya tashqarisida yo‘q


hisoblagich = 0


def bittaga_oshir():
    global hisoblagich
    hisoblagich += 1


bittaga_oshir()
print(hisoblagich)


# ------------------------------------------------------------
# LAMBDA FUNKSIYA
# ------------------------------------------------------------

"""
lambda — qisqa, bir qatorli funksiya.
Murakkab vazifalar uchun oddiy def ishlatish tavsiya qilinadi.

Sintaksisi:
    lambda parametrlar: qaytariladigan_qiymat
"""


kvadrat_lambda = lambda son: son ** 2
qoshish_lambda = lambda a, b: a + b

print(kvadrat_lambda(4))
print(qoshish_lambda(10, 20))


# ------------------------------------------------------------
# AMALIY MISOL 1 — KALKULYATOR FUNKSIYALARI
# ------------------------------------------------------------


def qosh(a, b):
    return a + b


def ayir(a, b):
    return a - b


def kopaytir(a, b):
    return a * b


def bol(a, b):
    if b == 0:
        return "0 ga bo‘lish mumkin emas"

    return a / b


print(qosh(10, 5))
print(ayir(10, 5))
print(kopaytir(10, 5))
print(bol(10, 5))
print(bol(10, 0))


# ------------------------------------------------------------
# AMALIY MISOL 2 — BAHO HISOBLASH
# ------------------------------------------------------------


def bahoni_aniqla(baho):
    if baho < 0 or baho > 100:
        return "Baho 0 dan 100 gacha bo‘lishi kerak"
    elif baho >= 86:
        return "5"
    elif baho >= 71:
        return "4"
    elif baho >= 56:
        return "3"

    return "2"


print("Sizning bahoyingiz:", bahoni_aniqla(78))


# ------------------------------------------------------------
# AMALIY MISOL 3 — PAROL TEKSHIRISH
# ------------------------------------------------------------


def parolni_tekshir(parol):
    togri_parol = "python123"

    if parol == togri_parol:
        return "Parol to‘g‘ri"

    return "Parol noto‘g‘ri"


print(parolni_tekshir("python123"))
print(parolni_tekshir("12345"))


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1:
  ismni_chiqar(ism) funksiyasini yarating.
  U "Assalomu alaykum, ism" deb chiqarsin.

TOPSHIRIQ 2:
  uchta_son_yigindisi(a, b, c) funksiyasini yarating.
  Natijani return bilan qaytaring.

TOPSHIRIQ 3:
  juftmi(son) funksiyasini yarating.
  Juft bo‘lsa True, aks holda False qaytarsin.

TOPSHIRIQ 4:
  max_son(*sonlar) funksiyasini yarating.
  max() ishlatmasdan eng katta sonni return qiling.

TOPSHIRIQ 5:
  valyuta_almashtir(summa, kurs=12500) funksiyasini yarating.
  So‘mni dollarga aylantirib return qilsin.
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O‘RGANDIK?
# ------------------------------------------------------------

"""
✔️ Funksiya nima ekanini
✔️ def bilan funksiya yaratishni
✔️ Parametr va argument farqini
✔️ return bilan qiymat qaytarishni
✔️ Default va keyword argumentlarni
✔️ *args va **kwargs ishlatishni
✔️ Local va global o‘zgaruvchilarni
✔️ Lambda funksiya yozishni
✔️ Kalkulyator, baho va parol funksiyalarini
"""
