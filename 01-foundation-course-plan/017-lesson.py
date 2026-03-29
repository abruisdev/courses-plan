# ============================================================
#   DARS 17: Pythonda OOP — Class va Object
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# OOP (Obyektga Yo'naltirilgan Dasturlash) NIMA?
# ------------------------------------------------------------

"""
OOP — bu dasturni "obyektlar" asosida tuzish usuli.

Kundalik hayotda hamma narsa — obyekt:
  🚗 Mashina:
      xususiyatlari (attribute): rang, marka, tezlik
      harakatlari   (method):    yur(), to'xta(), siqnal_ber()

  👤 Inson:
      xususiyatlari: ism, yosh, bo'y
      harakatlari:   gapir(), yur(), uxla()

  📱 Telefon:
      xususiyatlari: model, xotira, rang
      harakatlari:   qo'ng'iroq_qil(), mesaj_yubor()

OOP asosiy tushunchalari:
  Class    — shablon (qolip), masalan: "Mashina" turi
  Object   — classdan yaratilgan haqiqiy narsa, masalan: "Mening mashinam"
  Attribute— ob'ektning xususiyatlari (o'zgaruvchilar)
  Method   — ob'ektning harakatlari (funksiyalar)

Nima uchun OOP?
  ✔️ Katta loyihalar uchun qulay
  ✔️ Kodni qayta ishlatish oson
  ✔️ Hayotiy modellashtirish
  ✔️ Xatoliklarni topish osonlashadi
"""


# ============================================================
# CLASS YARATISH
# ============================================================

"""
Sintaksis:
  class ClassName:
      def __init__(self, parametrlar):
          self.xususiyat = qiymat

      def metod(self):
          ...

Qoidalar:
  - Class nomi CamelCase bilan yoziladi (har so'z bosh harfdan)
  - self — ob'ektning o'ziga ishora qiladi
"""

# ── ENG ODDIY CLASS ───────────────────────────────────────────
class Salom:
    def ayt(self):
        print("Assalomu alaykum!")

s = Salom()    # ob'ekt yaratish
s.ayt()        # Assalomu alaykum!

# ── __init__() — Konstruktor ──────────────────────────────────
"""
__init__() — ob'ekt yaratilganda AVTOMATIK chaqiriladi.
Ob'ektning boshlang'ich xususiyatlarini belgilash uchun ishlatiladi.

self — ob'ektning o'zi. Har bir metodda BIRINCHI parametr bo'lishi shart.
"""

class Talaba:
    def __init__(self, ism, yosh, sinf):
        self.ism  = ism     # self.ism = ob'ektning "ism" xususiyati
        self.yosh = yosh
        self.sinf = sinf

# Ob'ekt yaratish:
t1 = Talaba("Ali", 15, "9-A")
t2 = Talaba("Vali", 16, "10-B")

# Xususiyatlariga murojaat:
print(t1.ism)     # Ali
print(t1.yosh)    # 15
print(t2.sinf)    # 10-B
print(t2.ism)     # Vali

# Xususiyatni o'zgartirish:
t1.yosh = 16
print(t1.yosh)    # 16


# ============================================================
# __str__() — CHIQARISH FORMATI
# ============================================================

"""
__str__() — print(ob'ekt) qilganda ko'rsatiladigan matnni belgilaydi.
Bu ham "dunder" (double underscore) metod deyiladi.
"""

class Talaba:
    def __init__(self, ism, yosh, sinf):
        self.ism  = ism
        self.yosh = yosh
        self.sinf = sinf

    def __str__(self):
        return f"Talaba({self.ism}, {self.yosh} yosh, {self.sinf})"

t = Talaba("Jasur", 17, "11-A")
print(t)    # Talaba(Jasur, 17 yosh, 11-A)
# __str__ bo'lmasa: <__main__.Talaba object at 0x...>


# ============================================================
# METODLAR
# ============================================================

"""
Metod — class ichida yozilgan funksiya.
Har doim birinchi parametr self bo'ladi.
"""

