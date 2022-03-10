# 5. Write a NumPy program to compute the eigenvalues and eigenvectors 
# of a given square array.

# import numpy as np
import numpy as np

a = np.array([[3, 1], [2, 2]])


w, v = np.linalg.eig(a)
# Eigenvalues of the said matrix"
print(w)
# Eigenvectors of the said matrix
print(v)
