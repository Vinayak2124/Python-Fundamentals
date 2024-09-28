import sqlite3

conn = sqlite3.connect("sqlite.db")

conn.execute('''
             create table fees(
                 s_id INT,
                 Amount VARCHAR(10)
             )
             '''

    
)

conn.close() 
