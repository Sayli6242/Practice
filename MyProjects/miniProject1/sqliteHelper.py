
def create_tables():
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    res = cursor.execute("CREATE TABLE Books(Book_title, Publication_year,ISBN_number)")
    res = cursor.execute("CREATE TABLE Members(member_name,member_address,member_contact)")
    res = cursor.execute("CREATE TABLE Records(memberID, book_ID)")
    con.commit()
    cursor.close()
    con.close()


def insert_book(Book_title, Publication_year,ISBN_number):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    res = cursor.execute('INSERT INTO Books(Book_title, Publication_year,ISBN_number) VALUES (?, ?, ?)', (Book_title, Publication_year,ISBN_number))
    con.commit()
    cursor.close()
    con.close()

    # click.echo(f'Book successfully added')

def insert_members():
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    res = cursor.execute('INSERT INTO Members(member_name, member_address, member_contact) VALUES (?, ?, ?)', (member_name, member_address, member_contact))
    con.commit()
    cursor.close()
    con.close()