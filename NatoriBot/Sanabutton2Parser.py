import random
import json


def Sanabutton2Parser(message):
    msg = message

    baseURL = "https://www.natorisana.love/sounds/"

    posts = json.load(open('data/posts.json', 'r'))

    cond_list = []

    for archive in posts:
        if 'stream_id' in archive.keys():
            for buttons in archive['buttons']:
                for button in buttons:
                    if msg in str(button['value']):
                        match_botton = {
                            "file-name": button['file-name'],
                            "stream_id": archive['stream_id']}
                        cond_list.append(match_botton)

    if cond_list == []:
        return None

    select_button = random.choice(cond_list)

    urls = {
        'button_url': baseURL + select_button['file-name'] + ".mp3",
        'archive_url': "https://youtu.be/" + select_button['stream_id'],
        'msg': msg
    }
    return urls
