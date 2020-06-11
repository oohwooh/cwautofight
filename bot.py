import os
from telethon import TelegramClient, events

# Get values from my.telegram.org
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

client = TelegramClient('session', api_id, api_hash)
client.start()
print('Logged in to telegram!')
pvebot_id = 807376493
chtwrs_id = 408101137


@client.on(events.NewMessage)
async def new_message(event):
    if event.from_id == pvebot_id:
        await event.forward_to(chtwrs_id)
        await event.mark_read()
        print('Forwarding message from PVE bot')
    elif event.from_id == chtwrs_id:
        if event.message.message == "Too late. Action is not available.":
            await event.mark_read()

client.run_until_disconnected()