import discord
from NatoriBot.vc_wrapper import vc_wrapper


async def vc_access(message, client):
    msg = message
    bot = vc_wrapper(client)
    if msg.author.voice is not None:
        if msg.content.endswith('join') and not bot.is_in_vc:
            await msg.author.voice.channel.connect()
        if msg.content.endswith('leave') and bot.is_in_vc:
            await bot.voice.disconnect()
