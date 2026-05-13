from telegram import Bot
import asyncio

TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

bot = Bot(token=TOKEN)

async def send_test():
    await bot.send_message(
        chat_id=CHAT_ID,
        text=
        "🚀 تنبيه تجريبي من النظام VIP 🚀\n\n"
        "📊 البوت يعمل الآن ويراقب السوق بشكل لحظي\n"
        "⚡ يتم فحص الاختراقات والزخم والسيولة\n"
        "🔥 متابعة الفرص القوية في السوق\n\n"
        "⛔️ للتجربة والاختبار فقط — ليست توصية شراء أو بيع"
    )

asyncio.run(send_test())

