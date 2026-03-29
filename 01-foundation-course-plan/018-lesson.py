# ============================================================
#   DARS 18: Pythonda Vorisdorlik va Polimorfizm
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# VORISDORLIK (Inheritance) NIMA?
# ------------------------------------------------------------

"""
Vorisdorlik — bir class boshqa classning barcha xususiyat va
metodlarini meros olishi.

Ota class  (Parent/Base class)   — umumiy qolip
Bola class (Child/Derived class) — ota classdan meros oladi + o'z narsalarini qo'shadi

Hayotiy misol:
  Hayvon (ota) → Mushuk (bola)
  Hayvon (ota) → It (bola)
  Hayvon (ota) → Qush (bola)

  Barcha hayvonlar: ism, yosh, ovqatlanadi(), uxlaydi()
  Mushuk: miyovlaydi(), tirnoq_chiqaradi()
  It:     huradi(), quyruq_likillatadi()

Nima uchun kerak?
  ✔️ Kodni qayta yozmaslik (DRY)
  ✔️ Mantiqiy ierarxiya yaratish
  ✔️ Yangi class yaratish osonlashadi
"""

# ============================================================
# OTA CLASS YARATISH
# ============================================================

class Hayvon:
    def __init__(self, ism, yosh):
        self.ism  = ism
        self.yosh = yosh

    def __str__(self):
        return f"{self.__class__.__name__}: {self.ism} ({self.yosh} yosh)"

    def ovqatlan(self):
        print(f"{self.ism} ovqatlanmoqda...")

    def uxla(self):
        print(f"{self.ism} uxlamoqda... 💤")

    def info(self):
        print(f"Ism: {self.ism}, Yosh: {self.yosh}")


# ============================================================
# BOLA CLASS — VORISDORLIK
# ============================================================

"""
Sintaksis:
  class BolaClass(OtaClass):
      ...
"""

# ── Mushuk — Hayvondan meros oladi ───────────────────────────
class Mushuk(Hayvon):
    def __init__(self, ism, yosh, rang):
        super().__init__(ism, yosh)   # ota classning __init__ chaqiriladi
        self.rang = rang              # o'z atributi

    def miyovla(self):
        print(f"{self.ism}: Miyov! 🐱")

    def tirnoq_chiqar(self):
        print(f"{self.ism} tirnoqlarini chiqarmoqda...")


# ── It — Hayvondan meros oladi ────────────────────────────────
class It(Hayvon):
    def __init__(self, ism, yosh, zoti):
        super().__init__(ism, yosh)
        self.zoti = zoti

    def hur(self):
        print(f"{self.ism}: Vov-vov! 🐶")

    def quyruq_lilkilat(self):
        print(f"{self.ism} quyruq lilkilatmoqda!")


# ── Qush — Hayvondan meros oladi ─────────────────────────────
class Qush(Hayvon):
    def __init__(self, ism, yosh, qanotlar_kengligi):
        super().__init__(ism, yosh)
        self.qanotlar_kengligi = qanotlar_kengligi

    def uchib_ket(self):
        print(f"{self.ism} uchmoqda! (qanot kengligi: {self.qanotlar_kengligi}cm) 🦅")

    def sayra(self):
        print(f"{self.ism}: Chiv-chiv! 🎵")


# ── Test ─────────────────────────────────────────────────────
mushuk = Mushuk("Miti", 3, "oq")
it     = It("Rex", 5, "Alabay")
qush   = Qush("Twitty", 2, 45)

# Ota classdan meros olingan metodlar:
mushuk.ovqatlan()     # Hayvon classi metodi
mushuk.uxla()         # Hayvon classi metodi

# O'z metodlari:
mushuk.miyovla()
mushuk.tirnoq_chiqar()

it.ovqatlan()
it.hur()
it.quyruq_lilkilat()

qush.uxla()
qush.uchib_ket()
qush.sayra()

# __str__ chiqarish:
print(mushuk)    # Mushuk: Miti (3 yosh)
print(it)        # It: Rex (5 yosh)


# ============================================================
# super() FUNKSIYASI
# ============================================================

"""
super() — ota classga murojaat qilish.

Asosiy ishlatish:
  1. Ota __init__ ni chaqirish
  2. Ota metodini chaqirish (kengaytirish)
"""

class Transport:
    def __init__(self, marka, yil):
        self.marka = marka
        self.yil   = yil
        self.tezlik = 0

    def __str__(self):
        return f"{self.yil} {self.marka}"

    def ma_lumot(self):
        print(f"Marka: {self.marka}, Yil: {self.yil}")


class Avtomobil(Transport):
    def __init__(self, marka, yil, eshiklar=4):
        super().__init__(marka, yil)         # ota __init__ chaqiriladi
        self.eshiklar = eshiklar

    def ma_lumot(self):
        super().ma_lumot()                    # ota metodini ham chaqiradi
        print(f"Eshiklar soni: {self.eshiklar}")  # o'zining qo'shimchasi


