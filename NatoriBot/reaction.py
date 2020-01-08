import discord
from NatoriBot.response import say_in_vc
from NatoriBot.vc_wrapper import vc_wrapper
import re

def reaction(client, message):
    bot = vc_wrapper(client)
    pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    url_list = re.findall(pattern, message.content)
    # print(url_list)
    if url_list == [] or len(url_list) < 2:
        return
    elif url_list[1].startswith('https://www.natorisana.love/'):
        url = url_list[1]
        if bot.is_in_vc:
            say_in_vc(url, bot)
        else:
            return
    else:
        return
