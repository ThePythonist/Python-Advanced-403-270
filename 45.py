import json, csv

file = open("orders.json")
data = json.load(file)
orders = []

for i in data["orders"]:
    for j in i["items"]:
        order = [i["customer"]["name"], i["order"]["order_id"], j["barcode"]]
        orders.append(order)

with open("orders.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(orders)
