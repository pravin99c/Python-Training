#1. From the given data set print the first and last five rows

import pandas as pd
import numpy as np

# making data frame
data = pd.read_csv('/home/woc/Pravin/Trainee/python_training/pandas/Automobile_data.csv')

# calling head() method first five row print 
first_five_row=data.head(5)
# print(first_five_row)

# calling tail() method last five row print
last_five_row=data.tail(5)
# print(last_five_row)



#------------------------------------------------------------------------------
#2. Clean data and update the CSV file (Replace all column values which contain ‘?’ and n.a with NaN.

# making data frame read
data = pd.read_csv('/home/woc/Pravin/Trainee/python_training/pandas/Automobile_data.csv')
data = data.replace(['?','n.a'],np.NaN)

# making data frame  to change
data.to_csv('/home/woc/Pravin/Trainee/python_training/pandas/Automobile_data.csv')
# print(data.head(20))


#-----------------------------------------------------------------------------------
# 3. Find the most expensive car company name

# make csv all data read or most expensive car company name

# expensive_car = data
# high_price_car =expensive_car[['make','price']][expensive_car.price == expensive_car['price'].max()]
# print(high_price_car)


#--------------------------------------------------------------
# Print All Toyota Cars details


all_car = data
# all_car_d = all_car.groupby('make')
# all_toyota_car = all_car_d.get_group('toyota') 

# print(all_toyota_car)

# -----------------------------------------------------------------------
# Count total car per company

# count_total_car_per_company = all_car['make'].value_counts()
# print(count_total_car_per_company)


# -----------------------------------------------
# Find each company’s Highest price car

all_car_d = all_car.groupby('make')
find_each_car_highest_price = all_car_d['make','price'].max()
# print(find_each_car_highest_price)


# --------------------------------------------------
# Find the average mileage of each car making company

# all_car_d = all_car.groupby('make')
# find_highway_average_mileage_price = all_car_d['make','highway-mpg'].mean()
# find_city_average_mileage_price = all_car_d['make','city-mpg'].mean()
# print(find_each_average_mileage_price)
# print(find_city_average_mileage_price)
find_highway = all_car[['highway-mpg','city-mpg']].mean(axis=1)
# print(find_highway)


# --------------------------------------------------
# Sort all cars by Price column

# sort_all_car = data.sort_values(by=['price'],ascending=False)
# print(sort_all_car)