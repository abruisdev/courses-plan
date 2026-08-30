# ============================================================
#   DARS 8: Pythonda String va String Metodlari
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ String yaratish, indekslash va slicing
  ✔️ len() va f-string
  ✔️ upper(), lower(), title(), capitalize()
  ✔️ find(), index(), count(), startswith(), endswith()
  ✔️ replace(), strip(), split(), join()
  ✔️ isdigit(), isalpha(), isalnum()
"""


# ------------------------------------------------------------
# STRING NIMA?
# ------------------------------------------------------------

"""
String (str) — matn ko‘rinishidagi ma’lumot.
String qo‘shtirnoq yoki birtirnoq ichida yoziladi.
"""

ism = "Ali Karimov"
shahar = 'Toshkent'
print(ism)
print(shahar)


# ------------------------------------------------------------
# INDEKSLASH VA SLICING
# ------------------------------------------------------------

"""
Stringdagi belgilar 0 dan boshlab raqamlanadi.

  P  y  t  h  o  n
  0  1  2  3  4  5

Manfiy indeks oxirdan boshlanadi:
  -6 -5 -4 -3 -2 -1
"""

soz = "Python"
print(soz[0])       # P
print(soz[2])       # t
print(soz[-1])      # n

# slicing: [boshlanish:tugash]
print(soz[0:3])     # Pyt
print(soz[2:])      # thon
print(soz[:4])      # Pyth
print(soz[::-1])    # nohtyP


# ------------------------------------------------------------
# len() VA f-string
# ------------------------------------------------------------

print(len("Python"))

ism = "Madina"
yosh = 20
print(f"Mening ismim {ism}, yoshim {yosh} da.")


# ------------------------------------------------------------
# REGISTR METODLARI
# ------------------------------------------------------------

matn = "salom python"
print(matn.upper())        # SALOM PYTHON
print(matn.lower())        # salom python
print(matn.title())        # Salom Python
print(matn.capitalize())   # Salom python
print(matn.swapcase())     # SALOM PYTHON


# ------------------------------------------------------------
# QIDIRISH METODLARI
# ------------------------------------------------------------

matn = "Python Backend kursi"
print(matn.find("Backend"))       # 7
print(matn.find("Java"))          # -1
print(matn.index("kursi"))        # 15
print(matn.count("o"))            # 2
print(matn.startswith("Python"))  # True
print(matn.endswith("kursi"))     # True
print("Backend" in matn)          # True

"""
find() topilmasa -1 qaytaradi.
index() topilmasa xato beradi.
Shuning uchun qidirishda find() yoki in ishlatish qulayroq.
"""


# ------------------------------------------------------------
# O‘ZGARTIRISH METODLARI
# ------------------------------------------------------------

matn = "   Assalomu alaykum   "
print(matn.strip())

telefon = "+998 90 123 45 67"
telefon_toza = telefon.replace(" ", "")
print(telefon_toza)

gap = "Men Python o‘rganayapman"
print(gap.replace("Python", "Backend"))


# ------------------------------------------------------------
# split() VA join()
# ------------------------------------------------------------

gap = "Ali Vali Hasan"
ismlar = gap.split()
print(ismlar)

sana = "2026-08-31"
qismlar = sana.split("-")
print(qismlar)

telefon_qismlari = ["+998", "90", "123", "45", "67"]
print(" ".join(telefon_qismlari))
print("-".join(qismlar))


# ------------------------------------------------------------
# TEKSHIRISH METODLARI
# ------------------------------------------------------------

print("12345".isdigit())       # True
print("12a45".isdigit())       # False
print("Python".isalpha())      # True
print("Python3".isalpha())     # False
print("Ali123".isalnum())      # True
print("Ali 123".isalnum())     # False
print("PYTHON".isupper())      # True
print("python".islower())      # True


# ------------------------------------------------------------
# AMALIY MISOL 1 — ISM FORMATLASH
# ------------------------------------------------------------

ism = input("Ismingizni kiriting: ").strip()
familiya = input("Familiyangizni kiriting: ").strip()

print(f"Assalomu alaykum, {ism.title()} {familiya.title()}!")


# ------------------------------------------------------------
# AMALIY MISOL 2 — TELEFON RAQAM TEKSHIRISH
# ------------------------------------------------------------

telefon = input("Telefon raqamingizni kiriting: ")
telefon = telefon.replace(" ", "").replace("-", "")

if telefon.startswith("+998") and telefon[1:].isdigit() and len(telefon) == 13:
    print("Telefon raqam to‘g‘ri")
else:
    print("Telefon raqam noto‘g‘ri")


# ------------------------------------------------------------
# AMALIY MISOL 3 — MATNDAGI SO‘ZLARNI SANASH
# ------------------------------------------------------------

matn = input("Matn kiriting: ").strip()
sozlar = matn.split()

print("Belgilar soni:", len(matn))
print("So‘zlar soni:", len(sozlar))


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1:
  Ismingizni oling va uning birinchi, oxirgi harfini hamda
  teskarisini chiqaring.

TOPSHIRIQ 2:
  Foydalanuvchidan email oling.
  Unda @ belgisi bo‘lsa "Email qabul qilindi" deb chiqaring.

TOPSHIRIQ 3:
  Foydalanuvchidan gap oling.
  Nechta "a" harfi borligini aniqlang.

TOPSHIRIQ 4:
  "python backend" matnini "Python Backend" ko‘rinishiga keltiring.

TOPSHIRIQ 5:
  Foydalanuvchidan ism-familiya oling.
  Uni "Familiya, Ism" ko‘rinishida chiqaring.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ String yaratish
✔️ Indekslash va slicing
✔️ len() va f-string
✔️ String metodlari
✔️ Matnni formatlash va tekshirish
✔️ Telefon raqam va matn tahlili dasturlarini
"""
