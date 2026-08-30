# ============================================================
#   DARS 13: JSON, Date, Random va Modullar
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

import json
import random
from datetime import date, datetime, timedelta
from pathlib import Path

"""
BUGUNGI DARSDA:
  ✔️ JSON bilan ishlash
  ✔️ datetime va date
  ✔️ random moduli
  ✔️ import va o‘z modulini yaratish
"""


# ------------------------------------------------------------
# JSON
# ------------------------------------------------------------

"""
JSON — dasturlar orasida ma’lumot almashish uchun keng ishlatiladigan
format. Python dictionary’ga juda o‘xshaydi.

dumps / loads  → string bilan ishlaydi
dump / load    → fayl bilan ishlaydi
"""

talaba = {"ism": "Ali", "yosh": 18, "kurs": "Python"}

json_matn = json.dumps(talaba, ensure_ascii=False, indent=4)
print(json_matn)

qayta_dict = json.loads(json_matn)
print(qayta_dict["ism"])

JSON_FAYL = Path("talaba.json")

with open(JSON_FAYL, "w", encoding="utf-8") as fayl:
    json.dump(talaba, fayl, ensure_ascii=False, indent=4)

with open(JSON_FAYL, "r", encoding="utf-8") as fayl:
    malumot = json.load(fayl)
    print(malumot)


# ------------------------------------------------------------
# datetime VA date
# ------------------------------------------------------------

hozir = datetime.now()
bugun = date.today()

print(hozir)
print(bugun)
print(hozir.strftime("%d.%m.%Y %H:%M"))

sana_matni = "31.08.2026"
sana = datetime.strptime(sana_matni, "%d.%m.%Y")
print(sana)

ertaga = bugun + timedelta(days=1)
bir_hafta_keyin = bugun + timedelta(days=7)
print(ertaga)
print(bir_hafta_keyin)


# ------------------------------------------------------------
# random MODULI
# ------------------------------------------------------------

print(random.randint(1, 10))
print(random.random())

ismlar = ["Ali", "Vali", "Madina", "Aziza"]
print(random.choice(ismlar))
print(random.sample(ismlar, k=2))

random.shuffle(ismlar)
print(ismlar)


# ------------------------------------------------------------
# AMALIY MISOL — SON TOPISH O‘YINI
# ------------------------------------------------------------

sirli_son = random.randint(1, 10)

while True:
    taxmin = int(input("1 dan 10 gacha son kiriting: "))

    if taxmin == sirli_son:
        print("Tabriklaymiz! Siz topdingiz!")
        break
    elif taxmin < sirli_son:
        print("Kattaroq son kiriting")
    else:
        print("Kichikroq son kiriting")


# ------------------------------------------------------------
# MODULLAR
# ------------------------------------------------------------

"""
Modul — ichida Python kodi bo‘lgan .py fayl.

Import usullari:
  import math
  from math import sqrt
  import math as m

O‘z modulini yaratish:
  1. yordamchi.py fayl yarating.
  2. Ichiga funksiya yozing.
  3. Boshqa faylda import yordamchi deb yozing.
"""

# yordamchi.py fayli:
# def salom_ber(ism):
#     return f"Salom, {ism}!"

# asosiy.py fayli:
# import yordamchi
# print(yordamchi.salom_ber("Ali"))


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. 5 ta o‘quvchini JSON faylga saqlang.
2. JSON fayldan o‘quvchilarni o‘qib ekranga chiqaring.
3. Tug‘ilgan sanadan foydalanuvchi yoshini taxminan aniqlang.
4. random.choice() bilan tasodifiy savol tanlaydigan quiz tuzing.
5. matematik_amallar.py modulini yarating va unda qoshish() yozing.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ JSON string va fayl bilan ishlashni
✔️ datetime, date va timedelta’ni
✔️ random funksiyalarini
✔️ Modul yaratish va import qilishni
"""
