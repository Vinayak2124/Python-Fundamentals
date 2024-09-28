import sqlite3

conn = sqlite3.connect("sqlite.db")

conn.execute('''
        update student set s_name = 'Atharva66' where s_id = 9 
             ''')
conn.commit()
conn.close()