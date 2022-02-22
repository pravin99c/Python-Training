"""
Write a Python function that takes a sequence of numbers and determines 
whether all the numbers are different from each other.
"""
list=[1,6,8,9,7,2,1]

def sequence_number(list):
    count=0
    for i in range(len(list)):
        for j in range(len(list)):
            if j!=i:
                if list[i]==list[j]:
                    count=count+1
                else:
                    count=count
    if count<1:
        return True
    else:
        return False
print(sequence_number(list))
