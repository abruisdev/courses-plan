# ============================================================
#   DARS 19: SQLite Ma’lumotlar Bazasi
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

import sqlite3

"""
BUGUNGI DARSDA:
  ✔️ Database nima
  ✔️ sqlite3 bilan ulanish
  ✔️ CREATE, INSERT, SELECT, UPDATE, DELETE
  ✔️ Parametrli SQL so‘rovlar
"""


# ------------------------------------------------------------
# DATABASE NIMA?
# ------------------------------------------------------------

"""
Database — ma’lumotlarni tartibli saqlash tizimi.
SQLite — alohida server talab qilmaydigan, .db fayl ichida ishlaydigan ma’lumotlar bazasi.

CRUD:
  Create — qo‘shish
  Read   — o‘qish
  Update — yangilash
  Delete — o‘chirish
"""


# ------------------------------------------------------------
# ULANISH VA JADVAL YARATISH
# ------------------------------------------------------------

db = sqlite3.connect("oquv_markaz.db")
kursor = db.cursor()

kursor.execute("""
CREATE TABLE IF NOT EXISTS oquvchilar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ism TEXT NOT NULL,
    yosh INTEGER NOT NULL,
    kurs TEXT NOT NULL
)
""")

db.commit()


# ------------------------------------------------------------
# INSERT — MA’LUMOT QO‘SHISH
# ------------------------------------------------------------

"""
SQL so‘roviga qiymat qo‘shishda ? placeholder ishlating.
Bu usul xavfsizroq: SQL injection xavfini kamaytiradi.
"""

kursor.execute(
    "INSERT INTO oquvchilar (ism, yosh, kurs) VALUES (?, ?, ?)",
    ("Ali", 18, "Python Foundation"),
)
db.commit()


# ------------------------------------------------------------
# SELECT — MA’LUMOT O‘QISH
# ------------------------------------------------------------

kursor.execute("SELECT id, ism, yosh, kurs FROM oquvchilar")
oquvchilar = kursor.fetchall()

for oquvchi in oquvchilar:
    print(oquvchi)

kursor.execute("SELECT * FROM oquvchilar WHERE ism = ?", ("Ali",))
oquvchi = kursor.fetchone()
print(oquvchi)


# ------------------------------------------------------------
# UPDATE VA DELETE
# ------------------------------------------------------------

kursor.execute(
    "UPDATE oquvchilar SET yosh = ? WHERE ism = ?",
    (19, "Ali"),
)
db.commit()

# Quyidagi qatorni kerak bo‘lgandagina ishga tushiring:
# kursor.execute("DELETE FROM oquvchilar WHERE ism = ?", ("Ali",))
# db.commit()


# ------------------------------------------------------------
# FUNKSIYALAR BILAN O‘QUVCHILAR TIZIMI
# ------------------------------------------------------------


def oquvchi_qoshish(ism, yosh, kurs):
    with sqlite3.connect("oquv_markaz.db") as ulanish:
        ulanish.execute(
            "INSERT INTO oquvchilar (ism, yosh, kurs) VALUES (?, ?, ?)",
            (ism, yosh, kurs),
        )


def oquvchilarni_korish():
    with sqlite3.connect("oquv_markaz.db") as ulanish:
        kursor = ulanish.execute("SELECT id, ism, yosh, kurs FROM oquvchilar")

        for identifikator, ism, yosh, kurs in kursor.fetchall():
            print(f"{identifikator}. {ism}, {yosh} yosh, {kurs}")


def oquvchi_yangilash(identifikator, yangi_kurs):
    with sqlite3.connect("oquv_markaz.db") as ulanish:
        ulanish.execute(
            "UPDATE oquvchilar SET kurs = ? WHERE id = ?",
            (yangi_kurs, identifikator),
        )


def oquvchi_ochirish(identifikator):
    with sqlite3.connect("oquv_markaz.db") as ulanish:
        ulanish.execute("DELETE FROM oquvchilar WHERE id = ?", (identifikator,))


# oquvchi_qoshish("Madina", 20, "Backend")
# oquvchilarni_korish()

db.close()


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. Kontaktlar jadvalini yarating: id, ism, telefon.
2. Kontakt qo‘shish, ko‘rish, yangilash, o‘chirish funksiyalarini yozing.
3. Xarajatlar jadvalini yarating: id, nomi, summa, sana.
4. Jami xarajatni SQL SUM() orqali aniqlang.
5. Hech qachon SQL so‘rovda f-string bilan foydalanuvchi qiymatini qo‘shmang; ? placeholder ishlating.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ SQLite database bilan ulanishni
✔️ CREATE TABLE ni
✔️ INSERT, SELECT, UPDATE, DELETE ni
✔️ commit() va close()ni
✔️ Parametrli SQL so‘rovlarni
✔️ O‘quvchilar bazasini
"""
