#3. Write a Python program to get a list, sorted in increasing order by the last
#out put  [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
 
list.sort(key=lambda x:x[1])
print(list)