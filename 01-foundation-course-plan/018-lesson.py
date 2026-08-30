# ============================================================
#   DARS 18: Inkapsulatsiya va Abstraktsiya
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

from abc import ABC, abstractmethod

"""
BUGUNGI DARSDA:
  ✔️ Inkapsulatsiya
  ✔️ public, protected va private attributelar
  ✔️ @property, getter va setter
  ✔️ Abstraktsiya
  ✔️ ABC va @abstractmethod
"""


# ------------------------------------------------------------
# INKAPSULATSIYA
# ------------------------------------------------------------

"""
Inkapsulatsiya — object ichidagi ma’lumotni tartibli va himoyalangan usulda boshqarish tamoyili.

  public       ism       → hamma joydan foydalanish mumkin
  protected    _ism      → class va vorislar uchun degan kelishuv
  private      __ism     → class ichida ishlatish tavsiya qilinadi
"""


class Foydalanuvchi:
    def __init__(self, ism, parol):
        self.ism = ism
        self._rol = "user"
        self.__parol = parol

    def parolni_tekshir(self, parol):
        return self.__parol == parol


foydalanuvchi = Foydalanuvchi("Ali", "python123")
print(foydalanuvchi.ism)
print(foydalanuvchi._rol)
print(foydalanuvchi.parolni_tekshir("python123"))

# print(foydalanuvchi.__parol)  # Xato beradi


# ------------------------------------------------------------
# @property, GETTER VA SETTER
# ------------------------------------------------------------

"""
@property attributega method orqali murojaat qilish, lekin tashqaridan oddiy attribute kabi foydalanish imkonini beradi.
Setter qiymatni o‘zgartirishdan oldin tekshiruv qo‘yadi.
"""


class BankHisobi:
    def __init__(self, egasi, balans=0):
        self.egasi = egasi
        self.__balans = 0
        self.balans = balans

    @property
    def balans(self):
        return self.__balans

    @balans.setter
    def balans(self, qiymat):
        if qiymat < 0:
            print("Balans manfiy bo‘lishi mumkin emas")
        else:
            self.__balans = qiymat

    def pul_qoshish(self, summa):
        if summa > 0:
            self.balans += summa


hisob = BankHisobi("Madina", 500_000)
print(hisob.balans)
hisob.balans = -10
hisob.pul_qoshish(100_000)
print(hisob.balans)


# ------------------------------------------------------------
# ABSTRAKTSIYA
# ------------------------------------------------------------

"""
Abstraktsiya — foydalanuvchiga kerakli interfeysni berib, ichki murakkablikni yashirish tamoyili.
Abstract class — andoza class. Undan to‘g‘ridan-to‘g‘ri object yaratib bo‘lmaydi.
"""


class Shakl(ABC):
    @abstractmethod
    def yuzi(self):
        pass


class Tortburchak(Shakl):
    def __init__(self, eni, boyi):
        self.eni = eni
        self.boyi = boyi

    def yuzi(self):
        return self.eni * self.boyi


class Doira(Shakl):
    def __init__(self, radius):
        self.radius = radius

    def yuzi(self):
        return 3.14 * self.radius ** 2


shakllar = [Tortburchak(5, 4), Doira(3)]

for shakl in shakllar:
    print("Yuzi:", shakl.yuzi())

# shakl = Shakl()  # Xato: abstract classdan object yaratilmaydi


# ------------------------------------------------------------
# AMALIY LOYIHA — TO‘LOV TIZIMI
# ------------------------------------------------------------


class TolovUsuli(ABC):
    @abstractmethod
    def tola(self, summa):
        pass


class KartaTolovi(TolovUsuli):
    def tola(self, summa):
        return f"Karta orqali {summa:,} so‘m to‘landi"


class NaqdTolov(TolovUsuli):
    def tola(self, summa):
        return f"Naqd pul bilan {summa:,} so‘m to‘landi"


tolovlar = [KartaTolovi(), NaqdTolov()]

for tolov in tolovlar:
    print(tolov.tola(50_000))


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. Mahsulot classida narx qiymatini @property bilan boshqaring. Narx manfiy bo‘lmasin.
2. Transport abstract class yarating. Avtomobil va Velosiped classlarida harakatlan() methodi bo‘lsin.
3. Xodim classida oylik private bo‘lsin; setter manfiy oylikni qabul qilmasin.
4. YetkazibBerish abstract classi va Kuryer, Pochta classlarini yarating.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ Inkapsulatsiyani
✔️ Public, protected va private attributelarni
✔️ @property va setterlarni
✔️ Abstraktsiyani
✔️ ABC va @abstractmethodni
✔️ To‘lov tizimi misolini
"""
