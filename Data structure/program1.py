list= [11, 45, 8, 23, 14, 12, 78, 45, 89,25,]

new_list=[]
n=3
len_list=int((len(list)/n))
for i in range(len_list):
    T=list[:3]
    T.reverse()
    new_list.append(T)
    list = list[3:]
print(new_list)
    