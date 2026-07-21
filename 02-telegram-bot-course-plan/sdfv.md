
# Dars 1. Telegram Bot API va Aiogram bilan tanishish

**Davomiyligi:** 90 daqiqa (1 soat 30 daqiqa)
**Daraja:** Boshlang'ich (Python asoslari — o'zgaruvchilar, funksiyalar, importlar — talab qilinadi)
**Kerakli narsalar:** Kompyuter (Windows/Mac/Linux), internet, Telegram akkaunti, Python 3.10+

## Darsning maqsadi

Dars oxirida talaba quyidagilarga erishadi:

- Telegram Bot API qanday ishlashini (update, message, webhook/polling) tushunadi
- Aiogram nima ekanini va uni boshqa kutubxonalardan nima farq qilishini biladi
- @BotFather yordamida o'zining shaxsiy botini yaratadi
- Loyiha uchun ish muhitini to'g'ri sozlaydi (venv, aiogram, python-dotenv)
- O'zining birinchi ishlaydigan botini — echo botni — yozadi va ishga tushiradi

## Darsning rejasi

| # | Mavzu | Vaqt |
|---|-------|------|
| 1 | Kirish: bot nima va nega kerak | 5 daqiqa |
| 2 | Telegram Bot API qanday ishlaydi | 20 daqiqa |
| 3 | Aiogram nima va nega aynan u | 15 daqiqa |
| 4 | @BotFather orqali bot yaratish | 10 daqiqa |
| 5 | Ish muhitini tayyorlash | 15 daqiqa |
| 6 | Birinchi bot: Echo bot | 20 daqiqa |
| 7 | Xulosa va uyga vazifa | 5 daqiqa |

---

## 1-QISM. Kirish: Bot nima va nega kerak? *(5 daqiqa)*

**Telegram bot** — bu odam o'rniga avtomatik ishlaydigan, xabarlarga javob beradigan va buyruqlarni bajaradigan oddiy dastur. Tashqi ko'rinishidan u xuddi oddiy Telegram foydalanuvchisidek — siz unga yozasiz, u sizga javob qaytaradi. Farqi shundaki, javoblarni odam emas, siz yozgan kod beradi.

Kundalik hayotda botlarni ko'p ko'rgansiz:

- Onlayn-do'kon botlari (mahsulotlarni ko'rsatish, buyurtma qabul qilish)
- Yetkazib berish va taksi xizmatlari botlari
- Bank va to'lov tizimlari botlari (balansni tekshirish, bildirishnomalar)
- Test va o'quv botlari
- Guruh va kanallarni boshqaruvchi (moderatsiya) botlar
- Yangiliklar va ob-havo botlari

**Nega aynan Telegram?**

- API'si ochiq, bepul va hujjatlari yaxshi yozilgan
- O'rnatish va ishga tushirish juda oson — server ijaraga olmasdan ham (localhost'da) sinab ko'rish mumkin
- O'zbekistonda va butun dunyoda foydalanuvchilar soni juda katta

**Botlarning afzalligi:** ular 24/7 ishlaydi, charchamaydi, bir vaqtning o'zida minglab foydalanuvchiga xizmat ko'rsata oladi va odam qiladigan ko'plab takrorlanuvchi ishlarni avtomatlashtiradi.

> 🤔 **Talabalar bilan muhokama uchun savol:** "Siz kundalik hayotingizda qaysi Telegram botlaridan foydalanasiz? Ular nima qiladi?" — bir necha javobni tinglab, doskaga yozib qo'ying, keyingi qismlarda ularga qaytib turing.

---

## 2-QISM. Telegram Bot API qanday ishlaydi *(20 daqiqa)*

### 2.1. Bot — bu maxsus turdagi Telegram akkaunt

Har bir bot, oddiy foydalanuvchi kabi, o'zining ID raqami va bir martalik maxsus **token**iga ega. Sizning dasturingiz (Python kodi) ushbu token yordamida Telegram serveriga HTTP so'rovlar yuboradi:

```
https://api.telegram.org/bot<TOKEN>/METOD_NOMI
```

Masalan, xabar yuborish uchun `sendMessage` metodiga so'rov yuboriladi. Aiogram bizni bu so'rovlarni qo'lda yozishdan ozod qiladi — biz shunchaki Python funksiyalarini chaqiramiz, kutubxona esa orqa fonda tegishli HTTP so'rovlarni tuzadi.

### 2.2. Update tushunchasi

Botga tegishli **har qanday voqea** — yangi xabar, tugma bosilishi, guruhga qo'shilish, kanalda post o'zgarishi va hokazo — Telegram tomonidan **Update** obyekti sifatida yuboriladi. Update — bu "nimadir sodir bo'ldi" degan xabarnoma, deb tushunish mumkin.

