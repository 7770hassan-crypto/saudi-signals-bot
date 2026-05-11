import asyncio
import yfinance as yf
from telegram import Bot
from config import TOKEN, CHAT_ID
from strategy import signal
from stocks import stocks
from datetime import datetime

bot = Bot(token=TOKEN)

async def run():
    while True:
        for stock in stocks:

            data = yf.download(stock + ".SR", period="5d", interval="1d")

            if data.empty:
                continue

            result = signal(data)

            if result:
                text = f"""
📊 إشارة جديدة

📅 {datetime.now().date()}
📈 السهم: {stock}
💰 الدخول: {result['entry']}
🎯 TP1: {result['tp1']}
🎯 TP2: {result['tp2']}
🛑 SL: {result['sl']}
"""

                await bot.send_message(chat_id=CHAT_ID, text=text)

        await asyncio.sleep(3600)

asyncio.run(run())
