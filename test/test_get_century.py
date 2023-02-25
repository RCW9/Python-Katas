from src.get_century.get_century import (get_century)

def test_the_correct_century_is_returned():
   assert get_century(2023) == '21st'
   assert get_century(1999) == '20th'
   assert get_century(1801) == '19th'
   assert get_century(5) == '1st'
   assert get_century(120) == '2nd'
   assert get_century(9999) == '100th'
   assert get_century(2000) == '21st'
   assert get_century(10000) == '101st'
   assert get_century(300) == '4th'