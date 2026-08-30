# ============================================================
#   DARS 10: Pythonda Tuple, Set va Dictionary
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ Tuple, Set va Dictionary nima ekanini
  ✔️ Ularning farqi va qo‘llanish holatlarini
  ✔️ Asosiy metodlarini
  ✔️ Kontaktlar va baholar tizimini
"""


# ------------------------------------------------------------
# TUPLE
# ------------------------------------------------------------

"""
Tuple — o‘zgarmas ketma-ketlik.
Tuple ( ) qavslar bilan yoziladi.
Listdan farqi: tuple yaratilgandan keyin elementlarini o‘zgartirib
bo‘lmaydi.
"""

ranglar = ("qizil", "yashil", "ko‘k")
print(ranglar[0])
print(ranglar[-1])
print(ranglar[1:])
print(ranglar.count("qizil"))
print(ranglar.index("yashil"))

# Bitta elementli tupleda vergul shart
bitta_son = (5,)
print(type(bitta_son))

# Packing va unpacking
talaba = ("Ali", 18, "Toshkent")
ism, yosh, shahar = talaba
print(ism, yosh, shahar)

# O‘zgaruvchilar qiymatini almashtirish
x = 10
y = 20
x, y = y, x
print(x, y)


# ------------------------------------------------------------
# SET
# ------------------------------------------------------------

"""
Set — takrorlanmaydigan, tartibsiz elementlar to‘plami.
Set { } qavslar bilan yoziladi.
Bo‘sh set yaratish uchun set() ishlatiladi.
"""

sonlar = {1, 2, 2, 3, 3, 3, 4}
print(sonlar)  # Takrorlar o‘chadi

bosh_set = set()
bosh_set.add("Python")
bosh_set.update(["Git", "SQL"])
print(bosh_set)

bosh_set.discard("Java")  # Xato bermaydi
bosh_set.remove("Git")    # Element bo‘lmasa xato beradi
print(bosh_set)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)  # Union — birlashtirish
print(a & b)  # Intersection — kesishma
print(a - b)  # Difference — farq
print(a ^ b)  # Symmetric difference


# ------------------------------------------------------------
# DICTIONARY
# ------------------------------------------------------------

"""
Dictionary — kalit: qiymat ko‘rinishida ma’lumot saqlaydi.
Dictionary { } qavslar bilan yoziladi.
Kalitlar takrorlanmasligi kerak.
"""

talaba = {
    "ism": "Ali",
    "yosh": 18,
    "shahar": "Toshkent",
}

print(talaba["ism"])
print(talaba.get("telefon"))
print("yosh" in talaba)

# Qo‘shish va yangilash
talaba["telefon"] = "+998901234567"
talaba["yosh"] = 19
talaba.update({"kurs": "Python Foundation"})
print(talaba)

# O‘chirish
talaba.pop("telefon")
del talaba["kurs"]

# keys(), values(), items()
print(talaba.keys())
print(talaba.values())
print(talaba.items())

for kalit, qiymat in talaba.items():
    print(f"{kalit}: {qiymat}")


# ------------------------------------------------------------
# ICHMA-ICH DICTIONARY
# ------------------------------------------------------------

oquvchilar = {
    "ali": {"ism": "Ali", "baho": 85},
    "madina": {"ism": "Madina", "baho": 92},
}

print(oquvchilar["ali"]["baho"])

for login, malumot in oquvchilar.items():
    print(login, "→", malumot["ism"], malumot["baho"])


# ------------------------------------------------------------
# DICTIONARY COMPREHENSION
# ------------------------------------------------------------

kvadratlar = {son: son ** 2 for son in range(1, 6)}
print(kvadratlar)


# ------------------------------------------------------------
# AMALIY LOYIHA — KONTAKTLAR DAFTARI
# ------------------------------------------------------------

kontaktlar = {}

while True:
    print("\n--- KONTAKTLAR ---")
    print("1. Kontakt qo‘shish")
    print("2. Kontaktni ko‘rish")
    print("3. Kontaktni o‘chirish")
    print("0. Chiqish")

    tanlov = input("Tanlov: ")

    if tanlov == "1":
        ism = input("Ism: ")
        telefon = input("Telefon: ")
        kontaktlar[ism] = telefon
    elif tanlov == "2":
        for ism, telefon in kontaktlar.items():
            print(f"{ism}: {telefon}")
    elif tanlov == "3":
        ism = input("O‘chiriladigan ism: ")
        kontaktlar.pop(ism, None)
    elif tanlov == "0":
        break


# ------------------------------------------------------------
# AMALIY LOYIHA — O‘QUVCHILAR BAHOSI
# ------------------------------------------------------------

baholar = {
    "Ali": 85,
    "Madina": 92,
    "Vali": 65,
}

for ism, baho in baholar.items():
    holat = "O‘tdi" if baho >= 56 else "O‘tmadi"
    print(f"{ism}: {baho} — {holat}")


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. 5 ta shahar saqlangan tuple yarating.
2. List ichidagi takrorlangan ismlarni set yordamida o‘chiring.
3. 2 ta set yaratib, ularning kesishmasini chiqaring.
4. O‘zingiz haqingizda dictionary yarating.
5. Kontaktlar dasturiga kontakt qidirish funksiyasini qo‘shing.
6. Baholar dictionarysidan o‘rtacha bahoni aniqlang.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ Tuple va unpacking
✔️ Set va set amallari
✔️ Dictionary yaratish va metodlari
✔️ Ichma-ich dictionary
✔️ Dictionary comprehension
✔️ Kontaktlar va baholar tizimini
"""
