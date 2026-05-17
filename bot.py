import asyncio
import yfinance as yf

from telegram import Bot

from datetime import datetime
from zoneinfo import ZoneInfo

from config import TOKEN, CHAT_ID
from strategy import score_stock
from stocks import stocks

bot = Bot(token=TOKEN)

# ⏰ وقت السوق السعودي
MARKET_START = 10
MARKET_END = 15

# 📅 أيام التداول
# الأحد=6 | الاثنين=0 | الثلاثاء=1 | الأربعاء=2 | الخميس=3
TRADING_DAYS = [6, 0, 1, 2, 3]

async def run():

    while True:

        # 🇸🇦 توقيت السعودية الحقيقي
        now = datetime.now(ZoneInfo("Asia/Riyadh"))

        current_hour = now.hour
        current_day = now.weekday()

        # 🚫 السوق مغلق
        if (
            current_day not in TRADING_DAYS
            or current_hour < MARKET_START
            or current_hour >= MARKET_END
        ):

            print("السوق السعودي مغلق")

            # ⏳ انتظر 30 دقيقة
            await asyncio.sleep(1800)
            continue

        # 🔥 السوق مفتوح
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

        # ⏳ تحديث كل 5 دقائق
        await asyncio.sleep(300)

asyncio.run(run())
 
