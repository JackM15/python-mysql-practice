#---- INSERT commend with Error Handling ----#

import sqlite3

#create the connection object
conn = sqlite3.connect("new.db")

#create cursor
cursor = conn.cursor()

try:
    #insert data
    cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8400000)")
    cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 800000)")

    #commit changes
    conn.commit()
except sqlite3.OperationalError:
    print("Oh No, something went wrong, try again!")

#close the db connection
conn.close()