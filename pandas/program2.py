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

input_date = str(input("Enter date and time from %d/%m/%y : "))
print(input_date)

# ufo = data[input_date]
# print(all_data)