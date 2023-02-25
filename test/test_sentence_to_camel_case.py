from src.sentence_to_camel_case.sentence_to_camel_case import (
    sentence_to_camel_case)


def test_returns_a_single_word_in_upper_if_true():
    expected = 'This'
    result = sentence_to_camel_case('this', True)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_two_joined_words_each_capitalized_if_true():
    expected = 'ThisSentence'
    result = sentence_to_camel_case('this sentence', True)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_all_joined_words_when_different_cased_characters_if_true():
    expected = "ThisBiggerStrangeSentence"
    result = sentence_to_camel_case("This Bigger strange Sentence", True)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_lowercase_word_when_passed_uppercaseword_if_false():
    expected = "this"
    result = sentence_to_camel_case("This", False)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_lowercase_word_followed_by_upper_case_words_if_false():
    expected = "thisSentence"
    result = sentence_to_camel_case("This sentence", False)
    print(f'Result is: {result}')
    assert result == expected

def test_multicase_string_returns_lowercase_first_word_and_rest_uppercase_if_false():
    expected = "thisBiggerStrangeSentence"
    result = sentence_to_camel_case("This bigger Strange sentence", False)
    print(f'Result is: {result}')
    assert result == expected

