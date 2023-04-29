import sqlite3
# import pbook

pbook.add_contact()

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
