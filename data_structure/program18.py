# Find the majority element of the given list.
# Majority element: count of the elements > N/2
# N = length of list
# A = [5, 2, 3, 5, 1, 5, 1, 2, 5, 5, 5]
# Ans = 5

A = [5, 2, 3, 5, 1, 1, 2, 5, 2, 2, 2, 2, 2]
list_lenth=len(A)//2
dictionary={}
for i in A:
    if i in dictionary:
        dictionary[i]+=1
    else:
        dictionary[i]=1
if dictionary[i] > list_lenth:
    print("length",list_lenth," :  majority element : ",i ,"count" ,dictionary[i])