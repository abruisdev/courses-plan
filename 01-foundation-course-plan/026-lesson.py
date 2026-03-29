# ============================================================
#   DARS 26: Stack (Stek)
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# DARS HAQIDA
# ------------------------------------------------------------

"""
Stack — LIFO (Last In, First Out) tamoyilida ishlaydigan
ma'lumotlar tuzilmasi.

LIFO = Oxirgi kirgan, birinchi chiqadi.

Kundalik hayotda:
  📚 Kitoblar to'plami — eng yuqoridagini olasiz
  🍽️ Likopchalar — eng yuqoridagini olasiz
  ↩️ Ctrl+Z (Undo) — oxirgi amalni bekor qilish
  🌐 Brauzerdagi "Orqaga" tugmasi
  📞 Funksiya chaqiruvlar (call stack)

Operatsiyalar:
  push()   — elementni qo'shish (tepaga)
  pop()    — elementni olib tashlash (tepadan)
  peek()   — tepaga qarash (olib tashlashsiz)
  isEmpty()— bo'shligini tekshirish
  isFull() — to'lganini tekshirish (chegaralangan stackda)
"""

print("=" * 55)
print("    STACK — LIFO tuzilmasi")
print("=" * 55)

print("""
  PUSH →  ┌───┐
           │ D │  ← push(D)
           ├───┤
           │ C │  ← push(C)
           ├───┤
           │ B │  ← push(B)
           ├───┤
           │ A │  ← push(A)
           └───┘
  POP  →   D chiqadi (oxirgi kirgan, birinchi chiqadi)
""")


# ============================================================
# 1-USUL: PYTHON LIST BILAN STACK
# ============================================================

print("=" * 55)
print("    1-USUL: Python list bilan Stack")
print("=" * 55)

"""
Python list — stack uchun tayyor vosita!
  append() → push()   — oxiriga qo'shish = tepaga qo'shish
  pop()    → pop()    — oxiridan olish   = tepadan olish
  [-1]     → peek()   — oxirgisiga qarash
"""

# ── Sodda list stack ──────────────────────────────────────────
stack = []

# push():
stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")
print("Stack:", stack)   # ['A', 'B', 'C', 'D']
print("Tepa:", stack[-1])# D

# pop():
chiqdi = stack.pop()
print(f"Pop: {chiqdi}")  # D
print("Stack:", stack)   # ['A', 'B', 'C']

chiqdi = stack.pop()
print(f"Pop: {chiqdi}")  # C
print("Stack:", stack)   # ['A', 'B']

# isEmpty():
print("Bo'shmi?", len(stack) == 0)  # False

# Bo'sh stackdan pop — XATO:
try:
    empty_stack = []
    empty_stack.pop()
except IndexError:
    print("Xato: Stack bo'sh!")


# ============================================================
# 2-USUL: KLASS BILAN STACK (CHEGARASIZ)
# ============================================================

print("\n" + "=" * 55)
print("    2-USUL: Stack klassi (Chegarasiz)")
print("=" * 55)

class Stack:
    """
    LIFO tamoyilidagi Stack ma'lumotlar tuzilmasi.
    list asosida qurilgan, chegaralanmagan.
    """

    def __init__(self):
        self._ma_lumot = []     # ichki ro'yxat

    # ── push() — Tepaga qo'shish — O(1) ──────────────────────
    def push(self, qiymat):
        """Elementni stackning tepasiga qo'shadi."""
        self._ma_lumot.append(qiymat)
        print(f"  push({qiymat}) → Stack: {self._ma_lumot}")

    # ── pop() — Tepadan olish — O(1) ─────────────────────────
    def pop(self):
        """Tepadan elementni olib qaytaradi."""
        if self.isEmpty():
            print("  Xato: Stack bo'sh!")
            return None
        element = self._ma_lumot.pop()
        print(f"  pop() → {element} | Stack: {self._ma_lumot}")
        return element

    # ── peek() — Tepaga qarash — O(1) ────────────────────────
    def peek(self):
        """Tepadagi elementni qaytaradi (o'chirmaydi)."""
        if self.isEmpty():
            return None
        return self._ma_lumot[-1]

    # ── isEmpty() — Bo'shligini tekshirish — O(1) ─────────────
    def isEmpty(self):
        """Stack bo'sh bo'lsa True qaytaradi."""
        return len(self._ma_lumot) == 0

    # ── size() — Elementlar soni — O(1) ──────────────────────
    def size(self):
        return len(self._ma_lumot)

    def __str__(self):
        if self.isEmpty():
            return "Stack: bo'sh"
        return f"Stack: {self._ma_lumot} ← tepa: {self.peek()}"


