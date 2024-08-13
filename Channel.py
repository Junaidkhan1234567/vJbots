from pyrogram.types import *

CHANNEL_ID = -1001909796512

@Client.on_message(filters.channel & (filters.media | filters.text))
async def add_button(client, message):
    if message.chat.id == CHANNEL_ID:
        button = InlineKeyboardMarkup(
                [[
                 InlineKeyboardButton(" button name", url="link") 
                ]])
        await message.edit_reply_markup(reply_markup=button)
