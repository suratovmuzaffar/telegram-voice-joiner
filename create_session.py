from telethon.sync import TelegramClient

api_id = 23892150
api_hash = 'c7582ccfdb35aaadfe4224e3d73d5d66'
phone = '+998333439909'  # O'z raqamingiz

client = TelegramClient('session_name', api_id, api_hash)
client.start(phone)
print("✅ Session fayli yaratildi!")
