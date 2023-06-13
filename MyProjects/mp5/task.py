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
@click.command()
def trigger_task_management():
    # 
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
        pass
    


    def update_task(self):
        pass


    def delete_task(self):
        pass

    
    def retrieve_task(self):
        pass


if __name__ == '__main__':
    T = task_manager()

    trigger_task_management()