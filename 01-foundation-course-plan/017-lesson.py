# ============================================================
#   DARS 17: Vorisdorlik va Polimorfizm
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ Vorisdorlik (inheritance)
  ✔️ super()
  ✔️ Method override
  ✔️ Ko‘p darajali vorisdorlik
  ✔️ isinstance() va issubclass()
  ✔️ Polimorfizm
"""


# ------------------------------------------------------------
# VORISDORLIK NIMA?
# ------------------------------------------------------------

"""
Vorisdorlik — bola class ota classning attribute va methodlarini olishi.

    class Bola(Ota):
        pass
"""


class Hayvon:
    def __init__(self, ism):
        self.ism = ism

    def ovqatlan(self):
        print(f"{self.ism} ovqatlanyapti")


class It(Hayvon):
    def vovulla(self):
        print(f"{self.ism}: Vov-vov!")


rex = It("Rex")
rex.ovqatlan()
rex.vovulla()


# ------------------------------------------------------------
# super()
# ------------------------------------------------------------

"""
super() ota classning methodiga murojaat qilish uchun ishlatiladi.
Ko‘pincha bola classning __init__() methodida ishlatiladi.
"""


class Xodim:
    def __init__(self, ism, oylik):
        self.ism = ism
        self.oylik = oylik

    def malumot(self):
        return f"{self.ism}: {self.oylik:,} so‘m"


class Dasturchi(Xodim):
    def __init__(self, ism, oylik, til):
        super().__init__(ism, oylik)
        self.til = til

    def malumot(self):
        return f"{super().malumot()}, Til: {self.til}"


dasturchi = Dasturchi("Ali", 8_000_000, "Python")
print(dasturchi.malumot())


# ------------------------------------------------------------
# METHOD OVERRIDE VA POLIMORFIZM
# ------------------------------------------------------------

"""
Method override — ota classdagi methodni bola classda qayta yozish.
Polimorfizm — bir xil method nomi turli objectlarda turlicha ishlashi.
"""


class Mushuk(Hayvon):
    def ovoz_ber(self):
        print(f"{self.ism}: Miyov!")


class Itcha(Hayvon):
    def ovoz_ber(self):
        print(f"{self.ism}: Vov-vov!")


hayvonlar = [Mushuk("Momiq"), Itcha("Rex")]

for hayvon in hayvonlar:
    hayvon.ovqatlan()
    hayvon.ovoz_ber()


# ------------------------------------------------------------
# KO‘P DARAJALI VORISDORLIK
# ------------------------------------------------------------


class Transport:
    def harakatlan(self):
        print("Transport harakatlanyapti")


class Avtomobil(Transport):
    def signal(self):
        print("Bi-bi!")


class Elektromobil(Avtomobil):
    def zaryadla(self):
        print("Elektromobil zaryadlanyapti")


tesla = Elektromobil()
tesla.harakatlan()
tesla.signal()
tesla.zaryadla()


# ------------------------------------------------------------
# isinstance() VA issubclass()
# ------------------------------------------------------------

print(isinstance(rex, It))
print(isinstance(rex, Hayvon))
print(issubclass(It, Hayvon))
print(issubclass(Hayvon, It))


# ------------------------------------------------------------
# AMALIY MISOL — XODIMLAR OYLIKLARI
# ------------------------------------------------------------


class Xodim:
    def __init__(self, ism, asosiy_oylik):
        self.ism = ism
        self.asosiy_oylik = asosiy_oylik

    def oylik_hisobla(self):
        return self.asosiy_oylik


class Menejer(Xodim):
    def oylik_hisobla(self):
        return self.asosiy_oylik + 1_000_000


class Sotuvchi(Xodim):
    def __init__(self, ism, asosiy_oylik, savdo_bonusi):
        super().__init__(ism, asosiy_oylik)
        self.savdo_bonusi = savdo_bonusi

    def oylik_hisobla(self):
        return self.asosiy_oylik + self.savdo_bonusi


xodimlar = [
    Xodim("Ali", 4_000_000),
    Menejer("Madina", 6_000_000),
    Sotuvchi("Vali", 3_000_000, 700_000),
]

for xodim in xodimlar:
    print(f"{xodim.ism}: {xodim.oylik_hisobla():,} so‘m")


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. Ota class sifatida Shakl yarating. Doira va Tortburchak classlarini
   undan voris qiling; har birida yuzi() methodi ishlasin.
2. Transport → Avtomobil → YukMashina vorisligini yarating.
3. Talaba va Ustoz classlarini Inson classidan voris qiling.
4. Bir xil tanishtir() methodi turlicha natija beradigan 3 ta class yarating.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ Vorisdorlikni
✔️ super() ishlatishni
✔️ Method override qilishni
✔️ Ko‘p darajali vorisdorlikni
✔️ isinstance() va issubclass()ni
✔️ Polimorfizmni
✔️ Xodimlar oyligi misolini
"""