class Samolyot(Transport):
    def __init__(self, marka, yil, qanotlar_soni):
        super().__init__(marka, yil)
        self.qanotlar_soni = qanotlar_soni

    def ma_lumot(self):
        super().ma_lumot()
        print(f"Qanotlar: {self.qanotlar_soni}")

    def uchib_ket(self):
        print(f"{self.marka} uchib ketmoqda! ✈️")


avto    = Avtomobil("Chevrolet", 2023, 4)
samolyot = Samolyot("Boeing", 2020, 2)

avto.ma_lumot()
print()
samolyot.ma_lumot()
samolyot.uchib_ket()


# ============================================================
# POLIMORFIZM (Polymorphism) NIMA?
# ============================================================

"""
Polimorfizm — "ko'p shakllilik".
Bir xil metod nomi, turli classlar uchun TURLICHA ishlashi.

Hayotiy misol:
  draw() metodi:
    Doira.draw()       — doira chizadi
    To'rtburchak.draw() — to'rtburchak chizadi
    Uchburchak.draw()  — uchburchak chizadi

  Hamma draw() deyiladi, lekin har biri boshqacha ishlaydi.
"""

# ── MISOL 1: Hayvonlar ovozi ──────────────────────────────────
class Hayvon:
    def __init__(self, ism):
        self.ism = ism

    def ovoz(self):
        return "..."     # ota class — umumiy


class Mushuk(Hayvon):
    def ovoz(self):      # ota metodini QAYTA YOZISH (override)
        return "Miyov!"


class It(Hayvon):
    def ovoz(self):      # override
        return "Vov-vov!"


class Sigir(Hayvon):
    def ovoz(self):      # override
        return "Moo!"


class Ot(Hayvon):
    def ovoz(self):      # override
        return "I-go-go!"


# Polimorfizm:
hayvonlar = [
    Mushuk("Miti"),
    It("Rex"),
    Sigir("Burenka"),
    Ot("Tulpar"),
]

for hayvon in hayvonlar:
    print(f"{hayvon.ism}: {hayvon.ovoz()}")
# Miti: Miyov!
# Rex: Vov-vov!
# Burenka: Moo!
# Tulpar: I-go-go!


# ── MISOL 2: Shakllar ─────────────────────────────────────────
import math

class Shakl:
    def yuzi(self):
        return 0

    def perimetri(self):
        return 0

    def info(self):
        print(f"{self.__class__.__name__}:")
        print(f"  Yuzi      : {self.yuzi():.2f}")
        print(f"  Perimetri : {self.perimetri():.2f}")


class Doira(Shakl):
    def __init__(self, radius):
        self.radius = radius

    def yuzi(self):
        return math.pi * self.radius ** 2

    def perimetri(self):
        return 2 * math.pi * self.radius


class To_g_ri_to_rtburchak(Shakl):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def yuzi(self):
        return self.a * self.b

    def perimetri(self):
        return 2 * (self.a + self.b)


class Uchburchak(Shakl):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def yuzi(self):
        # Geron formulasi: s = √(p(p-a)(p-b)(p-c)), p = (a+b+c)/2
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p-self.a) * (p-self.b) * (p-self.c))

    def perimetri(self):
        return self.a + self.b + self.c


# Polimorfizm — bir xil interfeys, turli natijalar:
shakllar = [
    Doira(5),
    To_g_ri_to_rtburchak(4, 6),
    Uchburchak(3, 4, 5),
]

for shakl in shakllar:
    shakl.info()
    print()


# ============================================================
# KO'P DARAJALI VORISDORLIK
# ============================================================

"""
Bola classning o'zi ham ota class bo'lishi mumkin.
"""

class Jonzot:
    def __init__(self, ism):
        self.ism = ism
        self.jonli = True

    def nafas_ol(self):
        print(f"{self.ism} nafas olmoqda")


class Hayvon(Jonzot):
    def __init__(self, ism, oyoqlar):
        super().__init__(ism)
        self.oyoqlar = oyoqlar

    def yur(self):
        print(f"{self.ism} {self.oyoqlar} oyoqda yurmoqda")


class It(Hayvon):
    def __init__(self, ism, zoti):
        super().__init__(ism, 4)       # itda 4 oyoq
        self.zoti = zoti

    def hur(self):
        print(f"{self.ism} ({self.zoti}): Vov!")


# Ko'p darajali meros:
it = It("Rex", "Nemis qo'ychi iti")
it.nafas_ol()    # Jonzot dan
it.yur()         # Hayvon dan
it.hur()         # It dan (o'zi)


# ============================================================
# isinstance() va issubclass()
# ============================================================

"""
isinstance(ob'ekt, class)     — ob'ekt shu classdan ekanini tekshiradi
issubclass(bola, ota)         — bola shu otadan merosmi tekshiradi
"""

