#Select statement with unicode characters removed

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("SELECT firstname, lastname from employees")

    # fetchall() retrieves all records from the query as a list of tuples
    rows = c.fetchall()

    #output rows to the screen row by row
    for row in rows:
        print(row[0], row[1])
        