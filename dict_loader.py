from urllib.request import urlopen


def load(link):
    with urlopen(link) as response:
        html_response = response.read()
        encoding = response.headers.get_content_charset('utf-8')
        contents = html_response.decode(encoding)
    dictionary = set(
            word.lower()
            for word in contents.splitlines()
        )
    return dictionary
