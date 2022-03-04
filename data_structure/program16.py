# Find the elements of the given list which are exactly the same as the entire product of the list except itself
# A = [1, 5, 1, 10, 50]
# Ans = 50
# A = [1, 2, 4, 8, 1]
# Ans = 8
A = [1, 1, 4, 8, 2]
ans=0
# for i in range(len(A)):
#     add=1
#     for j in range(len(A)):
#         if j!=i:
#             add = add*A[j]
#     if A[i]==add:
#         ans=add
# print(ans)
ans=0
sum = 1
# for i in range(len(A)):
#     sum *= A[i]
#     if (sum/A[i])==A[i]:
#         ans=A[i]
# print(ans)


for i in range(len(A)):
    sum *= A[i]
for i in A:
    if sum/i==i:
        print(i)
