import sqlite3
from pbook import update_contact
def add_contact_query():

    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute('INSERT INTO contacts (name, phone,EmailId) VALUES (?, ?, ?)', (name, phone,EmailId))
    con.commit()
    con.close()
    click.echo(f'contact successfully added')


update_contact()
# import pbook

# pbook.add_contact()

# Connect to the database
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object
cursor = conn.cursor()

# Execute the query to check if the table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='mytable'")

# Fetch the results
result = cursor.fetchone()

# Check if the table exists
if result:
    print("Table exists.")
else:
    print("Table does not exist.")

# Close the cursor and the database connection
cursor.close()
conn.close()
