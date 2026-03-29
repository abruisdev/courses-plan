# ============================================================
#   DARS 25: Data Structure kirish va LinkedList
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# DARS HAQIDA
# ------------------------------------------------------------

"""
Ma'lumotlar tuzilmasi (Data Structure) — ma'lumotlarni
kompyuter xotirasida samarali saqlash va boshqarish usuli.

Nima uchun muhim?
  ✔️ To'g'ri tuzilma = tez va samarali dastur
  ✔️ Interview savollarining asosiy qismi
  ✔️ Katta ma'lumotlar bilan ishlashda zarur

Bugun o'rganamiz:
  1️⃣  Data Structure turlari (umumiy ko'rish)
  2️⃣  LinkedList — bog'langan ro'yxat
      - Tugun (Node)
      - Bir tomonlama LinkedList
      - push(), append(), insertAfter(), deleteNode()
      - Ko'p qo'llaniladigan amallar

Keyingi darslarda:
  → Stack (26-dars)
  → Queue (27-dars)
  → Tree  (28-dars)
"""


# ============================================================
# DATA STRUCTURE TURLARI — UMUMIY KO'RISH
# ============================================================

print("=" * 55)
print("    DATA STRUCTURE TURLARI")
print("=" * 55)

"""
┌──────────────────────────────────────────────────────────┐
│                DATA STRUCTURE TURLARI                    │
├─────────────────────────┬────────────────────────────────┤
│  Chiziqli (Linear)      │  Chiziqsiz (Non-linear)        │
├─────────────────────────┼────────────────────────────────┤
│  ✔️ Array / List        │  ✔️ Tree (Daraxt)               │
│  ✔️ LinkedList          │  ✔️ Graph (Graf)                │
│  ✔️ Stack               │  ✔️ Heap                        │
│  ✔️ Queue               │                                │
├─────────────────────────┴────────────────────────────────┤
│  Python da mavjud:                                       │
│  list, tuple, dict, set → o'rganildi                     │
│  LinkedList, Stack, Queue, Tree → shu darsda boshlaymiz  │
└──────────────────────────────────────────────────────────┘

Array vs LinkedList:
  Array (list):
    - Xotirada ketma-ket saqlanadi
    - Indeks bilan O(1) murojaat
    - O'rtaga qo'shish/o'chirish — O(n) (surilish kerak)

  LinkedList:
    - Xotirada tarqoq saqlanadi, har biri keyingisiga ishora qiladi
    - Indeks bilan murojaat — O(n) (boshidan yurib borish kerak)
    - Boshiga qo'shish/o'chirish — O(1)
"""


# ============================================================
# LINKEDLIST — BOG'LANGAN RO'YXAT
# ============================================================

# ------------------------------------------------------------
# TUGUN (NODE) NIMA?
# ------------------------------------------------------------

"""
LinkedList — zanjir kabi birbiriga bog'langan tugunlardan iborat.

Har bir tugun (Node) ikki narsadan iborat:
  1. data  — saqlanadigan ma'lumot
  2. next  — keyingi tugunga ishora (pointer)

Tasavvur:
  [10 | →] → [20 | →] → [30 | →] → [40 | None]
   HEAD                              TAIL (oxirgi)

Tugun tuzilmasi:
  class Node:
      def __init__(self, data):
          self.data = data
          self.next = None
"""

print("\n" + "=" * 55)
print("    LINKEDLIST — Bog'langan ro'yxat")
print("=" * 55)


# ── Tugun (Node) klassi ───────────────────────────────────────
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    # dastlab keyingisi yo'q

    def __str__(self):
        return str(self.data)


# ── Oddiy tugunlar bog'lash (qo'lda) ─────────────────────────
print("\n--- Qo'lda bog'lash ---")
t1 = Node(10)
t2 = Node(20)
t3 = Node(30)

t1.next = t2    # 10 → 20
t2.next = t3    # 20 → 30

# Zanjir bo'ylab yurib chiqish:
joriy = t1
while joriy:
    print(joriy.data, end=" → ")
    joriy = joriy.next
print("None")
# 10 → 20 → 30 → None


# ============================================================
# LINKEDLIST KLASSI
# ============================================================

