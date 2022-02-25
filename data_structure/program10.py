#  Find the max sum of sub array
# 			Ex L = [5, 4, 7, -2, 5, 0, 6, 9, 15, -3]
# 			Output = 49

# L = [5, 4, 7, -2, 5, 0, 6, 9, 15, -3]
list = [6, 3, -2, -1, -4, -2, -3, -15, 7, 9, 8]

def Max_sum(L,len_l):
    sum=0
    max=0
    for i in range(0,len_l):
        max=max+list[i]
        if sum < max:
            sum=max
        if max < 0:
            max=0
    return sum
print(Max_sum(list,len(list)))