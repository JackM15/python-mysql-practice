# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

#create a new database if the database doesnt exist already
conn = sqlite3.connect("new.db")

#create a cursor object to execute sql commands
cursor = conn.cursor()

#add data to the database
cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8400000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

#commit the changes to db
conn.commit()

#close the database connection
conn.close()