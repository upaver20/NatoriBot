import discord
from NatoriBot.Sanabutton2Parser import Sanabutton2Parser
from NatoriBot.downloader import download
from NatoriBot.vc_wrapper import vc_wrapper


async def voice_response(message, client):
    msg = message
    bot = vc_wrapper(client)
    urls = Sanabutton2Parser(msg.content)
    if urls is None:
        reply = f"{msg.author.mention} {msg.content}は見つかりませんでした"
        print(reply)
        await msg.channel.send(reply)
    else:
        reply = f"{msg.author.mention} \n"\
                f"検索語句: {urls['msg']}\n"\
                f"アーカイブ: {urls['archive_url']}\n"\
                f"ボタン: {urls['button_url']}"
        print(reply)
        await msg.channel.send(reply)
        if bot.is_in_vc:
            say_in_vc(urls['button_url'], bot)
            print("Talked!")

    await msg.delete()
    return


def say_in_vc(url, bot):
    if bot.voice.is_connected() and not bot.voice.is_playing():
        download(url)
        source = discord.FFmpegPCMAudio("button.mp3")
        bot.voice.play(source)

    return
