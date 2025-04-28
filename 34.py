import json

f1 = open("states.json")
data = json.load(f1)
selection = []

for i in data["states"]:
    if i["name"].lower() in ["alaska", "new york", "florida"]:
        selection.append(i)

output = {"states": selection}
f2 = open("selected_states.json", "w")
json.dump(output, f2, indent=4)
