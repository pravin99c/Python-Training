numbers = [5, 17, 2, 6, 3]
# numbers = [10, 5, 7, 12, 3, 6]
nums_greater_than_right = []
for i in range(len(numbers)):
    if i != len(numbers)-1:
        if numbers[i] > max(numbers[i+1:]):
            nums_greater_than_right.append(numbers[i])
    else:
        nums_greater_than_right.append(numbers[i])         
print(nums_greater_than_right)
