import discord
from NatoriBot.Sanabutton2Parser import Sanabutton2Parser
from NatoriBot.downloader import download
from NatoriBot.vc_wrapper import vc_wrapper

async def voice_response(message, client):
    msg = message
    bot = vc_wrapper(client)
    urls = Sanabutton2Parser(msg.content)
    if urls == None:
        reply = f"{msg.author.mention} {msg.content}は見つかりませんでした"
        return
    else:
        reply = f"{msg.author.mention} \n 検索語句: {urls['msg']}\n アーカイブ: {urls['archive_url']}　\n ボタン: {urls['button_url']}"
    await msg.channel.send(reply)
    await msg.delete()
    if bot.voice.is_connected() and not bot.voice.is_playing() and bot.is_in_vc:
        download(urls['button_url'])
        source = discord.FFmpegPCMAudio("button.mp3")
        bot.voice.play(source)
    else:
        return
