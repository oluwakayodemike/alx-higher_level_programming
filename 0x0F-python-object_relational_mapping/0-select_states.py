#!/usr/bin/python3
import MySQLdb
import sys

# Gather command line args
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
db_name = sys.argv[3]

# Connect to MySQL server
db = MySQLdb.connect(user=mysql_username, passwd=mysql_password, db=db_name, port=3306, host="localhost")

# Create cursor and execute query
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch results and display them
query_results = cur.fetchall()
for row in query_results:
    print(row)

# Close cursor and database connection
cur.close()
db.close()

