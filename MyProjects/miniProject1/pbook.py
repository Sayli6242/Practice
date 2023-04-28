"""
1) get mode (add, search)
2) if add,
    - get contact details
    - store into file/database
3) if search,
    - ask for details to be search
    - search by detail
        - if found ,show details
        - else, show not found.

"""
import sqlite3
import click

# @click is decorator 
@click.command()
@click.argument('entity')
@click.argument('operation')
def phonebook(entity,operation):
    if operation == 'add':
        add_contact()   

    if operation == 'search':
        search_contact_by_details()
       
    # click.echo(entity,operation)
def Create_table_If_not_exist():
    # check if table exist return from function
    # if not exist create
    con = sqlite3.connect("database.db")
    cur.execute("CREATE TABLE Phonebook(username, contact, EmailId)")
    con.cursor()
    pass

def add_contact():
    name = input("username")
    contact = int(input("contact"))
    EmailId = input("EmailId")
        

u8
def search_contact_by_details():
        pass


if __name__ == '__main__':
    Create_table_If_not_exist()
    phonebook()
    