class LinkedList:
    """
    Bir tomonlama bog'langan ro'yxat.
    head — birinchi tugunga ishora.
    """

    def __init__(self):
        self.head = None    # bo'sh ro'yxat

    # ── Ko'rsatish ────────────────────────────────────────────
    def ko_rsat(self):
        """Barcha elementlarni chiziqli ko'rinishda chiqaradi"""
        if not self.head:
            print("LinkedList bo'sh!")
            return
        joriy = self.head
        elementlar = []
        while joriy:
            elementlar.append(str(joriy.data))
            joriy = joriy.next
        print(" → ".join(elementlar) + " → None")

    def uzunlik(self):
        """Elementlar sonini qaytaradi — O(n)"""
        son = 0
        joriy = self.head
        while joriy:
            son += 1
            joriy = joriy.next
        return son

    # ──────────────────────────────────────────────────────────
    # push() — BOSHIGA QO'SHISH — O(1)
    # ──────────────────────────────────────────────────────────
    def push(self, data):
        """
        Ro'yxat BOSHIGA yangi tugun qo'shadi.
        Yangi tugun → eski head bo'ladi.
        Vaqt: O(1) — juda tez!
        """
        yangi = Node(data)
        yangi.next = self.head      # yangi tugunning keyingisi = eski head
        self.head = yangi           # head yangi tugunga ishora qiladi

    # ──────────────────────────────────────────────────────────
    # append() — OXIRIGA QO'SHISH — O(n)
    # ──────────────────────────────────────────────────────────
    def append(self, data):
        """
        Ro'yxat OXIRIGA yangi tugun qo'shadi.
        Oxirgi tugunni topib, uning next ini yangi tugunga yo'naltiradi.
        Vaqt: O(n) — oxirga yetguncha borish kerak
        """
        yangi = Node(data)
        if not self.head:
            self.head = yangi       # ro'yxat bo'sh bo'lsa, head = yangi
            return
        joriy = self.head
        while joriy.next:           # oxirgi tugunga yetguncha bor
            joriy = joriy.next
        joriy.next = yangi          # oxirgi tugundan yangiga ishora

    # ──────────────────────────────────────────────────────────
    # insertAfter() — BELGILANGAN JOYDAN KEYIN QO'SHISH — O(n)
    # ──────────────────────────────────────────────────────────
    def insertAfter(self, oldingi_data, yangi_data):
        """
        oldingi_data qiymatli tugundan KEYIN yangi tugun qo'shadi.
        Vaqt: O(n) — oldingi tugunni qidirish kerak
        """
        joriy = self.head
        while joriy:
            if joriy.data == oldingi_data:
                yangi = Node(yangi_data)
                yangi.next = joriy.next     # yangi tugun → oldingi keyingisiga
                joriy.next = yangi          # oldingi → yangi tugunga
                return
            joriy = joriy.next
        print(f"✗ {oldingi_data} topilmadi!")

    # ──────────────────────────────────────────────────────────
    # deleteNode() — TUGUNNI O'CHIRISH — O(n)
    # ──────────────────────────────────────────────────────────
    def deleteNode(self, data):
        """
        data qiymatli birinchi tugunni o'chiradi.
        Vaqt: O(n) — tugunni qidirish kerak
        """
        if not self.head:
            print("Ro'yxat bo'sh!")
            return

        # Agar head o'chirilsa:
        if self.head.data == data:
            self.head = self.head.next
            print(f"✓ {data} o'chirildi (boshdan)")
            return

        # O'chirilayotgan tugunning oldingisini topish:
        joriy = self.head
        while joriy.next:
            if joriy.next.data == data:
                joriy.next = joriy.next.next    # o'tkazib yuborish
                print(f"✓ {data} o'chirildi")
                return
            joriy = joriy.next

        print(f"✗ {data} topilmadi!")

    # ──────────────────────────────────────────────────────────
    # search() — QIDIRISH — O(n)
    # ──────────────────────────────────────────────────────────
    def search(self, data):
        """data ni ro'yxatda qidiradi. Topsa True, topmasda False."""
        joriy = self.head
        pozitsiya = 0
        while joriy:
            if joriy.data == data:
                print(f"✓ {data} topildi ({pozitsiya}-pozitsiyada)")
                return True
            joriy = joriy.next
            pozitsiya += 1
        print(f"✗ {data} topilmadi")
        return False

    # ── Qo'shimcha metodlar ───────────────────────────────────
    def teskari(self):
        """Ro'yxat tartibini teskari qiladi — O(n)"""
        oldingi = None
        joriy   = self.head
        while joriy:
            keyingi       = joriy.next
            joriy.next    = oldingi
            oldingi       = joriy
            joriy         = keyingi
        self.head = oldingi

    def o_rta_topish(self):
        """Tezkor va sekin pointer bilan o'rta elementni topadi — O(n)"""
        sekin = self.head
        tez   = self.head
        while tez and tez.next:
            sekin = sekin.next
            tez   = tez.next.next
        return sekin.data if sekin else None


