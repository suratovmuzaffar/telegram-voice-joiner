
from telethon import TelegramClient
import asyncio

api_id = 23892150
api_hash = 'c7582ccfdb35aaadfe4224e3d73d5d66'
session_name = 'session_name'  # session fayl nomi (extensionsiz)

async def main():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start()
    print("Bot ishga tushdi!")

    # Guruhlar ro'yxatini oling
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if dialog.is_group or dialog.is_channel:
            print(f"Kirildi: {dialog.name} ({dialog.id})")

    # Barcha guruhlar videochatiga ovozsiz kirish
    for dialog in dialogs:
        if dialog.is_group or dialog.is_channel:
            try:
                await client.send(
                    client.tl.functions.channels.GetFullChannelRequest(channel=dialog.entity)
                )
                await client(functions.channels.JoinChannelRequest(dialog.entity))
                await client(functions.channels.EditAdminRequest(
                    channel=dialog.entity,
                    user_id='me',
                    admin_rights=client.tl.types.ChatAdminRights(
                        change_info=False,
                        post_messages=False,
                        edit_messages=False,
                        delete_messages=False,
                        ban_users=False,
                        invite_users=False,
                        pin_messages=False,
                        add_admins=False
                    ),
                    rank='Bot'
                ))
                print(f"Videochatga kirildi: {dialog.name}")
            except Exception as e:
                print(f"Error: {dialog.name} -> {str(e)}")

    await client.run_until_disconnected()

asyncio.run(main())
