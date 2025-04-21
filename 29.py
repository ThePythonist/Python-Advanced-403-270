import sqlite3


def create_table():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS students (name,field,grade);")

    conn.commit()
    conn.close()
    print("Done")


def insert_data():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO students VALUES ('mahdieh','memari',17.56);")
    cur.execute("INSERT INTO students VALUES ('reza','mohandesi bargh',14.78);")
    cur.execute("INSERT INTO students VALUES ('saeed','olom computer',19.35);")
    cur.execute("INSERT INTO students VALUES ('kiana','daroo sazi',16.98);")

    conn.commit()
    conn.close()
    print("Done")


def select_table():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM students;")
    records = cur.fetchall()

    for i in records:
        if i[-1] >= 17:
            print(i)

    conn.close()


# create_table()
# insert_data()
select_table()