# ============================================================
# LINKEDLIST METODLARINI SINAB KO'RISH
# ============================================================

print("\n--- LinkedList metodlari ---\n")

ll = LinkedList()

# push() — boshiga qo'shish:
print("push() — boshiga qo'shish:")
ll.push(10)
ll.ko_rsat()   # 10 → None
ll.push(20)
ll.ko_rsat()   # 20 → 10 → None
ll.push(30)
ll.ko_rsat()   # 30 → 20 → 10 → None

# append() — oxiriga qo'shish:
print("\nappend() — oxiriga qo'shish:")
ll.append(5)
ll.ko_rsat()   # 30 → 20 → 10 → 5 → None
ll.append(1)
ll.ko_rsat()   # 30 → 20 → 10 → 5 → 1 → None

# insertAfter() — oraliqqa qo'shish:
print("\ninsertAfter(10, 99) — 10 dan keyin 99 qo'shish:")
ll.insertAfter(10, 99)
ll.ko_rsat()   # 30 → 20 → 10 → 99 → 5 → 1 → None

# deleteNode() — o'chirish:
print("\ndeleteNode(20) — 20 ni o'chirish:")
ll.deleteNode(20)
ll.ko_rsat()   # 30 → 10 → 99 → 5 → 1 → None

print("deleteNode(30) — bosh elementni o'chirish:")
ll.deleteNode(30)
ll.ko_rsat()   # 10 → 99 → 5 → 1 → None

print("deleteNode(999) — mavjud bo'lmagan:")
ll.deleteNode(999)

# search():
print("\nsearch():")
ll.search(99)
ll.search(999)

# uzunlik:
print(f"\nUzunlik: {ll.uzunlik()}")

# teskari:
print("\nteskari():")
ll.teskari()
ll.ko_rsat()   # 1 → 5 → 99 → 10 → None

# o'rta topish:
print(f"O'rta element: {ll.o_rta_topish()}")


# ============================================================
# LINKEDLIST TURLARI
# ============================================================

print("\n" + "=" * 55)
print("    LINKEDLIST TURLARI")
print("=" * 55)

"""
┌─────────────────────────────────────────────────────────┐
│                LINKEDLIST TURLARI                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. Bir tomonlama (Singly):                             │
│     [10|→] → [20|→] → [30|→] → None                   │
│                                                         │
│  2. Ikki tomonlama (Doubly):                            │
│     None ← [←|10|→] ↔ [←|20|→] ↔ [←|30|→] → None    │
│     (har tugunning oldingi va keyingisi bor)            │
│                                                         │
│  3. Aylana (Circular):                                  │
│     [10|→] → [20|→] → [30|→] → [10|→] (davra)         │
│                                                         │
└─────────────────────────────────────────────────────────┘
"""

# ── Ikki tomonlama LinkedList (Doubly) ────────────────────────
print("--- Doubly LinkedList ---")

