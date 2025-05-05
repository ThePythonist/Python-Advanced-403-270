import xmltodict

file = open("payments.xml").read()
xml_dict = xmltodict.parse(file)
root = xml_dict["employees"]
employees = root["employee"]

for i in employees:
    if int(i["age"]) <= 30:
        print(i)
