#!/usr/bin/node
import MySQLdb

db = MySQLdb.connect(host="localhost", user='root', passwd='123456', db='hbtn_0e_0_usa')
cur = db.cursor()

states = cur.execute('SELECT states FROM hbtn_0e_0_usa')

for element in states:
    print(element)
