from datetime import date

tues = date(2014, 5, 13)
print(date(2014, 5, 19) - tues)
print(tues.strftime('%A, %B %d'))  # "fmt"即数据表示方式
