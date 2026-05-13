import asyncio
import yfinance as yf
from telegram import Bot
from config import TOKEN, CHAT_ID
from strategy import score_stock
from stocks import stocks

bot = Bot(token=TOKEN)

async def run():

    await bot.send_message(
        chat_id=CHAT_ID,
        text="✅ البوت شغال الآن ويبحث عن أفضل الفرص"
    )

    best_stock = None
    best_score = 0

    while True:

        best_stock = None
        best_score = 0

        for stock in stocks:

            try:
                data = yf.download(
                    stock,
                    period="5d",
                    interval="1h",
                    progress=False
                )

                score = score_stock(data)

                if score and score > best_score:
                    best_score = score
                    best_stock = stock

            except Exception as e:
                print(f"{stock} Error: {e}")

        # 🔥 إرسال أفضل سهم فقط
        if best_stock:

            message = f"""
🔥 أفضل سهم الآن

📊 السهم: {best_stock}
⭐ القوة: {best_score}

📈 فرصة محتملة قوية في السوق
"""

            await bot.send_message(
                chat_id=CHAT_ID,
                text=message
            )

        await asyncio.sleep(300)

asyncio.run(run())
