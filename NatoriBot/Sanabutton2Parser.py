import requests
from bs4 import BeautifulSoup
import random
import re

def Sanabutton2Parser(message):
    msg = message
    # msg = message.content
    baseURL = "https://www.natorisana.love/"
    res = requests.get(baseURL)

    soup = BeautifulSoup(res.content, "html.parser")

    cond_list = []
    for button in soup.select(".sounds"):
        if msg in button.text:
            cond_list.append(button.get("data-file"))

    if cond_list == []:
        return None

    button_name = random.choice(cond_list)
    button_url = baseURL + 'sounds/' + button_name + '.mp3'
    archive_name = button_name.split('/')[0]

    archive_url = ""
    for span in soup.select('span'):
        if span.get("id") == None:
            continue
        span_id = span.get("id").split('/')[3]
        if archive_name in span_id:
            archive_url = span.find('a').attrs['href']
            break

    urls = {
        'button_url' : button_url,
        'archive_url' : archive_url,
        'msg' : msg
    }

    return urls

if __name__ == "__main__":
    print(Sanabutton2Parser("おはようございナース（ポケセン）"))