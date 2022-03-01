# Find the majority element of the given list.
# Majority element: count of the elements > N/2
# N = length of list
# A = [5, 2, 3, 5, 1, 5, 1, 2, 5, 5, 5]
# Ans = 5

A = [5, 2, 3, 5, 1, 5, 1, 2, 5, 5, 5]
N=len(A)//2
count=0
for i in range(len(A)):
    if N==A[i]:
        count += 1
if count > N:
    print(N)