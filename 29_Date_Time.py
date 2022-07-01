# Date Time in Python
import datetime as dt

current_date=dt.date.today()
print("Current Date : ",current_date)

new =dt.date(2021,10,25)
print(new)
print("Year : ",new.year)
print("Month : ",new.month)
print("Day : ",new.day)
print("-----------------")
a=dt.time(10,45,5,555505)
print(a)
print("Hour : ",a.hour )
print("minute : ",a.minute)
print("second : ",a.second)
print("microsecond : ",a.microsecond)
print("--------------------------------")
current_time=dt.datetime.now()
print("Current Time : ",current_time)
print("----------------------------------")
new =dt.datetime(2021,5,31,12,2,10)
print(new)
print(new.date())
print(new.time())
print("---------------------------")
current=dt.datetime.now()
new_year=dt.datetime(2022,1,1)
difference=new_year-current
print(difference)
print("---------------------------")
current=dt.datetime.now()
print(current)
s=current.strftime("%A %b %d %Y")
print(s)




