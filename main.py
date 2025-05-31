from telethon.sync import TelegramClient
from telethon.tl.functions.phone import CreateGroupCallRequest, JoinGroupCallRequest
from telethon.tl.functions.messages import GetFullChatRequest
import asyncio

api_id = 23892150       # O'zingizni Telegram API ID
api_hash = 'c7582ccfdb35aaadfe4224e3d73d5d66'  # API Hash
phone = '+998333439909'  # O'zingizning raqamingiz

client = TelegramClient('anon', api_id, api_hash)

async def join_calls():
    await client.start(phone=phone)

    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if dialog.is_group:
            try:
                full_chat = await client(GetFullChatRequest(dialog.entity.id))
                if full_chat.full_chat.call:
                    call = full_chat.full_chat.call
                    await client(JoinGroupCallRequest(call=call, params={}))
                    print(f"✅ Joined call in {dialog.name}")
            except Exception as e:
                print(f"❌ {dialog.name} - Error: {e}")

with client:
    client.loop.run_until_complete(join_calls())
