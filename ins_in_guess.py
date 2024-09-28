from noguessing import name, guess_count;
import sqlite3

conn = sqlite3.connect("sqlite.db")

ins = (""" INSERT INTO GUESSING_GAME (U_NAME , U_GUESS) VALUES ({guess.name}, {guess.guess_count})
""")
conn.execute(ins)
conn.commit()
conn.close()