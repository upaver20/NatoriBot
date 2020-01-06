import discord
from NatoriBot.Sanabutton2Parser import Sanabutton2Parser
from NatoriBot.downloader import download
from NatoriBot.vc_wrapper import vc_wrapper

async def voice_response(message, client):
    msg = message
    bot = vc_wrapper(client)
    url = Sanabutton2Parser(msg.content)
    reply = f'{msg.author.mention} {url}'
    await msg.channel.send(reply)
    if bot.is_in_vc:
        if bot.voice.is_connected() and not bot.voice.is_playing() :
            download(url)
            source = discord.FFmpegPCMAudio("button.mp3")
            bot.voice.play(source)
