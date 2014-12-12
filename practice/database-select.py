#!/usr/bin/python
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","python" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql="insert * from employee"

# execute SQL query using execute() method.

try:

    cursor.execute(sql)
    
    result=cursor.fetchall()
    
    for row in result:
        print 'xx'
        
except:
    print "Error"
# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " %data

# disconnect from server
db.close()

