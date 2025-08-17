def get_num_words(book_text):
       return len(book_text.split())

def get_character_count(book_text):
	str_to_int = {}
	for character in book_text:
		char = character.lower()
		if char not in str_to_int:
			str_to_int[char] = 1
		else:
			str_to_int[char] += 1
	return str_to_int

def sort_on(items):
	return items["num"]

def sort_by_char_count(str_to_int):
	list_of_dictionaries = []
	for string in str_to_int:
		itself_and_count = {}
		itself_and_count["char"] = string
		itself_and_count["num"] = str_to_int[string]
		list_of_dictionaries.append(itself_and_count)
	return sorted(list_of_dictionaries, reverse=True, key=sort_on)
