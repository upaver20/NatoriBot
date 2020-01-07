import requests
from bs4 import BeautifulSoup
import random
import re

def Sanabutton2Parser(message):
    msg = message
    baseURL = "https://www.natorisana.love/"
    res = requests.get(baseURL)

    soup = BeautifulSoup(res.content, "html.parser")

    cond_list = []
    for button in soup.select(".sounds"):
        if msg in button.text:
            cond_list.append(button)

    if cond_list == []:
        return None

    i = 0

    while True:
        select_button = random.choice(cond_list)
        select_span = select_button.find_previous_sibling('span')
        if select_span.find('a') != None:
            break
        if i > 5:
            return None
        i = i + 1

    button_url = baseURL + 'sounds/' + select_button.get("data-file") + '.mp3'
    archive_url = select_span.find('a').attrs['href']

    urls = {
        'button_url' : button_url,
        'archive_url' : archive_url,
        'msg' : msg
    }

    return urls

if __name__ == "__main__":
    fuga = Sanabutton2Parser("お")
    print(fuga)