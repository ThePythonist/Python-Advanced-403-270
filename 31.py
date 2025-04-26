import sqlite3


def create_table():
    conn = sqlite3.connect("tables.db")
    cur = conn.cursor()

    table_name = input("Enter table name : ")
    table_columns = tuple(input("Enter table columns : ").split(","))

    query = f"CREATE TABLE IF NOT EXISTS {table_name} {table_columns};"
    cur.execute(query)

    print("Created table")
    conn.commit()
    conn.close()


def insert_record():
    pass


def select_table():
    conn = sqlite3.connect("tables.db")
    cur = conn.cursor()

    table_name = input("Enter table name : ")
    query = f"SELECT * FROM {table_name};"
    cur.execute(query)
    records = cur.fetchall()

    for i in records:
        print(i)

    conn.close()


def main():
    entry = input("""
Hello, Welcome to DB manager
1 : Create table
2 : Insert record into table
3 : See a table
Choose : """)

    if entry == "1":
        create_table()
    elif entry == "2":
        insert_record()
    elif entry == "3":
        select_table()
    else:
        print("Invalid option, Try again.")
        main()


main()
