import asyncio
import datetime
import re
from datetime import datetime

from telethon import custom, events

from NekoRobot import tbot as bot
from NekoRobot import tbot as tgbot
from NekoRobot.events import register

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://te.legra.ph/file/8f9df3c46b0ee27ba6ee9.jpg"
file2 = "https://te.legra.ph/file/349cf5ded28be244fbfd4.jpg"
file3 = "https://te.legra.ph/file/97f7c3ddbb17b6a6f5a06.jpg"
file4 = "https://te.legra.ph/file/5561b91b4547a49c09987.jpg"
file5 = "https://te.legra.ph/file/a14904e785a7b1a8f3e84.jpg"
""" =======================CONSTANTS====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    betsy = event.sender.first_name
    button = [[custom.Button.inline("ᴄʟɪᴄᴋ ʜᴇʀᴇ ", data="information")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"ʜᴇʏ {betsy}, ɪ'ᴍ ᴛsᴏ ᴍᴀɴᴀɢᴇʀ\nɪ'ᴍ ᴄʀᴇᴀᴛᴇᴅ ʙʏ [TSO KING](tg://user?id=5686536025)\n♡ Click The Button Below To Get Your Info",
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        NEKO = "ʏᴏᴜʀ  ᴅᴇᴛᴀɪʟs ʙʏ ᴛsᴏ ᴍᴀɴᴀɢᴇʀ \n\n"
        NEKO += f"ғɪʀsᴛ ɴᴀᴍᴇ : {PRO.first_name} \n"
        NEKO += f"ʟᴀsᴛ ɴᴀᴍᴇ : {PRO.last_name}\n"
        NEKO += f"ʏᴏᴜ ʙᴏᴛ : {PRO.bot} \n"
        NEKO += f"ʀᴇsᴛʀɪᴄᴛᴇᴅ : {PRO.restricted} \n"
        NEKO += f"ᴜsᴇʀ ɪᴅ  : {boy}\n"
        NEKO += f"ᴜsᴇʀɴᴀᴍᴇ : {PRO.username}\n"
        await event.answer(NEKO, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__help__ = """
/myinfo: sʜᴏᴡ ʏᴏᴜʀ ɪɴғᴏ ɪɴ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴ
"""

__mod_name__ = "myinfo"
__command_list__ = ["myinfo"]
