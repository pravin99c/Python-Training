# 6.Replace all special characters with space using regex
import re
string ="fy@cgkjzkjx%8ghguj*@hxkhz$jkZXkj"

name = re.sub(r'[~!@#$%^&*?]'," ",string)
print(name)