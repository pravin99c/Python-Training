# 1. Slice list into 3 equal chunks and reverse each chunk

list= [11, 45, 8, 23, 14, 12, 78, 45, 89,25,]

# create empty list
new_list=[]

# Slice list into 3
slice_list_number=3

# len of list 
len_list=int((len(list)/slice_list_number))
for i in range(len_list):
    list_3_number=list[:3]
    list_3_number.reverse()
    new_list.append(list_3_number)
    list = list[3:]
print(new_list)
    