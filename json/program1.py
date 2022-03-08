# 1. Create class Vehicle with properties name, engine, and price.
#  Create vehicle object and convert it into JSON and vice-versa.

import json
class Vehicle():
    def __init__(self,name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

    
vehicle = Vehicle("Scorpio s11", "2179 cc", "18.15lakh")

json_convert = json.dumps(vehicle.__dict__)
print(type(json_convert))

with open('file.json','w') as file:
    json.dump(vehicle.__dict__,file)

with open('file.json','r') as file:
    x=json.load(file)
