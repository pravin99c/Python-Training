#Count the occurrence of each element from a list
list= [11, 45, 8, 11, 23, 45, 23, 45, 89]

# create empty ductionary
dictionary={}

# i is iterator number
for i in list:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i]=1
print(dictionary)