class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None    # keyingisi
        self.prev = None    # oldingisi

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None    # oxirgi tugunni saqlaymiz (O(1) oxiriga qo'shish!)

    def append(self, data):
        yangi = DoubleNode(data)
        if not self.head:
            self.head = self.tail = yangi
            return
        yangi.prev     = self.tail
        self.tail.next = yangi
        self.tail      = yangi

    def ko_rsat_oldinga(self):
        joriy = self.head
        qismlar = []
        while joriy:
            qismlar.append(str(joriy.data))
            joriy = joriy.next
        print("Oldinga: " + " ↔ ".join(qismlar))

    def ko_rsat_teskari(self):
        joriy = self.tail
        qismlar = []
        while joriy:
            qismlar.append(str(joriy.data))
            joriy = joriy.prev
        print("Teskari: " + " ↔ ".join(qismlar))


dll = DoublyLinkedList()
for x in [10, 20, 30, 40, 50]:
    dll.append(x)
dll.ko_rsat_oldinga()
dll.ko_rsat_teskari()


# ============================================================
# ARRAY vs LINKEDLIST: QACHON NIMA ISHLATISH
# ============================================================

print("""
┌──────────────────────────────────────────────────────────┐
│          ARRAY vs LINKEDLIST TAQQOSLASH                  │
├──────────────────┬────────────────┬──────────────────────┤
│ Amal             │  Array (list)  │  LinkedList          │
├──────────────────┼────────────────┼──────────────────────┤
│ Murojaat [i]     │  O(1) ⭐       │  O(n)                │
│ Boshiga qo'shish │  O(n)          │  O(1) ⭐             │
│ Oxiriga qo'shish │  O(1) ⭐       │  O(n)                │
│ O'rtaga qo'shish │  O(n)          │  O(1)* ⭐            │
│ Boshidan o'chirish│ O(n)          │  O(1) ⭐             │
│ Oxiridan o'chirish│ O(1) ⭐       │  O(n)                │
│ Qidirish         │  O(n)          │  O(n)                │
│ Xotira           │  Ixcham ⭐     │  Ko'proq              │
└──────────────────┴────────────────┴──────────────────────┘
* O'rtaga qo'shishda qo'shni tugun topilgan bo'lsa O(1)

LinkedList ishlatish kerak bo'lgan hollat:
  ✔️ Ko'p boshiga qo'shish/o'chirish
  ✔️ Elementlar soni oldindan noma'lum
  ✔️ Stack va Queue qurishda

Array ishlatish kerak bo'lgan holat:
  ✔️ Indeks orqali tez murojaat kerak
  ✔️ Xotira samarali bo'lishi kerak
  ✔️ Ko'p o'qish, kam yozish
""")


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Asosiy (Oson):
  LinkedList ga 1 dan 10 gacha sonlarni append() bilan qo'shing.
  Ko'rsating, keyin barcha juft sonlarni o'chiring.
  Natijani ko'rsating.

TOPSHIRIQ 2 — O'rta:
  LinkedList ga push() bilan: 5, 3, 8, 1, 9, 2 qo'shing.
  a) Uzunligini toping
  b) O'rta elementni toping
  c) Ro'yxatni teskari qiling
  d) Tartiblang (bubble sort bilan)

TOPSHIRIQ 3 — O'rta:
  Palindromni tekshirish:
  LinkedList bo'lgan raqamlar palindrom bo'lsa True qaytarsin.
  Misol: [1, 2, 3, 2, 1] → True
         [1, 2, 3, 4, 5] → False

TOPSHIRIQ 4 — Qiyin:
  Ikkita tartiblangan LinkedList ni birlashtiring:
  [1, 3, 5, 7] va [2, 4, 6, 8]
  → [1, 2, 3, 4, 5, 6, 7, 8]
  (merge sort kabi)
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ Data Structure nima va turlari
✔️ Array vs LinkedList farqi va qachon nima ishlatish
✔️ Tugun (Node) — data va next
✔️ Bir tomonlama LinkedList:
    push()        — boshiga qo'shish     O(1)
    append()      — oxiriga qo'shish     O(n)
    insertAfter() — oraliqqa qo'shish    O(n)
    deleteNode()  — o'chirish            O(n)
    search()      — qidirish             O(n)
    teskari()     — tartibni teskari     O(n)
    o_rta_topish()— o'rta elementni top  O(n)
✔️ Ikki tomonlama LinkedList (Doubly LinkedList)
✔️ LinkedList turlari: Singly, Doubly, Circular
"""