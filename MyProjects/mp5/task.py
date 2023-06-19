"""

This program should provide various operations such as

    - create task

    - setting due dates

    - assinging priorities

    - tracking status

1) ask user to choose database (sqlite OR PostgreSQL)
    if user choose Sqlite then. 
    - create table Repository_Sqlite if not exist to store task and their details.
    if user choose PostgreSQL.
    - create table Repository_PostgreSQL if not exist to store task and their details.
2) define fucntion name trigger_task_management.
    - this function act as entry point of task management app
    - it diplay list of options to the user and allow them to choose which operation they want to perform(create_task, update_task, delete_task , retrieve_data).
    - take user choice as input and validate to ensure choice is within range of options
    - 
3) 

"""
import click
from mp4helpers.validationHelper import check_number_in_range
from mp4helpers.validationHelper import check_name_validation
from mp4helpers.validationHelper import check_validation_of_provide_ID
from mp4helpers.validationHelper import validate_due_date
from database import sqlite_Repository  
from database import postgreSQL_Repository
@click.command()
def trigger_task_management():

    click.echo("which database you want to use to store task:\n 1) Sqlite  \n 2) PostgreSQL")
    database_choice = int(input("enter your choice: "))
    if database_choice == 1:
        db = sqlite_Repository8
    elif database_choice == 2:
        db = postgreSQL_Repository
    else:
        print("Invalid Choice")
        return
 
    lst = ['Create Task','Update Task','Delete Task','Retrieve Task']
   
    while True:
        for i, item in enumerate(lst, ):
            click.echo(f"{i+1}) {item}")

        choice = int(input("Enter your choice: ").strip())
        if not  check_number_in_range(choice,len(lst)):
            print('choice must be an number from given choices')
            return

        if choice == 1:
            T.create_task()
        
        if choice == 2:
            T.delete_task()

        if choice == 3:
            T.update_task()

        if choice == 4:
            T.retrieve_task()


def create_table_if_not_exist():
    pass
    # create object of selected database
    # execute required query(insert,delete,update)
    # 

class task_manager:

    def __init__(self):
        pass
    

    def create_task(self):
        task_title = input('Enter the title of the task: ')
        if not check_name_validation(task_title):
            print('enter valid title')
            return

        task_description = input('Enter the task description: ')
        if not check_name_validation(task_description):
            print('invalid input')
            return

        task_due_date = input('Enter the due date of the task (YYYY-MM-DD): ')
        if not validate_due_date(task_due_date):
            print('Invalid date format. Please enter the date in the format YYYY-MM-DD.')
            return

        z = sqlite_Repository()
        

    def update_task(self):
        task_id = input('Enter the ID of the task you want to update: ')
        if not check_validation_of_provide_ID(task_id):
            print("Invalid expense_id")
            return

        task_title = input('Enter the updated title of the task: ')
        if not check_name_validation(task_title):
            print('Enter a valid title')
            return

        task_description = input('Enter the updated task description: ')
        if not check_name_validation(task_description):
            print('Invalid input')
            return

        task_due_date = input('Enter the updated due date of the task (YYYY-MM-DD): ')
        if not validate_due_date(task_due_date):
            print('Invalid date format. Please enter the date in the format YYYY-MM-DD.')
            return

            
    def delete_task(self):
        task_id = input('Enter the ID of the task you want to update: ')
        if not check_validation_of_provide_ID(task_id):
            print("Invalid expense_id")
            return
    
    def retrieve_task(self):
        pass
        
    
    

        


if __name__ == '__main__':
    T = task_manager()
    trigger_task_management()
    