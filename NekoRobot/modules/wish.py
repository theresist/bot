import random

from telethon import events

from NekoRobot import tbot as neko


@neko.on(events.NewMessage(pattern="/wish ?(.*)"))
async def wish(e):
    if e.is_reply:
        mm = random.randint(1, 100)
        lol = await e.get_reply_message()
        fire = "https://te.legra.ph/file/7c0556c8629ba25374b00.jpg"
        await neko.send_file(
            e.chat_id,
            fire,
            caption=f"**ʜᴇʏ [{e.sender.first_name}](tg://user?id={e.sender.id}), ʏᴏᴜʀ ᴡɪsʜ ʜᴀs ʙᴇᴇɴ ᴄᴀsᴛ 🖤**\n\n__chance of success {mm}%__",
            reply_to=lol,
        )
    if not e.is_reply:
        mm = random.randint(1, 100)
        fire = "https://te.legra.ph/file/7c0556c8629ba25374b00.jpg"
        await neko.send_file(
            e.chat_id,
            fire,
            caption=f"**ʜᴇʏ [{e.sender.first_name}](tg://user?id={e.sender.id}), ʏᴏᴜʀ ᴡɪsʜ ʜᴀs ʙᴇᴇɴ ᴄᴀsᴛ 🖤**\n\n__chance of success {mm}%__",
            reply_to=e,
        )
