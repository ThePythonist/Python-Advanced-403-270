import json

salaries = {}
with open("payments.json") as f:
    data = json.load(f)
    employees = data["employees"]

    for i in employees:
        avg = sum(i["monthly_payment"].values()) / 12
        salaries.setdefault(i["name"], avg)

print(sorted(salaries.items(), key=lambda x: x[1]))
