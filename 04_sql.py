#---- Import from CSV ----#

#import csv library
import csv
import sqlite3

#make connection and cursor
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    #open the csv file and assign it to a variable
    employees = csv.reader(open("employees.csv", 'rU'))

    #create a new table in the database called employees
    c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

    #insert data into the table
    c.executemany("INSERT INTO employees(firstname, lastname) values (?, ?)", employees)
