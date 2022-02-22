# Introduction to python
## 1.Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

## Input:
    list1=[1,6,8,9,7,2,1]
    list2=[1,2,4,5,6,7]
## Output :
    1.False
    2.True
# testcases

| Input | Output |
| ------ | ------ |
| list1 | False |
| list2| True |
## Development
create list and find sequence of numbers and determines
and check to for loop and ans=false and true


## 2.Write a Python program to add two positive integers without using the '+' operator

## Input:
    a=10
    b=20
## Output :
    30
# testcases

| Input | Output |
| ------ | ------ |
| a=10,b=20 | 30 |
| a=5 b=25 | 30|

## 3.Write a Python program to find common divisors between two numbers in a given pair

## Input:
    a=10
    b=6
## Output :
    2
# testcases

| Input | Output |
| ------ | ------ |
| a=10,b=6 | 2 |
| a=5 , b=25| 5 |


## 4.Write a Python program to filter(even and odd) a list of integers using Lambda.

## Input:
    list1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
## Output :
    odd number
    even number
# testcases

| Input | Output |
| ------ | ------ |
| [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] | even=list1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],odd=list1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |

## 5.Write a Python program to extract year, month, date and time using Lambda.


## Input:
    import datetime
    x = datetime.datetime.now()
## Output :
    year,month,date,time
# testcases

| Input | Output |
| ------ | ------ |
| year| 2022 |
| month| 02 |
| data | 22|
| time | 18:39:51.305865|
## Development

first import datetime
and one varible creat x= datetime.datetime.now()
and than  year= lambda x:x.year or  print function 

