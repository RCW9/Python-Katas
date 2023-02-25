from src.get_frequencies.get_frequencies import (get_frequencies)

def test_single_character_string_returns_dictionary_with_one_property():
    expected = {'a' : 1}
    result = get_frequencies('a')
    print(f'Result is: {result}')
    assert result == expected
    
def test_string_with_no_repeating_chars_returns_dictionary_with_each_letter_have_value_1():
    expected = {'a': 1, 'b': 1, 'c': 1, 'd': 1}
    result = get_frequencies('abcd')
    print(f'Result is: {result}')
    assert result == expected

def test_string_with_repeating_chars_returns_dictionary_with_each_letter_have_correct_value():
    expected = {'a': 2, 'b': 1, 'c': 1, 'd': 3}
    result = get_frequencies('aabcddd')
    print(f'Result is: {result}')
    assert result == expected

def test_string_with_space_does_not_return_an_object_where_spaces_are_included():
    expected = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    result = get_frequencies('hello world')
    print(f'Result is: {result}')
    assert result == expected