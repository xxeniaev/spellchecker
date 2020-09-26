import re
import codecs
import sys
import trie_distance

from DictCreator import DictCreator
from DictLoader import DictLoader


class Spellchecker:
    def __init__(self, given, opt, lang):
        if opt == 'create':
            self.dict = DictCreator(given).create()
        else:
            self.dict = DictLoader(given).load()
        self.lang = lang
        if not self.dict:
            raise AttributeError("sorry, dictionary can't be loaded")
            sys.exit(1)

    def check_if_word_is_correct(self, word):
        return word in self.dict

    def to_correct_word(self, word):
        """
        :param word: takes word to correct
        :return: corrected word
        """
        if word.upper() in self.dict:
            return word.upper()
        word.lower()
        if self.lang == 'eng' or self.lang == 'test_eng':
            if re.search(r'([a-zA-Z]+)', word) is None:
                return word
        if self.lang == 'rus' or self.lang == 'test_rus':
            if re.search(r'([а-яА-Я]+)', word) is None:
                return word
        trie = trie_distance.dict_to_trie(self.dict)
        for i in range(len(word)+1):
            results = trie_distance.search(word, i, trie)
            if results:
                return results[0][0]


class Writer:
    def __init__(self, text, spellchecker, out, inp):
        if inp == 'console':
            self.old_text = text
        else:
            self.old_text = codecs.decode(codecs.encode(text, 'cp1251'),
                                          'utf8')
        self.spellchecker = spellchecker
        self.out = out

    def create_corrected_text(self):
        pattern = re.compile(r'([a-zA-Zа-яА-Я]+)')
        # составляется словарь, где ключ - старое слово, а значение - новое
        # значение(исправленное либо верное слово)
        dictionary = check_text(prepare_text(self.old_text), self.spellchecker)
        new_text = []
        for word in self.old_text.split():
            temp = word
            if pattern.search(word).group().lower() \
                    != dictionary[pattern.search(
                    word).group()]:
                temp = word.replace(
                    pattern.search(word).group(),
                    '{} <{}>'.format(pattern.search(word).group(),
                                     dictionary[pattern.search(word).group()]))
            new_text.append(temp)
        return ' '.join(new_text)

    def write_corrected_text(self):
        if self.out == 'console':
            print(self.create_corrected_text())
        else:
            with open(self.out, 'w') as f:
                f.write(self.create_corrected_text())


def prepare_text(text):
    """
    :param text:  given text to be splited
    :return:  list of words in the text (words are not low cased)
    """

    pattern = re.compile(r'([a-zA-Zа-яА-Я]+)\W*')
    return pattern.findall(text)


def check_text(words, spellchecker):
    """takes split text and returns list of not checked and checked words
    plus an indication if they are correct or not"""

    words_and_changes = {}
    for word in words:
        if word not in words_and_changes:
            if spellchecker.check_if_word_is_correct(word):
                words_and_changes[word] = word
            else:
                words_and_changes[word] = spellchecker.to_correct_word(word)
    return words_and_changes
