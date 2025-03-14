import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

# Bot tokeni va kanal ID
BOT_TOKEN = "8045139770:AAHUhUrFWxy7MVZsdpCrk_BkBz3umrM-Qcs"
CHANNEL_ID = -1002361380161  

# Bot va dispatcher obyektlari
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Kino ID lug‘ati (Qo‘lda to‘ldirilishi kerak!)
kino_id_lugat = {
    "1234": 2  # 1234 ID – kanal xabarining message_id = 70
}

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("🎬 Qaysi kinoni ko‘rmoqchisiz? ID ni kiriting.")

@dp.message()
async def find_movie(message: Message):
    kino_id = message.text.strip()

    if kino_id in kino_id_lugat:
        post_id = kino_id_lugat[kino_id]
        
        # Xabarni forward qilmasdan, to‘g‘ridan-to‘g‘ri nusxalab jo‘natish
        await bot.copy_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=post_id)
    
    else:
        await message.answer("❌ Bunday ID bilan kino topilmadi. Iltimos, tekshirib qayta kiriting.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def webhook():
    return "Bot ishlayapti!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

