# 2. Write a NumPy program to compute the outer product of two given vectors.

# import numpy 
import numpy as np

# created array of vectors
array1 = np.array([1,2])
array2 = np.array([5,6])

# ans of outer product of two given vectors
ans = np.outer(array1,array2)

# print answer
print(ans)
