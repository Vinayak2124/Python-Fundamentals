import sqlite3
conn = sqlite3.connect("sqlite.db")
ins = '''
    insert into student (s_id,s_name,s_class,S_email) VALUES (11,'xyz',"T.E IT","bac@gmail.com")
    
    
    
'''
conn.execute(ins)
conn.commit()
conn.close()