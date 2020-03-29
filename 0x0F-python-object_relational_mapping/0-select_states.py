#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hbtn_0e_0_usa')

cur = db.cursor()

states = cur.execute("SELECT * FROM states")
print(type(states))
