#!/usr/bin/python3

'''
    List all states mathch the arguments db
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        exit(1)

    username, password, database = argv[1], argv[2], argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
