#!/usr/bin/python3
""" Module for task 4"""

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", port=3306,
                     user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute("""
SELECT c.id, c.name, s.name
FROM cities AS c, states AS s
WHERE c.state_id = s.id
ORDER BY c.id ASC
""")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
