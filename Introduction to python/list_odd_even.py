list1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range(len(list)):
#     if list[i]%2==0:
#         print("Even number is ",list[i])
#     else:
#         print("Odd number is ",list[i])
odd=[]
even=[]
for i in list1:
    num=lambda i:i%2

    if num(i)==0:
        even.append(i)
    else:
        odd.append(i)
print("Even : ",even)
print("Odd : ",odd)