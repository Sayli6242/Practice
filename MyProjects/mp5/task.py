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
        

        self.db.insert_query("task",['task_title','task_description','due_date'], [task_title,task_description,due_date] )
        

       
    def update_task(self):
        task_id = input('Enter the ID of the task you want to update: ')
        if not check_validation_of_provide_ID(task_id):
            print("Invalid expense_id")
            return

        updated_task_title = input('Enter the updated title of the task: ')
        if not check_name_validation(updated_task_title):
            print('Enter a valid title')
            return

        updated_task_description = input('Enter the updated task description: ')
        if not check_name_validation(updated_task_description):
            print('Invalid input')
            return

        updated_due_date = input('Enter the updated due date of the task (YYYY-MM-DD): ')
        if not validate_due_date(updated_due_date):
            print('Invalid date format. Please enter the date in the format YYYY-MM-DD.')
            return

        status_lst = ['pending','inprogress','completed']
        for i, item in enumerate(status_lst):
            print(f"{i+1}) {item}")

        update_task_status = int(input('enter updated status of task: ').strip())
        if not  check_number_in_range(update_task_status,len(status_lst)):
            print('choice must be an number from given choices')
            return
        if update_task_status == 1:
            status = 'pending'
        elif update_task_status == 2:
            status = 'inprogress'
        elif update_task_status == 3:
            status = 'completed'
        self.db.update_query("task",{"task_title":updated_task_title,"task_description":updated_task_description,"due_date":updated_due_date,"status":status},"task_id",task_id)
            
    def delete_task(self):
        task_id = input('Enter the ID of the task you want to delete: ')
        if not check_validation_of_provide_ID(task_id):
            print("Invalid expense_id")
            return

        self.db.delete_query('task','task_id',task_id)


    def retrieve_task(self):
        print('choose retrive task based on which functionality: ')
        lst = ["By status","By priority", "By due_dates"]
        for i, item in enumerate(lst, ):
            print(f"{i+1}) {item}")
        choice = int(input("enter choice to retrieve task: "))
        if not check_number_in_range(choice, lst):
            print('choice must be an number from given choices')
            return
        if choice == 1:
            task = self.db.retrieve_pending_tasks(status)
        elif choice == 2:
            task = self.db.retrieve_inprogress_tasks(status)
        elif choice == 3:
            task = self.db.retrieve_completed_tasks(status)
        else:
            ('invalid choice')
            return
        
        for task in tasks:
            print(f"Task ID: {task['task_id']}")
            print(f"Title: {task['task_title']}")
            print(f"Description: {task['task_description']}")
            print(f"Due Date: {task['task_due_date']}")
            print("")




if __name__ == '__main__':
    create_table()
    trigger_task_management()
    
    