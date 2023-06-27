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


statuses = {
    1:"pending",
    2:"inprogress",
    3:"completed"
}
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
        
        priorities = ["high","low"]
        for i, item in enumerate(priorities, ):
            print(f"{i+1}) {item}")

        priority_choice = int(input('enter priority: '))
        if not check_number_in_range(priority_choice, len(priorities)):
            print('choice must be an number from given choices')
            return
        elif priority_choice == 1:
            priority = 'high'
        elif priority_choice == 2:
            priority = 'low'
        self.db.insert_query("task",['task_title','task_description','due_date','priority'], [task_title,task_description,due_date,priority] )
        

       
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
        
        priorities = ["high","low"]
        for i, item in enumerate(priorities, ):
            print(f"{i+1}) {item}")

        priority_choice = int(input('enter priority: '))
        if not check_number_in_range(priority_choice, len(priorities)):
            print('choice must be an number from given choices')
            return
        elif priority_choice == 1:
            priority = 'high'
        elif priority_choice == 2:
            priority = 'low'

        self.db.update_query("task",{"task_title":updated_task_title,"task_description":updated_task_description,"due_date":updated_due_date,"status":status,"priority":priority  },"task_id",task_id)
            
    def delete_task(self):
        task_id = input('Enter the ID of the task you want to delete: ')
        if not check_validation_of_provide_ID(task_id):
            print("Invalid expense_id")
            return

        self.db.delete_query('task','task_id',task_id)


    def retrieve_task(self):

        print('choose retrive task based on which functionality: ')

        status_lst = ["By status","By priority", "By due_dates"]

        for i, item in enumerate(status_lst, ):
            print(f"{i+1}) {item}")

        choice = int(input("enter choice to retrieve task: "))
        if not check_number_in_range(choice, len(status_lst)):
            print('choice must be an number from given choices')
            return
         
        elif choice == 1:
            
            options = ["pending","inprogress","completed"]
            for i, item in enumerate(options, ):
                print(f"{i+1}) {item}")
            
            option_choice = int(input('enter by which status you wants to filtr task: '))
            if not check_number_in_range(choice, len(options)):
                print('choice must be an number from given choices')
                return
            # if option_choice == 1:
            filter_tasks = self.db.retrieve_query('task','status',statuses[option_choice])
            # if option_choice == 2:
            #     filter_tasks = self.db.retrieve_query('task','status','inprogress')
            # if option_choice == 3:
            #     filter_tasks = self.db.retrieve_query('task','status','completed')

        elif choice == 2:
            priorities = ["high","low"]
            for i, item in enumerate(priorities, ):
                print(f"{i+1}) {item}")
            priority_choice = int(input('enter priority: '))
            if not check_number_in_range(choice, len(priorities)):
                print('choice must be an number from given choices')
                return
            if priority_choice == 1:
                filter_tasks = self.db.retrieve_query("task","priority",'high')
            elif priority_choice == 2:
                filter_tasks = self.db.retrieve_query("task","priority","low")

            for row in filter_tasks:
                task_id, title, description, due_date, priority, status = row
                print(f"{task_id}\t{title}\t\t{description}\t\t{due_date}\t{priority}\t\t{status}")

        elif choice == 3:
            date = (input('enter due_date that u want to filter task: '))
            filter_tasks = self.db.retrieve_query("task","due_date",date)
            for row in filter_tasks:
                task_id, title, description, due_date, priority, status = row
                print(f"{task_id}\t{title}\t\t{description}\t\t{due_date}\t{priority}\t\t{status}")



if __name__ == '__main__':
    
    trigger_task_management()
    
    