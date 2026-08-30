<!doctype html>
<!-- =========================================================
     DARS 18: JavaScript, DOM va fetch()
     Muallif: Isroilov Rustam (Abruisdev)
     ========================================================= -->
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript Mini App</title>
</head>
<body>
  <h1>Mahsulotlar</h1>
  <section id="products"></section>
  <p id="cart-total">Savat: 0 so‘m</p>

  <script>
    // O‘zgaruvchi va array.
    const products = [
      { id: 1, name: "Python Foundation", price: 500000 },
      { id: 2, name: "Telegram Bot", price: 700000 },
    ];

    const cart = [];
    const productsElement = document.querySelector("#products");
    const totalElement = document.querySelector("#cart-total");

    // DOM’ga mahsulot kartalarini chiqarish.
    function renderProducts() {
      productsElement.innerHTML = products.map((product) => `
        <article>
          <h2>${product.name}</h2>
          <p>${product.price.toLocaleString("uz-UZ")} so‘m</p>
          <button data-id="${product.id}">Savatga qo‘shish</button>
        </article>
      `).join("");
    }

    function renderTotal() {
      const total = cart.reduce((sum, product) => sum + product.price, 0);
      totalElement.textContent = `Savat: ${total.toLocaleString("uz-UZ")} so‘m`;
    }

    productsElement.addEventListener("click", (event) => {
      const productId = Number(event.target.dataset.id);

      if (!productId) return;

      const product = products.find((item) => item.id === productId);
      cart.push(product);
      renderTotal();
    });

    // Backendga ma’lumot yuborish namunasi.
    async function sendOrder() {
      const response = await fetch("/api/orders", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-Telegram-Init-Data": window.Telegram?.WebApp?.initData ?? "",
        },
        body: JSON.stringify({ product_ids: cart.map((product) => product.id) }),
      });

      const result = await response.json();
      console.log(result);
    }

    renderProducts();
    renderTotal();
  </script>

  <!--
  BUGUNGI DARSDA:
    ✔️ const, array va object
    ✔️ function va event listener
    ✔️ DOM: querySelector va innerHTML
    ✔️ map, find, reduce
    ✔️ fetch orqali API ga POST so‘rov

  MUSTAQIL MASHQ:
    1. Savatdan mahsulot o‘chirish tugmasini qo‘shing.
    2. Miqdorni oshirish/kamaytirish funksiyasini yozing.
    3. Savatni localStorage’da saqlang.
    4. fetch xatosini try/catch bilan boshqaring.
  -->
</body>
</html>
