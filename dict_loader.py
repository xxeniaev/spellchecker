from urllib.request import urlopen
import codecs


def load(link):
    with urlopen(link) as response:
        html_response = response.read()
        contents = codecs.decode(html_response, 'utf8')
    dictionary = set()
    dictionary.update(contents.lower().split())

    return dictionary
