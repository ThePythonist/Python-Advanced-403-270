import json
from colorama import Fore

salaries = {}
with open("payments.json") as f:
    data = json.load(f)
    employees = data["employees"]

    for i in employees:
        avg = sum(i["monthly_payment"].values()) / 12
        salaries.setdefault(i["name"], avg)

    max_salary = max(salaries.values())

    for k, v in salaries.items():
        if v == max_salary:
            print(Fore.CYAN + k, ":", v)
        else:
            print(Fore.LIGHTWHITE_EX + k, ":", v)
