from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("details"))
async def details(bot, message): 
    await message.reply_text(
        text=f"""
