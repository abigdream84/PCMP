#!/usr/bin/env python

import sqlite3

h=[]
conn = sqlite3.connect('pcmpdb')

cursor = conn.execute("SELECT ipaddrs from cmdb_host")
for row in cursor:
   print row[0]
   h.append(row[0])
print(h)
conn.close()


