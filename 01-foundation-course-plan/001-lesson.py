# ============================================================
#   DARS 1: Kirish, Python O‘rnatish, Terminal, GitHub
#           va Birinchi Dastur
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================


# ------------------------------------------------------------
# DARSNING MAQSADI
# ------------------------------------------------------------

"""
Bugungi darsda:

  ✔️ Python nima ekanini bilib olamiz
  ✔️ Python dasturlash tilini o‘rnatamiz
  ✔️ PyCharm dasturini o‘rnatamiz
  ✔️ Terminal bilan tanishamiz
  ✔️ Birinchi Python dasturimizni yozamiz
  ✔️ print() funksiyasi bilan ishlaymiz
  ✔️ Izoh (comment) yozishni o‘rganamiz
  ✔️ Git va GitHub nima ekanini bilib olamiz
  ✔️ Birinchi loyihamizni GitHub’ga yuklaymiz
"""


# ------------------------------------------------------------
# PYTHON NIMA?
# ------------------------------------------------------------

"""
Python — bu dasturlash tili.

U 1991-yilda yaratilgan va hozirda dunyodagi eng mashhur
dasturlash tillaridan biri hisoblanadi.

Python qayerlarda ishlatiladi?

  - Web saytlar va Backend yaratishda
  - Telegram botlar yaratishda
  - Sun’iy intellekt (AI) va Machine Learning’da
  - Ma’lumotlar tahlilida
  - Avtomatlashtirishda
  - O‘yinlar va desktop dasturlarda
  - API va serverlar yaratishda

Nega aynan Python?

  ✔️ O‘qish va yozish oson
  ✔️ Ingliz tiliga yaqin
  ✔️ Juda ko‘p kutubxonalari bor
  ✔️ Bepul va open-source
  ✔️ Telegram Bot va Backend uchun juda qulay
  ✔️ Katta jamoa va ko‘p resurslar mavjud
"""


# ------------------------------------------------------------
# PYTHON O‘RNATISH
# ------------------------------------------------------------

"""
QADAM 1 — Python yuklab olish:

  1. https://www.python.org/downloads/ saytiga kiring
  2. "Download Python" tugmasini bosing
  3. Python 3 ning eng yangi barqaror versiyasini yuklab oling

QADAM 2 — O‘rnatish:

  ✔️ "Add Python to PATH" katagini ALBATTA belgilang!
  ✔️ "Install Now" tugmasini bosing
  ✔️ O‘rnatish tugashini kuting

"Add Python to PATH" nima uchun kerak?

  Bu belgi Python’ni terminal orqali istalgan joydan
  ishga tushirish imkonini beradi.

Agar bu belgi belgilanmasa, terminalda python buyrug‘i
ishlamasligi mumkin.
"""


# ------------------------------------------------------------
# PYTHON O‘RNATILGANINI TEKSHIRISH
# ------------------------------------------------------------

"""
Terminalni oching.

Windows:
  Win + R → cmd → Enter

Mac:
  Command + Space → Terminal deb qidiring

Linux:
  Ctrl + Alt + T

Terminalga quyidagi buyruqlardan birini yozing:
"""

# Windows uchun:
# python --version

# Agar Windows’da ishlamasa:
# py --version

# Mac yoki Linux uchun:
# python3 --version

"""
Agar quyidagiga o‘xshash natija chiqsa:

  Python 3.x.x

demak Python muvaffaqiyatli o‘rnatilgan.
"""


# ------------------------------------------------------------
# PYCHARM O‘RNATISH
# ------------------------------------------------------------

"""
PyCharm — bu Python uchun kod yozish muhiti (IDE).

IDE yordamida:

  ✔️ Kod yozish osonlashadi
  ✔️ Xatolar tez topiladi
  ✔️ Kodni ishga tushirish mumkin
  ✔️ Terminal ishlatish mumkin
  ✔️ GitHub bilan ishlash mumkin
  ✔️ Debug qilish mumkin

O‘rnatish:

  1. https://www.jetbrains.com/pycharm/download/ saytiga kiring
  2. Operatsion tizimingizga mos versiyani yuklab oling
  3. Dasturni o‘rnating
  4. PyCharm’ni oching
"""


# ------------------------------------------------------------
# YANGI PROJECT YARATISH
# ------------------------------------------------------------

