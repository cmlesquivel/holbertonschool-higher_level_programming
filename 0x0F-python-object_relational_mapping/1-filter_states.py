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

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=my_user, passwd=my_pasword, db=my_db)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    result_set = cur.fetchall()
    for row in result_set:
        print(row)
