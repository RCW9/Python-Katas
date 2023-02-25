from src.herd_the_babies.herd_the_babies import (
    herd_the_babies)


def test_a_single_character_string_returns_a_single_character():
      expected = 'a'
      result = herd_the_babies('a')
      assert result == expected

def test_string_is_returned_alphabetically():
    expected = 'abc'
    result = herd_the_babies('bca')
    assert result == expected

def test_one_letter_returns_capital_before_lowercase():
    expected = 'Aa'
    result = herd_the_babies('aA')
    assert result == expected

def test_multiple_letters_returns_capital_before_lowercase():
    expected = 'AaBbbCcc'
    result = herd_the_babies("bbaBccAC")
    assert result == expected
    