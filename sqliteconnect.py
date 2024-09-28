import sqlite3

conn =sqlite3.connect("sqlite.db")

conn.execute('''
             Create table student(
                 s_id INT AUTO_INCREMENT PRIMARY KEY,
                 s_name VARCHAR(50),
                 s_class VARCHAR(10),
                 S_email VARCHAR(30)
             )
             ''')

# ins = '''
#     insert into student values(1,"ravi","T.E IT","ravi12@gmail.com")
# '''
# conn.execute(ins)
# conn.commit
conn.close()