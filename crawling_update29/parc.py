import datetime
from datetime import date
from matrix import *

today = date.today()
oneday = datetime.timedelta(days=1)
yesterday = today - oneday
a = str(today)
b = str(yesterday)


print(b)