# ============================================================
#   DARS 19: Inkapsulatsiya va Abstraktsiya
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# INKAPSULATSIYA NIMA?
# ------------------------------------------------------------

"""
Inkapsulatsiya — ma'lumotlarni yashirish va himoya qilish.
Ob'ektning ichki ma'lumotlariga to'g'ridan-to'g'ri kirishni cheklash.

Hayotiy misol:
  Bank hisobi:
    - Balansni to'g'ridan-to'g'ri o'zgartira olmaysiz
    - Faqat maxsus metodlar (kirim, chiqim) orqali o'zgartiriladi
    - Bu — ma'lumotni himoya qilish

  Mashina:
    - Dvigatel ichidagi detallarni ko'rmaysiz
    - Faqat gaz, tormoz, rul orqali boshqarasiz

Python'da 3 xil kirish darajasi:
  public    — ism         — hamma joydan ko'rish mumkin
  protected — _ism        — faqat class va bolasida (konventsiya)
  private   — __ism       — faqat class ichida (haqiqiy yashirish)
"""


# ============================================================
# PUBLIC ATRIBUTLAR
# ============================================================

class Talaba:
    def __init__(self, ism, yosh):
        self.ism  = ism      # public — hamma joydan o'zgartirilishi mumkin
        self.yosh = yosh

t = Talaba("Ali", 15)
print(t.ism)        # Ali
t.ism = "Vali"      # to'g'ridan-to'g'ri o'zgartirish mumkin
print(t.ism)        # Vali


# ============================================================
# PROTECTED ATRIBUTLAR — _ism
# ============================================================

"""
_ (bitta pastki chiziq) — "bu protected, tashqarida ishlatma" degan signal.
Python buni MAJBURLAB cheklamaydi — bu kelishuv (convention).
"""

class BankHisobi:
    def __init__(self, egasi, balans):
        self.egasi    = egasi          # public
        self._balans  = balans         # protected — ichida ishlatish uchun
        self._tarix   = []

    def kirim(self, miqdor):
        self._balans += miqdor
        self._tarix.append(f"+{miqdor:,}")

    def ko_rish(self):
        print(f"Balans: {self._balans:,} so'm")

h = BankHisobi("Ali", 100_000)
h.kirim(50_000)
h.ko_rish()

# Protected ga tashqaridan kirish mumkin, lekin tavsiya etilmaydi:
print(h._balans)    # ishlaydi, lekin noto'g'ri amaliyot


# ============================================================
# PRIVATE ATRIBUTLAR — __ism
# ============================================================

"""
__ (ikki pastki chiziq) — haqiqiy yashirish.
Python buni "name mangling" bilan _ClassName__atribut ga aylantiradi.
Tashqaridan to'g'ridan-to'g'ri kirish qiyinlashadi.
"""

class BankHisobi:
    def __init__(self, egasi, balans=0):
        self.egasi    = egasi           # public
        self.__balans = balans          # private — yashirin!
        self.__tarix  = []
        self.__pin    = "0000"          # PIN kod — maxfiy!

    def __str__(self):
        return f"Hisob: {self.egasi}"

    def kirim(self, miqdor):
        if miqdor <= 0:
            raise ValueError("Miqdor musbat bo'lishi kerak!")
        self.__balans += miqdor
        self.__tarix.append(f"+{miqdor:,}")
        print(f"✓ Kirim: {miqdor:,} so'm | Balans: {self.__balans:,}")

    def chiqim(self, miqdor, pin):
        if pin != self.__pin:
            print("❌ Noto'g'ri PIN!")
            return
        if miqdor > self.__balans:
            print("❌ Mablag' yetarli emas!")
            return
        self.__balans -= miqdor
        self.__tarix.append(f"-{miqdor:,}")
        print(f"✓ Chiqim: {miqdor:,} so'm | Balans: {self.__balans:,}")

    def balans_ko_rish(self, pin):
        if pin != self.__pin:
            print("❌ Noto'g'ri PIN!")
            return None
        return self.__balans

    def pin_ozgartir(self, eski_pin, yangi_pin):
        if eski_pin != self.__pin:
            print("❌ Eski PIN noto'g'ri!")
            return
        if len(yangi_pin) != 4 or not yangi_pin.isdigit():
            print("❌ PIN 4 ta raqamdan iborat bo'lishi kerak!")
            return
        self.__pin = yangi_pin
        print("✓ PIN muvaffaqiyatli o'zgartirildi!")

    def tarix_ko_rish(self, pin):
        if pin != self.__pin:
            print("❌ Noto'g'ri PIN!")
            return
        print("\nOperatsiyalar tarixi:")
        for op in self.__tarix:
            print(f"  {op} so'm")


