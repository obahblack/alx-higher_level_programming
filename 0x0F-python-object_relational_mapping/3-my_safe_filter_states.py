#!/usr/bin/python3
"""
How to accept arguments thats safe from MySQL injection
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to db
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (argv[4],))

    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
