import sqlite3

conn = sqlite3.connect("sqlite.db")

data = conn.execute("SELECT * FROM student limit 0,5")

for n in data:
    print(n)
