from src.years_of_growth.years_of_growth import (
    years_of_growth)

def test_returns_an_integer():
    assert isinstance((years_of_growth(1, 10, 1.1, 2)), int) == True
       

def test_returns_correct_years_to_reach_end_target():
    result = years_of_growth(1, 10, 1.1, 2)
    expected = 4
    assert result == expected

def test_if_start_population_is_zero__population_starts_with_net_migtration_at_year_1():
    result = years_of_growth(0, 1000, 1.9, 50)
    expected = 5
    assert result == expected
