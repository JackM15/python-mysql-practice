#---- Update the quantity of cars on 2 records then print all from the table ----#

import sqlite3

with sqlite3.connect("cars.db") as db:
    cursor = db.cursor()

    #update values
    try:
        cursor.execute("UPDATE cars SET quantity = 90 WHERE model = 'Mustang'")
        cursor.execute("UPDATE cars SET quantity = 10 WHERE model = 'Accord'")
    except sqlite3.OperationalError:
        print("Something went wrong, try again.")

    #print values, select all then fetch then print
    cursor.execute("SELECT * FROM cars")
    rows = cursor.fetchall()

    for car in rows:
        print(car[0], car[1], car[2])