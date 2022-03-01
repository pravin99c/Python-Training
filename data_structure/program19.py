# Find the overlapping area of two rectangles
# Rectangles can be in any direction
# A = 2      E = 4   left point
# B = 2      F = 4   top point
# C = 6      G = 8   right point
# D = 6      H = 8   bottom point

# Ans = 4

def overlapping(A1,A2,A3,A4):
    x=0
    y=0
    left_point = min(A2[x],A4[x])-max(A1[y],A3[y])
    right_point = min(A2[x],A4[x])-max(A1[y],A3[y])
    
    ans=0
    if left_point>0 and right_point>0:
        ans = left_point * right_point
    return ans

A1=[2,2]
A2=[6,6]
A3=[4,4]
A4=[8,8]
print(overlapping(A1,A2,A3,A4))

