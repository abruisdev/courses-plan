# ============================================================
#   DARS 21: Pythonda Fayllar bilan ishlash
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# FAYLLAR BILAN ISHLASH NIMA VA NIMA UCHUN KERAK?
# ------------------------------------------------------------

"""
Dastur ishlaganda ma'lumotlar xotirada (RAM) saqlanadi.
Dastur yopilganda — hammasi o'chadi.

Fayllar yordamida:
  ✔️ Ma'lumotlarni DOIMIY saqlash mumkin (disk)
  ✔️ Keyingi safar ochib ishlatish mumkin
  ✔️ Boshqa dasturlar bilan almashish mumkin

Kundalik hayotda:
  📝 Matn fayllari (.txt) — hisobotlar, loglar
  📊 CSV fayllar          — Excel ma'lumotlari
  🔐 Konfiguratsiya       — dastur sozlamalari
  📋 Lug'atlar, ro'yxatlar
"""


# ============================================================
# FAYL OCHISH — open()
# ============================================================

"""
Sintaksis:
  fayl = open("fayl_nomi.txt", rejim)

Rejimlar:
  "r"   — o'qish (read)   — fayl yo'q bo'lsa XATO
  "w"   — yozish (write)  — fayl yo'q bo'lsa YARATADI, bor bo'lsa O'CHIRADI!
  "a"   — qo'shish (append) — fayl oxiriga qo'shadi
  "x"   — yangi yaratish  — fayl bor bo'lsa XATO
  "r+"  — o'qish + yozish
  "rb"  — binary o'qish   — rasm, video, audio
  "wb"  — binary yozish

MUHIM: Faylni ochgandan so'ng ALBATTA yopish kerak!
  fayl.close()   — yoki   with open(...) as f: — avtomatik yopadi
"""


# ============================================================
# FAYL YOZISH — write() va "w" rejim
# ============================================================

print("=== FAYL YOZISH ===")

# ── 1-usul: open() va close() ────────────────────────────────
fayl = open("salom.txt", "w")
fayl.write("Salom, Dunyo!\n")
fayl.write("Python bilan fayllar o'rganamiz.\n")
fayl.write("Bu bizning birinchi faylimiz!")
fayl.close()
print("✓ salom.txt yozildi")

# ── 2-usul: with open() — TAVSIYA ETILADI ───────────────────
"""
with open(...) as f:
    ...kod...
# Blok tugagach fayl AVTOMATIK yopiladi
# Xato bo'lsa ham yopiladi — ishonchli usul!
"""

with open("ma_lumot.txt", "w") as f:
    f.write("Ism: Ali Karimov\n")
    f.write("Yosh: 20\n")
    f.write("Shahar: Toshkent\n")
print("✓ ma_lumot.txt yozildi")

# ── Bir nechta qator — writelines() ─────────────────────────
qatorlar = [
    "1-qator: Python\n",
    "2-qator: Java\n",
    "3-qator: JavaScript\n"
]
with open("tillar.txt", "w") as f:
    f.writelines(qatorlar)
print("✓ tillar.txt yozildi")


# ============================================================
# FAYL O'QISH — read(), readline(), readlines()
# ============================================================

print("\n=== FAYL O'QISH ===")

# ── read() — Hammasini bir matn sifatida o'qiydi ─────────────
with open("salom.txt", "r") as f:
    matn = f.read()
print("read():")
print(matn)

# ── readline() — Faqat BITTA qator o'qiydi ───────────────────
with open("ma_lumot.txt", "r") as f:
    birinchi = f.readline()
    ikkinchi = f.readline()
print("\nreadline():")
print(birinchi, end="")
print(ikkinchi, end="")

# ── readlines() — Barcha qatorlar → LIST ─────────────────────
with open("tillar.txt", "r") as f:
    qatorlar = f.readlines()
print("\nreadlines():")
print(qatorlar)
# ['1-qator: Python\n', '2-qator: Java\n', '3-qator: JavaScript\n']

# ── for sikli bilan o'qish — ENG SAMARALI ───────────────────
print("\nfor sikli bilan:")
with open("tillar.txt", "r") as f:
    for qator in f:
        print(qator.strip())    # strip() — \n ni olib tashlaydi


# ============================================================
# FAYL OXIRIGA QO'SHISH — "a" rejim (append)
# ============================================================

print("\n=== APPEND REJIM ===")

# "w" → faylni o'chirib qayta yozadi
# "a" → fayl oxiriga QO'SHADI (eski ma'lumotlar saqlanadi)

with open("tillar.txt", "a") as f:
    f.write("4-qator: Kotlin\n")
    f.write("5-qator: Swift\n")
print("✓ Fayl oxiriga qo'shildi")

with open("tillar.txt", "r") as f:
    print(f.read())


# ============================================================
# FAYL MAVJUDLIGINI TEKSHIRISH — os moduli
# ============================================================

print("=== FAYL TEKSHIRISH ===")

import os

# Mavjudligini tekshirish
print(os.path.exists("salom.txt"))     # True
print(os.path.exists("yoq.txt"))       # False

# Fayl yoki papka ekanligini tekshirish
print(os.path.isfile("salom.txt"))     # True
print(os.path.isdir("salom.txt"))      # False

