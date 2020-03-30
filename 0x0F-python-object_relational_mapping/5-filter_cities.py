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
    my_state = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=my_user, passwd=my_pasword, db=my_db)
    cur = db.cursor()

    cur.execute('''SELECT cities.name
    FROM states INNER JOIN cities
    ON states.id=cities.state_id
    WHERE states.name=%s ORDER BY cities.id''', (my_state,))

    result_set = cur.fetchall()
    print(", ".join(city[0] for city in result_set))
    cur.close()
    db.close()
