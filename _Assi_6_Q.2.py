
# Q.2). Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

import json

json_obj = """{
"1) Maharashtra": "Mumbai",
"2) Andhra Pradesh": "Amaravati",
"3) Arunachal Pradesh": "Itanagar",
"4) Assam": "Dispur",
"5) Bihar": "Patna",
"6) Chhattisgarh":	"Raipur",
"7) Gujarat":	"Gandhinagar"
}"""

data = json.loads(json_obj)
print(data)

print("\n",type(data))