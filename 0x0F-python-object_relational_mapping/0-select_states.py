#!/usr/bin/python3
"""
This module contains a script that lists all states from the database hbtn_0e_0_usa sorted by states.id
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """Connect to the database and retrieve the states"""
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

