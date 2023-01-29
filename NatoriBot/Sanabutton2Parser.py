import requests
import random
import json


def Sanabutton2Parser(message):
    msg = message

    baseURL = "https://www.natorisana.love/"
    jsonURL = baseURL + "api/v1/buttons.json"
    archive_list = json.loads(requests.get(jsonURL).text)

    cond_list = []

    for archive in archive_list:
        for block_archive in archive:
            for button in block_archive:
                if msg in str(button["value"]):
                    cond_list.append(button)

    if cond_list == []:
        return None

    select_button = random.choice(cond_list)

    buttonURL = baseURL + "sounds/" + select_button['file-name'] + ".mp3"

    urls = {
            'button_url': buttonURL,
            'msg': msg
            }
    return urls
