# import datetime
# now= datetime,datetime.now
# year=lambda x:x.year
# print(year(now))
import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

# lambda 
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print("year",year(x))
print("month",month(x))
print("day",day(x))
print("time",t(x))



 

 

 