"""
PyCharm’da yangi loyiha yaratish:

  1. New Project tugmasini bosing
  2. Loyiha nomini yozing:

       python_foundation

  3. Loyiha joylashadigan papkani tanlang
  4. "Create" tugmasini bosing

PyCharm avtomatik ravishda virtual environment yaratishi mumkin.
Hozircha default holatda qoldiramiz.

Virtual environment va pip mavzularini keyingi darslarda
batafsil o‘rganamiz.
"""


# ------------------------------------------------------------
# BIRINCHI PYTHON FAYLINI YARATISH
# ------------------------------------------------------------

"""
Project ichida yangi Python fayl yaratamiz:

  1. Chap tarafdagi loyiha papkasini bosing
  2. Sichqonchaning o‘ng tugmasini bosing
  3. New → Python File ni tanlang
  4. Fayl nomini yozing:

       dars_01

Python fayllari .py kengaytmaga ega bo‘ladi:

       dars_01.py
"""


# ------------------------------------------------------------
# print() FUNKSIYASI — EKRANGA CHIQARISH
# ------------------------------------------------------------

"""
print() — Pythondagi eng asosiy funksiyalardan biri.

U qavs ichidagi ma’lumotni ekranga chiqaradi.

Matn har doim qo‘shtirnoq ichida yoziladi.
"""

# MISOL 1 — Oddiy matn chiqarish
print("Assalomu alaykum!")
print("Python Foundation kursiga xush kelibsiz!")
print("Men Python o‘rganishni boshladim.")

# MISOL 2 — Son chiqarish
# Sonlar qo‘shtirnoqsiz yoziladi
print(2026)
print(100)
print(3.14)

# MISOL 3 — Bir nechta qator chiqarish
print("Ism: Ali")
print("Yosh: 15")
print("Kasb: Dasturchi bo‘laman")

# MISOL 4 — Bo‘sh qator chiqarish
print("Birinchi qator")
print()
print("Uchinchi qator")

# MISOL 5 — Matn va belgilar chiqarish
print("---------------------------")
print("    PYTHON FOUNDATION")
print("---------------------------")


# ------------------------------------------------------------
# KODNI ISHGA TUSHIRISH
# ------------------------------------------------------------

"""
PyCharm’da kodni ishga tushirish uchun:

  1. Kod yozilgan fayl ustiga o‘ng tugmani bosing
  2. Run 'dars_01' tugmasini tanlang

Yoki klaviaturadan:

  Windows / Linux:
      Shift + F10

  Mac:
      Control + R

Natija pastdagi Run oynasida chiqadi.
"""


# ------------------------------------------------------------
# IZOHLAR (COMMENTS)
# ------------------------------------------------------------

"""
Izoh — bu kod ichidagi tushuntirish matni.

Python izohlarni bajarmaydi.
Izoh yozish uchun # belgisi ishlatiladi.

Izoh nima uchun kerak?

  ✔️ Kodni tushuntirish uchun
  ✔️ Keyinchalik o‘zingiz eslab olishingiz uchun
  ✔️ Boshqa dasturchilar kodingizni tushunishi uchun
  ✔️ Muammoli qatorni vaqtincha o‘chirish uchun
"""

# Bu izoh, Python uni bajarmaydi

print("Salom!")  # Bu qator ishlaydi, yonidagi qism izoh

# Quyidagi qator vaqtincha o‘chirilgan:
# print("Bu qator hozir ishlamaydi")

# Dasturchi haqida ma’lumot chiqarish
print("Ism: Rustam")
print("Yo‘nalish: Python Backend")


# ------------------------------------------------------------
# TERMINAL BILAN TANISHISH
# ------------------------------------------------------------

"""
Terminal — bu kompyuterga buyruq yozib boshqariladigan oyna.

PyCharm ichida terminalni ochish:

  View → Tool Windows → Terminal

yoki pastki qismdagi Terminal tugmasini bosing.

Asosiy buyruqlar:

  pwd
      Hozir qaysi papkada turganingizni ko‘rsatadi
      (Mac va Linux’da)

  dir
      Papka ichidagi fayllarni ko‘rsatadi
      (Windows’da)

  ls
      Papka ichidagi fayllarni ko‘rsatadi
      (Mac va Linux’da)

  cd papka_nomi
      Boshqa papkaga kirish

  cd ..
      Bir pog‘ona yuqoridagi papkaga chiqish

  python dars_01.py
      Python faylini ishga tushirish
      (Windows’da)

  python3 dars_01.py
      Python faylini ishga tushirish
      (Mac va Linux’da)
"""


# ------------------------------------------------------------
# GIT VA GITHUB NIMA?
# ------------------------------------------------------------