class Talaba:
    def __init__(self, ism, yosh):
        self.ism  = ism
        self.yosh = yosh
        self.baholar = []        # bo'sh list — keyinchalik to'ldiriladi

    def __str__(self):
        return f"{self.ism} ({self.yosh} yosh)"

    # ── Metod 1: Baho qo'shish ────────────────────────────────
    def baho_qo_sh(self, baho):
        self.baholar.append(baho)
        print(f"{self.ism}ga {baho} baho qo'shildi")

    # ── Metod 2: O'rtacha baho ────────────────────────────────
    def ortacha_baho(self):
        if not self.baholar:
            return 0
        return round(sum(self.baholar) / len(self.baholar), 1)

    # ── Metod 3: Ma'lumot chiqarish ───────────────────────────
    def info(self):
        print(f"\n--- {self.ism} haqida ---")
        print(f"Yosh          : {self.yosh}")
        print(f"Baholar       : {self.baholar}")
        print(f"O'rtacha baho : {self.ortacha_baho()}")

    # ── Metod 4: Darajani aniqlash ────────────────────────────
    def daraja(self):
        ort = self.ortacha_baho()
        if ort >= 90: return "A"
        elif ort >= 80: return "B"
        elif ort >= 70: return "C"
        elif ort >= 50: return "D"
        else: return "F"


# Ishlatish:
t1 = Talaba("Ali", 15)
t1.baho_qo_sh(85)
t1.baho_qo_sh(92)
t1.baho_qo_sh(78)
t1.info()
print(f"Daraja: {t1.daraja()}")

t2 = Talaba("Vali", 16)
t2.baho_qo_sh(95)
t2.baho_qo_sh(98)
print(f"\n{t2} — Daraja: {t2.daraja()}")


# ============================================================
# CLASS ATRIBUTLARI vs INSTANCE ATRIBUTLARI
# ============================================================

"""
Instance attribute — har ob'ektda ALOHIDA (self.nom bilan)
Class attribute    — BARCHA ob'ektlar uchun umumiy (class darajasida)
"""

class Talaba:
    maktab = "15-sonli maktab"      # Class attribute — umumiy
    soni   = 0                       # Nechta ob'ekt yaratilgan

    def __init__(self, ism, yosh):
        self.ism  = ism              # Instance attribute — har birida alohida
        self.yosh = yosh
        Talaba.soni += 1            # har ob'ekt yaratilganda oshadi

    def __str__(self):
        return f"{self.ism} | {Talaba.maktab}"

t1 = Talaba("Ali",  15)
t2 = Talaba("Vali", 16)
t3 = Talaba("Jasur",17)

print(t1)               # Ali | 15-sonli maktab
print(t2.maktab)        # 15-sonli maktab  (class attribute)
print(Talaba.maktab)    # 15-sonli maktab  (class orqali ham)
print(Talaba.soni)      # 3  — 3 ta ob'ekt yaratildi


# ============================================================
# AMALIY MISOLLAR
# ============================================================

# ── MISOL 1: Bank Hisobi ──────────────────────────────────────
class BankHisobi:
    def __init__(self, egasi, balans=0):
        self.egasi  = egasi
        self.balans = balans
        self.tarix  = []

    def __str__(self):
        return f"{self.egasi} | Balans: {self.balans:,} so'm"

    def kirim(self, miqdor):
        if miqdor <= 0:
            print("Miqdor musbat bo'lishi kerak!")
            return
        self.balans += miqdor
        self.tarix.append(f"+{miqdor:,}")
        print(f"✓ {miqdor:,} so'm kirim. Balans: {self.balans:,}")

    def chiqim(self, miqdor):
        if miqdor <= 0:
            print("Miqdor musbat bo'lishi kerak!")
            return
        if miqdor > self.balans:
            print("Mablag' yetarli emas!")
            return
        self.balans -= miqdor
        self.tarix.append(f"-{miqdor:,}")
        print(f"✓ {miqdor:,} so'm chiqim. Balans: {self.balans:,}")

    def ko_chirish(self):
        print(f"\n--- {self.egasi} hisobi tarixi ---")
        for tr in self.tarix:
            print(f"  {tr} so'm")
        print(f"Joriy balans: {self.balans:,} so'm")


hisob = BankHisobi("Ali Karimov", 100_000)
print(hisob)
hisob.kirim(50_000)
hisob.kirim(25_000)
hisob.chiqim(30_000)
hisob.chiqim(200_000)   # Xato
hisob.ko_chirish()

