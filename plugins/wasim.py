from pyrogram import Client, filters

@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.message:
     msg = await bot.reply_text("jdbdvdvvdvfvdvdvdv")
    else:
