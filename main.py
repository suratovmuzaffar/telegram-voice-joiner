from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact

api_id = 23892150
api_hash = 'c7582ccfdb35aaadfe4224e3d73d5d66'
phone = '+998XXYYYYYYY'  # Telefon raqamingiz

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)

    # Guruh username (masalan: 'uzbek_chat') - faqat @ dan keyingi qismi
    group_username = 'BRAWL_STARS_CHAT'
    group = await client.get_entity(group_username)

    # Foydalanuvchini telefon raqami orqali kontakt sifatida qo‘shish
    contact = InputPhoneContact(
        client_id=0,
        phone='+998ZZZZZZZZZ',  # Bu foydalanuvchining raqami
        first_name='Name',
        last_name=''
    )
    result = await client(ImportContactsRequest([contact]))
    user = result.users[0]

    # Kanal yoki megagroupga qo‘shish
    await client(InviteToChannelRequest(
        channel=group,
        users=[user]
    ))

with client:
    client.loop.run_until_complete(main())
