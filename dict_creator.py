import re
from tqdm import tqdm


def create(file_name):
    try:
        with open(file_name) as f:
            text = f.read()
    except TypeError:
        print('please, choose language or file for creating '
              'your own dictionary')
        exit(1)
    dictionary = set()
    pattern = re.compile(r'([a-zA-Zа-яА-Я]+)\W*')
    list_of_words = pattern.findall(text.lower())
    count = len(list_of_words)
    loop = tqdm(total=count, position=0, leave=False)
    for k in range(count):
        loop.set_description('loading...'.format(k))
        dictionary.add(list_of_words[k])
        loop.update(1)
    loop.close()

    return dictionary
