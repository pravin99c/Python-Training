#1. Write a Pandas program to create today's date
#2. Write a Pandas program to calculate all the sighting days of the unidentified 
# - flying object (ufo) from the current date.


#  -----------------------------   1   ------------------------------------
import pandas as pd
import numpy as np
from datetime import date

# making data frame
data = pd.read_csv('/home/woc/Pravin/Trainee/python_training/pandas/ufo_sighting_data.csv')
# print(data)

now = pd.to_datetime(str(date.today()), format='%Y-%m-%d')
print("Today's date: ",now)

#  -----------------------------   2   ------------------------------------
# input date for user
input_date = str(input("Enter date and time from %m/%d/%y : "))
# print(input_date)

ufo = data

# convert 'datedocumented' datetime.
ufo['date_documented'] = pd.to_datetime(ufo['date_documented'])

# print(ufo['date_documented'])

ufo_date = (ufo['date_documented']>input_date)

# print all greaterthen date in cruuent date
all_greaterthen_date = ufo.loc[ufo_date]
print(all_greaterthen_date)
print(len(all_greaterthen_date))
