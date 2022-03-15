# 2. Check if the given number is prime or not
num = int(input("Enter number : "))
for i in range(2,(num//2)):
    if num%i==0:
        print(num,"Not a prime number")
        break
else:
    print(num,"prime number")
