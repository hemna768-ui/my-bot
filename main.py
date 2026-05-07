import os
from pyrogram import Client

# وەرگرتنی زانیارییەکان لە سێرڤەر
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message()
async def hello(client, message):
    await message.reply_text("سڵاو! بۆتەکەت بە سەرکەوتوویی کار دەکات.")

print("بۆتەکە ئێستا ئامادەیە...")
app.run()
