#!/usr/bin/python3
"""
filters and return states startin with 'N'
parameters given to script: username, password, database
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    
    # connect to database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    results = cursor.fetchall()

    for row in results:
        print(row)
    cursor.close()
    db.close()
