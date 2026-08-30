<!doctype html>
<!-- =========================================================
     DARS 19: Telegram WebApp JavaScript API
     Muallif: Isroilov Rustam (Abruisdev)
     ========================================================= -->
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Telegram WebApp API</title>
</head>
<body>
  <h1 id="title">Web App</h1>
  <button id="alert-button">Xabar ko‘rsatish</button>

  <script src="https://telegram.org/js/telegram-web-app.js"></script>
  <script>
    const tg = window.Telegram?.WebApp;

    if (tg) {
      // Mini App tayyorligini Telegram’ga bildirish va ekranni kengaytirish.
      tg.ready();
      tg.expand();

      // initDataUnsafe UI ko‘rsatish uchun qulay, lekin serverda ishonchli emas.
      const user = tg.initDataUnsafe.user;
      document.querySelector("#title").textContent = `Salom, ${user?.first_name ?? "foydalanuvchi"}!`;

      // Telegram Main Button.
      tg.MainButton.setText("Buyurtmani yuborish");
      tg.MainButton.show();
      tg.MainButton.onClick(() => {
        tg.showAlert("Buyurtma backendga yuboriladi.");
      });

      // Telegram Back Button.
      tg.BackButton.show();
      tg.BackButton.onClick(() => {
        tg.showConfirm("Chiqmoqchimisiz?", (confirmed) => {
          if (confirmed) tg.close();
        });
      });
    }

    document.querySelector("#alert-button").addEventListener("click", () => {
      if (tg) {
        tg.showPopup({ title: "Salom", message: "Telegram WebApp API ishlayapti." });
      } else {
        alert("Browser preview rejimi");
      }
    });
  </script>

  <!--
  BUGUNGI DARSDA:
    ✔️ Telegram.WebApp
    ✔️ ready() va expand()
    ✔️ MainButton va BackButton
    ✔️ showAlert, showPopup va showConfirm
    ✔️ initDataUnsafe faqat frontend preview uchun ekanligi

  MUHIM QOIDA:
    user ID yoki username asosida ruxsat berishdan oldin backendda initData’ni validate qiling.
  -->
</body>
</html>
