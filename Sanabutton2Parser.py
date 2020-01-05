import requests
import json
import random

def Sanabutton2Parser(msg):

    url = 'https://www.natorisana.love/api/v1/buttons.json'

    response = requests.get(url)
    jsonData = response.json()

# print('羊すやすや' in str(jsonData[23][0][1]['value']))

    cond_list = []
    for category in jsonData:
        for archive in category:
            for button in archive:
                if msg in str(button['value']):
                    cond_list.append(button['file-name'])

    button_name = random.choice(cond_list)
    button_url = 'https://www.natorisana.love/sounds/' + button_name + '.mp3'

    return button_url