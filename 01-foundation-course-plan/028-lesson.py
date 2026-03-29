# ============================================================
#   DARS 28: Tree (Daraxt)
#   Muallif: Isroilov Rustam (Abruisdev)
# ============================================================

# ------------------------------------------------------------
# DARS HAQIDA
# ------------------------------------------------------------

"""
Tree (Daraxt) — tugunlar ierarxiyasidan iborat chiziqsiz
(non-linear) ma'lumotlar tuzilmasi.

Kundalik hayotda:
  🌳 Oila daraxtlari (shajara)
  📁 Fayl tizimi (papkalar)
  🏢 Kompaniya tuzilmasi
  🌐 HTML DOM tuzilmasi
  📖 Lug'at (trie)

Terminologiya:
  Root (Ildiz)    — eng yuqori tugun (otasi yo'q)
  Node (Tugun)    — daraxtning har bir elementi
  Edge (Qirra)    — tugunlar o'rtasidagi bog'lanish
  Parent (Ota)    — yuqoridagi tugun
  Child (Bola)    — quyi tugun
  Leaf (Barg)     — bolalari yo'q tugun
  Height (Balandlik) — ildizdan eng chuqur barggacha
  Depth (Chuqurlik)  — ildizdan shu tugunga qadar

Daraxt turlari:
  Binary Tree           — har tugunning maks 2 ta bola
  Binary Search Tree    — chap < ota ≤ o'ng
  AVL Tree              — muvozanatlangan BST
  N-ary Tree            — n ta bolali daraxt
"""

print("=" * 55)
print("    TREE — Daraxt ma'lumotlar tuzilmasi")
print("=" * 55)

print("""
  Binary Tree ko'rinishi:

              [10]          ← Root (ildiz)
             /    \\
          [5]      [15]
         /   \\    /   \\
       [3]  [7] [12] [20]   ← Leaf (barglar)

  10 → ota
  5, 15 → 10 ning bolalari
  3, 7 → 5 ning bolalari
  3, 7, 12, 20 → barglar (bolasiz)
""")


# ============================================================
# BINARY TREE TUGUN (NODE)
# ============================================================

class TreeNode:
    """Binary Tree uchun tugun."""

    def __init__(self, data):
        self.data = data
        self.left = None  # chap bola
        self.right = None  # o'ng bola

    def __str__(self):
        return str(self.data)


# ── Qo'lda daraxt qurish ──────────────────────────────────────
print("--- Qo'lda daraxt qurish ---")

ildiz = TreeNode(10)
ildiz.left = TreeNode(5)
ildiz.right = TreeNode(15)
ildiz.left.left = TreeNode(3)
ildiz.left.right = TreeNode(7)
ildiz.right.left = TreeNode(12)
ildiz.right.right = TreeNode(20)

print(f"Ildiz: {ildiz.data}")
print(f"Ildiz chap: {ildiz.left.data}")
print(f"Ildiz o'ng: {ildiz.right.data}")
print(f"Chap→chap:  {ildiz.left.left.data}")
print(f"Chap→o'ng:  {ildiz.left.right.data}")

# ============================================================
# DARAXTNI AYLANIB CHIQISH (TRAVERSAL)
# ============================================================

print("\n" + "=" * 55)
print("    TRAVERSAL — Aylanib chiqish usullari")
print("=" * 55)

"""
Daraxtni 3 xil tartibda aylanib chiqish mumkin:

  1. Inorder   (LNR) — Chap → Ildiz → O'ng
  2. Preorder  (NLR) — Ildiz → Chap → O'ng
  3. Postorder (LRN) — Chap → O'ng → Ildiz

Qisqa:
  N = Node (tugun),  L = Left (chap),  R = Right (o'ng)

BST da Inorder → tartiblangan ketma-ketlik qaytaradi!
"""


# ── 1. Inorder traversal — Chap → Ildiz → O'ng ───────────────
def inorder(tugun):
    """LNR — Chap, Ildiz, O'ng (rekursiv)"""
    if tugun is None:
        return
    inorder(tugun.left)  # avval chapga
    print(tugun.data, end=" ")  # keyin o'zini
    inorder(tugun.right)  # keyin o'ngga


# ── 2. Preorder traversal — Ildiz → Chap → O'ng ──────────────
def preorder(tugun):
    """NLR — Ildiz, Chap, O'ng (rekursiv)"""
    if tugun is None:
        return
    print(tugun.data, end=" ")  # avval o'zini
    preorder(tugun.left)
    preorder(tugun.right)


