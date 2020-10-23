import unittest
import spellcheck
import trie_distance
from DictCreator import DictCreator
from DictLoader import DictLoader
import main

s_eng = spellcheck.Spellchecker(
    'https://drive.google.com/'
    'uc?export=download&id=1oHIU8fYI3ZxIqB1ZhmdGEr6rkqQE1nZx', 'load', 'eng')
s_rus = spellcheck.Spellchecker(
    'https://drive.google.com/'
    'uc?export=download&id=1vtGbi9ozjV7nWDXHleS_ilTv7bsrpcif', 'load', 'rus')
s_created = spellcheck.Spellchecker('test_create_eng.txt', 'create', 'create')
w_eng = spellcheck.Writer('Programming is awsome!', s_eng,
                          'console', 'console')
w_rus = spellcheck.Writer('Программирование васхитительно!', s_rus,
                          'console', 'console')


class SpellcheckerTest(unittest.TestCase):

    def test_dict(self):
        self.assertIsNotNone(s_eng.dict)
        self.assertIsNotNone(s_rus.dict)
        self.assertEqual(s_eng.dict, {'programming', 'in', 'python', 'is',
                                      'awesome', 'I', 'want', 'to', 'program',
                                      'everyday', 'hope', 'if', 'continue',
                                      'will', 'be', 'good', 'enough', 'a',
                                      'professional', 'programmer', 'one',
                                      'day'})
        self.assertEqual(s_rus.dict, {'программирование', 'на', 'питоне',
                                      'восхитительно', 'я', 'хочу',
                                      'программировать', 'ежедневно',
                                      'надеюсь', 'что', 'если', 'продолжу',
                                      'то', 'однажды', 'стану', 'крутым',
                                      'программистом', 'слышала', 'они',
                                      'много', 'работают', 'ГОС', 'кое-где',
                                      'привет', 'как', 'дела'})

    def test_check_if_word_is_correct(self):
        s = spellcheck.Spellchecker(
            'https://drive.google.com/uc?export=download&id='
            '1dNmTiVbc0YQp_LGnCMM7vFzA7XSVODMH', 'load', 'eng')

        # words with hyphen
        self.assertTrue(s.check_if_word_is_correct('кое-где'))
        self.assertTrue(s.check_if_word_is_correct('откуда-то'))
        self.assertFalse(s.check_if_word_is_correct('кои-где'))
        # abbreviations
        self.assertTrue(s.check_if_word_is_correct('вуз'))
        self.assertTrue(s.check_if_word_is_correct('ГОС'))
        # numerals
        self.assertTrue(s.check_if_word_is_correct('первый'))
        self.assertTrue(s.check_if_word_is_correct('четвёртый'))
        # forms of words
        self.assertTrue(s.check_if_word_is_correct('красивому'))
        self.assertTrue(s.check_if_word_is_correct('растапливала'))
        self.assertTrue(s.check_if_word_is_correct('полем'))

        self.assertTrue(s_eng.check_if_word_is_correct('awesome'))
        self.assertFalse(s_eng.check_if_word_is_correct('awsome'))
        self.assertTrue(s_rus.check_if_word_is_correct('восхитительно'))
        self.assertFalse(s_rus.check_if_word_is_correct('васхитительно'))

    def test_to_correct_word(self):
        self.assertEqual(s_eng.to_correct_word('awsome'), 'awesome')
        self.assertEqual(s_rus.to_correct_word('васхитительно'),
                         'восхитительно')
        self.assertEqual(s_rus.to_correct_word('гос'), 'ГОС')
        self.assertEqual(s_rus.to_correct_word('коегде'), 'кое-где')
        self.assertEqual(s_rus.to_correct_word('приветкакдела'),
                         'привет{ }как{ }дела')

    def test_create_corrected_text(self):
        self.assertEqual(w_eng.create_corrected_text(),
                         'Programming is awsome <awesome>!')
        self.assertEqual(w_rus.create_corrected_text(),
                         'Программирование васхитительно <восхитительно>!')

    def test_prepare_text(self):
        self.assertEqual(spellcheck.prepare_text('Programming is awsome!'),
                         ['Programming', 'is', 'awsome'])
        self.assertEqual(spellcheck.prepare_text(
            'Программирование васхитительно!'), ['Программирование',
                                                 'васхитительно'])

    def test_check_text(self):
        self.assertEqual(spellcheck.check_text(['Programming', 'is', 'awsome'],
                                               s_eng), {
            'Programming': 'programming', 'is': 'is', 'awsome': 'awesome'})
        self.assertEqual(spellcheck.check_text(['Программирование',
                                                'васхитительно'], s_rus),
                         {'Программирование': 'программирование',
                          'васхитительно': 'восхитительно'})

    def test_dict_loader(self):
        dict_eng = DictLoader('https://drive.google.com/uc?export=download'
                              '&id=1oHIU8fYI3ZxIqB1ZhmdGEr6rkqQE1nZx')
        dict_rus = DictLoader('https://drive.google.com/uc?export=download'
                              '&id=1vtGbi9ozjV7nWDXHleS_ilTv7bsrpcif')

        self.assertIsNotNone(dict_eng)
        self.assertIsNotNone(dict_rus)
        self.assertIn('awesome', dict_eng.load())
        self.assertIn('восхитительно', dict_rus.load())
        self.assertNotIn('awsome', dict_eng.load())
        self.assertNotIn('васхитительно', dict_rus.load())

    def test_dict_creator(self):
        dictionary = DictCreator('test_create_eng.txt')

        self.assertIsNotNone(dictionary)
        self.assertIn('awesome', dictionary.create())
        self.assertNotIn('awsome', dictionary.create())

    def test_main(self):
        self.assertIsNotNone(main.get_link('eng'))
        self.assertIsNotNone(main.get_link('rus'))

    def test_trie_distance(self):
        trie_rus = trie_distance.dict_to_trie(s_rus.dict)
        trie_eng = trie_distance.dict_to_trie(s_eng.dict)

        self.assertEqual(trie_distance.search('васхитительно', 0, trie_rus),
                         [])
        self.assertEqual(trie_distance.search('васхитительно', 1, trie_rus),
                         [('восхитительно', 1)])
        self.assertEqual(trie_distance.search('васхитительно', 2, trie_rus),
                         [('восхитительно', 1)])
        self.assertEqual(trie_distance.search('awsome', 0, trie_eng), [])
        self.assertEqual(trie_distance.search('awsome', 1, trie_eng),
                         [('awesome', 1)])
        self.assertEqual(trie_distance.search('awsome', 2, trie_eng),
                         [('awesome', 1)])