# Test:
print("\n--- Stack klassi sinovi ---")
s = Stack()
print(s)

s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(f"\nTepa: {s.peek()}")
print(f"Hajm: {s.size()}")
print(s)

print()
s.pop()
s.pop()
print(s)
print(f"Bo'shmi? {s.isEmpty()}")


# ============================================================
# 3-USUL: CHEGARALANGAN STACK (Maxsize bilan)
# ============================================================

print("\n" + "=" * 55)
print("    3-USUL: Chegaralangan Stack")
print("=" * 55)

class ChegaralanganStack:
    """
    Maksimal hajm chegaralangan Stack.
    Real tizimlarda (xotira chegarasi) ishlatiladi.
    """

    def __init__(self, maxsize):
        self.maxsize     = maxsize
        self._ma_lumot   = []

    def push(self, qiymat):
        if self.isFull():
            print(f"  ✗ Stack to'la! (max={self.maxsize})")
            return False
        self._ma_lumot.append(qiymat)
        print(f"  ✓ push({qiymat})")
        return True

    def pop(self):
        if self.isEmpty():
            print("  ✗ Stack bo'sh!")
            return None
        return self._ma_lumot.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self._ma_lumot[-1]

    def isEmpty(self):
        return len(self._ma_lumot) == 0

    def isFull(self):
        """Stack to'la bo'lsa True qaytaradi."""
        return len(self._ma_lumot) == self.maxsize

    def size(self):
        return len(self._ma_lumot)

    def __str__(self):
        return f"Stack({self.size()}/{self.maxsize}): {self._ma_lumot}"


cs = ChegaralanganStack(maxsize=4)
cs.push(1)
cs.push(2)
cs.push(3)
cs.push(4)
cs.push(5)   # To'la!
print(cs)
print(f"To'lami? {cs.isFull()}")
print(f"Pop: {cs.pop()}")
print(cs)


# ============================================================
# AMALIY MISOLLAR
# ============================================================

print("\n" + "=" * 55)
print("    AMALIY MISOLLAR")
print("=" * 55)

# ── MISOL 1: Qavslar muvozanati ───────────────────────────────
"""
Dasturlashda eng ko'p ishlatiladigan Stack misoli:
Qavslar to'g'ri yopilganmi?
"""

def qavs_tekshir(matn):
    """
    Stack yordamida qavslar muvozanatini tekshiradi.
    '(', '{', '[' → ochiladi → stack ga push
    ')', '}', ']' → yopiladi → stack dan pop + mosligini tekshir
    """
    stack = []
    mos = {')': '(', '}': '{', ']': '['}

    for belgi in matn:
        if belgi in '({[':
            stack.append(belgi)
        elif belgi in ')}]':
            if not stack or stack[-1] != mos[belgi]:
                return False
            stack.pop()

    return len(stack) == 0   # barcha ochilganlar yopilgan bo'lsin

print("\n--- Qavslar muvozanati ---")
sinovlar = [
    ("([]{})", True),
    ("([)]",   False),
    ("{[()]}",  True),
    ("(((",     False),
    ("",        True),
    ("{[}]",    False),
]
for matn, kutilgan in sinovlar:
    natija = qavs_tekshir(matn)
    belgi = "✓" if natija == kutilgan else "✗"
    print(f"  {belgi} '{matn:10}' → {'To\'g\'ri' if natija else 'Xato'}")


# ── MISOL 2: Undo/Redo tizimi ─────────────────────────────────
print("\n--- Undo / Redo tizimi ---")

class MatnTahrirlash:
    """
    Stack yordamida Undo/Redo funksiyasi.
    """

    def __init__(self):
        self.matn        = ""
        self.undo_stack  = Stack()
        self.redo_stack  = Stack()

    def yoz(self, qo_shimcha):
        self.undo_stack.push(self.matn)    # oldingi holatni saqlash
        self.matn += qo_shimcha
        self.redo_stack = Stack()          # yangi amal = redo tozalash
        print(f"  Yozildi: '{self.matn}'")

    def undo(self):
        if self.undo_stack.isEmpty():
            print("  Undo yo'q!")
            return
        self.redo_stack.push(self.matn)
        self.matn = self.undo_stack.pop()
        print(f"  Undo → '{self.matn}'")

    def redo(self):
        if self.redo_stack.isEmpty():
            print("  Redo yo'q!")
            return
        self.undo_stack.push(self.matn)
        self.matn = self.redo_stack.pop()
        print(f"  Redo → '{self.matn}'")

    def holat(self):
        print(f"  Hozirgi matn: '{self.matn}'")


