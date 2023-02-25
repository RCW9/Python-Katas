def get_distinct_letters(str1, str2):
	new_string = ""
	for letter in str1:
		if letter not in str2:
			new_string+= letter
	for letter in str2:
		if letter not in str1 and letter not in new_string:
			new_string+= letter
	return ''.join(sorted(new_string))

			
	
