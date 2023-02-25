from src.lengthen_date.lengthen_date import (
    lengthen_date)


def test_date_that_ends_with_st_returns_st():
    expected = 'Saturday 1st January 2022'
    result = lengthen_date('01.01.2022')
    print(f'Result is: {result}')
    assert result == expected

def test_date_that_ends_with_nd_returns_nd():
    expected = 'Friday 2nd September 2022'
    result = lengthen_date('02.09.2022')
    print(f'Result is: {result}')
    assert result == expected

def test_date_that_ends_with_th_returns_th():
    expected = 'Friday 24th July 2020'
    result = lengthen_date('24.07.2020')
    print(f'Result is: {result}')
    assert result == expected

def test_date_that_ends_with_rd_returns_rd():
    expected = 'Tuesday 3rd September 2019'
    result = lengthen_date('03.09.2019')
    print(f'Result is: {result}')
    assert result == expected