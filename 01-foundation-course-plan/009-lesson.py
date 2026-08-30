# ============================================================
#   DARS 9: Pythonda List
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ List nima va yaratish usullari
  ✔️ Indekslash va slicing
  ✔️ append(), insert(), extend()
  ✔️ remove(), pop(), del, clear()
  ✔️ sort(), sorted(), reverse()
  ✔️ count(), index(), enumerate()
  ✔️ List comprehension
"""


# ------------------------------------------------------------
# LIST NIMA?
# ------------------------------------------------------------

"""
List — bir nechta qiymatni bitta o‘zgaruvchida saqlash usuli.
List [ ] qavslar ichida yoziladi va o‘zgaruvchan (mutable) bo‘ladi.
"""

ismlar = ["Ali", "Vali", "Madina"]
sonlar = [10, 20, 30, 40]
aralash = ["Ali", 18, 3.14, True]
bosh_list = []

print(ismlar)
print(sonlar)


# ------------------------------------------------------------
# INDEKSLASH VA SLICING
# ------------------------------------------------------------

mevalar = ["olma", "banan", "anor", "uzum"]
print(mevalar[0])
print(mevalar[-1])
print(mevalar[1:3])

# Elementni o‘zgartirish
mevalar[1] = "shaftoli"
print(mevalar)

print("anor" in mevalar)
print(len(mevalar))


# ------------------------------------------------------------
# QO‘SHISH METODLARI
# ------------------------------------------------------------

ismlar = ["Ali", "Vali"]
ismlar.append("Hasan")             # Oxiriga qo‘shadi
ismlar.insert(1, "Madina")         # Berilgan indeksga qo‘shadi
ismlar.extend(["Husan", "Aziza"]) # Boshqa listni qo‘shadi
print(ismlar)


# ------------------------------------------------------------
# O‘CHIRISH METODLARI
# ------------------------------------------------------------

sonlar = [10, 20, 30, 40, 50]
sonlar.remove(20)        # Qiymat bo‘yicha o‘chiradi
ochirilgan = sonlar.pop() # Oxirgi elementni o‘chirib qaytaradi
print(ochirilgan)
sonlar.pop(0)            # Indeks bo‘yicha o‘chiradi
del sonlar[0]
print(sonlar)

vaqtinchalik = [1, 2, 3]
vaqtinchalik.clear()
print(vaqtinchalik)


# ------------------------------------------------------------
# SARALASH VA QIDIRISH
# ------------------------------------------------------------

sonlar = [40, 10, 80, 25, 5]
sonlar.sort()
print(sonlar)

sonlar.sort(reverse=True)
print(sonlar)

asl_sonlar = [40, 10, 80, 25, 5]
saralangan = sorted(asl_sonlar)
print(asl_sonlar)
print(saralangan)

ismlar = ["Ali", "Vali", "Ali", "Madina"]
print(ismlar.count("Ali"))
print(ismlar.index("Vali"))


# ------------------------------------------------------------
# for VA enumerate()
# ------------------------------------------------------------

fanlar = ["Python", "Git", "SQL"]

for fan in fanlar:
    print(fan)

for indeks, fan in enumerate(fanlar, start=1):
    print(indeks, fan)


# ------------------------------------------------------------
# LIST COMPREHENSION
# ------------------------------------------------------------

"""
List comprehension — listni qisqa usulda yaratish.

    [ifoda for element in ketma_ketlik]
"""

kvadratlar = [son ** 2 for son in range(1, 6)]
juft_sonlar = [son for son in range(1, 21) if son % 2 == 0]
katta_harflar = [harf.upper() for harf in "python"]

print(kvadratlar)
print(juft_sonlar)
print(katta_harflar)


# ------------------------------------------------------------
# AMALIY MISOL 1 — XARAJATLAR RO‘YXATI
# ------------------------------------------------------------

xarajatlar = []

while True:
    summa = input("Xarajat summasini kiriting (exit - chiqish): ")

    if summa == "exit":
        break

    xarajatlar.append(float(summa))

print("Xarajatlar:", xarajatlar)
print("Jami xarajat:", sum(xarajatlar))


# ------------------------------------------------------------
# AMALIY MISOL 2 — BAHOLAR TIZIMI
# ------------------------------------------------------------

baholar = [85, 72, 90, 55, 68]
print("Eng katta baho:", max(baholar))
print("Eng kichik baho:", min(baholar))
print("O‘rtacha baho:", sum(baholar) / len(baholar))


# ------------------------------------------------------------
# AMALIY MISOL 3 — TO-DO LIST
# ------------------------------------------------------------

vazifalar = []

while True:
    print("\n1. Vazifa qo‘shish")
    print("2. Vazifalarni ko‘rish")
    print("3. Vazifani o‘chirish")
    print("0. Chiqish")

    tanlov = input("Tanlov: ")

    if tanlov == "1":
        vazifa = input("Vazifa nomi: ")
        vazifalar.append(vazifa)
    elif tanlov == "2":
        for indeks, vazifa in enumerate(vazifalar, start=1):
            print(indeks, ".", vazifa)
    elif tanlov == "3":
        vazifa = input("O‘chiriladigan vazifa: ")

        if vazifa in vazifalar:
            vazifalar.remove(vazifa)
        else:
            print("Bunday vazifa topilmadi")
    elif tanlov == "0":
        break


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. 5 ta meva saqlangan list yarating va 3-elementini chiqaring.
2. Listga 3 ta yangi ism qo‘shing, bittasini o‘chiring.
3. Sonlar listidan faqat musbat sonlarni yangi listga o‘tkazing.
4. Foydalanuvchidan 5 ta son olib, ularni saralang.
5. To-do list dasturiga "tahrirlash" funksiyasini qo‘shing.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ List yaratish va elementga murojaat qilish
✔️ append(), insert(), extend()
✔️ remove(), pop(), del, clear()
✔️ sort(), sorted(), reverse()
✔️ count(), index(), enumerate()
✔️ List comprehension
✔️ Xarajatlar va To-do list dasturlarini
"""
