import edit_distance
import re
import dict_loader


class Word:
    def __init__(self, a, b, c):
        self.not_checked = a
        self.is_correct = b
        self.checked = c


class Spellchecker:
    def __init__(self, link):
        self.dict = dict_loader.load(link)
        if not self.dict:
            print('ERROR')

    def check_if_word_is_correct(self, word):
        word = word.lower()
        return word in self.dict

    def to_correct_word(self, word):
        word = word.lower()
        min_distance = 9999999
        for st in self.dict:
            levenshtein_distance = edit_distance.levenshtein_distance(st,
                                                                      word)
            if levenshtein_distance == 1:
                correct_word = st
                break
            if levenshtein_distance < min_distance:
                min_distance = levenshtein_distance
                correct_word = st
        return correct_word


class Writer:
    def __init__(self, text, spellchecker, out):
        self.old_text = text
        self.spellchecker = spellchecker
        self.out = out

    def create_corrected_text(self):
        word = ''
        new_text = ''
        for letter in self.old_text:
            for e in check_text(prepare_text(self.old_text), self.spellchecker):
                if word == e.not_checked and not e.is_correct:
                    new_text = new_text.replace(word,
                                                '{} <{}>'.format(e.not_checked,
                                                                 e.checked))
            word += letter
            new_text += letter
            if not letter.isalpha():
                word = ''
        return new_text

    def write_corrected_text(self):
        if self.out == 'console':
            print(self.create_corrected_text())
        else:
            with open(self.out, 'w') as f:
                f.write(self.create_corrected_text())


def prepare_text(text):
    """takes not checked text and splits it by words (words are not low cased)"""

    pattern = re.compile(r'([a-zA-Z]+)\W*')
    return pattern.findall(text)


def check_text(words, spellchecker):
    """takes split text and returns list of not checked and checked words
    plus an indication if they are correct or not"""

    words_and_changes = []
    for word in words:
        is_correct = spellchecker.check_if_word_is_correct(word)
        if is_correct:
            words_and_changes.append(Word(word, is_correct, word))
        else:
            corrected_word = spellchecker.to_correct_word(word)
            words_and_changes.append(Word(word, is_correct, corrected_word))
    return words_and_changes
