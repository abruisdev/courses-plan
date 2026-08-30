# ============================================================
#   DARS 16: Pythonda OOP — Class va Object
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ OOP nima
  ✔️ Class va Object
  ✔️ Attribute va Method
  ✔️ __init__() konstruktori va self
  ✔️ __str__()
  ✔️ Instance attribute va class attribute
"""


# ------------------------------------------------------------
# OOP NIMA?
# ------------------------------------------------------------

"""
OOP — Object-Oriented Programming, ya’ni obyektga yo‘naltirilgan
dasturlash.

Class — andoza, chizma yoki qolip.
Object — class asosida yaratilgan haqiqiy obyekt.

Masalan:
  Class: Mashina
  Object: Cobalt, Nexia, BYD
"""


# ------------------------------------------------------------
# BIRINCHI CLASS VA OBJECT
# ------------------------------------------------------------


class Mashina:
    pass


cobalt = Mashina()
nexia = Mashina()

print(type(cobalt))


# ------------------------------------------------------------
# ATTRIBUTE VA METHOD
# ------------------------------------------------------------

"""
Attribute — objectning xususiyati.
Method — object bajaradigan funksiya.
"""


class OddiyMashina:
    marka = "Chevrolet"

    def signal_ber(self):
        print("Bi-bi!")


mashina = OddiyMashina()
print(mashina.marka)
mashina.signal_ber()


# ------------------------------------------------------------
# __init__ VA self
# ------------------------------------------------------------

"""
__init__() — object yaratilganda avtomatik ishlaydigan konstruktor.
self — aynan yaratilayotgan objectning o‘ziga murojaat qiladi.
"""


class Talaba:
    def __init__(self, ism, yosh, kurs):
        self.ism = ism
        self.yosh = yosh
        self.kurs = kurs

    def tanishtir(self):
        print(f"Men {self.ism}, {self.yosh} yoshdaman.")


ali = Talaba("Ali", 18, "Python Foundation")
madina = Talaba("Madina", 20, "Backend")

print(ali.ism)
print(madina.kurs)
ali.tanishtir()

# Attribute qiymatini o‘zgartirish
ali.yosh = 19
print(ali.yosh)


# ------------------------------------------------------------
# __str__
# ------------------------------------------------------------

"""
__str__() objectni print() qilganda chiroyli ko‘rinish beradi.
"""


class Mahsulot:
    def __init__(self, nomi, narxi):
        self.nomi = nomi
        self.narxi = narxi

    def __str__(self):
        return f"{self.nomi} — {self.narxi:,} so‘m"


noutbuk = Mahsulot("Noutbuk", 8_500_000)
print(noutbuk)


# ------------------------------------------------------------
# INSTANCE ATTRIBUTE VA CLASS ATTRIBUTE
# ------------------------------------------------------------

"""
Instance attribute — har bir objectga xos qiymat.
Class attribute — barcha objectlar uchun umumiy qiymat.
"""


class Oquvchi:
    maktab_nomi = "Abruisdev Academy"  # Class attribute

    def __init__(self, ism):
        self.ism = ism  # Instance attribute


birinchi = Oquvchi("Ali")
ikkinchi = Oquvchi("Madina")

print(birinchi.ism)
print(ikkinchi.ism)
print(birinchi.maktab_nomi)
print(Oquvchi.maktab_nomi)


# ------------------------------------------------------------
# AMALIY MISOL 1 — BANK HISOBI
# ------------------------------------------------------------


class BankHisobi:
    def __init__(self, egasi, balans=0):
        self.egasi = egasi
        self.balans = balans

    def pul_qoshish(self, summa):
        if summa > 0:
            self.balans += summa

    def pul_yechish(self, summa):
        if summa <= self.balans:
            self.balans -= summa
            return "Pul muvaffaqiyatli yechildi"

        return "Balans yetarli emas"

    def malumot(self):
        return f"Egasi: {self.egasi}, Balans: {self.balans:,} so‘m"


hisob = BankHisobi("Ali", 500_000)
hisob.pul_qoshish(100_000)
print(hisob.pul_yechish(200_000))
print(hisob.malumot())


# ------------------------------------------------------------
# AMALIY MISOL 2 — MASHINA
# ------------------------------------------------------------


class Avtomobil:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.yoqilgan = False

    def yoqish(self):
        self.yoqilgan = True
        print("Mashina yoqildi")

    def ochirish(self):
        self.yoqilgan = False
        print("Mashina o‘chirildi")

    def __str__(self):
        return f"{self.marka} {self.model} ({self.yil})"


cobalt = Avtomobil("Chevrolet", "Cobalt", 2024)
print(cobalt)
cobalt.yoqish()


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. Kitob class yarating: nomi, muallifi, narxi attribute bo‘lsin.
2. Telefon class yarating: marka, model, xotira attribute bo‘lsin.
3. Oquvchi classiga baho attribute va baho_qoshish() method qo‘shing.
4. Savat class yarating: mahsulot qoshish va jami narxni hisoblash methodlari bo‘lsin.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ OOP, class va objectni
✔️ Attribute va methodni
✔️ __init__ va self ni
✔️ __str__ ni
✔️ Instance va class attributelarini
✔️ Bank hisobi va mashina classlarini
"""