Soddalashtirilgan Update namunasi shunday ko'rinadi:

```json
{
  "update_id": 100000001,
  "message": {
    "message_id": 1,
    "from": {
      "id": 987654321,
      "is_bot": false,
      "first_name": "Aziz",
      "username": "aziz_dev"
    },
    "chat": {
      "id": 987654321,
      "type": "private"
    },
    "date": 1721000000,
    "text": "Salom!"
  }
}
```

Har bir Update ichida qaysi turdagi voqea sodir bo'lganiga qarab turli maydonlar bo'lishi mumkin: `message`, `edited_message`, `callback_query` (tugma bosilganda), `my_chat_member` (botni guruhga qo'shishganda) va boshqalar.

### 2.3. Message obyekti

Eng ko'p ishlatiladigan qism — bu `message`. U quyidagi asosiy ma'lumotlarni o'z ichiga oladi:

| Maydon | Nima uchun kerak |
|---|---|
| `message_id` | Xabarning noyob raqami |
| `from` | Xabarni kim yuborgani (ism, username, ID) |
| `chat` | Qaysi chatda yuborilgani (shaxsiy, guruh, kanal) |
| `date` | Yuborilgan vaqt |
| `text` | Xabar matni |

Aiogram bu JSON'ni avtomatik ravishda qulay Python obyektiga aylantirib beradi — masalan, `message.text`, `message.from_user.full_name` kabi.

### 2.4. Yangilikni olishning ikki yo'li: Polling va Webhook

Bot Telegram serveridan yangi Update'larni ikki xil usulda olishi mumkin.

**Polling (so'rab-so'rab olish):**

```
[Bot]  ---- "Yangilik bormi?" ---->  [Telegram server]
[Bot]  <---- "Ha, mana xabar" ----   [Telegram server]

(bu savol-javob doimiy, masalan har soniyada, takrorlanaveradi)
```

Bot o'zi Telegramga muntazam ravishda "menga yangilik bormi?" deb so'rov yuboradi (`getUpdates` metodi). Bu — xuddi pochta qutingizni har kuni o'zingiz borib tekshirib turishga o'xshaydi.

**Webhook (o'zi xabar berish):**

```
[Foydalanuvchi xabar yozadi] --> [Telegram server]
[Telegram server] -- POST so'rov --> [Sizning server manzilingiz: https://sayt.uz/webhook]
```

Bu holatda Telegram serveri o'zi, voqea sodir bo'lishi bilanoq, sizning belgilagan URL manzilingizga so'rov yuboradi. Bu — pochtachi xat kelganda to'g'ridan-to'g'ri eshigingizni qoqishiga o'xshaydi.

**Qaysi birini qachon ishlatish kerak:**

| | Polling | Webhook |
|---|---|---|
| Sozlash qiyinligi | Juda oson | Server, domen va SSL sertifikat talab qiladi |
| Localhost'da ishlaydimi | Ha | Yo'q (ochiq manzil kerak) |
| Katta yuklama uchun | Kamroq samarali | Yaxshiroq samarali |
| Kimlar uchun mos | O'rganish, kichik/o'rta loyihalar | Production, yuqori trafikli botlar |

**Bu kursda biz Polling'dan foydalanamiz** — chunki u sozlashni talab qilmaydi va o'z kompyuteringizda darhol ishga tushirsa bo'ladi. Webhook haqida keyingi darslarda, botni serverga joylashtirish (deploy) mavzusida to'xtalamiz.

---

## 3-QISM. Aiogram nima va nega aynan u? *(15 daqiqa)*

### 3.1. Aiogram — to'liq asinxron framework

**Aiogram** — Python tilida yozilgan, Telegram Bot API bilan ishlash uchun mo'ljallangan, **to'liq asinxron (async)** framework. U `asyncio` va `aiohttp` kutubxonalari asosida qurilgan. Hozirgi kunda Aiogram 3.x versiyasi asosiy versiya hisoblanadi va faol rivojlantirilmoqda.

### 3.2. Asinxron dasturlash haqida qisqacha

Tasavvur qiling: bitta oshpaz (sinxron/**sync**) navbat bilan bitta taomni to'liq tayyorlab bo'lgach, keyingisiga o'tadi — agar bitta taom uzoq pishsa, boshqa mijozlar kutib turishadi.

**Asinxron (async)** yondashuvda esa oshpaz bir taomni o't ustiga qo'yib, u pishayotgan vaqtda boshqa taomga o'tadi, keyin yana birinchisiga qaytadi. Natijada bitta oshpaz bir nechta taomni deyarli bir vaqtda boshqara oladi.

Botlar uchun bu juda muhim: sizning botingizga bir vaqtning o'zida yuzlab, minglab foydalanuvchi xabar yozishi mumkin. Agar bot sinxron ishlasa, u har bir xabarni navbat bilan qayta ishlaydi va foydalanuvchilar javobni kutib qolishadi. Asinxron bot esa bitta xabarni qayta ishlab turgan vaqtda (masalan, bazaga so'rov yuborayotganda) boshqa foydalanuvchilarning xabarlarini ham parallel qayta isha boshlaydi.

Python'da bu `async def` va `await` kalit so'zlari orqali amalga oshiriladi — buni 6-qismdagi kodda amalda ko'ramiz.

### 3.3. Boshqa kutubxonalar bilan solishtirish

Python'da Telegram bot yozish uchun bir nechta mashhur kutubxona mavjud:

| Xususiyat | **Aiogram** | python-telegram-bot | pyTelegramBotAPI (telebot) |
|---|---|---|---|
| Asinxronlik | To'liq async (boshidanoq shunday loyihalangan) | Async (yangi versiyalarida) | Asosan sinxron |
| O'rganish qiyinligi | O'rtacha | O'rtacha–yuqori | Eng past, juda sodda |
| Tuzilishi | Router asosida modulli | Handler'lar asosida | Oddiy, kichik loyihalar uchun |
| Holatlar mashinasi (FSM) | Ichkarida tayyor mavjud | Alohida qo'shimcha orqali | Qo'lda yozish kerak |
| Kimlar uchun mos | Zamonaviy, o'rta va katta loyihalar | Xalqaro, keng qamrovli loyihalar | Tez prototip, juda boshlang'ich daraja |

Har uchalasi ham ishlaydigan, hayotiy loyihalarda qo'llaniladigan kutubxonalar — biri ikkinchisidan "yomon" emas, ular shunchaki turli ehtiyojlar uchun mo'ljallangan.

### 3.4. Nega bu kursda aynan Aiogram?

- Zamonaviy va toza arxitektura (Router tizimi kod ko'p bo'lganda loyihani bo'lim-bo'lim tashkil qilishga yordam beradi)
- Holatlar mashinasi (FSM) o'rnatilgan holda mavjud — ko'p qadamli suhbatlar (masalan, ro'yxatdan o'tish) uchun juda qulay
- Katta va faol jamiyat, sifatli hujjatlar (docs.aiogram.dev)
- Ishlab chiqarish (production) darajasidagi loyihalarda keng qo'llaniladi

---

## 4-QISM. @BotFather orqali bot yaratish *(10 daqiqa)*

**@BotFather** — bu Telegramning o'zi tomonidan yaratilgan rasmiy bot bo'lib, uning yordamida yangi botlar yaratiladi va sozlanadi.

**Amaliy qadamlar:**

1. Telegram'da qidiruv orqali **@BotFather**ni toping va uni oching
2. `/start` buyrug'ini yuboring
3. Yangi bot yaratish uchun `/newbot` buyrug'ini yuboring
4. BotFather botingiz uchun **nom (ism)** so'raydi — bu foydalanuvchilarga ko'rinadigan nom, masalan: `Mening Birinchi Botim`
5. Keyin **username** so'raladi — bu noyob bo'lishi va albatta `bot` bilan tugashi kerak, masalan: `mening_birinchi_bot` yoki `mening_birinchi_bot_uz`
6. Muvaffaqiyatli yaratilgach, BotFather sizga maxsus **token** beradi — u taxminan shunday ko'rinishda bo'ladi:

```
123456789:AAHk8x7QvN2eR-Fake_Example_Token_Uchun
```

> ⚠️ **Muhim xavfsizlik qoidasi:** Token — bu botingizning "paroli". Uni hech kimga bermang, GitHub'ga ochiq repozitoriyga yuklamang, skrinshotlarda ko'rsatmang. Token kimningdir qo'liga tushsa, u sizning botingiz nomidan to'liq boshqaruv qila oladi. Agar token oshkor bo'lib qolgan bo'lsa, BotFather'dagi `/revoke` buyrug'i orqali uni bekor qilib, yangisini olish mumkin.

**Qo'shimcha sozlashlar (ixtiyoriy, lekin tavsiya etiladi):**

- `/setdescription` — bot Telegram qidiruvida ko'rinadigan tavsifni belgilash
- `/setabouttext` — botning profilidagi "Haqida" matni
- `/setuserpic` — botga rasm (avatar) qo'yish

> 🤔 **Amaliyot:** Har bir talaba shu daqiqada o'z botini yaratsin va tokenni vaqtincha biror joyga (masalan, matn muharririga) yozib qo'ysin — u keyingi qismda kerak bo'ladi.

---

## 5-QISM. Ish muhitini tayyorlash *(15 daqiqa)*

### 5.1. Python borligini tekshirish

Terminal (Windows'da CMD/PowerShell, Mac/Linux'da Terminal) oching va tekshiring:

```bash
python --version
# yoki, ba'zi tizimlarda:
python3 --version
```

Natija `Python 3.10` yoki undan yuqori bo'lishi kerak.

### 5.2. Loyiha papkasini yaratish

```bash
mkdir birinchi_bot
cd birinchi_bot
```

### 5.3. Virtual muhit (venv) yaratish

**Nega venv kerak?** Har bir Python loyihasi ko'pincha turli kutubxona versiyalaridan foydalanadi. Agar barcha kutubxonalar kompyuterga "umumiy" o'rnatilsa, loyihalar bir-biriga zid kelib qolishi mumkin. Virtual muhit — bu har bir loyiha uchun alohida, izolyatsiyalangan "quti" yaratadi.

**Windows uchun:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux uchun:**

```bash
python3 -m venv venv
source venv/bin/activate
```

Muvaffaqiyatli faollashsa, terminal qatorining boshida `(venv)` degan yozuv paydo bo'ladi — bu venv faol ekanligining belgisi.

### 5.4. Aiogram'ni o'rnatish

```bash
pip install aiogram
```

Bu buyruq Aiogram'ning eng so'nggi 3.x versiyasini (hozircha 3.29 atrofida) o'rnatadi.

### 5.5. python-dotenv — tokenni xavfsiz saqlash

Tokenni to'g'ridan-to'g'ri kod ichiga yozish yomon amaliyot hisoblanadi — chunki kodni GitHub'ga yuklaganingizda token ham oshkor bo'lib qoladi. Buning o'rniga token alohida `.env` faylida saqlanadi, kod esa uni shu fayldan o'qiydi.

```bash
pip install python-dotenv
```

Loyiha papkasida `.env` nomli fayl yarating (nuqtadan boshlanadi, kengaytmasiz) va ichiga shunday yozing:

```env
BOT_TOKEN=123456789:AAHk8x7QvN2eR-Fake_Example_Token_Uchun
```

> 💡 **Maslahat:** Agar loyihani Git orqali boshqarsangiz, `.gitignore` fayliga `.env` qatorini albatta qo'shing — shunda token tasodifan ochiq repozitoriyga yuklanib qolmaydi.

### 5.6. Loyiha tuzilishi

Shu bosqichda loyiha papkangiz taxminan shunday ko'rinishga ega bo'lishi kerak:

```
birinchi_bot/
├── venv/           <- virtual muhit (avtomatik yaratilgan)
├── .env            <- token shu yerda saqlanadi
├── .gitignore      <- (ixtiyoriy, .env shu yerda ko'rsatiladi)
└── bot.py          <- botning asosiy kodi (hozir yaratamiz)
```

---

## 6-QISM. Birinchi oddiy bot: Echo bot *(20 daqiqa)*

Endi eng qiziqarli qismga — o'z botimizni yozishga o'tamiz. **Echo bot** — foydalanuvchi yuborgan har qanday matnni aynan o'zi qaytarib beradigan eng sodda bot turi. U Aiogram asoslarini o'rganish uchun ideal boshlang'ich nuqta.

Loyiha papkasida `bot.py` faylini yarating va quyidagi kodni yozing:

```python
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

# .env faylidagi o'zgaruvchilarni yuklaymiz
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Loglarni yoqamiz — terminalda nima bo'layotganini ko'rish uchun foydali
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher obyektlarini yaratamiz
bot = Bot(token=TOKEN)
dp = Dispatcher()


# /start buyrug'i yuborilganda ishlaydigan handler
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Salom, {message.from_user.full_name}! 👋\n"
        f"Men — echo botman. Menga istalgan xabarni yuboring, "
        f"men uni aynan shu ko'rinishda qaytaraman."
    )


# Qolgan barcha matnli xabarlarga javob beruvchi handler (echo)
@dp.message()
async def echo_handler(message: Message):
    await message.answer(message.text)


# Botni ishga tushirish
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
```

### Kod nimalardan iborat — qadam-baqadam tushuntirish

- **`load_dotenv()` va `os.getenv("BOT_TOKEN")`** — `.env` faylidan tokenni xavfsiz tarzda o'qib oladi
- **`bot = Bot(token=TOKEN)`** — Telegram bilan aloqa qiluvchi asosiy obyekt
- **`dp = Dispatcher()`** — kelgan Update'larni tegishli handler'larga yo'naltiruvchi "dispetcher"
- **`@dp.message(CommandStart())`** — bu handler faqat `/start` buyrug'i kelganda ishga tushadi
- **`@dp.message()`** — filtersiz handler, ya'ni filtrlanmagan qolgan barcha matnli xabarlarni ushlab qoladi
- **`async def` va `await`** — bu funksiyalar asinxron ekanligini bildiradi (3-qismda muhokama qilgan tushuncha)
- **`dp.start_polling(bot)`** — botni Polling rejimida ishga tushiradi (2-qismda ko'rgan usul)

> ⚠️ **Muhim:** Handler'lar ro'yxatdan o'tkazilgan tartibda tekshiriladi. Shuning uchun aniq filtrli handler'lar (`CommandStart()` kabi) har doim umumiy, filtrsiz handler'dan **oldin** yozilishi kerak — aks holda umumiy handler barcha xabarlarni "birinchi bo'lib" ushlab qolib, `/start` ham oddiy matn sifatida qaytarilib ketadi.

### Botni ishga tushirish

Terminalda (venv faol holatda) quyidagini yozing:

```bash
python bot.py
```

Agar hammasi to'g'ri bo'lsa, terminalda log yozuvlari chiqadi va dastur "muallaq" holatda qoladi — bu bot ishlab turganini bildiradi (to'xtatish uchun `Ctrl+C`).

Endi Telegram'ni oching, o'zingiz yaratgan botni toping, `/start` yuboring — botdan salomlashuv xabari kelishi kerak. Keyin istalgan matn yozib ko'ring — bot uni aynan qaytarib beradi.

### Tez-tez uchraydigan xatolar

| Xato | Sababi va yechimi |
|---|---|
| `ModuleNotFoundError: No module named 'aiogram'` | venv faollashtirilmagan yoki aiogram o'rnatilmagan — `pip install aiogram` ni venv faol holatda qayta bajaring |
| `Unauthorized` / token bilan bog'liq xato | `.env` fayldagi token noto'g'ri nusxalangan yoki bo'sh qolgan bo'lishi mumkin — tokenni qayta tekshiring |
| Bot ishga tushadi, lekin hech qanday javob bermaydi | Boshqa joyda (masalan, boshqa terminalda) shu botning eski nusxasi hali ham ishlab turgan bo'lishi mumkin — bitta bot bir vaqtda faqat bitta joyda Polling qila oladi. Barcha eski jarayonlarni to'xtating |
| `.env` o'qilmayapti, `TOKEN` qiymati `None` | `.env` fayli `bot.py` bilan bir xil papkada emasligi yoki fayl nomi noto'g'ri yozilgani mumkin |

---

## 7-QISM. Xulosa va uyga vazifa *(5 daqiqa)*

### Bugungi darsda o'rgandik:

- ✅ Bot nima va Telegram Bot API Update/Message orqali qanday ishlashi
- ✅ Polling va Webhook o'rtasidagi farq va qachon qaysi birini tanlash
- ✅ Aiogram nima, u asinxron ekanligi va boshqa kutubxonalardan farqi
- ✅ @BotFather orqali shaxsiy bot yaratish va tokenni xavfsiz saqlash
- ✅ venv, aiogram, python-dotenv bilan ish muhitini sozlash
- ✅ Ishlaydigan birinchi botni — echo botni — yozib, ishga tushirdik

### Uyga vazifa

1. Echo botga `/help` buyrug'ini qo'shing — u bosilganda bot nima qila olishi haqida qisqacha ma'lumot chiqarsin
2. Salomlashuv xabarini o'zgartiring — unga foydalanuvchining `username`'ini ham qo'shing (`message.from_user.username`)
3. **(Qo'shimcha, murakkabroq)**: Bot faqat matnni qaytarish o'rniga, uni katta harflarga o'girib qaytaradigan qilib o'zgartiring (`message.text.upper()`)

### Keyingi darsda

Keyingi darsda handler'lar va filtrlar bilan chuqurroq ishlaymiz — turli buyruqlar, matn shartlari va foydalanuvchi harakatlariga qarab botni "aqlliroq" qilishni o'rganamiz.

---

## Foydali havolalar

- Aiogram rasmiy hujjatlari: https://docs.aiogram.dev
- Telegram Bot API rasmiy hujjatlari: https://core.telegram.org/bots/api
- @BotFather: Telegram ilovasida qidiruv orqali topiladi
