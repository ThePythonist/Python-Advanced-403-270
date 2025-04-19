import sqlite3

conn = sqlite3.connect("info.db")
cur = conn.cursor()

# cur.execute("CREATE TABLE customers (name,city,phone);")
# cur.execute("INSERT INTO customers VALUES ('mohammad','yazd','09300348590');")
# cur.execute("INSERT INTO customers VALUES ('kiarash','qazvin','09394807140');")
# cur.execute("INSERT INTO customers VALUES ('sina','rasht','09309130561');")
# cur.execute("INSERT INTO customers VALUES ('reza','tehran','09308758649');")

cur.execute("SELECT * FROM customers;")
# cur.execute("SELECT phone FROM customers;")
records = cur.fetchall()

for i in records:
    print(i[-1])
    # print(i)

conn.commit()
conn.close()
