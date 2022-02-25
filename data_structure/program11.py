# Return product of minimum of odd and maximum of even from a given list.
#   Sample = [7, 5,  2, 3, 12, 9, 15, 24]
#        Output = 72          #  (24 max even * 3 min odd)

list1 = [7, 5,  2, 3, 12, 9, 15, 24]
max=0
min=0
for i in list1:
    if i%2==0:
        if max < i:
            max = i
    elif i%1==0:
        if min==0:
            min=i
        elif min > i:
            min = i
print(max*min)
