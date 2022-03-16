# 2. Check if the given number is prime or not

input_number = int(input("Enter number : "))
for i in range(2,(input_number//2)):
    if input_number%i==0:
        print(input_number,"Not a prime number")
        break
else:
    print(input_number,"prime number")
