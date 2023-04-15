#!/usr/bin/python3
"""
This module retrieves all the states from the hbtn_0e_0_usa database and
prints them in ascending order by ID.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Retrieve all states from the database
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    # Print the states in the desired format
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    conn.close()

