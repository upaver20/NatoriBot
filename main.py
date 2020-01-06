import discord
import os
import Sanabutton2Parser
import downloader

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
        bot = vc_warapper(client.voice_clients)
        if client.user in message.mentions:
            if message.author.voice != None:
                if message.content.endswith('join') and not bot .is_in_vc:
                    await message.author.voice.channel.connect()
                if message.content.endswith('leave') and bot.is_in_vc:
                    await bot.voice.disconnect()
        elif message.content != "":
            url = Sanabutton2Parser.Sanabutton2Parser(message.content)
            reply = f'{message.author.mention} {url}'
            await message.channel.send(reply)
            if bot.voice.is_connected() and not bot.voice.is_playing():
                downloader.download(url)
                source = discord.FFmpegPCMAudio("button.mp3")
                bot.voice.play(source)

class vc_warapper():
    def __init__(self, voice_clients):
        if voice_clients != []:
            self.voice = voice_clients[0]
            self.is_in_vc = True
        else:
            self.is_in_vc = False

client.run(os.environ['TOKEN'])
