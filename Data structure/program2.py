#Count the occurrence of each element from a list
list= [11, 45, 8, 11, 23, 45, 23, 45, 89]
d={}
# for i in range(len(list)):
#     d[list[i]]={}
#     count=1
#     for j in range(len(list)):
#         if j!=i:
#             if list[i]==list[j]:
#                 count += 1
#         d[list[i]]=count
# print(d)

for i in list:
    if i in d:
        d[i] += 1
    else:
        d[i]=1
print(d)