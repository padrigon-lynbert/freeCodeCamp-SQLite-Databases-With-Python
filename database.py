import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

# c.execute(""" CREATE TABLE customers (
#     f_name text,
#     l_name text,
#     email text
# )""")

# c.execute("INSERT INTO customers VALUES ('noname', 'yesname', 'noname@yesname.com')")

# many_customers = [
#                     ('random', 'human', 'random@human.com'), 
#                     ('ok', 'notokay', 'okay@notokay.com'), 
#                     ('no', 'iwont', 'no@iwont.com')
#                 ]

# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# c.execute("SELECT * FROM customers")
# print(c.fetchall())

conn.commit()
conn.close()