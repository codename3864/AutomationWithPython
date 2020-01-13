# import sqlite3

# conn = sqlite3.connect('quotes.db')
# curr = conn.cursor()


# curr.execute("""CREATE table quotes_tb(
# 		title text,
# 		author text,
# 		tags text
# 		)""")

# # curr.execute("INSERT INTO quotes_tb VALUES('X','anonymous','python')")
# curr.execute("SELECT *FROM quotes_tb")
# print(curr.fetchone())
# conn.commit()
# conn.close()