h = BankHisobi("Ali Karimov", 500_000)
print(h)
h.kirim(200_000)
h.chiqim(100_000, "0000")
h.chiqim(100_000, "1234")    # Noto'g'ri PIN

print(h.balans_ko_rish("0000"))

# Private ga to'g'ridan-to'g'ri kirish bo'lmaydi:
# print(h.__balans)   → AttributeError!

# Lekin name mangling orqali (tavsiya etilmaydi):
# print(h._BankHisobi__balans)   # ishlaydi lekin noto'g'ri

h.pin_ozgartir("0000", "1234")
h.tarix_ko_rish("1234")


# ============================================================
# GETTER va SETTER — @property
# ============================================================

"""
Getter — xususiyat qiymatini olish
Setter — xususiyat qiymatini tekshirib o'zgartirish

@property dekorator bilan yoziladi.
Tashqaridan oddiy atribut kabi ko'rinadi, lekin ichida metod ishlaydi.
"""

class Talaba:
    def __init__(self, ism, yosh):
        self.__ism  = ism
        self.__yosh = yosh

    # ── Getter ────────────────────────────────────────────────
    @property
    def ism(self):
        return self.__ism

    @property
    def yosh(self):
        return self.__yosh

    # ── Setter ────────────────────────────────────────────────
    @ism.setter
    def ism(self, yangi_ism):
        if not isinstance(yangi_ism, str):
            raise TypeError("Ism string bo'lishi kerak!")
        if len(yangi_ism) < 2:
            raise ValueError("Ism kamida 2 ta harf bo'lishi kerak!")
        self.__ism = yangi_ism.strip().title()

    @yosh.setter
    def yosh(self, yangi_yosh):
        if not isinstance(yangi_yosh, int):
            raise TypeError("Yosh butun son bo'lishi kerak!")
        if not (1 <= yangi_yosh <= 120):
            raise ValueError("Yosh 1 dan 120 gacha bo'lishi kerak!")
        self.__yosh = yangi_yosh

    def __str__(self):
        return f"Talaba({self.__ism}, {self.__yosh} yosh)"


t = Talaba("ali karimov", 15)
print(t)            # Talaba(Ali Karimov, 15 yosh)  — title() qo'llandi

# Getter orqali o'qish (oddiy atribut kabi):
print(t.ism)        # Ali Karimov
print(t.yosh)       # 15

# Setter orqali o'zgartirish:
t.ism  = "  vali rahimov  "   # bo'sh joylar tozalanadi, title() qo'llanadi
t.yosh = 16
print(t)            # Talaba(Vali Rahimov, 16 yosh)

# Noto'g'ri qiymat:
try:
    t.yosh = 200    # ValueError!
except ValueError as e:
    print(f"Xato: {e}")

try:
    t.ism = "A"     # ValueError!
except ValueError as e:
    print(f"Xato: {e}")


# ============================================================
# uuid — UNIKAL ID YARATISH
# ============================================================

"""
uuid — Universal Unique Identifier (Universalro'yxat Yagona Identifikator)
Har safar yangi, takrorlanmas ID yaratadi.

import uuid
uuid.uuid4()  — tasodifiy UUID yaratadi
"""

import uuid

