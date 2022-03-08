# 4.Loop through the list and apply the regex to each element so that only items
#  ending with a semicolon (;) are matched


import re

str = ['dfsghzchjj;' 'hkjh,mb', 'jKHJ;' ,'cjczkh', 'x','khb' 'Z','hkn', 'khjn;']
for i in str:
    if re.findall(r';$',i):
        print(i)
