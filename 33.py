import json

f1 = open("states.json")
data = json.load(f1)
names = []

for i in data["states"]:
    names.append(i["name"])

output = {"states": names}
f2 = open("state_names.json", "w")
json.dump(output, f2, indent=4)
