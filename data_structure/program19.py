# Find the overlapping area of two rectangles
# Rectangles can be in any direction
# A = 2      E = 4   left point
# B = 2      F = 4   top point
# C = 6      G = 8   right point
# D = 6      H = 8   bottom point

# Ans = 4

# def overlapping(A1,A2,A3,A4):
#     x=0
#     y=0
#     left_point = min(A2[x],A4[x])-max(A1[y],A3[y])
#     right_point = min(A2[x],A4[x])-max(A1[y],A3[y])
#     ans=0
#     if left_point>0 and right_point>0:
#         ans = left_point * right_point
#     return ans

# A1=[2, 1]
# A2=[3, 2]
# A3=[5, 5]
# A4=[5, 7]
# print(overlapping(A1,A2,A3,A4))



def overlappingArea(l1, r1, l2, r2):
    x = 0
    y = 1
 
    x_dist = (min(r1[x], r2[x]) - max(l1[x], l2[x]))
 
    y_dist = (min(r1[y], r2[y]) - max(l1[y], l2[y]))
    areaI = 0
    if x_dist > 0 and y_dist > 0:
        areaI = x_dist * y_dist
 
    # return (area1 + area2 - areaI)
    return areaI
 
# Driver's Code
l1 = [0, 0]
r1 = [2, 2]
l2 = [1.5, -1]
r2 = [3, 3]

print(overlappingArea(l1, r1, l2, r2))