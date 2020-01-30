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
            await msg.delete()

        if msg.content.endswith('leave') and bot.is_in_vc:
            await bot.voice.disconnect()
            reply = f"{msg.author.mention} 退室しました\n"
            print(reply)
            await msg.channel.send(reply)
            await msg.delete()
