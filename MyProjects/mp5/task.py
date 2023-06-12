"""

This program should provide various operations such as

    - create task

    - setting due dates

    - assinging priorities

    - tracking status

1) ask user to choose database (sqlite OR PostgreSQL)

    - create table Repository_Sqlite if not exist to store task and their details.

    - create table Repository_PostgreSQL if not exist to store task and their details.

2) make class of Task_manager

    - define their attributes 

        - 


3)

4)

5)



"""

from validationHelper import check_number_in_range

def trigger_task_management():
    # 
    lst = ['Create Task','Update Task','Delete Task']

    for i, item in enumerate(lst, ):
        click.echo(f"{i+1}) {item}")

    while True:
        choice = int(input("Enter your choice: ").strip())
        if not  check_number_in_range(choice,len(lst)):
            print('choice must be an number from given choices')
            return

        if choice == 1:
            T.create_task()
        
        if choice == 2:
            delete_task()

        if choice == 3:
            update_task()

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










if __name__ == '__main__':

    trigger_task_management()