# ── 3. Postorder traversal — Chap → O'ng → Ildiz ─────────────
def postorder(tugun):
    """LRN — Chap, O'ng, Ildiz (rekursiv)"""
    if tugun is None:
        return
    postorder(tugun.left)
    postorder(tugun.right)
    print(tugun.data, end=" ")  # eng oxirida o'zini


print("\n--- Traversal natijalari ---")
print("Inorder   (Chap→Ildiz→O'ng): ", end="")
inorder(ildiz)
print()  # 3 5 7 10 12 15 20

print("Preorder  (Ildiz→Chap→O'ng): ", end="")
preorder(ildiz)
print()  # 10 5 3 7 15 12 20

print("Postorder (Chap→O'ng→Ildiz): ", end="")
postorder(ildiz)
print()  # 3 7 5 12 20 15 10

# ── 4. Level Order (BFS) — Qatl bo'yicha ─────────────────────
from collections import deque


def level_order(ildiz):
    """Queue yordamida daraxtni qatl-qatl ko'rib chiqish."""
    if not ildiz:
        return
    navbat = deque([ildiz])
    qatl = 0
    while navbat:
        qatl_soni = len(navbat)
        print(f"  Qatl {qatl}: ", end="")
        for _ in range(qatl_soni):
            tugun = navbat.popleft()
            print(tugun.data, end=" ")
            if tugun.left:
                navbat.append(tugun.left)
            if tugun.right:
                navbat.append(tugun.right)
        print()
        qatl += 1


print("\n--- Level Order (BFS) ---")
level_order(ildiz)

# ============================================================
# BINARY SEARCH TREE (BST)
# ============================================================

print("\n" + "=" * 55)
print("    BINARY SEARCH TREE (BST)")
print("=" * 55)

"""
BST qoidasi:
  har bir tugun uchun:
    Chap bola  < Ota tugun
    O'ng bola >= Ota tugun

Bu qoida tufayli:
  ✔️ Qidirish   — O(log n) o'rtacha
  ✔️ Qo'shish   — O(log n) o'rtacha
  ✔️ O'chirish  — O(log n) o'rtacha
  ✔️ Inorder traversal → tartiblangan ketma-ketlik!

Misol: [10, 5, 15, 3, 7, 12, 20] ni BST ga kiritish:
              [10]
             /    \\
          [5]      [15]
         /   \\    /   \\
       [3]  [7] [12] [20]
"""


class BST:
    """Binary Search Tree."""

    def __init__(self):
        self.ildiz = None

    # ── insert() — Qo'shish — O(log n) ───────────────────────
    def insert(self, data):
        """Yangi qiymat qo'shadi (BST qoidasini saqlagan holda)."""
        if not self.ildiz:
            self.ildiz = TreeNode(data)
        else:
            self._insert_rekursiv(self.ildiz, data)

    def _insert_rekursiv(self, tugun, data):
        if data < tugun.data:
            if tugun.left is None:
                tugun.left = TreeNode(data)
            else:
                self._insert_rekursiv(tugun.left, data)
        else:
            if tugun.right is None:
                tugun.right = TreeNode(data)
            else:
                self._insert_rekursiv(tugun.right, data)

    # ── search() — Qidirish — O(log n) ───────────────────────
    def search(self, data):
        """data ni BST da qidiradi."""
        return self._search_rekursiv(self.ildiz, data)

    def _search_rekursiv(self, tugun, data):
        if tugun is None:
            return False
        if tugun.data == data:
            return True
        elif data < tugun.data:
            return self._search_rekursiv(tugun.left, data)
        else:
            return self._search_rekursiv(tugun.right, data)

    # ── inorder() — Tartiblangan chiqarish ───────────────────
    def inorder(self):
        """Tartiblangan ketma-ketlikda chiqaradi."""
        natija = []
        self._inorder_rekursiv(self.ildiz, natija)
        return natija

    def _inorder_rekursiv(self, tugun, natija):
        if tugun:
            self._inorder_rekursiv(tugun.left, natija)
            natija.append(tugun.data)
            self._inorder_rekursiv(tugun.right, natija)

    # ── height() — Balandlik ──────────────────────────────────
    def height(self):
        """Daraxtning balandligini hisoblaydi."""
        return self._height_rekursiv(self.ildiz)

    def _height_rekursiv(self, tugun):
        if tugun is None:
            return 0
        chap_b = self._height_rekursiv(tugun.left)
        ong_b = self._height_rekursiv(tugun.right)
        return 1 + max(chap_b, ong_b)

    # ── count() — Tugunlar soni ───────────────────────────────
    def count(self):
        return self._count_rekursiv(self.ildiz)

    def _count_rekursiv(self, tugun):
        if tugun is None:
            return 0
        return 1 + self._count_rekursiv(tugun.left) + self._count_rekursiv(tugun.right)

    # ── min() va max() ────────────────────────────────────────
    def min_qiymat(self):
        """Eng kichik qiymat — eng chap tugun."""
        if not self.ildiz:
            return None
        joriy = self.ildiz
        while joriy.left:
            joriy = joriy.left
        return joriy.data

    def max_qiymat(self):
        """Eng katta qiymat — eng o'ng tugun."""
        if not self.ildiz:
            return None
        joriy = self.ildiz
        while joriy.right:
            joriy = joriy.right
        return joriy.data

    # ── Chiroyli chiqarish ────────────────────────────────────
    def chiqar(self):
        """Daraxtni chiroyli tarzda chiqaradi."""
        self._chiqar_rekursiv(self.ildiz, "", True)

    def _chiqar_rekursiv(self, tugun, chegara, oxirgimi):
        if tugun:
            print(chegara + ("└── " if oxirgimi else "├── ") + str(tugun.data))
            yangi_chegara = chegara + ("    " if oxirgimi else "│   ")
            if tugun.left or tugun.right:
                if tugun.right:
                    self._chiqar_rekursiv(tugun.right, yangi_chegara, not bool(tugun.left))
                if tugun.left:
                    self._chiqar_rekursiv(tugun.left, yangi_chegara, True)