mushuk = Mushuk("Miti")
print(isinstance(mushuk, Mushuk))    # True
print(isinstance(mushuk, Hayvon))    # True  (Hayvon dan meros!)
print(isinstance(mushuk, It))        # False

print(issubclass(Mushuk, Hayvon))    # True
print(issubclass(It,     Hayvon))    # True
print(issubclass(Hayvon, Mushuk))    # False


# ============================================================
# AMALIY DASTUR — Xodimlar tizimi
# ============================================================

class Xodim:
    def __init__(self, ism, id, maosh):
        self.ism   = ism
        self.id    = id
        self.maosh = maosh

    def __str__(self):
        return f"[{self.id}] {self.ism}"

    def info(self):
        print(f"\n{'─' * 35}")
        print(f"  Ism       : {self.ism}")
        print(f"  ID        : {self.id}")
        print(f"  Maosh     : {self.maosh:,} so'm")
        print(f"  Lavozim   : {self.__class__.__name__}")

    def bonus(self):
        return 0    # ota class — bonus yo'q


class Dasturchi(Xodim):
    def __init__(self, ism, id, maosh, til):
        super().__init__(ism, id, maosh)
        self.dasturlash_tili = til

    def info(self):
        super().info()
        print(f"  Til       : {self.dasturlash_tili}")

    def bonus(self):
        return self.maosh * 0.2    # 20% bonus


class Menejer(Xodim):
    def __init__(self, ism, id, maosh, jamoa_soni):
        super().__init__(ism, id, maosh)
        self.jamoa_soni = jamoa_soni

    def info(self):
        super().info()
        print(f"  Jamoa     : {self.jamoa_soni} kishi")

    def bonus(self):
        return self.maosh * 0.15 + self.jamoa_soni * 50_000


class Dizayner(Xodim):
    def __init__(self, ism, id, maosh, dastur):
        super().__init__(ism, id, maosh)
        self.dastur = dastur

    def info(self):
        super().info()
        print(f"  Dastur    : {self.dastur}")

    def bonus(self):
        return self.maosh * 0.1


# Test:
xodimlar = [
    Dasturchi("Ali Karimov",    "D001", 8_000_000, "Python"),
    Menejer("Vali Rahimov",     "M001", 12_000_000, 8),
    Dizayner("Jasur Toshev",    "DZ001", 7_000_000, "Figma"),
    Dasturchi("Bobur Hasanov",  "D002", 9_000_000, "Java"),
]

print("=== XODIMLAR RO'YXATI ===")
jami_maosh  = 0
jami_bonus  = 0

for x in xodimlar:
    x.info()
    bonus = x.bonus()
    print(f"  Bonus     : {bonus:,.0f} so'm")
    jami_maosh += x.maosh
    jami_bonus += bonus

print(f"\n{'=' * 35}")
print(f"  Jami maosh : {jami_maosh:,} so'm")
print(f"  Jami bonus : {jami_bonus:,.0f} so'm")
print(f"  To'liq to'lov: {jami_maosh + jami_bonus:,.0f} so'm")


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Vorisdorlik (O'rta):
  Transport → Avtomobil, Mototsikl, Velosiped
    Transport: marka, tezlik, yur(), to'xta()
    Avtomobil: + eshiklar_soni, siqnal()
    Mototsikl: + motor_hajmi, drift()
    Velosiped: + g_ildirak_o_lchami, pedalda()

TOPSHIRIQ 2 — Polimorfizm (O'rta):
  Hisoblash masinasi yarating:
    Amal (ota): bajar(a, b)
    Qo'shish(Amal): a + b
    Ayirish(Amal): a - b
    Ko'paytirish(Amal): a * b
    Bo'lish(Amal): a / b

  amallar = [Qo'shish(), Ayirish(), Ko'paytirish(), Bo'lish()]
  for amal in amallar:
      print(amal.bajar(10, 3))

TOPSHIRIQ 3 — Murakkab (Qiyin):
  Onlayn do'kon:
    Mahsulot (ota): nom, narx, miqdor
    Elektron(Mahsulot): + kafolat_yil, texnik_xizmat()
    Kiyim(Mahsulot): + o'lcham, rang, yuvish_yo'riqnomasi()
    Oziq_ovqat(Mahsulot): + sana, + muddati_o'tish(), yangiligini_tekshir()
  Do'kon classida: mahsulotlar_qo'sh(), sotish(), inventar_hisobot()
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ Vorisdorlik nima — ota va bola class
✔️ class Bola(Ota): — sintaksis
✔️ super() — ota classga murojaat
✔️ Metodlarni override qilish (qayta yozish)
✔️ Ko'p darajali vorisdorlik
✔️ isinstance() va issubclass()
✔️ Polimorfizm nima — bir nom, turli xatti-harakat
✔️ Amaliy misollar:
    - Hayvonlar ierarxiyasi
    - Geometrik shakllar
    - Xodimlar tizimi
"""