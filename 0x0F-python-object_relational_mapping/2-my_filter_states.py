#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 5:
        exit(1)

    username, password, database, statename = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(host='localhost', port=3305, user=username, passwd=password, db=database, charset='utf8')

    cursor = db.cursor()

    cursor.execute('SELECT * FROM states WHERE name=%s LIMIT 1', (statename,))

    query_r = cursor.fetchall()

    print(query_r)

    cursor.close()
    db.close()
