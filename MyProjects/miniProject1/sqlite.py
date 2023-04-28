import sqlite3

con = sqlite3.connect("database.db")

# cur.execute("CREATE TABLE Phonebook(username, contact, EmailId)")
cur = con.cursor()

a = cur.execute("SELECT name FROM sqlite_master WHERE name='contact'")
a = cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

z = a.fetchone() is None

print(z)