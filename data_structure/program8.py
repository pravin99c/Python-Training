# Return the sum of duplicates elements from the given List
			# Ex. L = [3, 5, 6, 11, 12, 3, 5, 2]
			# Output = 8 (3+5)
# L = [3, 5, 6, 11, 12, 3, 5, 2]
# d={}
# sum=0
# for i in L:
# 	if i in d:
# 		sum += i
# 	else:
# 		d[i] = i
# print(sum)

list1 = [3, 5, 6, 11, 12, 3, 5, 2,3]

dictonary = {}
count = 0

for i in list1:
	if i not in dictonary.keys():
		dictonary[i] = 1
	else:
		x=dictonary[i]
		dictonary[i] += x+1
for key,value in dictonary.items():
	if value > 1:
		count += int(key)
print(count) 

