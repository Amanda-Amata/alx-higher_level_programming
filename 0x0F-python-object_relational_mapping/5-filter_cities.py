#!/usr/bin/python3
"""ists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = mydb.cursor()
    cur.execute("""SELECT cities.name FROM cities INNER JOIN states ON cities.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    results = cur.fetchall()
    tmp = list(results[0] for row in results)
    print(*tmp, sep=", ")
    cur.close()
    mydb.close()

