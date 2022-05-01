from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio




@Client.on_message(filters.command("details"))
async def details(bot, message): 
    await message.reply_text(
        text = """
<b>First Name</b> - {message.from_user.first_name}
<b>Last Name</b>  - {message.from_user.last_name}
<b>User Name</b>  - {message.from_user.username}
      <b>ID</b>   - {message.from_user.id}
 <b>Chat ID</b>   - {message.chat.id}
<b>LAST SEEN</b>  - {last_online(from_user)}
<b>USER LINK</b>  - {from_user.mention}"""
        reply_markup=InlineKeyboardMarkup( [[   
        InlineKeyboardButton("🔐CLOSE", callback_data="close_data")
        ]] 
        )          
    )
    
    
@Client.on_callback_query()
async def callback(bot, message):
    if message.data == "details":
        #loading code
        
        reply1 = await message.message.reply_text("L")

        await asyncio.sleep(0.5) 

        reply2 = await reply1.edit("LO")

        await asyncio.sleep(0.5)

        reply3 = await reply2.edit("LOA") 

        await asyncio.sleep(0.5)

        reply4 = await reply3.edit("LOAD")

        await asyncio.sleep(0.5)

        reply5 = await reply4.edit("LOADI") 
        
        await asyncio.sleep(0.5)
        
        reply6 = await reply5.edit("LOADIN") 
        
        await asyncio.sleep(0.5)
        
        reply7 = await reply6.edit("LOADING") 
     
        await asyncio.sleep(0.5)

        await reply7.delete()  
        
        await message.message.edit(  
            text=DETAILS_TXT
            reply_markup=InlineKeyboardMarkup( [[ 
                InlineKeyboardButton("JOIN OUR CHANNEL", url="t.me/Movietymofficial"),
                InlineKeyboardButton("🔙",  callback_data="help")
                ],[
                InlineKeyboardButton("🔐CLOSE",  callback_data="close_data")
                ]] 
                )    
            )
        
        
