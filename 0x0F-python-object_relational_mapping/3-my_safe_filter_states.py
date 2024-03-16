#!/usr/bin/python3
""" takes in arguments and displays all values in the states table
    write one that is safe from MySQL injections!"""
import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = mydb.cursor()
    match = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    mydb.close()
