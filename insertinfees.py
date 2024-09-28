import sqlite3

conn = sqlite3.connect("sqlite.db")

ins = '''
    insert into fees VALUES (4,"5500")
'''
conn.execute(ins)
conn.commit()
conn.close()