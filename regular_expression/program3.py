# 3.Find the numbers starting with 212 from a string.


import re
str='hjsfuskh bushi 212sf 212656  hagjg zh 212 21256 212shf'


word=re.split('\s',str)

for i in word:
    if re.search(r'^212\d',i):
        print(i)