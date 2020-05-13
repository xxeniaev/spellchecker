from urllib.request import urlopen
import codecs
import re
from tqdm import tqdm


def create(link):
    contents = load(link)
    dictionary = set()
    pattern = re.compile(r'([a-zA-Zа-яА-Я]+)\W*')
    list_of_words = pattern.findall(contents.lower())
    count = len(list_of_words)
    loop = tqdm(total=count, position=0, leave=False)
    for k in range(count):
        loop.set_description('loading...'.format(k))
        dictionary.add(list_of_words[k])
        loop.update(1)
    loop.close()

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
