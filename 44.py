import csv

with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if "computer" in row[-1]:
            print(row)
