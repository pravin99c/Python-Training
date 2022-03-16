# 1. Finding the sum of all digits of a number until the sum becomes a single digit.
# Examples. 10589=>5 , 121=>4, 99=>9, 10=>1

from numpy import number

# input user number
input_number = int(input("Enter number for sum : "))

def sum_number(input_number):
    """
    sum of input number for user with logical(use Maths logic)
    """
    if input_number == 0:
        return input_number
    elif (input_number % 9 ==0):
        return 9
    else:
        return (input_number % 9)

print(sum_number(input_number))