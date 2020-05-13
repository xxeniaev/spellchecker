from urllib.request import urlopen
import codecs
import re


def create(link):
    contents = load(link)
    dictionary = set()
    pattern = re.compile(r'([a-zA-Zа-яА-Я]+)\W*')
    dictionary.update(pattern.findall(contents.lower()))

    return dictionary


def load(link):
    try:
        with urlopen(link) as response:
            html_response = response.read()
            contents = codecs.decode(html_response, 'utf8')
    except PermissionError:
        print('probably you don\'t have permission for opening this document')
        exit(1)
    except Exception:
        print('probably you don\'t have internet connection')
        exit(1)

    return contents