# Test:
print("\n--- BST qurilishi ---")
bst = BST()
qiymatlar = [10, 5, 15, 3, 7, 12, 20, 1, 4]
for q in qiymatlar:
    bst.insert(q)

print("Daraxt tuzilmasi:")
bst.chiqar()

print(f"\nInorder (tartiblangan): {bst.inorder()}")
print(f"Balandlik: {bst.height()}")
print(f"Tugunlar soni: {bst.count()}")
print(f"Minimum: {bst.min_qiymat()}")
print(f"Maksimum: {bst.max_qiymat()}")

print("\n--- Qidirish ---")
for q in [7, 99, 1, 20, 50]:
    natija = bst.search(q)
    print(f"  {q} → {'Topildi ✓' if natija else 'Topilmadi ✗'}")

# ============================================================
# DARAXT TURLARI HAQIDA QISQACHA
# ============================================================

print("""
┌──────────────────────────────────────────────────────────┐
│              DARAXT TURLARI                              │
├───────────────────┬──────────────────────────────────────┤
│ Tur               │ Tavsif                               │
├───────────────────┼──────────────────────────────────────┤
│ Binary Tree       │ Har tugunning max 2 ta bolasi        │
│ BST               │ Chap<Ildiz≤O'ng (qidirish uchun)    │
│ AVL Tree          │ Muvozanatlangan BST (har qadamda)    │
│ Heap              │ Ota ≤ yoki ≥ bolalar (priority queue)│
│ Trie              │ So'z/satrlar uchun                   │
│ N-ary Tree        │ N ta bolali (fayl tizimi)            │
├───────────────────┼──────────────────────────────────────┤
│ Traversal         │ Tartib                               │
├───────────────────┼──────────────────────────────────────┤
│ Inorder   (LNR)   │ Chap → Ildiz → O'ng                 │
│ Preorder  (NLR)   │ Ildiz → Chap → O'ng                 │
│ Postorder (LRN)   │ Chap → O'ng → Ildiz                 │
│ Level Order (BFS) │ Qatl-qatl (Queue ishlatadi)         │
└───────────────────┴──────────────────────────────────────┘
""")

# ============================================================
# AMALIY MISOL — Fayl tizimi (N-ary Tree)
# ============================================================

print("=== FAYL TIZIMI SIMULYATSIYASI ===\n")


class FaylNode:
    """Fayl tizimi uchun N-ary Tree tugun."""

    def __init__(self, nom, tur="papka"):
        self.nom = nom
        self.tur = tur  # "papka" yoki "fayl"
        self.bolalar = []

    def qo_sh(self, bola):
        self.bolalar.append(bola)
        return bola


