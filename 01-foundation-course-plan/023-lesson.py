# ============================================================
#   DARS 23: Yakuniy Loyiha — O‘quv Markazi Tizimi
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BU LOYIHADA ISHLATILGAN MAVZULAR:
  ✔️ Funksiyalar
  ✔️ Class va Object
  ✔️ while True menyu
  ✔️ try / except
  ✔️ SQLite
  ✔️ CRUD: Create, Read, Update, Delete

Ishga tushirish:
  python 23_yakuniy_loyiha_oquv_markazi.py
"""

import sqlite3


DB_NOMI = "oquv_markazi_final.db"


# ------------------------------------------------------------
# OQUVCHI CLASSI
# ------------------------------------------------------------


class Oquvchi:
    def __init__(self, ism, yosh, kurs):
        self.ism = ism.strip().title()
        self.yosh = yosh
        self.kurs = kurs.strip().title()

    def tuple_korinishida(self):
        return self.ism, self.yosh, self.kurs


# ------------------------------------------------------------
# DATABASE FUNKSIYALARI
# ------------------------------------------------------------


def database_yaratish():
    with sqlite3.connect(DB_NOMI) as db:
        db.execute("""
        CREATE TABLE IF NOT EXISTS oquvchilar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ism TEXT NOT NULL,
            yosh INTEGER NOT NULL,
            kurs TEXT NOT NULL
        )
        """)


def oquvchi_qoshish(oquvchi):
    with sqlite3.connect(DB_NOMI) as db:
        db.execute(
            "INSERT INTO oquvchilar (ism, yosh, kurs) VALUES (?, ?, ?)",
            oquvchi.tuple_korinishida(),
        )


def oquvchilarni_korish():
    with sqlite3.connect(DB_NOMI) as db:
        natija = db.execute(
            "SELECT id, ism, yosh, kurs FROM oquvchilar ORDER BY id"
        ).fetchall()

    if not natija:
        print("Hozircha o‘quvchilar mavjud emas")
        return

    print("\n--- O‘QUVCHILAR RO‘YXATI ---")
    for identifikator, ism, yosh, kurs in natija:
        print(f"{identifikator}. {ism} | {yosh} yosh | {kurs}")


def oquvchini_qidirish(identifikator):
    with sqlite3.connect(DB_NOMI) as db:
        return db.execute(
            "SELECT id, ism, yosh, kurs FROM oquvchilar WHERE id = ?",
            (identifikator,),
        ).fetchone()


def kursni_yangilash(identifikator, yangi_kurs):
    with sqlite3.connect(DB_NOMI) as db:
        kursor = db.execute(
            "UPDATE oquvchilar SET kurs = ? WHERE id = ?",
            (yangi_kurs.strip().title(), identifikator),
        )
        return kursor.rowcount


def oquvchini_ochirish(identifikator):
    with sqlite3.connect(DB_NOMI) as db:
        kursor = db.execute(
            "DELETE FROM oquvchilar WHERE id = ?",
            (identifikator,),
        )
        return kursor.rowcount


# ------------------------------------------------------------
# INPUT YORDAMCHI FUNKSIYASI
# ------------------------------------------------------------


def butun_son_olish(xabar):
    while True:
        try:
            return int(input(xabar))
        except ValueError:
            print("Iltimos, butun son kiriting")


# ------------------------------------------------------------
# KONSOL MENYU
# ------------------------------------------------------------


def menu():
    database_yaratish()

    while True:
        print("\n========== O‘QUV MARKAZI ==========")
        print("1. O‘quvchi qo‘shish")
        print("2. Barcha o‘quvchilarni ko‘rish")
        print("3. ID bo‘yicha qidirish")
        print("4. Kursni yangilash")
        print("5. O‘quvchini o‘chirish")
        print("0. Chiqish")

        tanlov = input("Tanlovingiz: ")

        if tanlov == "1":
            ism = input("Ism: ")
            yosh = butun_son_olish("Yosh: ")
            kurs = input("Kurs: ")

            if not ism or not kurs or yosh <= 0:
                print("Ma’lumotlar noto‘g‘ri kiritildi")
                continue

            oquvchi = Oquvchi(ism, yosh, kurs)
            oquvchi_qoshish(oquvchi)
            print("O‘quvchi muvaffaqiyatli qo‘shildi")

        elif tanlov == "2":
            oquvchilarni_korish()

        elif tanlov == "3":
            identifikator = butun_son_olish("O‘quvchi IDsi: ")
            oquvchi = oquvchini_qidirish(identifikator)

            if oquvchi:
                print(f"ID: {oquvchi[0]}, Ism: {oquvchi[1]}, Yosh: {oquvchi[2]}, Kurs: {oquvchi[3]}")
            else:
                print("Bunday IDli o‘quvchi topilmadi")

        elif tanlov == "4":
            identifikator = butun_son_olish("O‘quvchi IDsi: ")
            yangi_kurs = input("Yangi kurs nomi: ")

            if kursni_yangilash(identifikator, yangi_kurs):
                print("Kurs yangilandi")
            else:
                print("Bunday IDli o‘quvchi topilmadi")

        elif tanlov == "5":
            identifikator = butun_son_olish("O‘quvchi IDsi: ")
            tasdiq = input("Rostdan o‘chirasizmi? (ha/yo‘q): ").lower()

            if tasdiq == "ha":
                if oquvchini_ochirish(identifikator):
                    print("O‘quvchi o‘chirildi")
                else:
                    print("Bunday IDli o‘quvchi topilmadi")
            else:
                print("O‘chirish bekor qilindi")

        elif tanlov == "0":
            print("Dastur tugadi. Xayr!")
            break

        else:
            print("Noto‘g‘ri tanlov")


if __name__ == "__main__":
    menu()


"""
LOYIHANI YAXSHILASH UCHUN G‘OYALAR:

  ✔️ O‘quvchini ism bo‘yicha qidirish.
  ✔️ O‘quvchilar sonini ko‘rsatish.
  ✔️ Kurslar bo‘yicha filter qilish.
  ✔️ O‘quvchini to‘liq tahrirlash.
  ✔️ Har bir o‘quvchiga telefon raqam qo‘shish.
  ✔️ Loyiha uchun README.md yozish.
  ✔️ Kodni GitHub’ga yuklash.
"""
