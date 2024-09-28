
import sqlite3

conn = sqlite3.connect("sqlite.db")

conn.execute(""" CREATE TABLE GUESSING_GAME(U_NAME VARCHAR(20),
             U_GUESS INT(3))
"""
)
conn.close()