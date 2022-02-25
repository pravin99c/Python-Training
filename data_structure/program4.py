#4. Find the intersection (common) of two sets and remove those elements from the first set.
from ast import Dict


dic1= {23, 42, 65, 57, 78, 83, 29}
dic2={57, 83, 29, 67, 73, 43, 48}
# d={}
# l=[]
# for i in dic1:
#     for j in dic2:
#         if i==j:
#             l.append(i)
# d=set(l)
# dic1-=d
# print(d,",",dic1)

print( dic1 & dic2, ",",dic1-dic2 )