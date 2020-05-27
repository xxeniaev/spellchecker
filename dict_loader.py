from urllib.request import urlopen
import codecs


def load(link):
    try:
        with urlopen(link) as response:
            html_response = response.read()
            contents = codecs.decode(html_response, 'utf8')
    except PermissionError:
        print('probably you don\'t have permission for opening this document')
        exit(1)
    except UnicodeDecodeError:
        print('problems with decoding')
        exit(1)
    except Exception:
        print('probably you don\'t have internet connection')
        exit(1)
    else:
        dictionary = set()
        dictionary.update(contents.lower().split())

    return dictionary
