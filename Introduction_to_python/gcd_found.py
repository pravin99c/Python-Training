def gcd(a,b):
    if (a==0):
        return b
    if (b == 0):
         return a
    return gcd(b, a%b)
a = 10
b = 6

if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('not found')