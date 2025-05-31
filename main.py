import os
from telethon import TelegramClient
from telethon.tl.functions.phone import JoinGroupCallRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone = os.getenv("PHONE_NUMBER")

client = TelegramClient("session", api_id, api_hash)

async def join_voice_chats():
    await client.start(phone=phone)

    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if dialog.is_group or dialog.is_channel:
            try:
                entity = await client.get_entity(dialog.id)
                full = await client(GetFullChannelRequest(entity))

                if full.full_chat.call:
                    call = full.full_chat.call
                    await client(JoinGroupCallRequest(call=call, params={}))
                    print(f"✅ Joined call in {dialog.name}")
            except Exception as e:
                print(f"❌ {dialog.name} - Error: {e}")

with client:
    client.loop.run_until_complete(join_voice_chats())
