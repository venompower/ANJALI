import math
from config import SUPPORT_CHAT, OWNER_USERNAME
from pyrogram.types import InlineKeyboardButton
from ANJALIMUSIC import app
import config
from ANJALIMUSIC.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 200
    umm = math.floor(percentage)
    if 0 < umm <= 14:
        bar = "🅜︎—————————————"
    elif 14 < umm < 28:
        bar = "🅜︎🅐︎————————————"
    elif 28 <= umm < 42:
        bar = "🅜︎🅐︎🅗︎———————————"
    elif 42 <= umm < 56:
        bar = "🅜︎🅐︎🅗︎🅣︎——————————"
    elif 56 <= umm < 70:
        bar = "🅜︎🅐︎🅗︎🅣︎🅞︎—————————"
    elif 70 <= umm < 84:
        bar = "🅜︎🅐︎🅗︎🅣︎🅞—————————"
    elif 84 <= umm < 98:
        bar = "🅜︎🅐︎🅗︎🅣︎🅞—❤️———————"
    elif 98 <= umm < 112:
        bar = "🅜︎🅐︎🅗︎🅣︎🅞—♥️—🅐︎—————"
    elif 112 <= umm < 126:
        bar = "🅜︎🅐︎🅗︎🅣︎🅞—❤️—🅐︎🅝︎————"
    elif 126 <= umm < 140:
        bar = "🅜︎🅐︎🅗︎🅣︎🅞—❤️—🅐︎🅝︎🅙︎︎———"
    elif 140 <= umm < 164:
        bar = "🅜︎🅐︎🅗︎🅣︎🅞—❤️—🅐︎🅝︎🅙︎🅐︎——"
    elif 164 <= umm < 178:    
        bar = "🅜︎🅐︎🅗︎🅣︎🅞—❤️—🅐︎🅝︎🅙︎🅐︎🅛︎—"
    else: 
        bar = "🅜︎🅐︎🅗︎🅣︎🅞—♥️—🅐︎🅝︎🅙︎🅐︎🅛︎🅘︎"
    buttons = [
         
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
          [
            InlineKeyboardButton(
                text="✰ 𝖡ᴧ፝֠֩ʙꭎ ✰", url="https://t.me/Zhangweii",
            ),
            InlineKeyboardButton(
                text="✰ 𝛅ᴏ፝֠֩𝛈ᴧ ✰", url="https://t.me/AnjaliOwnerBot",
            )
        ],
          [ InlineKeyboardButton(text="✰ ᴍᴀ፝֩֠֠֩sᴛɪ ᴋɪ ʙᴀ፝֠֩֠֩sᴛɪ ✰", url=f"https://t.me/+b1gc4qrvfLZlNGI1")],
          [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons

def stream_markup(_, chat_id):
    buttons = [
        
         [
            InlineKeyboardButton(
                text="✰ 𝖡ᴧ፝֠֩ʙꭎ ✰", url="https://t.me/Zhangweii",
            ),
            InlineKeyboardButton(
                text="✰ 𝛅ᴏ፝֠֩𝛈ᴧ ✰", url="https://t.me/AnjaliOwnerBot",
            )
        ],
          [ InlineKeyboardButton(text="✰ ᴍᴀ፝֩֠֠֩sᴛɪ ᴋɪ ʙᴀ፝֠֩֠֩sᴛɪ ✰", url=f"https://t.me/+b1gc4qrvfLZlNGI1")],
          [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
