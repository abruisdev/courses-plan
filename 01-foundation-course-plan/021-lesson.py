# ============================================================
#   DARS 21: Algoritmlashga Kirish
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

"""
BUGUNGI DARSDA:
  ✔️ Algoritm nima
  ✔️ O(1), O(n), O(log n)
  ✔️ List, Set va Dictionary farqi
  ✔️ Linear Search
  ✔️ Binary Search
  ✔️ sorted() va sort()
  ✔️ LeetCode bilan tanishish
"""


# ------------------------------------------------------------
# ALGORITM NIMA?
# ------------------------------------------------------------

"""
Algoritm — muammoni hal qilish uchun ketma-ket va aniq qadamlar.

Masalan, choy damlash algoritmi:
  1. Choynakka suv solish.
  2. Suvni qaynatish.
  3. Choy solish.
  4. Qaynoq suv quyish.
  5. Kutish.
"""


# ------------------------------------------------------------
# VAQT MURAKKABLIGI
# ------------------------------------------------------------

"""
O(...) algoritm ma’lumot ko‘payganda qanchalik tez yoki sekin
ishlashini taxminan bildiradi.

  O(1)      — deyarli o‘zgarmas vaqt. Dictionary va Setdan qidirish.
  O(n)      — elementlar soni bilan birga ortadi. Listda qidirish.
  O(log n)  — har qadamda yarmini qisqartiradi. Binary Search.
"""


# ------------------------------------------------------------
# LIST, SET VA DICTIONARY QACHON?
# ------------------------------------------------------------

"""
List:
  - Tartib muhim bo‘lsa.
  - Takroriy qiymatlar kerak bo‘lsa.
  - Indeks bilan ishlash kerak bo‘lsa.

Set:
  - Takrorlar kerak bo‘lmasa.
  - "mavjudmi?" tekshiruvi tez bo‘lishi kerak bo‘lsa.

Dictionary:
  - Kalit orqali qiymat olish kerak bo‘lsa.
  - Masalan: login → foydalanuvchi ma’lumoti.
"""

ismlar_listi = ["Ali", "Vali", "Madina"]
ismlar_seti = {"Ali", "Vali", "Madina"}
foydalanuvchilar = {"ali": {"yosh": 18}}

print("Ali" in ismlar_listi)
print("Ali" in ismlar_seti)
print(foydalanuvchilar["ali"])


# ------------------------------------------------------------
# LINEAR SEARCH
# ------------------------------------------------------------

"""
Linear Search — elementlarni boshidan oxirigacha bittalab qidirish.
List tartiblangan bo‘lishi shart emas.
Murakkabligi: O(n).
"""


def linear_search(sonlar, qidiriladigan_son):
    for indeks, son in enumerate(sonlar):
        if son == qidiriladigan_son:
            return indeks

    return -1


sonlar = [12, 5, 78, 32, 19]
natija = linear_search(sonlar, 32)
print("Indeks:", natija)


# ------------------------------------------------------------
# BINARY SEARCH
# ------------------------------------------------------------

"""
Binary Search — faqat TARTIBLANGAN listda ishlaydi.
Har qadamda qidiruv oralig‘ining yarmini tashlab yuboradi.
Murakkabligi: O(log n).
"""


def binary_search(sonlar, qidiriladigan_son):
    chap = 0
    ong = len(sonlar) - 1

    while chap <= ong:
        orta = (chap + ong) // 2

        if sonlar[orta] == qidiriladigan_son:
            return orta
        elif sonlar[orta] < qidiriladigan_son:
            chap = orta + 1
        else:
            ong = orta - 1

    return -1


saralangan_sonlar = [3, 7, 12, 19, 25, 32, 78, 100]
print(binary_search(saralangan_sonlar, 32))
print(binary_search(saralangan_sonlar, 50))


# ------------------------------------------------------------
# sorted() VA sort()
# ------------------------------------------------------------

sonlar = [40, 5, 25, 10]

yangi_saralangan_list = sorted(sonlar)
print(sonlar)
print(yangi_saralangan_list)

sonlar.sort(reverse=True)
print(sonlar)


"""
sort()   — mavjud listning o‘zini o‘zgartiradi.
sorted() — yangi saralangan list qaytaradi.
"""


# ------------------------------------------------------------
# LEETCODE BILAN TANISHISH
# ------------------------------------------------------------

"""
LeetCode — algoritmik masalalar ishlash platformasi.

Boshlash uchun tavsiya qilinadigan sodda masalalar:
  ✔️ Two Sum
  ✔️ Palindrome Number
  ✔️ Fizz Buzz
  ✔️ Valid Parentheses
  ✔️ Contains Duplicate

Muhim qoida: avval masalani o‘zingiz yechishga urinib ko‘ring,
keyin yechimlarni tahlil qiling.
"""


"""
MUSTAQIL MASHQ TOPSHIRIQLARI:

1. linear_search() yordamida ismlar listidan ism qidiring.
2. Binary Search yordamida 1 dan 100 gacha saralangan listdan son qidiring.
3. Listdagi takroriy elementlarni Set yordamida aniqlang.
4. Dictionary yordamida matndagi har bir harf necha marta qatnashganini hisoblang.
5. LeetCode’dan Fizz Buzz masalasini ishlang.
"""


"""
BUGUNGI DARSDA NIMALAR O‘RGANDIK?
✔️ Algoritm va vaqt murakkabligini
✔️ List, Set va Dictionary tanlashni
✔️ Linear Searchni
✔️ Binary Searchni
✔️ sorted() va sort() farqini
✔️ LeetCode bilan ishlashni
"""
