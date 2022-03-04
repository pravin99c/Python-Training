# Return the array which contains the elements which are greater than from its right side
# Sample = [5, 17, 2, 6, 3]
	# Output = [17, 6, 3] 

# list1 = [5, 17, 2, 6, 3]
# list2=[]
# s=len(list1)-1
# for i in range(len(list1)):
#     value=list1[i]
#     flags=0
#     for j in range(i+1,len(list1)):
#         if value > list1[j]:
#             flags=1
#         else:
#             flags = 0
#             break
#     if flags > 0:
#         list2.append(value)
#     elif i==s:
#         list2.append(value)
                    
# print(list2)



number_list=[5, 17, 2, 6, 3]
number_list2=[]

for i in range(len(number_list)):
    if i !=(len(number_list)-1):
        if number_list[i] > max(number_list[i+1:]):
            number_list2.append(number_list[i])
    else:
        number_list2.append(number_list[i])
print(number_list2)

