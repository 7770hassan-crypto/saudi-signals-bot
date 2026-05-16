import asyncio
import yfinance as yf
from telegram import Bot
from datetime import datetime
from config import TOKEN, CHAT_ID
from strategy import score_stock
from stocks import stocks

bot = Bot(token=TOKEN)

# ⏰ أوقات السوق
MARKET_START = 10
MARKET_END = 15

async def run():

    while True:

        now = datetime.now()

        # 🚫 خارج وقت السوق
        if now.hour < MARKET_START or now.hour >= MARKET_END:

            print("السوق مغلق")

            await asyncio.sleep(1800)
            continue

        # 🔥 داخل وقت السوق
        await bot.send_message(
            chat_id=CHAT_ID,
            text="🔥 نظام السيولة يفحص السوق الآن..."
        )

        candidates = []

        for stock in stocks:

            try:

                data = yf.download(
                    stock,
                    period="5d",
                    interval="30m",
                    progress=False
                )

                if data is None or data.empty:
                    continue

                score = score_stock(data)

                if score:
                    candidates.append((stock, score))

            except Exception as e:
                print(f"{stock} Error: {e}")

        # 📊 ترتيب الأسهم
        candidates.sort(key=lambda x: x[1], reverse=True)

        top3 = candidates[:3]

        if top3:

            msg = "🔥 الأسهم النشطة الآن\n\n"

            for i, (stock, score) in enumerate(top3, 1):
                msg += f"{i}- {stock} | القوة: {score}\n"

            msg += "\n📊 نشاط + سيولة + زخم"

            await bot.send_message(
                chat_id=CHAT_ID,
                text=msg
            )

        else:

            print("السوق هادئ")

        await asyncio.sleep(300)

asyncio.run(run())
 
