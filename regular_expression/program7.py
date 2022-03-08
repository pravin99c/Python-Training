# 7. Replace the space character that occurs after a word ending with a or r with a newline character
# Sample input: area not a _a2_ roar took 22
# Sample output:
# area
# not a
# _a2_ roar
# took 22


import re

string =  "area not a _a2_ roar took 22"

reg = r'\b[a-z]*a\b|\b[a-z]*r\b'

word = re.findall(reg,string)
string_list=string.split()
str_count =''

for i in string_list:
    str_count=str_count+i+' '
    if i in word:
        str_count = str_count + '\n'
print(str_count)