"""
Git — koddagi o‘zgarishlarni saqlab boruvchi dastur.

GitHub — loyihalarni internetda saqlash va boshqalar bilan
ulashish platformasi.

Oddiy misol:

  Git       → kompyuteringizdagi o‘zgarishlar tarixi
  GitHub    → loyihangizning internetdagi manzili

GitHub nima uchun kerak?

  ✔️ Loyihalarni xavfsiz saqlash uchun
  ✔️ Portfolio yaratish uchun
  ✔️ Ishga topshirishda kodni ko‘rsatish uchun
  ✔️ Boshqa dasturchilar bilan ishlash uchun
  ✔️ Eski kodlarga qaytish uchun

Repository (repo) — GitHub’dagi loyiha papkasi.
"""


# ------------------------------------------------------------
# GITHUB AKKAUNT VA REPOSITORY YARATISH
# ------------------------------------------------------------

"""
QADAM 1 — GitHub akkaunt ochish:

  1. https://github.com/signup saytiga kiring
  2. Email orqali akkaunt yarating
  3. Email manzilingizni tasdiqlang
  4. Username tanlang

Masalan:

  rustamdev
  ali_python
  kodchi_uz

QADAM 2 — Repository yaratish:

  1. GitHub’ga kiring
  2. Yuqori o‘ng tarafdagi + belgisini bosing
  3. New repository ni tanlang
  4. Repository nomini yozing:

       python-foundation

  5. Public tanlang
  6. "Add a README file" belgisini HOZIRCHA belgilang
  7. Create repository tugmasini bosing

README.md — loyiha haqida qisqacha ma’lumot yoziladigan fayl.
"""


# ------------------------------------------------------------
# GIT O‘RNATISH VA BIRINCHI COMMIT
# ------------------------------------------------------------

"""
Git o‘rnatilganini terminalda tekshiring:

    git --version

Agar versiya chiqmasa, Git’ni quyidagi saytdan o‘rnating:

    https://git-scm.com/downloads

PyCharm ichida loyihani Git bilan bog‘lash:

  1. Git → Create Git Repository ni tanlang
  2. Project papkasini belgilang
  3. GitHub’ga login qiling
  4. Commit oynasini oching
  5. Fayllarni belgilang
  6. Commit message yozing:

       Dars 1: birinchi Python dasturi

  7. Commit and Push tugmasini bosing

Commit — koddaki o‘zgarishlarni saqlash.
Push — saqlangan kodni GitHub’ga yuklash.
"""


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Oson:

  Quyidagi ma’lumotlarni print() orqali ekranga chiqaring:

    - Ismingiz
    - Yoshingiz
    - Yashaydigan shahringiz
    - Kelajakdagi kasbingiz


TOPSHIRIQ 2 — O‘rta:

  Quyidagiga o‘xshash “Dasturchi kartasi” chiqaring:

    ┌──────────────────────────────┐
    │      DASTURCHI KARTASI       │
    │                              │
    │  Ism     : Ali Karimov       │
    │  Yosh    : 15                │
    │  Yo‘nalish: Python Backend   │
    │  Maqsad  : Dasturchi bo‘lish │
    └──────────────────────────────┘


TOPSHIRIQ 3 — Izoh bilan:

  5 ta print() yozing.

  Har bir kod qatorining ustiga yoki yoniga izoh yozing.
  Izohda ushbu qator nima qilishini tushuntiring.


TOPSHIRIQ 4 — Terminal:

  Terminalni oching va quyidagilarni bajaring:

    - Python versiyasini tekshiring
    - Git versiyasini tekshiring
    - dars_01.py faylini terminal orqali ishga tushiring


TOPSHIRIQ 5 — GitHub:

  GitHub akkaunt oching.

  Quyidagi nom bilan repository yarating:

      python-foundation

  Birinchi darsdagi dars_01.py faylini repository’ga yuklang.
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O‘RGANDIK?
# ------------------------------------------------------------

"""
✔️ Python nima va qayerlarda ishlatilishi
✔️ Python dasturini o‘rnatish
✔️ Terminal orqali Python versiyasini tekshirish
✔️ PyCharm o‘rnatish
✔️ Yangi project va Python fayl yaratish
✔️ print() funksiyasi bilan ekranga chiqarish
✔️ Izoh yozish
✔️ Terminal nima ekanligi
✔️ Git va GitHub nima ekanligi
✔️ GitHub repository yaratish
✔️ Birinchi Python loyihasini GitHub’ga yuklash
"""
