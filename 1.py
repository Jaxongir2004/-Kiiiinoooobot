import asyncio
from flask import Flask, request
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

# Bot tokeni va kanal ID
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = -1002361380161  
WEBHOOK_URL = "https://your-app-name.onrender.com/webhook"

# Flask server yaratish
app = Flask(__name__)

# Bot va Dispatcher obyektlari
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Kino ID lug‘ati
kino_id_lugat = {
    "1234": 2
}

@app.route("/webhook", methods=["POST"])
async def receive_update():
    update = types.Update(**request.json)
    await dp._process_update(update)
    return "OK", 200

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("🎬 Qaysi kinoni ko‘rmoqchisiz? ID ni kiriting.")

@dp.message()
async def find_movie(message: Message):
    kino_id = message.text.strip()

    if kino_id in kino_id_lugat:
        post_id = kino_id_lugat[kino_id]
        await bot.forward_message(message.chat.id, CHANNEL_ID, post_id)
    else:
        await message.answer("❌ Bunday ID bilan kino topilmadi. Iltimos, tekshirib qayta kiriting.")

async def main():
    await bot.set_webhook(WEBHOOK_URL)
    await dp.start_polling(bot)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling(bot))
    app.run(host="0.0.0.0", port=10000)
