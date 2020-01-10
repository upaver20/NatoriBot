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
    archive_url = ''
    while True:
        select_button = random.choice(cond_list)
        select_span = select_button.find_previous_sibling('span')
        if select_span.find('a') != None:
            archive_url = select_span.find('a').attrs['href']
            break
        if i > 5:
            archive_url = archive_parser(select_button, soup)
            break
        i = i + 1

    button_url = baseURL + 'sounds/' + select_button.get("data-file") + '.mp3'

    urls = {
        'button_url' : button_url,
        'archive_url' : archive_url,
        'msg' : msg
    }

    if urls["button_url"].startswith('https://www.natorisana.love/') and urls["button_url"].endswith('.mp3') and urls["archive_url"].startswith('https://youtu.be/'):
        return urls
    else:
        return None

    return urls

def archive_parser(button, soup):
    archive_name = button.get("data-file").split('/')[0]
    archive_url = ""
    for span in soup.find_all('span'):
        if span.get("id") == None:
            continue
        if archive_name in span.get("id"):
            archive_url = span.find('a').attrs['href']
            break
    return archive_url




if __name__ == "__main__":
    fuga = Sanabutton2Parser("お")
    print(fuga)