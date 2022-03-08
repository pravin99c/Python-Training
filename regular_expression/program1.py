# 1. Write a regular expression to search digits inside a string

import re
str = "11hello 3562655and"

array = re.findall(r'[0-9]+', str)
  
print(*array)
print(array)