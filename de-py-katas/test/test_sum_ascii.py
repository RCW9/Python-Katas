from src.sum_ascii.sum_ascii import (
    sum_ascii
)

def test_integer_is_returned():
    assert isinstance(sum_ascii(['A']), int) == False

def test_list_of_one_character_returns_one_ascii():
    result = sum_ascii(['A'])
    expected = {'A': 97}
    assert result == expected


def test_list_of_one_string_element_returns_sum_of_all_chars_in_string():
    result = sum_ascii(['Bob'])
    expected ={'Bob':307}
    assert result == expected

def test_two_strings_score_and_highest_score_string_returned():
    result = sum_ascii(['Bob', 'Alice'])
    expected = {'Alice': 510}
    assert result == expected

def test_multiple_strings_of_various_cases():
    result = sum_ascii(['Bob', 'Alice', 'zepeddee', 'Lisa'])
    expected = {'zepeddee': 838}
    assert result == expected