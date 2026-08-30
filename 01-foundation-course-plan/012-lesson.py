# ============================================================
#   DARS 12: Pythonda Fayllar bilan Ishlash
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

from pathlib import Path

"""
BUGUNGI DARSDA:
  ✔️ open() va r, w, a rejimlari
  ✔️ with open(...) as f
  ✔️ read(), readline(), readlines()
  ✔️ write(), writelines()
  ✔️ encoding="utf-8"
  ✔️ pathlib bilan fayl va papkalar
"""


# ------------------------------------------------------------
# FAYL OCHISH REJIMLARI
# ------------------------------------------------------------

"""
  r   — o‘qish. Fayl bo‘lmasa xato beradi.
  w   — yozish. Fayl bo‘lmasa yaratadi, bo‘lsa eski ichini o‘chiradi.
  a   — oxiriga qo‘shib yozish. Fayl bo‘lmasa yaratadi.

with open(...) ishlatish tavsiya qilinadi.
U ish tugagach faylni avtomatik yopadi.
"""


# ------------------------------------------------------------
# write() — FAYLGA YOZISH
# ------------------------------------------------------------

with open("salom.txt", "w", encoding="utf-8") as fayl:
    fayl.write("Assalomu alaykum!\n")
    fayl.write("Bu Python fayllar darsi.\n")


# ------------------------------------------------------------
# read(), readline(), readlines()
# ------------------------------------------------------------

with open("salom.txt", "r", encoding="utf-8") as fayl:
    matn = fayl.read()
    print(matn)

with open("salom.txt", "r", encoding="utf-8") as fayl:
    birinchi_qator = fayl.readline()
    print(birinchi_qator)

with open("salom.txt", "r", encoding="utf-8") as fayl:
    qatorlar = fayl.readlines()
    print(qatorlar)


# ------------------------------------------------------------
# a REJIMI — OXIRIGA QO‘SHIB YOZISH
# ------------------------------------------------------------

with open("salom.txt", "a", encoding="utf-8") as fayl:
    fayl.write("Bu qator fayl oxiriga qo‘shildi.\n")


# ------------------------------------------------------------
# writelines()
# ------------------------------------------------------------

fanlar = ["Python\n", "Git\n", "SQL\n"]

with open("fanlar.txt", "w", encoding="utf-8") as fayl:
    fayl.writelines(fanlar)


# ------------------------------------------------------------
# pathlib MODULI
# ------------------------------------------------------------

"""
pathlib fayl va papka yo‘llari bilan ishlashni qulaylashtiradi.
"""

fayl_yoli = Path("salom.txt")
print(fayl_yoli.exists())
print(fayl_yoli.name)
print(fayl_yoli.suffix)

papka = Path("loyiham")
papka.mkdir(exist_ok=True)

ichki_fayl = papka / "malumot.txt"
ichki_fayl.write_text("Salom, Python!", encoding="utf-8")
print(ichki_fayl.read_text(encoding="utf-8"))


# ------------------------------------------------------------
# AMALIY LOYIHA — TO-DO LISTNI FAYLGA SAQLASH
# ------------------------------------------------------------

TODO_FAYL = Path("vazifalar.txt")


def vazifalarni_korish():
    if not TODO_FAYL.exists():
        print("Hozircha vazifalar yo‘q")
        return

    qatorlar = TODO_FAYL.read_text(encoding="utf-8").splitlines()

    for indeks, vazifa in enumerate(qatorlar, start=1):
        print(f"{indeks}. {vazifa}")


def vazifa_qoshish(vazifa):
    with open(TODO_FAYL, "a", encoding="utf-8") as fayl:
        fayl.write(vazifa + "\n")


# vazifa_qoshish("Python mashq qilish")
# vazifalarni_korish()


# ------------------------------------------------------------
# AMALIY LOYIHA — O‘QUVCHI MA’LUMOTLARI
# ------------------------------------------------------------

OQUVCHI_FAYL = Path("oquvchilar.txt")


def oquvchi_qoshish(ism, yosh, kurs):
    qator = f"{ism};{yosh};{kurs}\n"

    with open(OQUVCHI_FAYL, "a", encoding="utf-8") as fayl:
        fayl.write(qator)


def oquvchilarni_korish():
    if not OQUVCHI_FAYL.exists():
        print("O‘quvchilar fayli mavjud emas")
        return

    with open(OQUVCHI_FAYL, "r", encoding="utf-8") as fayl:
        for qator in fayl:
            ism, yosh, kurs = qator.strip().split(";")
            print(f"Ism: {ism}, Yosh: {yosh}, Kurs: {kurs}")


# oquvchi_qoshish("Ali", 18, "Python Foundation")
# oquvchilarni_korish()


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. O‘zingiz haqingizda 3 qatorli fayl yarating.
2. Foydalanuvchi kiritgan matnni kundalik.txt fayliga saqlang.
3. Kundalik.txt ichidagi qatorlar sonini aniqlang.
4. To-do list dasturiga barcha vazifalarni o‘chirish funksiyasini qo‘shing.
5. pathlib yordamida "rasmlar" papkasini yarating.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ Fayl rejimlarini
✔️ read(), readline(), readlines()
✔️ write(), writelines()
✔️ with open va encoding="utf-8"
✔️ pathlib bilan ishlashni
✔️ Faylga saqlanadigan To-do listni
"""
