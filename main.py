import argparse
import spellcheck

parser = argparse.ArgumentParser(description='enter input and/or output files(console by default)')
parser.add_argument('--input', type=str, metavar='', default='test.txt', help='enter the name of input file')
parser.add_argument('--output', type=str, metavar='', default='corrected_test.txt', help='enter the name of output file')
args = parser.parse_args()

inp = args.input
out = args.output

if inp == 'console':
    text = input('enter your text:')
else:
    with open(inp, 'r') as f:
        text = f.read()

link = 'https://drive.google.com/uc?export=download&id=1oHIU8fYI3ZxIqB1ZhmdGEr6rkqQE1nZx'
# link = input('enter the link for the dictionary(you can find some in links.txt):')
s = spellcheck.Spellchecker(link)
w = spellcheck.Writer(text)
w.write_corrected_text()
