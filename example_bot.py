import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel_id = int(os.environ['LOG_CHANNEL_ID'])
    channel = client.get_channel(channel_id)
    print(channel)
    await channel.send(content="おはようござい🍆")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.environ['TOKEN'])
