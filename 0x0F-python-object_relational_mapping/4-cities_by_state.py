#!/usr/bin/python3
"""
Script that show cities by states
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

    cur.execute('''SELECT cities.id, cities.name, states.name
                FROM states
                INNER JOIN cities
                ON states.id=cities.state_id ORDER BY states.id''')

    result_set = cur.fetchall()
    for row in result_set:
        print(row)
