# Add 1 to given list elements. Do not use string conversion.
# Sample = [1, 2, 3]
# Output = [1, 2, 4]


list1 = [1,2,3]
list_len=len(list1)
sum=1
len_of_list=len(list1)-1
for i in range(len(list1)):
    s = 10 ** len_of_list
    val = list1[i]*s
    sum = sum + val
    len_of_list -= 1
list2=[]
# print(sum)
list3=[]
while(sum>0):
    temp=sum%10
    list2.append(temp)
    sum=sum//10

for i in range(len(list2)-1,-1,-1):
    list3.append(list2[i])
print(list3)