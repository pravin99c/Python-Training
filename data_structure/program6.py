# 6. Create a function to reverse the entire list without any function and 
# also do not use any indexing or slicing shortcut. Time Complexity O(logn)

list=[1,2,3,4,5,6,7,8,9]

list_len=len(list)
strat_index=0
end_index=list_len-1

while strat_index < end_index:
    list[strat_index],list[end_index] = list[end_index], list[strat_index]
    strat_index += 1
    end_index -= 1
print(list)