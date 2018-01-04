# SQLite Functions
import sqlite3

with sqlite3.connect("new.db") as db:
    cursor = db.cursor()

    #create a dictionary of SQL queries
    sql = {
        'average': "SELECT avg(population) FROM population",
        'maximum': "SELECT max(population) FROM population",
        'minimum': "SELECT min(population) FROM population",
        'sum': "SELECT sum(population) FROM population",
        'count': "SELECT count(city) FROM population"
    }

    #run each query item in the dictionary
    for keys, values in sql.items():
        cursor.execute(values)

        #fetchone returns a single record from the query
        result = cursor.fetchone()

        #ouput to screen
        print(keys + "'", result[0])