# 7. Write a NumPy program to compute the sum of the diagonal elements of a given array.


# import numpy as np
import numpy as np
array1 = n_array = np.array([[55, 25, 15],[30, 44, 2]])

# Finding the diagonal elements of a matrix
diag = np.diagonal(array1)
print(diag)

# sum of diagonal array
result =  np.sum(diag)
# print result for sum of diagonal array
print(result)