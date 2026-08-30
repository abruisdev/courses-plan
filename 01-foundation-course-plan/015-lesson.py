# ============================================================
#   DARS 15: API va requests Kutubxonasi
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ API va HTTP nima
  ✔️ GET so‘rov yuborish
  ✔️ status_code va json()
  ✔️ timeout va raise_for_status()
  ✔️ API xatolarini boshqarish
"""

import requests


# ------------------------------------------------------------
# API VA HTTP NIMA?
# ------------------------------------------------------------

"""
API — bir dastur boshqa dasturdan ma’lumot yoki xizmat olishi uchun
ishlatiladigan aloqa usuli.

HTTP metodlari:
  GET    — ma’lumot olish
  POST   — ma’lumot qo‘shish
  PUT    — ma’lumotni to‘liq yangilash
  PATCH  — ma’lumotning bir qismini yangilash
  DELETE — ma’lumotni o‘chirish

Bugun GET so‘rovi bilan ishlaymiz.
"""


# ------------------------------------------------------------
# requests.get()
# ------------------------------------------------------------

url = "https://api.github.com/users/octocat"

try:
    response = requests.get(url, timeout=10)
    print("Status code:", response.status_code)

    response.raise_for_status()
    malumot = response.json()

    print("Login:", malumot["login"])
    print("Profil:", malumot["html_url"])
except requests.RequestException as error:
    print("API bilan bog‘lanishda xato:", error)


# ------------------------------------------------------------
# GET PARAMETRLARI
# ------------------------------------------------------------

"""
params orqali URL’ga so‘rov parametrlari beriladi.
"""

url = "https://api.github.com/search/repositories"
params = {"q": "python", "per_page": 3}

try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    natija = response.json()

    for repository in natija["items"]:
        print(repository["full_name"])
except requests.RequestException as error:
    print("Xato:", error)


# ------------------------------------------------------------
# API DAN KELGAN JSON BILAN ISHLASH
# ------------------------------------------------------------

"""
response.json() JSON javobni Python dictionary yoki listga aylantiradi.
Ma’lumot tuzilishini print(malumot) qilib tekshirib oling.
Keyin kerakli kalitni oling.
"""


def github_foydalanuvchi(login):
    url = f"https://api.github.com/users/{login}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        malumot = response.json()

        print("Login:", malumot["login"])
        print("Ism:", malumot.get("name"))
        print("Public repositorylar:", malumot["public_repos"])
    except requests.HTTPError as error:
        print("Bunday foydalanuvchi topilmadi yoki ruxsat yo‘q:", error)
    except requests.RequestException as error:
        print("Tarmoq xatosi:", error)


# github_foydalanuvchi("octocat")


# ------------------------------------------------------------
# API KEY VA .env
# ------------------------------------------------------------

"""
Ba’zi API’lar API key talab qiladi.
Keyni hech qachon kodga yozmang va GitHub’ga yuklamang.

To‘g‘ri yo‘l:

  .env fayl:
      WEATHER_API_KEY=haqiqiy_key

  Python kodi:
      from dotenv import load_dotenv
      import os
      load_dotenv()
      api_key = os.getenv("WEATHER_API_KEY")
"""


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. GitHub foydalanuvchi loginini input orqali olib, profilini chiqaring.
2. GitHub search API orqali "telegram bot" qidirib, 5 ta repository nomini chiqaring.
3. API xatolarini try / except bilan boshqaring.
4. O‘zingiz tanlagan ob-havo yoki valyuta API’sining hujjatini o‘qing,
   keyini .env orqali saqlang va kerakli ma’lumotni chiqaring.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ API va HTTP metodlarini
✔️ requests.get() bilan GET so‘rov yuborishni
✔️ status_code, raise_for_status() va json()ni
✔️ params bilan so‘rov yuborishni
✔️ API xatolarini boshqarishni
✔️ API keyni .env’da xavfsiz saqlashni
"""
