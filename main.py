from telethon import TelegramClient

api_id = 23892150
api_hash = 'c7582ccfdb35aaadfe4224e3d73d5d66'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.connect()
    if not await client.is_user_authorized():
        print("Sessiya ruxsati yo'q! Avval lokalda sessiya yarating!")
        return

    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if dialog.is_group or dialog.is_channel:
            print(f"- {dialog.name} (ID: {dialog.id})")

with client:
    client.loop.run_until_complete(main())
