from src.create_counter.create_counter import (
    create_counter)

counter = create_counter(1)
up = counter['up']
down = counter['down']


def test_calling_up_increments_counter_by_1():
    expected = 2
    result = up()
    print(f'Result is: {result}')
    assert result == expected

def test_calling_up_second_time_moves_counter_up_to_3():
    expected = 3
    result = up()
    print(f'Result is: {result}')
    assert result == expected

def test_calling_up_second_time_moves_counter_up_to_2():
    expected = 2
    result = down()
    print(f'Result is: {result}')
    assert result == expected

def test_calling_down_second_time_moves_counter_down_to_1():
    expected = 1
    result = down()
    print(f'Result is: {result}')
    assert result == expected

