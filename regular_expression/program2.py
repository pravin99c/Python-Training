# 2. Find the words with exactly 8 letters from paragraph using regex
import re

str = "sjkfjjcap dxgvhjhx fsjh klklZAx bkjhbz bch" 
array = re.findall(r'\b[a-zA-Z]{8}\b', str)
print(*array)
