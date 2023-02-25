
from datetime import datetime


def lengthen_date(date):
    new_date = datetime.strptime(date, '%d.%m.%Y')
    day = new_date.strftime('%A')
    month = new_date.strftime('%B')
    split_date = date.split('.')
    year = int(split_date[2])
    day_date = int(split_date[0])
    if (3 < day_date < 21) or (23 < day_date < 31):
        day_date = str(day_date) + 'th'
    else:
        suffixes ={1: 'st', 2: 'nd', 3: 'rd'}
        day_date = str(day_date) + suffixes[day_date % 10]
   
    return f'{day} {day_date} {month} {year}'
    
lengthen_date('21.03.2017')