def fayl_tizimini_chiqar(tugun, chegara=""):
    """Fayl tizimini daraxt ko'rinishida chiqaradi."""
    belgi = "📁" if tugun.tur == "papka" else "📄"
    print(f"{chegara}{belgi} {tugun.nom}")
    for i, bola in enumerate(tugun.bolalar):
        yangi_chegara = chegara + ("│   " if i < len(tugun.bolalar) - 1 else "    ")
        fayl_tizimini_chiqar(bola, yangi_chegara)


# Fayl tizimi quramiz:
uy = FaylNode("Mening kompyuterim")
hujjatlar = uy.qo_sh(FaylNode("Hujjatlar"))
rasmlar = uy.qo_sh(FaylNode("Rasmlar"))
musiqalar = uy.qo_sh(FaylNode("Musiqalar"))

# Hujjatlar ichiga:
python_pr = hujjatlar.qo_sh(FaylNode("Python loyiha"))
hujjatlar.qo_sh(FaylNode("Resume.docx", "fayl"))
python_pr.qo_sh(FaylNode("main.py", "fayl"))
python_pr.qo_sh(FaylNode("utils.py", "fayl"))
python_pr.qo_sh(FaylNode("README.md", "fayl"))

# Rasmlar ichiga:
tatil = rasmlar.qo_sh(FaylNode("Tatil_2024"))
tatil.qo_sh(FaylNode("IMG_001.jpg", "fayl"))
tatil.qo_sh(FaylNode("IMG_002.jpg", "fayl"))
rasmlar.qo_sh(FaylNode("Profil.png", "fayl"))

# Musiqalar:
musiqalar.qo_sh(FaylNode("Jazz", "papka")).qo_sh(FaylNode("Miles_Davis.mp3", "fayl"))
musiqalar.qo_sh(FaylNode("Pop", "papka")).qo_sh(FaylNode("Song.mp3", "fayl"))

fayl_tizimini_chiqar(uy)

# ------------------------------------------------------------
# MUSTAQIL MASHQ TOPSHIRIQLARI
# ------------------------------------------------------------

"""
TOPSHIRIQ 1 — Asosiy (Oson):
  BST qurib, quyidagi sonlarni kiriting:
    [50, 30, 70, 20, 40, 60, 80]
  a) Inorder traversal chiqaring (tartiblangan bo'lishi kerak)
  b) Balandligini toping
  c) 40 ni qidiring
  d) Minimum va maksimumni toping

TOPSHIRIQ 2 — O'rta:
  Binary Tree uchun quyidagi funksiyalarni yozing:
  a) Barcha elementlar yig'indisi
  b) Eng katta element
  c) Barglar soni (leaf count)
  d) Muayyan qatlning elementlari

TOPSHIRIQ 3 — O'rta:
  Ikkita BST bir xilmi yoki yo'qmi tekshiring.
  (Ikki daraxtning tuzilmasi va qiymatlari bir xil bo'lsa)

TOPSHIRIQ 4 — Qiyin:
  BST dan element o'chirish (delete) funksiyasini yozing.
  3 holat:
    a) Barg — shunchaki o'chiriladi
    b) 1 bolali — bola o'rniga o'tadi
    c) 2 bolali — o'ng pastki daraxtning minimumini toping,
                  o'chirilayotgan tugun joyiga qo'ying
"""

# ------------------------------------------------------------
# BUGUNGI DARSDA NIMALAR O'RGANDIK?
# ------------------------------------------------------------

"""
✔️ Tree (Daraxt) nima va terminologiyasi:
    Root, Node, Edge, Parent, Child, Leaf, Height, Depth
✔️ Binary Tree — har tugunning max 2 ta bolasi
✔️ Tugun (TreeNode) — data, left, right
✔️ Traversal usullari:
    Inorder   (LNR)  → Chap → Ildiz → O'ng (BST da tartiblangan!)
    Preorder  (NLR)  → Ildiz → Chap → O'ng
    Postorder (LRN)  → Chap → O'ng → Ildiz
    Level Order (BFS)→ Qatl-qatl (Queue yordamida)
✔️ Binary Search Tree (BST):
    Chap < Ildiz ≤ O'ng qoidasi
    insert(), search(), min(), max(), height(), count()
    Qidirish/qo'shish: O(log n) o'rtacha
✔️ N-ary Tree — n ta bolali daraxt (fayl tizimi)
✔️ Daraxt turlari: Binary, BST, AVL, Heap, Trie
"""