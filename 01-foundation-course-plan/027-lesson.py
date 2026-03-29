# ============================================================
#   DARS 27: Queue (Navbat)
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# DARS HAQIDA
# ------------------------------------------------------------

"""
Queue — FIFO (First In, First Out) tamoyilida ishlaydigan
ma'lumotlar tuzilmasi.

FIFO = Birinchi kirgan, birinchi chiqadi.

Kundalik hayotda:
  🏦 Bank navbati    — birinchi kelgan, birinchi xizmat oladi
  🖨️ Printer navbati — birinchi yuborilgan hujjat birinchi chiqadi
  🚗 Avtomobil navbati — birinchi kelgan, birinchi o'tadi
  📨 Email/Xabar navbati — birinchi yuborilgan birinchi yetkaziladi

Stack vs Queue:
  Stack → LIFO → oxirgi kirgan, birinchi chiqadi (vertikal)
  Queue → FIFO → birinchi kirgan, birinchi chiqadi (gorizontal)

Operatsiyalar:
  enqueue() — navbatga qo'shish (orqadan)
  dequeue() — navbatdan olish  (oldidan)
  peek()    — oldingiga qarash (olib tashlashsiz)
  isEmpty() — bo'shligini tekshirish
"""

print("=" * 55)
print("    QUEUE — FIFO tuzilmasi")
print("=" * 55)

print("""
  ENQUEUE →  Orqa (Back)          Old (Front)  → DEQUEUE
              ┌────┬────┬────┬────┐
              │  D │  C │  B │  A │
              └────┴────┴────┴────┘
              ↑ Yangi kiradi       ↑ Eski chiqadi

  A birinchi kirgan → A birinchi chiqadi!
""")

from collections import deque


# ============================================================
# 1-USUL: PYTHON LIST BILAN QUEUE
# ============================================================

print("=" * 55)
print("    1-USUL: List bilan Queue (Sekin!)")
print("=" * 55)

"""
List bilan Queue MUMKIN, lekin SAMARASIZ.
  append()  → enqueue (O(1)) — tezkor
  pop(0)    → dequeue (O(n)) — SEKIN! (barcha suriladi)
"""

navbat = []

# enqueue:
navbat.append("Ali")
navbat.append("Vali")
navbat.append("Jasur")
navbat.append("Bobur")
print("Navbat:", navbat)

# dequeue:
chiqdi = navbat.pop(0)   # O(n) — sekin!
print(f"Xizmat: {chiqdi}")
print("Navbat:", navbat)


# ============================================================
# 2-USUL: collections.deque — TAVSIYA ETILADI
# ============================================================

print("\n" + "=" * 55)
print("    2-USUL: collections.deque (Tezkor!)")
print("=" * 55)

"""
deque (double-ended queue) — ikkala tomondan O(1) da qo'shish/olish.
Queue uchun eng samarali Python vositasi.

  appendleft() / popleft() — chapdan
  append()     / pop()     — o'ngdan
"""

navbat = deque()

# enqueue — o'ngdan qo'shish:
navbat.append("Ali")
navbat.append("Vali")
navbat.append("Jasur")
navbat.append("Bobur")
print("Navbat:", list(navbat))

# dequeue — chapdan olish:
chiqdi = navbat.popleft()   # O(1) — tezkor!
print(f"Xizmat: {chiqdi}")
print("Navbat:", list(navbat))

chiqdi = navbat.popleft()
print(f"Xizmat: {chiqdi}")
print("Navbat:", list(navbat))

print(f"\nNavbat uzunligi: {len(navbat)}")
print(f"Birinchi: {navbat[0]}")   # peek — oldingisi
print(f"Oxirgi:   {navbat[-1]}")  # oxirgisi


# ============================================================
# 3-USUL: QUEUE KLASSI
# ============================================================

print("\n" + "=" * 55)
print("    3-USUL: Queue klassi")
print("=" * 55)

class Queue:
    """
    FIFO tamoyilidagi Queue ma'lumotlar tuzilmasi.
    collections.deque asosida qurilgan.
    """

    def __init__(self):
        self._ma_lumot = deque()

    # ── enqueue() — Orqadan qo'shish — O(1) ──────────────────
    def enqueue(self, qiymat):
        """Elementni navbat oxiriga qo'shadi."""
        self._ma_lumot.append(qiymat)
        print(f"  enqueue({qiymat}) → Navbat: {list(self._ma_lumot)}")

    # ── dequeue() — Oldidan olish — O(1) ─────────────────────
    def dequeue(self):
        """Navbat boshidan elementni olib qaytaradi."""
        if self.isEmpty():
            print("  Xato: Navbat bo'sh!")
            return None
        element = self._ma_lumot.popleft()
        print(f"  dequeue() → {element} | Navbat: {list(self._ma_lumot)}")
        return element

    # ── peek() — Oldinga qarash — O(1) ───────────────────────
    def peek(self):
        """Navbat boshidagi elementni qaytaradi (o'chirmaydi)."""
        if self.isEmpty():
            return None
        return self._ma_lumot[0]

    # ── isEmpty() — Bo'shligini tekshirish — O(1) ─────────────
    def isEmpty(self):
        return len(self._ma_lumot) == 0

    # ── size() ────────────────────────────────────────────────
    def size(self):
        return len(self._ma_lumot)

    def __str__(self):
        if self.isEmpty():
            return "Queue: bo'sh"
        return f"Old→{list(self._ma_lumot)}←Orqa | Hajm: {self.size()}"


