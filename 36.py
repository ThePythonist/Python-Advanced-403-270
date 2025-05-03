import json



# ========================== 1 ==========================
# salaries = []
# with open("payments.json") as f:
#     data = json.load(f)
#     employees = data["employees"]
#
#     for i in employees:
#         for j in i["monthly_payment"].values():
#             salaries.append(j)
#
# avg = sum(salaries) / len(salaries)
# print(f"Average salary for company : {avg}")

# ========================== 2 ==========================

with open("payments.json") as f:
    data = json.load(f)
    employees = data["employees"]

    for i in employees:
        avg = sum(i["monthly_payment"].values()) / 12
        print(avg)
