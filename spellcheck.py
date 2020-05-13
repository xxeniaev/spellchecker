import edit_distance
import re
import dict_loader
import dict_creator
import codecs
import sys


class Spellchecker:
    def __init__(self, link, lang):
        if lang == 'created':
            self.dict = dict_creator.create(link)
        else:
            self.dict = dict_loader.load(link)
        if not self.dict:
            raise AttributeError("sorry, dictionary can't be loaded")
            sys.exit(0)

    def check_if_word_is_correct(self, word):
        word = word.lower()
        return word in self.dict

    def to_correct_word(self, word):
        word = word.lower()
        min_distance = 9999999
        for st in self.dict:
            levenshtein_distance = edit_distance.levenshtein_distance(st, word)
            # if the 'incorrect' word doesn't have letters from dict it means
            # that the word is correct but is written in different language
            if levenshtein_distance == len(word):
                correct_word = word
                break
            if levenshtein_distance == 1:
                correct_word = st
                break
            if levenshtein_distance < min_distance:
                min_distance = levenshtein_distance
                correct_word = st
        return correct_word


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
        dictionary = check_text(prepare_text(self.old_text), self.spellchecker)
        new_text = []
        for word in self.old_text.split():
            temp = word
            if pattern.search(word).group().lower() \
                    != dictionary[pattern.search(
                    word.lower()).group()]:
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
    """takes not checked text and splits it by words
    (words are not low cased)"""

    pattern = re.compile(r'([a-zA-Zа-яА-Я]+)\W*')
    return pattern.findall(text)


def check_text(words, spellchecker):
    """takes split text and returns list of not checked and checked words
    plus an indication if they are correct or not"""

    words_and_changes = {}
    for word in words:
        word = word.lower()
        if word not in words_and_changes:
            if spellchecker.check_if_word_is_correct(word):
                words_and_changes[word] = word
            else:
                words_and_changes[word] = spellchecker.to_correct_word(word)
    return words_and_changes
