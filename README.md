# Spellchecker
highlights mistakes in texts and corrects them.
## Getting Started
you'll have to download the program from here and have spellchecking mood ***(optional)***.
### Requirements
* `tqdm` (installing by pip)
## Usage
### Notes
* use `--input` or `-in` for choosing file to be corrected (make sure that it is located in the directory where the spellchecker is). if you don't wanna use this option you can write the text on your own below in `enter your text:`  line ***(optional)***.
* use `--output` or `-out` for choosing the name of file where you'd like to be written the corrected text for you. you are able to not use this option and to get the wonderful corrected text below, on the console ***(optional)***.
* use `--lang` or `-l` for choosing language or creating dictionary from your text.
  * `eng`(for choosing English)
  * `rus`(for choosing Russian)
  * `created`(creating dictionary):
    * enter link for the text in `enter link for creating dictionary:` line
* `done!` message says that chellcheck is correctly complited :)
### Examples
```
python main.py --input file_name.txt --output file_name.txt --lang eng
```
```
python main.py --input file_name.txt --lang eng
```
```
python main.py --output file_name.txt --lang eng
```
```
python main.py --lang eng
```
## Modules
* `main.py` launching
* `spellcheck.py` spellchecking
* `trie_distance.py` algorithm of Levenshtein Distance + bor trie
* `dict_loader.py` loading dictionary
* `dict_creator.py` creating dictionary
* `test_spellchecker.py` testing program
## Future versions
* more tests(words with hyphen, abbreviations, numerals, forms of words)
* make counting faster(n-gramms, automation, hashing, data structures, fuzzy serch, pre-calculation)
* parsing arguments with `sys.stdin`
* ignoring foreign language words
## Authors
* **Xenia Evdokimova** ([xxeniaev](https://github.com/xxeniaev))
