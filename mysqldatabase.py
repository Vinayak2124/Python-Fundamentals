import pymysql as mq

# server name - localhost
# username - root
# passwd - " "

myobj = mq.connect(host="localhost", user="root",passwd=" ")
sqlcursor = myobj.cursor()
try:
    db = "create database school"
    sqlcursor.execute(db)
    print("Database created")
except :
    print("Database already existed")