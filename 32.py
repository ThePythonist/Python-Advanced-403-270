import json

f = open("states.json")
data = json.load(f)

for i in data["states"]:
    print(i["name"])