class Mahsulot:
    def __init__(self, nom, narx):
        self.__id   = str(uuid.uuid4())    # avtomatik unikal ID
        self.nom    = nom
        self.__narx = narx

    @property
    def id(self):
        return self.__id   # faqat o'qish (setter yo'q)

    @property
    def narx(self):
        return self.__narx

    @narx.setter
    def narx(self, yangi_narx):
        if yangi_narx < 0:
            raise ValueError("Narx manfiy bo'lishi mumkin emas!")
        self.__narx = yangi_narx

    def __str__(self):
        return f"[{self.__id[:8]}...] {self.nom}: {self.__narx:,} so'm"


m1 = Mahsulot("Non", 3000)
m2 = Mahsulot("Sut", 8000)
m3 = Mahsulot("Tuxum", 15000)

print(m1)
print(m2)
print(m3)

# ID faqat o'qish mumkin:
print(m1.id)       # UUID
# m1.id = "yangi"  → AttributeError! (setter yo'q)


# ============================================================
# ABSTRAKTSIYA NIMA?
# ============================================================

"""
Abstraktsiya — ichki murakkablikni yashirib, faqat zarur interfeysni ko'rsatish.

Hayotiy misol:
  Avtomobil:
    - Siz faqat gaz, tormoz, rul ko'rasiz
    - Dvigatel, KPP, elektr tizimi — yashirin
    - Siz faqat boshqarishni bilishingiz kifoya

  Printer:
    - Siz faqat "Chop et" tugmasini bosasiz
    - Ichida nima bo'layotgani siz uchun muhim emas

Python'da abstraktsiya:
  ABC (Abstract Base Class) — abstract class
  @abstractmethod — amalga oshirilishi MAJBURIY metod
"""

from abc import ABC, abstractmethod

# ── Abstract class ────────────────────────────────────────────
class Shakl(ABC):    # ABC dan meros — bu abstract class
    """
    Bu abstract class — to'g'ridan-to'g'ri ob'ekt yaratib bo'lmaydi.
    Faqat meros olish orqali ishlatiladi.
    """

    @abstractmethod
    def yuzi(self):
        """Yuzni hisoblash — har class o'zi amalga oshiradi"""
        pass

    @abstractmethod
    def perimetri(self):
        """Perimetrni hisoblash — har class o'zi amalga oshiradi"""
        pass

    # Oddiy metod — bola classlar uchun umumiy
    def info(self):
        print(f"{self.__class__.__name__}:")
        print(f"  Yuzi      : {self.yuzi():.4f}")
        print(f"  Perimetri : {self.perimetri():.4f}")


# Abstract classdan to'g'ridan-to'g'ri ob'ekt yaratib bo'lmaydi:
# s = Shakl()   → TypeError!

# ── Bola classlar — abstractlarni amalga oshiradi ────────────
import math

class Doira(Shakl):
    def __init__(self, r):
        self.r = r

    def yuzi(self):          # MAJBURIY
        return math.pi * self.r ** 2

    def perimetri(self):     # MAJBURIY
        return 2 * math.pi * self.r


class To_rtburchak(Shakl):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def yuzi(self):
        return self.a * self.b

    def perimetri(self):
        return 2 * (self.a + self.b)


class Uchburchak(Shakl):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def yuzi(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p-self.a) * (p-self.b) * (p-self.c))

    def perimetri(self):
        return self.a + self.b + self.c


# Test:
shakllar = [Doira(5), To_rtburchak(4, 6), Uchburchak(3, 4, 5)]

for shakl in shakllar:
    shakl.info()
    print()


# ============================================================
# AMALIY DASTUR — To'lov tizimi
# ============================================================

from abc import ABC, abstractmethod