# Test:
print("\n--- Queue klassi sinovi ---")
q = Queue()
print(q)

q.enqueue("Ali")
q.enqueue("Vali")
q.enqueue("Jasur")
q.enqueue("Bobur")

print(f"\nBirinchi navbatda: {q.peek()}")
print(f"Hajm: {q.size()}")
print(q)

print()
q.dequeue()
q.dequeue()
print(q)
print(f"Bo'shmi? {q.isEmpty()}")


# ============================================================
# DEQUE — IKKI TOMONLAMA NAVBAT
# ============================================================

print("\n" + "=" * 55)
print("    DEQUE — Ikki tomonlama navbat")
print("=" * 55)

"""
Deque (Double-Ended Queue) — ikkala tomondan qo'shish va olish mumkin.
Stack + Queue kombinatsiyasi.

  appendleft(x) — chapga qo'shish  O(1)
  append(x)     — o'ngga qo'shish  O(1)
  popleft()     — chapdan olish     O(1)
  pop()         — o'ngdan olish     O(1)
"""

class Deque:
    """Ikki tomonlama navbat."""

    def __init__(self):
        self._ma_lumot = deque()

    def qo_sh_oldiga(self, qiymat):
        """Old (chap) tomonga qo'shish."""
        self._ma_lumot.appendleft(qiymat)

    def qo_sh_orqaga(self, qiymat):
        """Orqa (o'ng) tomonga qo'shish."""
        self._ma_lumot.append(qiymat)

    def ol_oldidan(self):
        """Old (chap) tomondan olish."""
        if self.isEmpty():
            return None
        return self._ma_lumot.popleft()

    def ol_orqadan(self):
        """Orqa (o'ng) tomondan olish."""
        if self.isEmpty():
            return None
        return self._ma_lumot.pop()

    def oldini_kor(self):
        return self._ma_lumot[0] if self._ma_lumot else None

    def orqasini_kor(self):
        return self._ma_lumot[-1] if self._ma_lumot else None

    def isEmpty(self):
        return len(self._ma_lumot) == 0

    def size(self):
        return len(self._ma_lumot)

    def __str__(self):
        return f"Deque: {list(self._ma_lumot)}"


dq = Deque()
dq.qo_sh_orqaga(10)
dq.qo_sh_orqaga(20)
dq.qo_sh_orqaga(30)
dq.qo_sh_oldiga(5)
dq.qo_sh_oldiga(1)
print(dq)

print(f"Old: {dq.ol_oldidan()}")
print(f"Orqa: {dq.ol_orqadan()}")
print(dq)


# ============================================================
# AMALIY MISOLLAR
# ============================================================

print("\n" + "=" * 55)
print("    AMALIY MISOLLAR")
print("=" * 55)


# ── MISOL 1: Bank navbat tizimi ───────────────────────────────
print("\n--- Bank navbat tizimi ---")

import time
import random

class BankNavbat:
    """
    Bank navbat simulyatsiyasi.
    Har xizmat 0.1 soniya davom etadi.
    """

    def __init__(self, bank_nomi):
        self.bank_nomi  = bank_nomi
        self.navbat     = Queue()
        self.ticket_no  = 0
        self.xizmat_soni = 0

    def keldi(self, ism):
        """Yangi mijoz keldi."""
        self.ticket_no += 1
        ticket = f"#{self.ticket_no:03d}"
        self.navbat.enqueue({"ism": ism, "ticket": ticket})
        print(f"  → {ism} keldi | Ticket: {ticket} | Navbat: {self.navbat.size()} kishi")

    def chaqirish(self):
        """Navbatdan birinchi mijozni chaqirish."""
        if self.navbat.isEmpty():
            print("  Navbat bo'sh!")
            return None
        mijoz = self.navbat.dequeue()
        self.xizmat_soni += 1
        print(f"  ✓ {mijoz['ticket']} — {mijoz['ism']} xizmatga chaqirildi")
        return mijoz

    def holat(self):
        print(f"\n  {self.bank_nomi} holati:")
        print(f"  Navbatdagilar: {self.navbat.size()} kishi")
        print(f"  Xizmat ko'rganlar: {self.xizmat_soni} kishi")


bank = BankNavbat("Agrobank Toshkent")

# Mijozlar keladi:
mijozlar = ["Ali", "Vali", "Jasur", "Bobur", "Nodir", "Sanjar"]
for ism in mijozlar:
    bank.keldi(ism)

bank.holat()

# Xizmat boshlanadi:
print("\n--- Xizmat boshlandi ---")
for _ in range(4):
    bank.chaqirish()

bank.holat()


# ── MISOL 2: Printer navbati ──────────────────────────────────
print("\n\n--- Printer navbati ---")

