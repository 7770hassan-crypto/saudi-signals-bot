import asyncio
import yfinance as yf
from telegram import Bot
from config import TOKEN, CHAT_ID
from strategy import signal
from stocks import stocks

bot = Bot(token=TOKEN)

async def run():

    # ✅ رسالة تشغيل
    await bot.send_message(
        chat_id=CHAT_ID,
        text="✅ البوت شغال الآن ويبحث عن الفرص"
    )

    while True:

        for stock in stocks:

            try:
                data = yf.download(
                    stock,
                    period="5d",
                    interval="1h",
                    progress=False
                )

                result = signal(data)

                if result:

                    text = f"""
🔥 إشارة جديدة

📊 السهم: {stock}
📈 النوع: {result['type']}

💰 سعر الدخول: {result['entry']}

🎯 الهدف الأول: {result['tp1']}
🎯 الهدف الثاني: {result['tp2']}

🛑 وقف الخسارة: {result['sl']}
"""

                    await bot.send_message(
                        chat_id=CHAT_ID,
                        text=text
                    )

            except Exception as e:
                print(f"خطأ في {stock}: {e}")

        await asyncio.sleep(300)

asyncio.run(run())
