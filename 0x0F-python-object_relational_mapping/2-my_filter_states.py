#!/usr/bin/python3
"""
Script that Filter states
"""

import MySQLdb
import sys

if __name__ == "__main__":
    my_user = sys.argv[1]
    my_pasword = sys.argv[2]
    my_db = sys.argv[3]
    myState = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=my_user,
                         passwd=my_pasword, db=my_db, charset="utf8")
    cur = db.cursor()
    query = 'SELECT * FROM states WHERE name ="{}" ORDER BY id'.format(myState)

    cur.execute(query)

    result_set = cur.fetchall()
    for row in result_set:
        print(row)
    cur.close()
    db.close()
