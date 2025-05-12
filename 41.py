import xmltodict
import dicttoxml

file = open("flights.xml").read()
xml_dict = xmltodict.parse(file)
root = xml_dict["flights"]
flights = root["flight"]
paris_flights = []

for i in flights:
    if i["destination"].lower() == "paris":
        paris_flights.append(i)

# ==========================================================


# Convert selected list into XML format
xml_output = dicttoxml.dicttoxml({'flights': paris_flights})
with open("paris_flights.xml", "wb") as f:
    f.write(xml_output)
