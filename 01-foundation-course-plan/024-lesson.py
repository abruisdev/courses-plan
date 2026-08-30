# ============================================================
#   DARS 24: Python Bo‘yicha Umumlashtirish
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ Asosiy mavzularni takrorlash
  ✔️ Nazariy savol-javoblar
  ✔️ Murakkab masalalar ishlash
  ✔️ GitHub portfolio tekshirish
  ✔️ Backend va Telegram Bot kursiga tayyorgarlik
"""


# ------------------------------------------------------------
# NAZARIY SAVOLLAR
# ------------------------------------------------------------

"""
1. Python nima va qayerlarda ishlatiladi?
2. str, int, float, bool farqi nima?
3. input() nima uchun casting bilan ishlatiladi?
4. if, elif, else qachon ishlatiladi?
5. for va while farqi nima?
6. List, Set, Tuple va Dictionary farqi nima?
7. Funksiyada return nima qiladi?
8. try / except nima uchun kerak?
9. JSON va SQLite farqi nima?
10. OOPning 4 ta tamoyili qaysilar?
11. Git va GitHub farqi nima?
12. API nima?
13. .env nima uchun kerak?
14. AI yozgan kodni nega tekshirish kerak?
"""


# ------------------------------------------------------------
# MURAKKAB MASALA 1 — PALINDROM
# ------------------------------------------------------------


def palindrommi(matn):
    """Matn teskari o‘qilganda ham bir xil bo‘lsa True qaytaradi."""
    tozalangan = matn.lower().replace(" ", "")
    return tozalangan == tozalangan[::-1]


print(palindrommi("alla"))
print(palindrommi("python"))


# ------------------------------------------------------------
# MURAKKAB MASALA 2 — ENG KO‘P UCHRAGAN HARF
# ------------------------------------------------------------


def eng_kop_harf(matn):
    hisob = {}

    for harf in matn.lower().replace(" ", ""):
        hisob[harf] = hisob.get(harf, 0) + 1

    return max(hisob, key=hisob.get)


print(eng_kop_harf("python foundation"))


# ------------------------------------------------------------
# MURAKKAB MASALA 3 — XARAJATLAR TAHLILI
# ------------------------------------------------------------


def xarajatlar_tahlili(xarajatlar):
    if not xarajatlar:
        return "Xarajatlar mavjud emas"

    return {
        "jami": sum(xarajatlar),
        "eng_katta": max(xarajatlar),
        "eng_kichik": min(xarajatlar),
        "orta": sum(xarajatlar) / len(xarajatlar),
    }


print(xarajatlar_tahlili([15_000, 20_000, 50_000, 10_000]))


# ------------------------------------------------------------
# GITHUB PORTFOLIO CHECKLIST
# ------------------------------------------------------------

"""
Har bir o‘quvchida quyidagilar bo‘lishi kerak:

  ✔️ GitHub profili va to‘g‘ri username.
  ✔️ Kamida 3 ta kichik loyiha repositorysi.
  ✔️ 1 ta yakuniy loyiha repositorysi.
  ✔️ Har repositoryda README.md.
  ✔️ .env va .venv GitHub’ga yuklanmagan.
  ✔️ Kodda tushunarli nomlar va izohlar.
"""


# ------------------------------------------------------------
# KEYINGI BOSQICH — BACKEND VA TELEGRAM BOT
# ------------------------------------------------------------

"""
Python Foundation’dan keyin o‘quvchi quyidagilarga tayyor bo‘ladi:

  Telegram Bot:
    - aiogram yoki python-telegram-bot
    - Bot token va .env
    - Handlerlar va tugmalar
    - SQLite bilan bot

  Backend:
    - HTTP va REST API
    - FastAPI yoki Django
    - PostgreSQL
    - Authentication
    - Deployment
"""


"""
UYGA VAZIFA:

1. Yakuniy loyihangizni GitHub’ga yuklang.
2. README.md yozing.
3. 10 ta nazariy savolga og‘zaki javob bering.
4. Portfolio havolangizni tayyorlab qo‘ying.
"""
