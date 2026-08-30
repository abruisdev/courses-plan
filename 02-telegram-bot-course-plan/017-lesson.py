<!doctype html>
<!-- =========================================================
     DARS 17: Mini App uchun HTML va CSS
     Muallif: Isroilov Rustam (Abruisdev)
     ========================================================= -->
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mini Store</title>
  <style>
    /* Telegram theme ranglari bo‘lmasa fallback ranglar ishlaydi. */
    :root {
      --bg: var(--tg-theme-bg-color, #ffffff);
      --text: var(--tg-theme-text-color, #111111);
      --hint: var(--tg-theme-hint-color, #707579);
      --button: var(--tg-theme-button-color, #2481cc);
      --button-text: var(--tg-theme-button-text-color, #ffffff);
    }

    * { box-sizing: border-box; }
    body {
      margin: 0;
      padding: 16px;
      font-family: Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
    }

    h1 { font-size: 24px; margin: 0 0 6px; }
    .subtitle { margin: 0 0 16px; color: var(--hint); }
    .catalog { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; }
    .card {
      border: 1px solid var(--hint);
      border-radius: 14px;
      padding: 12px;
    }
    .card img { width: 100%; border-radius: 10px; }
    .price { font-weight: bold; margin: 8px 0; }
    button {
      width: 100%; border: 0; border-radius: 10px; padding: 12px;
      background: var(--button); color: var(--button-text); cursor: pointer;
    }
  </style>
</head>
<body>
  <h1>Mini Store</h1>
  <p class="subtitle">Mahsulotni tanlang</p>

  <main class="catalog">
    <article class="card">
      <img src="https://placehold.co/300x200" alt="Python kursi">
      <h2>Python Foundation</h2>
      <p class="price">500 000 so‘m</p>
      <button>Tanlash</button>
    </article>

    <article class="card">
      <img src="https://placehold.co/300x200" alt="Telegram Bot kursi">
      <h2>Telegram Bot</h2>
      <p class="price">700 000 so‘m</p>
      <button>Tanlash</button>
    </article>
  </main>

  <!--
  BUGUNGI DARSDA:
    ✔️ HTML: h1, p, main, article, img, button
    ✔️ CSS: color, padding, margin, border, border-radius
    ✔️ CSS Grid va responsive mobile UI
    ✔️ Telegram theme CSS variables

  MUSTAQIL MASHQ:
    1. Yana 2 ta mahsulot kartasi qo‘shing.
    2. Card ichiga mahsulot tavsifini yozing.
    3. Kartalarni mobil ekranda 1 ustun, katta ekranda 2 ustun qiling.
    4. Telegram dark mode’da dizaynni tekshiring.
  -->
</body>
</html>
