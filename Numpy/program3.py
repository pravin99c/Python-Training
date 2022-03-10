# 3. Write a NumPy program to compute the cross-product of two given vectors.

# import numpy 
import numpy as np

# created array of vectors
array1 = np.array([5,2])
array2 = np.array([5,6])

# he cross-product of two given vectors
ans = np.cross(array1,array2)
ans1 = np.cross(array2,array1)
# print answer
print(ans)
print(ans1)
