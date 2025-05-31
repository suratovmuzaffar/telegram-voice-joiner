from telethon import TelegramClient

api_id = 23892150
api_hash = 'c7582ccfdb35aaadfe4224e3d73d5d66'
phone = '++998333439909'  # Telefon raqamingizni kiriting

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)
    print("Sessiya yaratildi va Telegramga ulandingiz!")

with client:
    client.loop.run_until_complete(main())
