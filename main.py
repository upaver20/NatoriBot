import discord
import os
import Sanabutton2Parser
import downloader

client = discord.Client()
voice_client = ""

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel_id = int(os.environ['LOG_CHANNEL_ID'])
    channel = client.get_channel(channel_id)
    await channel.send(content="おはようござい🍆")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == int(os.environ['LOG_CHANNEL_ID']):
        if client.user in message.mentions:
            if message.author.voice != None:
                if message.content.endswith('join') and (client.voice_clients == []):
                    await message.author.voice.channel.connect()
                if message.content.endswith('leave') and (client.voice_clients != []):
                    await client.voice_clients[0].disconnect()
        else:
            url = Sanabutton2Parser.Sanabutton2Parser(message.content)
            await message.channel.send(url)
            if client.voice_clients[0].is_connected() and not client.voice_clients[0].is_playing():
                downloader.download(url)
                source = discord.FFmpegPCMAudio("button.mp3")
                client.voice_clients[0].play(source)

client.run(os.environ['TOKEN'])
