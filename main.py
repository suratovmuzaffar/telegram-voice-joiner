from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, GetFullChannelRequest
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact

api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
phone = '+998XXYYYYYYY'  # Telefon raqamingiz

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)

    # Guruh username yoki link (faqat username qismi)
    group_username = '@BRAWL_STARS_AKKAUNT_SAVDO_UZ1'  # Masalan: 'mygroup'

    # Guruhni olish
    group = await client.get_entity(group_username)

    # Userni qo‘shish (raqam orqali kontakt sifatida)
    contact = InputPhoneContact(client_id=0, phone='+998ZZZZZZZZZ', first_name='Name', last_name='')

    result = await client(ImportContactsRequest([contact]))
    user = result.users[0]

    # Kanalga (yoki megagroup) qo‘shish
    await client(InviteToChannelRequest(
        channel=group,
        users=[user]
    ))

with client:
    client.loop.run_until_complete(main())
