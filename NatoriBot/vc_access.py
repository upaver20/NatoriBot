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

        if msg.content.endswith('help') and bot.is_in_vc:
            reply = \
                f"さなボタン(2)様にある音声をDiscordに流すBotです．\n"\
                f"<https://www.natorisana.love/>\n"\
                f"\n"\
                f"使い方：\n"\
                f"`{client.user.mention} join`\n"\
                f"あなたがいるボイスチャンネルに入室します．\n"\
                f"`{client.user.mention} leave`\n"\
                f"ボイスチャンネルから退室します．\n"\
                f"`任意の文字列\n`"\
                f"検索結果からランダムに音声を再生します．\n"\
                f"`{client.user.mention} help`\n"\
                f"これです．"
            print(reply)
            await msg.channel.send(reply)

        await msg.delete()

    return
