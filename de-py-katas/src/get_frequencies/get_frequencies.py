def get_frequencies(str):
	dict_letters = {}
	no_spaces = str.replace(" ", "")
	for letter in no_spaces:
		if letter not in dict_letters:
			dict_letters[letter] = 1
		else:
			dict_letters[letter] += 1
	return dict_letters
			
			
		


