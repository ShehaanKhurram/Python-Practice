
# _______________ Object into Json Strign _______________
"""
import json
data = {
    "name" : "Shehaan",
    "age" : 20,
    "skills" : ["Python", "C++", "SQL", "UI/UX"]
}
print(type(data))
string = json.dumps(data)
"""

# _______________ Save To and Read From Json File _______________

import json
data = {
    "brand" : "Version",
    "type" : "T-Shirt",
    "price" : 1500
}
# Write
with open("product.json", "w") as f:
    json.dump(data,f)

# Read
#json.load(file) vs json.loads(str)
with open("product.json","r") as f:
    # loaded_data = json.load(f) # passing file
    content = f.read()
    loaded_data = json.loads(content) #passnig string

print(loaded_data)
print(type(loaded_data))

