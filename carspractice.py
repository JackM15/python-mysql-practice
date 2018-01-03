# ---- Cars Practice ---- #
import sqlite3

#create new db
db = sqlite3.connect("cars.db")
#create new cursor
cursor = db.cursor()

#add table called inventory with "make, model, quantity" fields.
cursor.execute("""CREATE TABLE cars
                (make TEXT, model TEXT, quantity INT)
                """)

#close the databse connection
db.close()
