import sqlite3
conn = sqlite3.connect("sqlite.db")

id = input("Enter the student id : ")
conn.execute("DELETE FROM student where s_id =" + id)
conn.commit()
conn.close()