import urllib.request
import urllib.parse


def download(url_ja, file_name):
    url = urllib.parse.quote(url_ja, safe='/:')
    urllib.request.urlretrieve(url, "{0}".format(file_name))
    return
