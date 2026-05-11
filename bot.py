import asyncio
from telegram import Bot
from config import TOKEN, CHAT_ID

bot = Bot(token=TOKEN)

async def main():
    while True:
        await bot.send_message(
            chat_id=CHAT_ID,
            text="البوت شغال الآن ✅"
        )
        await asyncio.sleep(60)

asyncio.run(main())