class TolovTizimi(ABC):
    def __init__(self, egasi):
        self.egasi = egasi
        self.__balans = 0.0

    @property
    def balans(self):
        return self.__balans

    def kirim(self, miqdor):
        if miqdor <= 0:
            raise ValueError("Miqdor musbat bo'lishi kerak!")
        self.__balans += miqdor

    def chiqim(self, miqdor):
        if miqdor > self.__balans:
            raise ValueError("Mablag' yetarli emas!")
        self.__balans -= miqdor

    @abstractmethod
    def tolov_qil(self, miqdor, qabul_qiluvchi):
        """Har tizim o'zi amalga oshiradi"""
        pass

    @abstractmethod
    def nomi(self):
        pass

    def __str__(self):
        return f"{self.nomi()} | {self.egasi} | {self.__balans:,.2f} so'm"


class PaymeTolov(TolovTizimi):
    def nomi(self):
        return "Payme"

    def tolov_qil(self, miqdor, qabul_qiluvchi):
        try:
            self.chiqim(miqdor)
            print(f"✓ Payme orqali {miqdor:,} so'm {qabul_qiluvchi}ga yuborildi")
        except ValueError as e:
            print(f"Payme xato: {e}")


class UzumTolov(TolovTizimi):
    def nomi(self):
        return "Uzum"

    def tolov_qil(self, miqdor, qabul_qiluvchi):
        komissiya = miqdor * 0.01   # 1% komissiya
        jami = miqdor + komissiya
        try:
            self.chiqim(jami)
            print(f"✓ Uzum orqali {miqdor:,} so'm ({komissiya:,.0f} so'm komissiya) {qabul_qiluvchi}ga yuborildi")
        except ValueError as e:
            print(f"Uzum xato: {e}")


# Test:
payme = PaymeTolov("Ali")
payme.kirim(500_000)
print(payme)
payme.tolov_qil(100_000, "Do'kon")
payme.tolov_qil(500_000, "Hamyon")  # Mablag' yetmaydi

uzum = UzumTolov("Vali")
uzum.kirim(1_000_000)
uzum.tolov_qil(200_000, "Market")
print(uzum)


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Inkapsulatsiya (O'rta):
  Parol menejeri classini yarating:
    - __parollar = {} (xizmat: parol)
    - __master_parol — o'zgarmas kirish kaliti
    - qo'sh(xizmat, parol, master) — yangi parol saqlash
    - ko'rish(xizmat, master) — parolni olish
    - o'chir(xizmat, master) — parolni o'chirish
    - ro'yxat(master) — barcha xizmatlar (parols yashirin)

TOPSHIRIQ 2 — @property (O'rta):
  Harorat classini yarating:
    - __celsius qiymati saqlanadi
    - celsius — getter/setter (−273.15 dan past bo'lmasin)
    - fahrenheit — getter (C*9/5+32) va setter (F ni C ga aylantiradi)
    - kelvin — getter (C+273.15)

TOPSHIRIQ 3 — Abstraktsiya (Qiyin):
  Xabar tizimi yarating:
    Xabar(ABC) — abstract:
      yuborish(mazmun, kimga) — abstract
    EmailXabar(Xabar)
    SMSXabar(Xabar)
    TelegramXabar(Xabar)

  Har bir class o'z formatida "xabar yuboradi" (print qiladi).
  Bir ro'yxatda barchani ko'rsating.
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ Inkapsulatsiya nima — ma'lumotni yashirish
✔️ Kirish darajalari:
    public     ism     — hamma ko'radi
    protected  _ism    — konventsiya (majburiy emas)
    private    __ism   — haqiqiy yashirish (name mangling)
✔️ @property   — getter (o'qish)
✔️ @nom.setter — setter (tekshirib yozish)
✔️ uuid.uuid4() — unikal ID yaratish
✔️ Abstraktsiya nima — murakkablikni yashirish
✔️ ABC va @abstractmethod:
    from abc import ABC, abstractmethod
    class Shakl(ABC):
        @abstractmethod
        def yuzi(self): pass
✔️ Abstract classdan to'g'ridan-to'g'ri ob'ekt yaratib bo'lmaydi
✔️ Bola class barcha @abstractmethod larni amalga oshirishi SHART
"""