#!/usr/bin/python3
"""
A script that takes in an argument input and displays all values in the state table that match the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    
    cursor = db.cursor()
    # this the select from state what is the same as user input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(argv[4])
    
    # execute the SQL query
    cursor.execute(query)
    results = cursor.fetchall()

    # Display the result
    for row in results:
        print(row)
    cursor.close()
    db.close()
