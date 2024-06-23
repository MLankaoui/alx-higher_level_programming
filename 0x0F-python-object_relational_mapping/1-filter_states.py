#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if (len(argv) != 4):
        exit(1)

    usernmane, password, database = argv[1], argv[2], argv[3]

    try:
        db = MySQLdb.connect(host='localhost', port=3006, user=usernmane, passwd=password, database=database)

        cursor = db.cursor()

        cursor.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY id ASC')

        query_r = cursor.fetchall()

        for element in query_r:
            print(element)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        exit(1)