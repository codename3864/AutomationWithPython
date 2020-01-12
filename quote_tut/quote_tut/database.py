import sqlite3

conn = sqlite3.connecy('quotes.db')
curr = conn.cursor()


curr.execute("""create table quotes_tb(
		title  text,
		author text,
		tags text
		)""")

conn.commit()
conn.close()
