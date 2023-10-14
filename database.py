from icecream import ic
import sqlite3

# conn = sqlite3.connect('customer.db')
# c = conn.cursor()

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

# print("name and email\n")
# for item in items:
#     # print(item)
#     # ic(item[0]) #name
#     print(f"{item[1]}, {item[0]}. \t| {item[2]}")

# c.execute("SELECT rowid, * FROM customers")
# items = c.fetchall()
# ic(items)

# where clause
# c.execute("SELECT rowid, * FROM customers WHERE l_name = 'human'")
# c.execute("SELECT rowid, * FROM customers WHERE l_name LIKE 'yes%'")
# c.execute("SELECT rowid, * FROM customers WHERE age = '>18'")
# items = c.fetchall()
# ic(items)

# update records

# c.execute("""UPDATE customers SET f_name = 'noname'
#           WHERE l_name = 'yesname'
#           """)
# conn.commit()

# c.execute("""UPDATE customers SET email = 'ihaveanamenow@yesname.com'
#           WHERE rowid = 3
#           """)
# conn.commit()
# c.execute("SELECT rowid, * FROM customers")
# items = c.fetchall()
# for item in items:
#     print(item)
# ic(items)

# delete records
# c.execute(" DELETE from customers WHERE rowid = 7") #didnt delete any
# conn.commit()

#order result
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid")
# c.execute("SELECT rowid, * FROM customers ORDER BY l_name DESC")

# and/or
# c.execute("SELECT rowid, * FROM customers WHERE l_name LIKE 'yes%' AND rowid = 3")
# c.execute("SELECT rowid, * FROM customers WHERE l_name LIKE 'yes%' OR rowid = 3")
# c.execute("SELECT rowid, * FROM customers WHERE l_name LIKE '%ye'")

# for item in items:
#     print(item)

# limiting results
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2") #or just the limit <#> is okay

#Dropping Table
# c.execute("DROP TABLE customer")

# Our app showing all function


def show_all():
    # Query the DB and return all records
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    ic(items)

    conn.commit()
    conn.close()
    
# new record to the table
def add_one(fn, ln, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO customers VALUES (?,?,?)", (fn, ln, email))
    
    conn.commit()
    conn.close()

#add multiple record
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    
    conn.commit()
    conn.close()
    
#delete record in the table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    
    c.execute("DELETE FROM customers WHERE rowid = (?)", id)
    
    conn.commit()
    conn.close()
    
# where clause function

def email_lokup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    
    c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))
    items = c.fetchall()
    ic(items)
    conn.commit()
    conn.close()
    
    