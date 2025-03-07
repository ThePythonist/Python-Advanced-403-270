from faker import Faker
from pprint import pprint
from tools import phonenumbers

fake = Faker()

people = []

for i in range(4):
    name = fake.name()
    person = {
        "name": name,
        "email": f"{name}@gmail.com".replace(" ", "_"),
        "country": fake.country(),
        "phone": phonenumbers.irancell()
    }

    people.append(person)

pprint(people)