# ── MISOL 2: Mashina ─────────────────────────────────────────
class Mashina:
    def __init__(self, marka, model, yil, rang="oq"):
        self.marka   = marka
        self.model   = model
        self.yil     = yil
        self.rang    = rang
        self.tezlik  = 0
        self.yoqildi = False

    def __str__(self):
        holat = "yoqilgan" if self.yoqildi else "o'chgan"
        return f"{self.yil} {self.marka} {self.model} ({self.rang}) — {holat}"

    def yoq(self):
        if not self.yoqildi:
            self.yoqildi = True
            print(f"{self.model} yoqildi!")
        else:
            print("Mashina allaqachon yonmoqda!")

    def o_chir(self):
        self.yoqildi = False
        self.tezlik  = 0
        print(f"{self.model} o'chirildi.")

    def tezlash(self, miqdor):
        if not self.yoqildi:
            print("Avval mashinani yoqing!")
            return
        self.tezlik += miqdor
        print(f"Tezlik: {self.tezlik} km/h")

    def tormoz(self):
        if self.tezlik > 0:
            self.tezlik = max(0, self.tezlik - 20)
            print(f"Tormoz! Tezlik: {self.tezlik} km/h")


mashina = Mashina("Chevrolet", "Malibu", 2023, "qora")
print(mashina)
mashina.yoq()
mashina.tezlash(30)
mashina.tezlash(50)
mashina.tormoz()
mashina.o_chir()


# ============================================================
# AMALIY DASTUR — O'quvchilar boshqaruv tizimi
# ============================================================

class O_quvchi:
    def __init__(self, ism, sinf):
        self.ism    = ism
        self.sinf   = sinf
        self.fanlar = {}    # fan: [baholar]

    def __str__(self):
        return f"{self.ism} ({self.sinf})"

    def baho_qo_sh(self, fan, baho):
        if fan not in self.fanlar:
            self.fanlar[fan] = []
        self.fanlar[fan].append(baho)

    def fan_ortacha(self, fan):
        if fan not in self.fanlar or not self.fanlar[fan]:
            return 0
        return round(sum(self.fanlar[fan]) / len(self.fanlar[fan]), 1)

    def umumiy_ortacha(self):
        if not self.fanlar:
            return 0
        hammasi = [b for baholar in self.fanlar.values() for b in baholar]
        return round(sum(hammasi) / len(hammasi), 1)

    def hisobot(self):
        print(f"\n{'=' * 40}")
        print(f"  {self.ism}  |  {self.sinf}")
        print(f"{'=' * 40}")
        for fan, baholar in self.fanlar.items():
            ort = self.fan_ortacha(fan)
            print(f"  {fan:<15} : {baholar}  → {ort}")
        print(f"{'─' * 40}")
        print(f"  Umumiy o'rtacha: {self.umumiy_ortacha()}")


o = O_quvchi("Jasur Toshev", "10-A")
o.baho_qo_sh("Matematika", 90)
o.baho_qo_sh("Matematika", 88)
o.baho_qo_sh("Fizika", 85)
o.baho_qo_sh("Fizika", 92)
o.baho_qo_sh("Ingliz", 95)
o.hisobot()


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Asosiy (Oson):
  Kitob classini yarating:
    Atributlar: nomi, muallif, yil, narx
    Metodlar:
      __str__()         — chiroyli chiqarish
      chegirma(foiz)    — chegirmadan keyingi narxni qaytaradi

TOPSHIRIQ 2 — O'rta:
  Doira classini yarating:
    Atributlar: radius
    Metodlar:
      yuzi()       — π * r²
      uzunligi()   — 2 * π * r
      __str__()    — "Doira(r=5, yuz=78.54)"

TOPSHIRIQ 3 — O'rta:
  Hayvon classini yarating:
    Atributlar: ism, tur, yosh
    Metodlar:
      ovoz_chiqar()  — turi bo'yicha ("Mushuk: miyov", "It: hav-hav")
      info()         — to'liq ma'lumot
      __str__()

TOPSHIRIQ 4 — Qiyin:
  Do'kon classini yarating:
    Atributlar: nomi, mahsulotlar = {} (nom: narx)
    Metodlar:
      qo_sh(nom, narx)   — mahsulot qo'shish
      o_chir(nom)        — mahsulot o'chirish
      qidirish(nom)      — narxini topish
      jami_qiymat()      — barcha mahsulot qiymati
      hisobot()          — barcha mahsulot ro'yxati
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ OOP nima — class, object, attribute, method
✔️ class yaratish sintaksisi
✔️ __init__() — konstruktor (ob'ekt yaratilganda chaqiriladi)
✔️ self — ob'ektning o'ziga ishora
✔️ __str__() — print() qilganda ko'rinadigan matn
✔️ Metodlar — class ichidagi funksiyalar
✔️ Atributlarga murojaat: ob'ekt.xususiyat
✔️ Xususiyatni o'zgartirish: ob'ekt.xususiyat = yangi
✔️ Instance attribute vs Class attribute
✔️ Amaliy misollar: BankHisobi, Mashina, O'quvchi
"""