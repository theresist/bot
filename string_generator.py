from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    """Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details"""
)
APP_ID = int(input("16201672"))
API_HASH = input("55f85061314c2c0f6edeec9751b90913")
with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
