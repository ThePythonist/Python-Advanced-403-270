import xmltodict

file = open("payments.xml").read()
xml_dict = xmltodict.parse(file)
root = xml_dict["employees"]
employees = root["employee"]

python_salaries = []

for i in employees:
    if "python" in i["job_title"].lower():
        employee_salary = []
        for j in i["monthly_payment"].values():
            employee_salary.append(int(j))

        # miangin daramad har shakhs dar 12 mah
        avg = sum(employee_salary) / 12
        python_salaries.append(avg)

# miangin daramad kole python kar ha
avg = sum(python_salaries) / len(python_salaries)
print("Average salary for a python developer :", avg)
