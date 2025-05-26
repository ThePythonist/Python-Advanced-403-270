import csv

students = [
    ["name", "grade", "field"],
    ["aria", "17.05", "computer engineering"],
    ["zahra", "18.95", "architecture"],
    ["taha", "16.17", "computer engineering"],
    ["kiana", "14.50", "chemical engineering"],
]


def write_students(data):
    with open("students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)


write_students(students)
