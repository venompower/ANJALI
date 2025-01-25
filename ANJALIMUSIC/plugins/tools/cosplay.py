import requests
from pyrogram import filters
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.enums import ChatAction
from ANJALIMUSIC import app
from config import BOT_USERNAME

ANJALI = [
    [
        InlineKeyboardButton(text="✙ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✙", url=f"https://t.me/TheAnjaliMusicBot?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="• sᴜᴘᴘᴏʀᴛ •", url=f"https://t.me/ANJALINETWORK"),
    ],
]

@app.on_message(filters.command("cosplay"))
async def cosplay(_,msg):
    img = requests.get("https://waifu-api.vercel.app").json()
    await msg.reply_photo(img, caption=f"❅ ᴄᴏsᴘʟᴀʏ ʙʏ ➠ ᴧᷟ󴺬ηᷣ󴺬ᴊᷤ󴺬ᴧ󴺬ʟ󴺬ɪ󴺬ᥫ᭡፝֟፝֟͞", reply_markup=InlineKeyboardMarkup(ANJALI),)
