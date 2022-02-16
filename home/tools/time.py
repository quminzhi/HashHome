from datetime import datetime
from pytz import timezone 
import random

la_tz = timezone('America/Los_Angeles')
la_time = datetime.now(la_tz)

def intro():
    cur_time = la_time.strftime("%a %b %d %H:%M:%S %Y")

    date = cur_time[0:10]
    hour = int(cur_time[11:13])
    greet = 'Good'
    if 5 <= hour < 13:
        greet += ' Morning'
    elif 13 <= hour < 19:
        greet += ' Afternoon'
    else:
        greet += ' Evening'

    return {
        'intro_slide1': random.randint(0, 24),
        'intro_slide2': random.randint(0, 24),
        'intro_slide3': random.randint(0, 24),
        'intro_greet': greet,
        'intro_date': date,
    }
