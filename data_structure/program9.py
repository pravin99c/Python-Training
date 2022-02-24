# Count the subsequence “AG” in the given string.
# 			Ex. S = “BCAHGBNAJKGTYUALKWG”
# 			Output: 6

S = "BCAHGBNAJAKGTYUALKWGG"
count=0
for i in S:
    if i=='A':
        count += 1
    elif i=='G':
        count += 1

print(count)