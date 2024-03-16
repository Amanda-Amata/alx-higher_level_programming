#!/usr/bin/python3
"""takes in an argument and displays all values in the
    states table where name matches the argument."""
import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur.MySQLdb.connect()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    mydb.close()
