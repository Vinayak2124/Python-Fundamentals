import sqlite3
conn = sqlite3.connect("sqlite.db")
data = conn.execute("SELECT f.s_id,s.s_name,f.Amount FROM fees as f inner join student as s where f.s_id = s.s_id ")
for a in data:
    print(a)
conn.close()
    
    