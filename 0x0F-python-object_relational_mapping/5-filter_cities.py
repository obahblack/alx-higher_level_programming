#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and list all cities of that state
"""

import MySQLdb
from sys import argv
if __name__ = "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    # command to execute to fetch cities data for the specified states
    query = "SELECT cities.name FROM states INNER JOIN cities ON states.id = cities.state_id WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (argv[4], ))

    # format the printing of cities of same separated by commas
    print(', '.join(["{:s}".format(row[0]) for row in cursor.fetchall()]))

    cursor.close()
    db.close()
