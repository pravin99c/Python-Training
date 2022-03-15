# 1. Finding the sum of all digits of a number until the sum becomes a single digit.
# Examples. 10589=>5 , 121=>4, 99=>9, 10=>1

# 2. Check is given number is prime or not
# 3. You have a line of two points, find the 3 point on the line on opposite direction.



# ----------------------------------------- 1 ---------------------------------


from tkinter import NUMERIC


number = input("Enter number for sum : ")

def sum_number(number):
    sum1 = 0
    for i in number:
        sum1 += int(i)
    number = str(sum1)
    sum1 = 0
    for i in number:
        sum1 += int(i)
    print(sum1)

sum_number(number)


# --------------------------------------------- 2 -------------------------

num = int(input("Enter number : "))
for i in range(2,(num//2)+1):
    if num%i==0:
        print(num,"Not a prime number")
        break
else:
    print(num,"prime number")
