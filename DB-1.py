import sqlite3

conn = sqlite3.connect("info.db")
cur = conn.cursor()

# cur.execute("CREATE TABLE students (name,age,phone);")
# cur.execute("INSERT INTO students VALUES ('mohammad','16','09300348590');")
# cur.execute("INSERT INTO students VALUES ('kiarash','20','09394807140');")
# cur.execute("INSERT INTO students VALUES ('sina','23','09309130561');")
# cur.execute("INSERT INTO students VALUES ('reza','24','09308758649');")

cur.execute("SELECT * FROM students;")  # Selects all records
# cur.execute("SELECT * FROM students WHERE age>='20';") # Selects specific records
# cur.execute("DELETE FROM students WHERE age>'23';") # Deletes specific records in a table
# cur.execute("DELETE FROM students;") # Deletes all records in the table
# cur.execute("DROP TABLE students;") # Deletes the table

records = cur.fetchall()

print(records)

# for i in records:
#     print(i)

conn.commit()
conn.close()
