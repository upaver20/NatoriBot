import urllib.request
import urllib.parse
import sys
import os

file_name = "data/button.mp3"


def download(url_ja):
    url = urllib.parse.quote(url_ja, safe='/:')
    urllib.request.urlretrieve(url, "{0}".format(file_name))
    return
