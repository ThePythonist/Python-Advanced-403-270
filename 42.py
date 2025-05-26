import xml.etree.ElementTree as ET

xml_data = open("flights.xml").read()
root = ET.fromstring(xml_data)
flights = root.findall("flight")
william_flights = []

for flight in flights:
    passengers_root = flight.find("passengers")
    for passenger in passengers_root:
        if passenger.find("name").text == "William Thompson":
            william_flights.append(flight.find("flight_number").text)

print(william_flights)
