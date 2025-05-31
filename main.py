from telethon import TelegramClient
import asyncio

api_id = 23892150
api_hash = 'c7582ccfdb35aaadfe4224e3d73d5d66'
phone = '+998333439909'  # Telefon raqamingizni kiriting

client = TelegramClient('session', api_id, api_hash)

async def main():
    await client.start(phone)

    print("Sizning guruhlaringiz ro'yxati:")
    dialogs = await client.get_dialogs()

    for dialog in dialogs:
        if dialog.is_group or dialog.is_channel:
            # Faqat guruh va kanallarni chiqaramiz
            print(f"- {dialog.name} (ID: {dialog.id})")

    print("Ro'yxat chiqarildi.")

with client:
    client.loop.run_until_complete(main())
