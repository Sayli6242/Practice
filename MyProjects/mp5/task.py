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
from mp4helpers.validationHelper import check_name_validation
from mp4helpers.validationHelper import check_validation_of_provide_ID
from mp4helpers.validationHelper import validate_due_date
from database import sqlite_Repository  
from database import postgreSQL_Repository
from mp4helpers.validationHelper import check_number_in_range

class task_manager:

    def __init__(self,db):
        self.db = db
       


    def create_task(self):
        task_title = input('Enter the title of the task: ')
        if not check_name_validation(task_title):
            print('enter valid title')
            return

        task_description = input('Enter the task description: ')
        if not check_name_validation(task_description):
            print('invalid input')
            return

        due_date = input('Enter the due date of the task (YYYY-MM-DD): ')
        if not validate_due_date(due_date):
            print('Invalid date format. Please enter the date in the format YYYY-MM-DD.')
            return

        self.db.insert_query(task_title, task_description,due_date,status)
        

       
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

        self.db.update_query(task_id, task_title, task_description, task_due_date)
            
    def delete_task(self):
        task_id = input('Enter the ID of the task you want to update: ')
        if not check_validation_of_provide_ID(task_id):
            print("Invalid expense_id")
            return

        self.db.delete_query(task_id)


    def retrieve_task(self):
        print('choose retrive task based on which functionality: ')
        lst = [status,priority, due_dates]
        for i, item in enumerate(lst, ):
            print(f"{i+1}) {item}")
        choice = int(input("enter choice to retrieve task: "))
        if not check_number_in_range(choice, lst):
            print('choice must be an number from given choices')
            return
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        else:
            ('invalid choice')



if __name__ == '__main__':
    create_table()
    trigger_task_management()
    
    