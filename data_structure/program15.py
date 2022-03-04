# Calculate the sum of the major and minor diagonals of the given matrix
# A = [ [2, 0, 7],
#       [4, 1, 9],
#       [8, 1, -1], 
#      ]
# ans = 2, 16
A = [ [2, 0, 7, 4],
      [4, 1, 9, 4],
      [8, 1, -1, 4],
      [8, 1, -1, 4] 
     ]
sum=0
sum1=0
# for i in range(len(A)):
#     for j in range(len(A)):
#         if i == j:
#             sum += (A[i][j])
#         if i + j == len(A)-1:
#             sum1 += A[i][j]
# print(sum,sum1)
count = len(A)-1
for i in range(len(A)):
    sum += A[i][i]
    sum1 += A[i][count]
    count -=1
print(sum,sum1)