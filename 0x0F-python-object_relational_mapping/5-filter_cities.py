#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    cursor.execute(
        "SELECT cities.name FROM cities JOIN states \
                ON cities.state_id = states.id "
        "WHERE states.name = %s ORDER BY cities.id",
        (state_name,)
    )

    cities = cursor.fetchall()
    print(", ".join(city[0] for city in cities))

    cursor.close()
    db.close()
