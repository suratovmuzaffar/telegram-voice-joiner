import asyncio
from telethon import TelegramClient
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.stream import StreamAudioEnded

api_id = 23892150
api_hash = 'c7582ccfdb35aaadfe4224e3d73d5d66'

client = TelegramClient('session_name', api_id, api_hash)
pytg = PyTgCalls(client)

# Guruhlar ro‘yxati
groups = [
    'OXIDE_SURVIVAL_AKKAUNT_SAVDO_UZ1',
    'BRAWL_STARS_AKKAUNT_SAVDO_UZ1',
    'CLASH_OF_CLANS_AKKAUNT_SAVDO_UZ1',
    'EFOOTBALL_AKKAUNT_SAVDO_UZ1',
    'PUBG_MOBILE_AKKAUNT_SAVDO_UZ1',
]

async def main():
    await client.start()
    await pytg.start()

    for group in groups:
        chat = await client.get_entity(group)
        try:
            await pytg.join_group_call(
                chat.id,
                InputAudioStream(
                    file_path='silent.mp3',  # ovozsiz fayl
                ),
                muted=True
            )
            print(f"✅ Videochatga kirildi: {group}")
        except Exception as e:
            print(f"❌ {group} uchun xatolik: {e}")

    # Doimiy ishlashi uchun
    await asyncio.get_event_loop().create_future()

with client:
    client.loop.run_until_complete(main())
