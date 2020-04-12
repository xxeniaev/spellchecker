import argparse
import spellcheck

parser = argparse.ArgumentParser(description='enter input and/or output files(console by default)')
parser.add_argument('--input', type=str, metavar='', default='console', help='enter the name of input file')
parser.add_argument('--output', type=str, metavar='', default='console', help='enter the name of output file')
args = parser.parse_args()

inp = args.input
out = args.output

if inp == 'console':
    text = input('enter your text: ')
else:
    with open(inp, 'r') as f:
        text = f.read()

lang = input('choose the language(eng/rus): ')
if lang == 'eng':
    link = 'https://drive.google.com/uc?export=download&id=1lbYlUr5QOaPdi4rqvHVt7eIk601cnX6K'
elif lang == 'test_eng':
    link = 'https://drive.google.com/uc?export=download&id=1oHIU8fYI3ZxIqB1ZhmdGEr6rkqQE1nZx'
elif lang == 'test_rus':
    link = 'https://drive.google.com/uc?export=download&id=1vtGbi9ozjV7nWDXHleS_ilTv7bsrpcif'
else:
    link = 'https://drive.google.com/uc?export=download&id=1vHrLRqukd6SJv8tbG9zDpJxA6xUk5usE'

s = spellcheck.Spellchecker(link)
w = spellcheck.Writer(text, s, out)
w.write_corrected_text()

print('Done!')
