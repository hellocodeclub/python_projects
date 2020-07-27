
def dow(year,month,day):
    if(month<3):
        month+=12
        year-=1
    result = (day + (int((13*(month-2))/5))+year+(int(year/4))-(int(year/100))-(int(year/400)))%7
    return int(result)+1

# Using datetime
import datetime
week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
week_num=datetime.date(2020,7,24).weekday()
print(week_days[week_num])

#
print(datetime.date(2020,7,24).strftime('%A'))
print(datetime.date(2020,7,24).strftime('%a'))
print(datetime.date(2020,7,24).strftime('%B'))

# Using pandas
import calendar

week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
weekday= calendar.weekday(2020,7,24)
print(week_days[weekday])

# Using no external libraries
week_num3=dow(2020,7,24)
print(week_days[week_num3])

