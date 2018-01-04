#---- Select all ford cars from db ----#
import sqlite3

with sqlite3.connect("cars.db") as db:
    cursor = db.cursor()

    try:
        #fetch all data that is a ford
        cursor.execute("SELECT * FROM cars WHERE make = 'Ford'")
    except sqlite3.OperationalError:
        print("fail.")
    
    #print data
    fords = cursor.fetchall()

    for car in fords:
        print(car[0], car[1], car[2])