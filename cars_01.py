#---- insert 5 records into the inventory table in the cars db ----#

import sqlite3

#connect to cars db which has the following columns (make, model, quantity)
with sqlite3.connect("cars.db") as db:
    cursor = db.cursor()

    #cars list of tuples
    cars = [
        ("Ford", "Escort", 49 ),
        ("Honda", "Civic", 50),
        ("Ford", "Mustang", 3),
        ("Ford", "Focus", 88),
        ("Honda", "Accord", 23)
    ]

    #insert data into table
    try:
        cursor.executemany('INSERT INTO cars VALUES(?, ?, ?)', cars)
    except sqlite3.OperationalError:
        print("Something went wrong, please try again!")