class PrinterNavbat:
    """Printer hujjatlar navbatini simulyatsiya qiladi."""

    def __init__(self):
        self.navbat      = Queue()
        self.chop_etildi = 0

    def yuborish(self, hujjat, sahifalar=1):
        """Hujjatni chop etish uchun yuborish."""
        self.navbat.enqueue({"nom": hujjat, "sahifalar": sahifalar})
        print(f"  📄 '{hujjat}' ({sahifalar} bet) navbatga qo'shildi")

    def chop_et(self):
        """Navbatdan birinchi hujjatni chop etish."""
        if self.navbat.isEmpty():
            print("  Printer navbati bo'sh!")
            return
        hujjat = self.navbat.dequeue()
        self.chop_etildi += hujjat["sahifalar"]
        print(f"  🖨️  Chop etildi: '{hujjat['nom']}' ({hujjat['sahifalar']} bet)")

    def holat(self):
        print(f"\n  Kutayotgan: {self.navbat.size()} hujjat")
        print(f"  Jami chop etildi: {self.chop_etildi} bet")


printer = PrinterNavbat()
printer.yuborish("Shartnoma.docx", 3)
printer.yuborish("Hisobot.pdf", 12)
printer.yuborish("Prezentatsiya.pptx", 7)
printer.yuborish("Ariza.docx", 1)

print("\n--- Chop etish ---")
printer.chop_et()
printer.chop_et()
printer.holat()


# ── MISOL 3: Palindrom tekshirish (Deque bilan) ───────────────
print("\n\n--- Palindrom tekshirish (Deque) ---")

"""
Palindrom — chapdan ham, o'ngdan ham o'qilganda bir xil:
  "radar", "level", "aba"

Deque yordamida:
  Har harfni deque ga qo'shib, ikkala tomondan birma-bir olamiz.
  Agar har safar ikkisi teng bo'lsa — palindrom!
"""

def palindrom_tekshir(so_z):
    so_z = so_z.lower().replace(" ", "")
    dq = deque(so_z)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

so_zlar = ["radar", "level", "Python", "aba", "kayak", "hello", "madam"]
for s in so_zlar:
    natija = palindrom_tekshir(s)
    print(f"  '{s}' → {'Palindrom ✓' if natija else 'Palindrom emas ✗'}")


# ============================================================
# STACK vs QUEUE TAQQOSLASH
# ============================================================

print("""
┌──────────────────────────────────────────────────────────┐
│              STACK vs QUEUE TAQQOSLASH                   │
├──────────────────┬─────────────────┬────────────────────┤
│ Xususiyat        │     STACK        │      QUEUE          │
├──────────────────┼─────────────────┼────────────────────┤
│ Tamoyil          │  LIFO           │  FIFO               │
│ Qo'shish         │  push() — tepa  │  enqueue() — orqa   │
│ Olish            │  pop()  — tepa  │  dequeue() — old    │
│ Qarash           │  peek() — tepa  │  peek() — old       │
│ Qo'llanish       │  Undo, rekursiya│  Navbat, printer    │
│                  │  qavs tekshirish│  BFS algoritmi      │
└──────────────────┴─────────────────┴────────────────────┘
""")


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Asosiy (Oson):
  Queue yordamida supermarket kassasi simulyatsiyasi:
  - 10 ta mijoz keladi (har biri tasodifiy 1-5 mahsulot bilan)
  - Kassir har safar birinchi mijozga xizmat ko'rsatadi
  - Har bir xizmat vaqtini hisoblang
  - Jami xizmat vaqtini chiqaring

TOPSHIRIQ 2 — O'rta:
  Hot Potato o'yini:
  - n ta o'yinchi aylana holda o'tiradi
  - Kartoshka k marta o'tkaziladi
  - k-chi o'yinchi chiqariladi
  - Oxirigacha qolgan g'olib
  (Hint: Queue dan foydalaning — chiqdi → oxiriga qo'shing)

TOPSHIRIQ 3 — O'rta:
  Stack orqali Queue yasash:
  - Faqat 2 ta Stack ishlatib Queue ni amalga oshiring
  - enqueue() va dequeue() metodlarini yozing

TOPSHIRIQ 4 — Qiyin:
  Labirint yechish (BFS bilan):
  - 2D massivda labirint: 0=yo'l, 1=devor
  - Start va finish beriladi
  - Queue yordamida BFS bilan eng qisqa yo'lni toping
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ Queue nima — FIFO (First In, First Out)
✔️ Kundalik misollari: bank, printer, xabar navbati
✔️ Queue metodlari:
    enqueue() — orqadan qo'shish   O(1)
    dequeue() — oldidan olish      O(1)
    peek()    — oldiga qarash      O(1)
    isEmpty() — bo'shligini tekshirish O(1)
✔️ 3 xil amalga oshirish:
    - Python list (sekin, pop(0) O(n))
    - collections.deque (tezkor, O(1))
    - Queue klassi (to'liq)
✔️ Deque — ikki tomonlama navbat (appendleft, popleft)
✔️ Amaliy misollar:
    - Bank navbat tizimi
    - Printer navbati
    - Palindrom tekshirish (Deque bilan)
✔️ Stack vs Queue taqqoslash
"""