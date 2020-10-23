import argparse


class ArgParser(argparse.ArgumentParser):
    """Парсер аргументов"""
    def __init__(self):
        super().__init__()

        self.description = 'enter input and/or output files(console ' \
                           'by default) and language'

        self.add_argument('--input', '-in', type=str, metavar='',
                          default='console',
                          help='enter the name of input file')
        self.add_argument('--output', '-out', type=str, metavar='',
                          default='console',
                          help='enter the name of output file')
        self.add_argument('--lang', '-l', type=str, metavar='',
                          help='enter language(eng/rus/created)')
        self.add_argument('--create', type=str, metavar='',
                          help='enter the base\'s of words name')
