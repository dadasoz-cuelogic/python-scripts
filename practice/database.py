#!/usr/bin/python
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","python" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql="insert into employee(name,email,mobile) values('vishal','vishal@gmail.com','9890555555')"

# execute SQL query using execute() method.

i=0;

while i<200000:
    cursor.execute(sql)
    i=i+1

#Commit the save changes on Database
db.commit()

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " %data

# disconnect from server
db.close()

