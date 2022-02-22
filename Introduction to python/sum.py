def add(x,y):
    while y!=0:
        # sum=0
        sum= x & y #add
        # print("sum",sum)
        x= x ^ y # Xor 
        # print("x",x)
        y= sum << 1 # shift
        # print(y)
    return x
print(add(10,20))
