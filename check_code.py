from unittest import result
import numpy as np
 
# # Integer datatype
# # guessed by Numpy
# x = np.array([1, 2])  
# print("Integer Datatype: ")
# print(x.dtype)         
 
# # Float datatype
# # guessed by Numpy
# x = np.array([1.0, 2.0]) 
# print("\nFloat Datatype: ")
# print(x.dtype)  
 
# # Forced Datatype
# x = np.array([1, 2], dtype = np.int64)   
# print("\nForcing a Datatype: ")
# print(x.dtype)


"""
# Creating array from list with type float
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
print ("Array created using passed list:\n", a)
 
# Creating array from tuple
b = np.array((1 , 3, 2))
print ("\nArray created using passed tuple:\n", b)
 
# Creating a 3X4 array with all zeros
c = np.zeros((3, 4))
print ("\nAn array initialized with all zeros:\n", c)
 
# Create a constant value array of complex type
d = np.full((3, 3), 6, dtype = 'complex')
print ("\nAn array initialized with all 6s.""Array type is complex:\n", d)
"""

"""
# Python program to demonstrate
# unary operators in numpy
import numpy as np
 
arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])
 
# maximum element of array
print ("Largest element is:", arr.max())
print ("Row-wise maximum elements:",
                    arr.max(axis = 1))
 
# minimum element of array
print ("Column-wise minimum elements:",
                        arr.min(axis = 0))
 
# sum of array elements
print ("Sum of all array elements:",
                            arr.sum())
 
# cumulative sum along each row
print ("Cumulative sum along each row:\n",
                        arr.cumsum(axis = 1))
"""
"""
import numpy as geek
 
# restep set to True
print("B\n", geek.linspace(2.0, 3.0, num=5, retstep=True), "\n")
 
# To evaluate sin() in long range 
x = geek.linspace(0, 2, 10)
print("A\n", geek.sin(x))


"""


# import numpy as np
 
# # Creating a rank 1 Array
# arr = np.array([1, 2, 3])
# print("Array with Rank 1: \n",arr)
 
# # Creating a rank 2 Array
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])
# print("Array with Rank 2: \n", arr)
 
# # Creating an array from tuple
# arr = np.array((1, 3, 2))
# print("\nArray created using "
#       "passed tuple:\n", arr)


# Initial Array
# arr = np.array([[-1, 2, 0, 4],
#                 [4, -0.5, 6, 0],
#                 [2.6, 0, 7, 8],
#                 [3, -7, 4, 2.0]])
# print("Initial Array: ")
# print(arr)
 
# Printing a range of Array
# with the use of slicing method
# sliced_arr = arr[:2, ::2]
# print ("Array with first 2 rows and"
#     " alternate columns(0 and 2):\n", sliced_arr)
 
# # Printing elements at
# # specific Indices
# Index_arr = arr[[1, 1, 0, 3], 
#                 [3, 2, 1, 0]]
# print ("\nElements at indices (1, 3), "
#     "(1, 2), (0, 1), (3, 0):\n", Index_arr)

# import numpy as np

# Creating array from list with type float
# a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
# print ("Array created using passed list:\n", a)

# # Creating array from tuple
# b = np.array((1 , 3, 2))
# print ("\nArray created using passed tuple:\n", b)

# # Creating a 3X4 array with all zeros
# c = np.zeros((3, 4),dtype = 'int')
# print ("\nAn array initialized with all zeros:\n", c)

# # Create a constant value array of complex type
# d = np.full((3, 3), 6, dtype = 'complex')
# print ("\nAn array initialized with all 6s."
# 			"Array type is complex:\n", d)

# iterate through rows

"""
index value get
import numpy as np
 
# NumPy array with elements from 1 to 9
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
 
# Index values can be negative.
arr = x[np.array([3, 3, -3])]
print("\n Elements are : \n",arr)

"""

# import numpy as np
 
# # A 3-Dimensional array
# a = np.array([[0, 1, 2, 3, 4, 5],
#               [6, 7, 8, 9, 10, 11],
#               [12, 13, 14, 15, 16, 17],
#               [18, 19, 20, 21, 22, 23],
#               [24, 25, 26, 27, 28, 29],
#               [30, 31, 32, 33, 34, 35]])
# print("\n Array is:\n ",a)
 
# # slicing and indexing
# print("\n a[0, 3:5]  = ",a[0, 3:5]) 
 
# print("\n a[4:, 4:]  = ",a[4:, 4:]) 
 
# print("\n a[:, 2]  = ",a[:, 2]) 
 
# print("\n a[2:;2, ::2]  = ",a[2::2,::2]) 

import numpy as np
 
b = np.array([[5, 5, 5],[4, 5, 3],[1, 4, 2]])
sumrow = b.sum(0)
print(sumrow)
print(b[sumrow%10==0])