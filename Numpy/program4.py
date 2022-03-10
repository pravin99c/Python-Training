# 4. Write a NumPy program to compute the determinant of a given square array.

# import numpy 
import numpy as np

# created square array
array1 = np.array([[1,2],[0,4]])

# ans the determinant of a given square array
ans =  np.linalg.det(array1)

# print answer
print(ans)