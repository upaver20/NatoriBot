import discord
import os
from NatoriBot.vc_access import vc_access
from NatoriBot.response import voice_response
from NatoriBot.reaction import reaction

client = discord.Client()

if not discord.opus.is_loaded():
    discord.opus.load_opus('heroku-buildpack-libopus')


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
        if client.user in message.mentions:
            await vc_access(message, client)
        elif message.content != "":
            await voice_response(message, client)
        else:
            return


@client.event
async def on_raw_reaction_add(payload):
    msg_id = payload.message_id
    channel_id = payload.channel_id
    if channel_id != int(os.environ['CHANNEL_ID']):
        return
    else:
        channel = await client.fetch_channel(channel_id)
        message = await channel.fetch_message(msg_id)
        reaction(client, message)
        return


client.run(os.environ['TOKEN'], reconnect=False)