# Fayl hajmi (baytda)
print(os.path.getsize("salom.txt"))    # son

# Xavfsiz o'qish (mavjud bo'lsa):
if os.path.exists("salom.txt"):
    with open("salom.txt", "r") as f:
        print(f.read())
else:
    print("Fayl topilmadi!")


# ============================================================
# XATOLIKLARNI USHLASH — try/except bilan
# ============================================================

print("\n=== TRY/EXCEPT ===")

# Mavjud bo'lmagan faylni ochishda — FileNotFoundError
try:
    with open("mavjud_emas.txt", "r") as f:
        matn = f.read()
except FileNotFoundError:
    print("Xato: Fayl topilmadi!")
except PermissionError:
    print("Xato: Ruxsat yo'q!")
except Exception as e:
    print(f"Kutilmagan xato: {e}")
else:
    print("Fayl muvaffaqiyatli o'qildi")
finally:
    print("Har doim bajariladi")


# ============================================================
# AMALIY DASTUR — Kundalik (Dnevnik)
# ============================================================

print("\n=== KUNDALIK DASTURI ===")

import datetime

FAYL = "kundalik.txt"

def yoz(matn):
    """Kundalikka yangi yozuv qo'shish"""
    vaqt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(FAYL, "a", encoding="utf-8") as f:
        f.write(f"\n[{vaqt}]\n{matn}\n{'─' * 30}\n")
    print("✓ Yozuv saqlandi!")

def o_qi():
    """Barcha yozuvlarni ko'rish"""
    if not os.path.exists(FAYL):
        print("Kundalik hali bo'sh.")
        return
    with open(FAYL, "r", encoding="utf-8") as f:
        matn = f.read()
    if matn.strip():
        print(matn)
    else:
        print("Kundalik bo'sh.")

def tozala():
    """Kundalikni tozalash"""
    with open(FAYL, "w") as f:
        f.write("")
    print("✓ Kundalik tozalandi.")


# Demo:
yoz("Bugun Python fayllar mavzusini o'rgandim. Juda qiziqarli!")
yoz("Ertaga OOP ni takrorlayman.")
o_qi()


# ============================================================
# AMALIY DASTUR 2 — Baholar jurnali (CSV usulda)
# ============================================================

print("\n=== BAHOLAR JURNALI ===")

JURNAL = "baholar.txt"

def baho_qo_sh(ism, fan, baho):
    with open(JURNAL, "a", encoding="utf-8") as f:
        f.write(f"{ism},{fan},{baho}\n")

def barcha_baholar():
    if not os.path.exists(JURNAL):
        print("Jurnal bo'sh.")
        return
    with open(JURNAL, "r", encoding="utf-8") as f:
        qatorlar = f.readlines()
    print(f"\n{'Ism':<15} {'Fan':<15} {'Baho'}")
    print("─" * 35)
    for q in qatorlar:
        q = q.strip()
        if q:
            qismlar = q.split(",")
            if len(qismlar) == 3:
                print(f"{qismlar[0]:<15} {qismlar[1]:<15} {qismlar[2]}")

# Demo:
baho_qo_sh("Ali", "Matematika", "90")
baho_qo_sh("Vali", "Fizika", "85")
baho_qo_sh("Jasur", "Matematika", "92")
barcha_baholar()


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Asosiy (Oson):
  a) "mening_faylim.txt" faylini yarating va ichiga ismingizni yozing
  b) Faylni o'qing va ekranga chiqaring
  c) Fayl oxiriga shahringizni qo'shing
  d) Faylni yana o'qing

TOPSHIRIQ 2 — O'rta:
  Hisoblagich dasturini yarating:
  - Faylda bir son saqlanadi (boshida 0)
  - Dastur ishlaganda sonni o'qiydi
  - 1 ga oshiradi
  - Faylga qayta yozadi
  - "Siz bu dasturni N-marta ishlatdingiz" deb chiqaradi

TOPSHIRIQ 3 — O'rta:
  So'z sanagich:
  - Foydalanuvchidan matn oling
  - Har bir so'z necha marta uchrashini hisoblang
  - Natijani "natija.txt" fayliga yozing
  - Faylni o'qib ekranga chiqaring

TOPSHIRIQ 4 — Qiyin:
  Kontaktlar kitobini fayl orqali saqlang:
  - Kontakt qo'shish (nom,telefon — faylga yozish)
  - Barcha kontaktlarni ko'rish (fayldan o'qish)
  - Kontakt qidirish (nom bo'yicha)
  - Kontakt o'chirish (faylni qayta yozish)
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ open() — fayl ochish va rejimlar: 'r', 'w', 'a', 'rb', 'wb'
✔️ with open(...) as f — tavsiya etiladigan usul (avtomatik yopadi)
✔️ read()      — barcha matnni o'qiydi
✔️ readline()  — bitta qator o'qiydi
✔️ readlines() — barcha qatorlar → list
✔️ write()     — yozish
✔️ writelines()— list dan yozish
✔️ os.path.exists() — fayl mavjudligini tekshirish
✔️ try/except bilan xatoliklarni ushlash
✔️ encoding="utf-8" — o'zbek/lotin harflari uchun
"""