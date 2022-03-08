# 2.Write a code to load a .json file and print JSON data.
#  Display error if a file is empty or data is not in a json format.  

import json

employee ='{"id":"09", "name":"pravin","deparment":"Python"}'


employee_dict = json.loads(employee)
print(employee_dict)
with open("data.json", "w") as outfile:
    json.dump(employee_dict, outfile)

try:
    f = open('data.json',)
    data = json.load(f)

    for i in data:
        print(i)

    f.close()
except Exception as e:
    print(e)