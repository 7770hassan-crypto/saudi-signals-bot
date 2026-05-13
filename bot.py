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
        text="🔍 البوت يفحص السوق الآن..."
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

    # 🔥 ترتيب أفضل الأسهم
    candidates.sort(key=lambda x: x[1], reverse=True)

    top3 = candidates[:3]

    if top3:

        msg = "🔥 أفضل الفرص الآن قبل إغلاق السوق\n\n"

        for i, (stock, score) in enumerate(top3, 1):
            msg += f"{i}- {stock} | القوة: {score}\n"

        msg += "\n📊 إشارات لحظية مبنية على الاختراق والزخم"

        await bot.send_message(
            chat_id=CHAT_ID,
            text=msg
        )

    else:

        await bot.send_message(
            chat_id=CHAT_ID,
            text="🟡 لا توجد فرص قوية حالياً في السوق"
        )

asyncio.run(run())
