"""
Library_management
    - Display options to user (add_books, registering_members, borrow_books, return_books, generate_report)
    - 

# check if tabel exist or not
    - if not then create BOOKS table 
    - if yes then continue programm
    - check members tabel exist or not
    - if not then create, if yes then continue to next step.
    - check table for Recods is exist or not.
    - if not then , create table using CREate Table query.
    - if yes then continue to next step.
1) adding books
    - take user input(book_title, author, publication year, ISBN number)
    - then add this detail in sqlite BOOKS_Table using INSERT queary 
    - then display massage(book successfully added)

2) register member
    - ask user to enter member(name, address, contacts_Information)
    - store user details to members table using INSERT query.
    - display massage(member successfully registered.)

3) borrow book
   
    - ask user for MemberID and BookId
    - check provided memberID and BookId is existed in Recods table or not using Select query.
    - then insert provided details(memberID and BookTd, status = 'borrowed') into Records table using Insert query.
    - 
4) return book
    - ask user for memberID and bookId
    - then check if user has borrowed the book by running select query where book status is 'borrowed'
    - if yes then update status to 'return' by runing update query.

5) generate report
    - display borrowed books and their member names
    - find unique bookId and their memberId.
    - and find book_title from books table and find member_name from members table.
    - then print all members name and all books name.
"""
import re
import click
import sqlite3

@click.command()
def library_management():

    while True :
            click.echo('choose options: as given below \n 1) add_book \n 2) register_members \n 3) borrowing_books  \n 4) returning_books  \n 5) generationg_reports')
            option_as_input = int(input('Enter operation you wants to perform: ').strip())
            if not check_validation_for_option_as_input(option_as_input):
                print('choice must be an number from given options')
                return

            # user_input = input("Enter your options: ")
            if option_as_input == 1: 
                adding_books()

            if option_as_input == 2:
                registering_members()

            if option_as_input == 3:
                borrowing_books()

            if option_as_input == 4:
                returning_books()

            if option_as_input == 5:
                generating_reports() 

           


def check_validation_for_option_as_input(option_as_input):
    if option_as_input >= 1 and option_as_input <= 4:
        return True
        
    else:
        return False


def Create_table_If_not_exist():
    
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Books'")
    result = cursor.fetchone()
        # Check if the table exists
    if result:
        
        print("Table exists.")
    else:
        res = cursor.execute("CREATE TABLE Books(Book_title, Publication_year,ISBN_number)")
        res = cursor.execute("CREATE TABLE Members(member_name,member_address,member_contact)")
        res = cursor.execute("CREATE TABLE Records(memberID,Book_ID)")
    
    cursor.close()
    con.close()


def check_name_validation(Book_title,member_name, member_address):
    pattern = r'^[a-zA-Z ]+$'
    if re.match(pattern, Book_title, member_name, member_address):
        return True
    else:
        return False

def check_year_validation(Publication_year):
    if Publication_year < 0  or Publication_year > 9999:
        return False    
    else:
        return True        

def check_ISBN_validation(ISBN_number):
    if ISBN_number ==  (r"^(?:ISBN(?:-13)?:?\s?)?(?=[0-9]{13}$|(?=(?:[0-9]+[-\s]){4})[-\s0-9]{17}$)[0-9]{1,5}[-\s]?[0-9]+[-\s]?[0-9]+[-\s]?[0-9]+[-\s]?[0-9]+$"):
        return False
    else:
        return True
    
def check_phone_validation(member_contact):
    if member_contact >= 1 and member_contact <= 10:
        return True     
    else:
        return False



def adding_books():
        Book_title = input("Book_Title").strip()
        if not check_name_validation(Book_title):
            print('Invalid name format') 
            return
              
        Publication_year = int(input("Publication_year").strip())
        while not check_year_validation(Publication_year):
            print('the integer must be in range 1-10')
            return
        
        ISBN_number = input("ISBN_number").strip()
        if not check_ISBN_validation(ISBN_number):
            print('invalid ISBN number')
            return

        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        res = cursor.execute('INSERT INTO Books(Book_title, Publication_year,ISBN_number) VALUES (?, ?, ?)', (Book_title, Publication_year,ISBN_number))
        con.commit()
        cursor.close()
        con.close()
        click.echo(f'Book successfully added')
    

def registering_members():
    member_name = (input('member name'))
    if not check_name_validation(member_name):
        print('Invalid name format') 
        return

    member_address = input('member_address')
    if not check_name_validation(member_address):
        print('Invalid name format') 
        return

    member_contact = input('member_contact')
    if not check_phone_validation(member_contact):
            print('the integer must be in range 1-10')
            return

    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    res = cursor.execute('INSERT INTO Members(member_name, member_address, member_contact) VALUES (?, ?, ?)', (member_name, member_address, member_contact))
    con.commit()
    cursor.close()
    con.close()
    click.echo(f'Book successfully added')
    


def borrowing_books():
    pass

def returning_books():
    pass

def generating_reports():
    pass


if __name__ == '__main__':
    Create_table_If_not_exist()
    library_management()
   
