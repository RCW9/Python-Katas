from src.get_distinct_letters.get_distinct_letters import (
    get_distinct_letters)


def test_empty_strings_returns_empty_string():
    expected = ''
    result = get_distinct_letters('', '')
    print(f'Result is: {result}')
    assert result == expected
    
def test_unique_single_character_strings_return_doublecharacter_sorted_string():
    expected = 'ab'
    result = get_distinct_letters('a', 'b')
    print(f'Result is: {result}')
    assert result == expected

def test_two_strings_return_only_letters_unique_to_each_string_in_alphabetical_order():
    expected = 'dehrw'
    result = get_distinct_letters('hello', 'world')
    print(f'Result is: {result}')
    assert result == expected

def test_two_strings_of_different_length_return_only_letters_unique_to_each_string_in_alphabetical_order():
    expected = 'dehrsw'
    result = get_distinct_letters('hello', 'worlds')
    print(f'Result is: {result}')
    assert result == expected
    
def test_two_strings__with_the_same_letters_return_an_empty_string():
    expected = ''
    result = get_distinct_letters('hello', 'hello')
    print(f'Result is: {result}')
    assert result == expected


