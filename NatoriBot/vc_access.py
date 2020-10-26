import discord
from NatoriBot.vc_wrapper import vc_wrapper


async def vc_access(message, client):
    msg = message
    bot = vc_wrapper(client)
    if msg.author.voice is not None:
        if msg.content.endswith('join') and not bot.is_in_vc:
            await msg.author.voice.channel.connect()
            reply = f"{msg.author.mention} 入室しました\n"
            print(reply)
            await msg.channel.send(reply)

        if msg.content.endswith('leave') and bot.is_in_vc:
            await bot.voice.disconnect()
            reply = f"{msg.author.mention} 退室しました\n"
            print(reply)
            await msg.channel.send(reply)

        if msg.content.endswith('help'):
            reply = \
                f"さなボタン(2)様にある音声をDiscordに流すBotです．\n"\
                f"<https://www.natorisana.love/>\n"\
                f"\n"\
                f"使い方：\n"\
                f"あなたがいるボイスチャンネルに入室します．\n"\
                f"```@{client.user} join```\n"\
                f"ボイスチャンネルから退室します．\n"\
                f"```@{client.user} leave```\n"\
                f"検索結果からランダムに音声を再生します．\n"\
                f"```任意の文字列```\n"\
                f"これです．\n"\
                f"```@{client.user} help```"

            print(reply)
            await msg.channel.send(reply)

        await msg.delete()

    return
