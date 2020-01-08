import discord
from NatoriBot.response import say_in_vc
from NatoriBot.vc_wrapper import vc_wrapper
import re
import urllib.parse

def reaction(client, message):
    msg = message.content
    bot = vc_wrapper(client)
    pattern = "https"
    itr_list = re.finditer(pattern, msg)
    url_list = list(itr_list)

    if url_list == [] or len(url_list) < 2:
        return

    start = list(url_list)[1].span()[0]
    end = len(msg)
    url = msg[start:end]

    if url.startswith('https://www.natorisana.love/') and url.endswith('.mp3') and bot.is_in_vc:
        say_in_vc(url, bot)
    else:
        return
