#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys import argv

if __name__ == "__main__":
    
    # connect to database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    # create cursor to exec queries using SQL
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    results = cursor.fetchall()
    
    # Display the reults
    for row in results:
        print(row)
    cursor.close()
    db.close()
