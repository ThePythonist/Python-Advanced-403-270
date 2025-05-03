import json

# f = open("payments.json")

with open("payments.json") as f:  # automatically closes the file
    data = json.load(f)
    employees = data["employees"]

    for i in employees:
        print(i["name"], ":", i["job_title"])
