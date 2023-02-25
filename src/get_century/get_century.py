
import math 

def get_century(year):
    century = (year) // 100 + 1 

    if century % 10 == 1 and century % 100 != 11:
      return f'{century}st'
  
    elif century % 10 == 2 and century % 100 != 12:
      return f'{century}nd'
  
    elif century % 10 == 3 and century % 100 != 13:
      return f'{century}rd'
  
    else:
        return f'{century}th'

