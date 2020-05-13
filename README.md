# Spellchecker
points your mistakes out in texts and corrects them.
## Getting Started
you'll have to download the program form here and have spellchecking mood ***(optional)***.
## Usage
### Notes
* use `--input` or `-in` for choosing file to be corrected (make sure that it is located in the directory where the spellchecker is). if you don't wanna use this option you can write the text on your own below in `enter your text:`  line ***(optional)***.
* use `--output` or `-out` for choosing the name of file where you'd like to be written the corrected text for you. you are able to not use this option and to get the wonderful corrected text below, on the console ***(optional)***.
* use `--lang` or `-l` for choosing language or creating dictionary from your text.
  * `eng`(for choosing English)
  * `rus`(for choosing Russian)
  * `created`(creating dictionary)
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
## Future versions
* more tests(words with hyphen, abbreviations, numerals, forms of words)
* make counting faster(n-gramms, automation, hashing, data structures, fuzzy serch, pre-calculation)
* parsing arguments with `sys.stdin`
## Authors
* **Xenia Evdokimova** ([xxeniaev](https://github.com/xxeniaev))
