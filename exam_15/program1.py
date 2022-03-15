# 1. Finding the sum of all digits of a number until the sum becomes a single digit.
# Examples. 10589=>5 , 121=>4, 99=>9, 10=>1

input_number = input("Enter number for sum : ")

def sum_number(input_number):
    sum1 = 0
    for i in input_number:
        sum1 += int(i)
    number = str(sum1)
    sum1 = 0
    for i in number:
        sum1 += int(i)
    print(sum1)

sum_number(input_number)