tahrir = MatnTahrirlash()
tahrir.yoz("Salom")
tahrir.yoz(", Dunyo")
tahrir.yoz("!")
tahrir.holat()
tahrir.undo()
tahrir.undo()
tahrir.holat()
tahrir.redo()
tahrir.holat()


# ── MISOL 3: Postfix hisoblash ───────────────────────────────
print("\n--- Postfix kalkulyator ---")

"""
Postfix (RPN) — operator operandlardan keyin yoziladi.
  Odatiy:  3 + 4    = 7
  Postfix: 3 4 +    = 7

  "3 4 + 2 *" = (3+4)*2 = 14

Algoritm:
  - Raqam → stack ga push
  - Operator (+, -, *, /) → ikki element pop, hisoblash, push
"""

def postfix_hisob(ifoda):
    stack = []
    tokenlar = ifoda.split()

    for token in tokenlar:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if   token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a / b)

    return stack[0]

sinovlar = [
    ("3 4 +",       7),     # 3+4
    ("3 4 + 2 *",   14),    # (3+4)*2
    ("5 1 2 + 4 * + 3 -", 14),  # 5+((1+2)*4)-3
]
for ifoda, javob in sinovlar:
    natija = postfix_hisob(ifoda)
    print(f"  '{ifoda}' = {natija}  ({'✓' if natija==javob else '✗'})")


# ============================================================
# LINKEDLIST YORDAMIDA STACK
# ============================================================

print("\n" + "=" * 55)
print("    LINKEDLIST YORDAMIDA STACK")
print("=" * 55)

class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLL:
    """LinkedList asosidagi Stack — dinamik xotira uchun ideal."""

    def __init__(self):
        self.tepa = None
        self._size = 0

    def push(self, data):
        yangi = LLNode(data)
        yangi.next = self.tepa
        self.tepa  = yangi
        self._size += 1

    def pop(self):
        if self.isEmpty():
            return None
        qiymat     = self.tepa.data
        self.tepa  = self.tepa.next
        self._size -= 1
        return qiymat

    def peek(self):
        return self.tepa.data if self.tepa else None

    def isEmpty(self):
        return self.tepa is None

    def size(self):
        return self._size

    def __str__(self):
        elementlar = []
        joriy = self.tepa
        while joriy:
            elementlar.append(str(joriy.data))
            joriy = joriy.next
        return "Tepa → " + " → ".join(elementlar)


sll = StackLL()
sll.push(10)
sll.push(20)
sll.push(30)
print(sll)
print(f"Tepa: {sll.peek()}")
print(f"Pop: {sll.pop()}")
print(sll)


# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Asosiy (Oson):
  Stack yordamida so'zni teskari aylantiring.
  "Python" → "nohtyP"
  Hint: Har harfni push qiling, keyin barchasini pop qiling.

TOPSHIRIQ 2 — O'rta:
  Brauzerdagi "Orqaga" va "Oldinga" tugmalarini simulyatsiya qiling:
  - visit(url)   — yangi sahifaga o'tish (undo stack ga push)
  - back()       — orqaga (undo dan pop, redo ga push)
  - forward()    — oldinga (redo dan pop, undo ga push)
  - current()    — hozirgi sahifa

TOPSHIRIQ 3 — O'rta:
  Son o'nlik tizimdan ikkilik tizimga aylantirish.
  Stack yordamida:
    42 → ikkilik:
      42 % 2 = 0 → push(0)
      21 % 2 = 1 → push(1)
      10 % 2 = 0 → push(0)
       5 % 2 = 1 → push(1)
       2 % 2 = 0 → push(0)
       1 % 2 = 1 → push(1)
    pop barchasini → "101010"

TOPSHIRIQ 4 — Qiyin:
  Stack yordamida arifmetik ifodani hisoblash dasturi yarating.
  "(3 + 4) * (2 - 1)" kabi oddiy ifodani qabul qilib hisoblang.
"""


# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ Stack nima — LIFO (Last In, First Out)
✔️ Kundalik misollari: kitoblar, undo, brauzer
✔️ Stack metodlari:
    push()   — tepaga qo'shish       O(1)
    pop()    — tepadan olish         O(1)
    peek()   — tepaga qarash         O(1)
    isEmpty()— bo'shligini tekshirish O(1)
    isFull() — to'lganini tekshirish  O(1)
✔️ 3 xil amalga oshirish:
    - Python list bilan (oddiy)
    - Stack klassi (chegarasiz)
    - Chegaralangan Stack (maxsize)
    - LinkedList bilan Stack
✔️ Amaliy misollar:
    - Qavslar muvozanati
    - Undo/Redo tizimi
    - Postfix kalkulyator
"""