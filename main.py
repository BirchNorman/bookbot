import sys

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

book_text = get_book_text(sys.argv[1])

from stats import get_num_words

print(f"{get_num_words(book_text)} words found in the document")

from stats import get_character_count

str_to_int = get_character_count(book_text)

from stats import sort_by_char_count
 
character_count_unformatted = sort_by_char_count(str_to_int)

print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------""")

for dictionary in character_count_unformatted:
	if dictionary ["char"].isalpha():
		print(dictionary["char"] + ': ' + str(dictionary["num"]))

print("============= END ===============")

