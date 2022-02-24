#Sort given array of three random elements. 0,1 & 2. Without any sorting
# list1=[1,0,2,2,0,1,0,1,2,0,0]
# output=[0,0,0,0,0,1,1,1,2,2,2]
list1=[1,0,2,2,0,1,0,1,2,0,0]

list2=[]
list3=[]
list4=[]
for i in list1:
    if i==0:
        list2.append(i)
    elif i==1:
        list3.append(i)
    else:
        list4.append(i)
list2.extend(list3)
list2.extend(list4)
print(list2)