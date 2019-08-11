#!/usr/bin/python3
""" Module for task 5"""

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", port=3306,
                     user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute("""
SELECT c.name FROM cities AS c
LEFT JOIN states ON states.id = c.state_id
WHERE states.name = '%s' ORDER BY c.id ASC
""" % (sys.argv[4], ))
rows = cur.fetchall()
print(", ".join([row[0] for row in rows]))
cur.close()
db.close()
