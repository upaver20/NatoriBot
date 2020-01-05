import discord
import os
import Sanabutton2Parser

client = discord.Client()
voice_client = ""

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel_id = int(os.environ['LOG_CHANNEL_ID'])
    channel = client.get_channel(channel_id)
    print(channel)
    await channel.send(content="おはようござい🍆")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.channel.id == int(os.environ['LOG_CHANNEL_ID']):
        if client.user in message.mentions:
            reply = f'{message.author.mention} 呼んだ？'
            await message.channel.send(reply)
            if message.author.voice != None:
                if message.content.endswith('join'):
                    await message.author.voice.channel.connect()
                if message.content.endswith('leave'):
                    await message.guild.voice_client.disconnect()
        else:
            url = Sanabutton2Parser.Sanabutton2Parser(message.content)
            await message.channel.send(url)




client.run(os.environ['TOKEN'])
