# ============================================================
#   DARS 20: Kod Sifati va AI bilan Dasturlash
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ PEP 8 va kod o‘qilishi
  ✔️ To‘g‘ri nomlash
  ✔️ Kichik funksiyalar
  ✔️ Type hint va docstring
  ✔️ assert bilan sodda test
  ✔️ AI’dan mas’uliyatli foydalanish
  ✔️ GitHub repositoryni tartibga keltirish
"""


# ------------------------------------------------------------
# KOD SIFATI
# ------------------------------------------------------------

"""
Yaxshi kod faqat ishlaydigan kod emas. Uni boshqa odam ham, siz ham bir necha oy o‘tgach o‘qib tushuna olishi kerak.

Asosiy qoidalar:
  ✔️ Tushunarli nom bering: yosh, jami_narx, oquvchi_soni
  ✔️ snake_case ishlating
  ✔️ Bitta funksiya bitta vazifani bajarsin
  ✔️ Keraksiz takrorni kamaytiring
  ✔️ Maxfiy token va parolni kodga yozmang
"""


# YOMON: nom tushunarsiz
def h(a, b):
    return a * b * 0.12


# YAXSHI: nom va maqsad tushunarli
def soliq_hisobla(summa: float, stavka: float = 0.12) -> float:
    """Berilgan summa uchun soliq miqdorini qaytaradi."""
    return summa * stavka


print(soliq_hisobla(1_000_000))


# ------------------------------------------------------------
# TYPE HINT VA DOCSTRING
# ------------------------------------------------------------

"""
Type hint Pythonni majburlamaydi, lekin kodni tushunish va IDE yordamida xatoni erta topishga yordam beradi.
Docstring funksiya nima qilishini tushuntiradi.
"""


def qoshish(a: int, b: int) -> int:
    """Ikki butun sonning yig‘indisini qaytaradi."""
    return a + b


def foydalanuvchi_haqida(ism: str, yosh: int) -> str:
    """Foydalanuvchi haqida bitta jumla qaytaradi."""
    return f"{ism}, {yosh} yoshda"


print(qoshish(5, 3))
print(foydalanuvchi_haqida("Ali", 18))


# ------------------------------------------------------------
# SODDA TEST — assert
# ------------------------------------------------------------

"""
assert — kutilgan natija to‘g‘riligini tekshiradi.
Shart False bo‘lsa AssertionError chiqadi.
"""


def juftmi(son: int) -> bool:
    return son % 2 == 0


assert juftmi(4) is True
assert juftmi(5) is False
assert qoshish(10, 20) == 30
print("Testlar muvaffaqiyatli o‘tdi")


# ------------------------------------------------------------
# AI BILAN DASTURLASH
# ------------------------------------------------------------

"""
AI yordamchi, lekin javobgarlik dasturchida qoladi.

AI’dan kod so‘raganda:
  1. Vazifani aniq yozing.
  2. Qaysi til va versiya kerakligini ayting.
  3. Kodni qatorma-qator tushunishga harakat qiling.
  4. Chegara holatlarini sinang: bo‘sh qiymat, 0, xato input.
  5. Test yozing.

AI’ga hech qachon haqiqiy bot token, parol, API key yoki o‘quvchilar shaxsiy ma’lumotlarini yubormang.
"""

AI_SOROV = """
Python 3 da xarajatlar ro‘yxati uchun funksiya yoz.
Funksiya manfiy summani qabul qilmasin, ValueError chiqarsin.
Type hint va 3 ta assert testi bo‘lsin. Kodni o‘zbekcha tushuntir.
"""

print(AI_SOROV)


# ------------------------------------------------------------
# GITHUB REPOSITORY TARTIBI
# ------------------------------------------------------------

"""
Tavsiya qilinadigan loyiha tuzilishi:

loyiham/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env                 # GitHub’ga yuklanmaydi
└── tests/

README.md ichida loyiha nima qilishi, o‘rnatish va ishga tushirish bosqichlari yoziladi.
"""


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. Oldingi darsdagi 3 ta funksiyaga type hint va docstring yozing.
2. Bir funksiya uchun kamida 3 ta assert testi yozing.
3. AI’dan funksiyangizni review qilishni so‘rang; tavsiyasini o‘zingiz tekshirib, faqat foydalisini qo‘llang.
4. Yakuniy loyihangiz uchun README.md rejasini yozing.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ O‘qilishi oson kod yozishni
✔️ Type hint va docstringni
✔️ assert bilan sodda test yozishni
✔️ AI javobini tekshirish kerakligini
✔️ Token va maxfiy ma’lumotni himoya qilishni
✔️ GitHub loyihasini tartibli qilishni
"""
