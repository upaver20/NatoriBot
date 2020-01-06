import discord
import os
from NatoriBot.vc_access import vc_access
from NatoriBot.response import voice_response

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel_id = int(os.environ['CHANNEL_ID'])
    channel = client.get_channel(channel_id)
    await channel.send(content="おはようござい🍆")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == int(os.environ['CHANNEL_ID']):
       #  bot = vc_wrapper(client.voice_clients)
        if client.user in message.mentions:
            await vc_access(message, client)
        elif message.content != "":
            await voice_response(message, client)

client.run(os.environ['TOKEN'])
