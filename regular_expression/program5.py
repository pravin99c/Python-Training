# 5.Write a regular expression to get only the part of the email before the "@" 
# sign and include the "@" sign

import re

email="pravinc._2022vj@gmail.com"

world=re.findall(r'[A-Za-z._0-9]+@',email)
print(world)