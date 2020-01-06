import discord
from NatoriBot.Sanabutton2Parser import Sanabutton2Parser
from NatoriBot.downloader import download
from NatoriBot.vc_wrapper import vc_wrapper

async def voice_response(message, client):
    msg = message
    bot = vc_wrapper(client)
    urls = Sanabutton2Parser(msg)
    if urls == None:
        reply = f"{msg.author.mention} {message.content}は見つかりませんでした"
    else:
        reply = f"{msg.author.mention} \n 検索語句: {urls['msg']}\n アーカイブ: {urls['archive_url']}　\n ボタン: {urls['button_url']}"
    await msg.channel.send(reply)
    if bot.is_in_vc:
        if bot.voice.is_connected() and not bot.voice.is_playing() :
            download(urls['button_url'])
            source = discord.FFmpegPCMAudio("button.mp3")
            bot.voice.play(source)
