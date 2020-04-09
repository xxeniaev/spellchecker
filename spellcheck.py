import edit_distance
import re
import dict_loader
import main


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
            if levenshtein_distance < min_distance:
                min_distance = levenshtein_distance
                correct_word = st
        return correct_word


class Writer:
    def __init__(self, text):
        self.old_text = text

    def create_corrected_text(self):
        word = ''
        new_text = ''
        for letter in self.old_text:
            for e in check_text(prepare_text(self.old_text)):
                if word == e.not_checked and not e.is_correct:
                    print(word)
                    new_text = new_text.replace(word,
                                                '{} <{}>'.format(e.not_checked,
                                                                 e.checked))
            word += letter
            new_text += letter
            if not letter.isalpha():
                word = ''
        return new_text

    def write_corrected_text(self):
        if main.out == 'console':
            print(self.create_corrected_text())
        else:
            with open(main.out, 'w') as f:
                f.write(self.create_corrected_text())


# takes not checked text and splits it by words (words are not low cased)
def prepare_text(text):
    pattern = re.compile(r'([a-zA-Z]+)\W*')
    return pattern.findall(text)


# takes split text and returns list of not checked and checked words
# plus an indication if they are correct or not
def check_text(words):
    words_and_changes = []
    for word in words:
        is_correct = main.s.check_if_word_is_correct(word)
        corrected_word = main.s.to_correct_word(word)
        words_and_changes.append(Word(word, is_correct, corrected_word))
    return words_and_changes
