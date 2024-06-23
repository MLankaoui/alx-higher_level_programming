#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 5:
        exit(1)

    username, password, database, statename = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'".format(statename))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
