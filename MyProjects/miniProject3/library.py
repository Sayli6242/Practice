"""
Library management system
# check if tabel exist or not
    - if not then create table
    - if yes then continue programm
1) adding books
    - take user input(book_title, author, publication year, ISBN number)
    - then add this detail in sqlite table using INSERT queary 
    - then display massage(book successfully added)
2) register member
    - ask user to enter member(name, address, contacts_Information)
3) borrow book
    - ask user for MemberID and BookId

4) return book
    - ask user for memberID and bookId

5) generate report
    - display borrowed books and their member names

"""
import click
import sqlite3


@click.command()
def library_management():
    
    click.echo('choose options: as given below \n 1) add_book \n 2) register_members \n 3) borrowing_books  \n 4) returning_books  \n 5) generationg_reports')
    user_input = input("Enter your options: ")
    if user_input == 1:
        adding_books()

    if user_input == 2:
        registering_members()

    if user_input == 3:
        borrowing_books()

    if user_input == 4:
        returning_books()

    if user_input == 5:
        generating_reports() 



def Create_table_If_not_exist():
    
    con = sqlite3.connect("labdata.db")
    cursor = con.cursor()

    res = cursor.execute("CREATE TABLE books(Book_Title, Author_name, Publication_year, ISBN_number)")
    res = cursor.execute("SELECT Author_name FROM sqlite_master WHERE type='table' AND name='books'")
    con.commit()
    cursor.close()
    con.close()

def adding_books():
    pass

def registering_members():
    pass

def borrowing_books():
    pass

def returning_books():
    pass

def generating_reports():
    pass


if __name__ == '__main__':
    library_management()

