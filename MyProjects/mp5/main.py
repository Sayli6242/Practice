"""
1) make function name trigger_task management 
    - first we have to create table for that we call database object 
    - 
    -
    - display obption to user to choice databse
        - if user choice is 1 then call object of database method of class sqlite_repository
        - if user choice is 2 then call object of database method of class postgreSQL_repository
        - else display "invalid choice" to user
    - display option to user and ask which operation user wants to perform 
        - make list of options and iterate list and display to user as options
        - ask user for choice and validate choice is in range or not.
        - 
        - 
"""


from mp4helpers.validationHelper import check_number_in_range
from database import sqlite_Repository, postgreSQL_Repository
from task import task_manager

def trigger_task_management():
    
    print("which database you want to use to store task:\n 1) Sqlite  \n 2) PostgreSQL")
    database_choice = int(input("enter your choice: "))
    if database_choice == 1:
        db = sqlite_Repository()
        db.create_table('task',["task_id INTEGER PRIMARY KEY AUTOINCREMENT","task_title TEXT","task_description TEXT","due_date INTEGER"])
        
       
    elif database_choice == 2:
        db = postgreSQL_Repository()
        db.create_table()
        
    else:
        print("Invalid Choice")
        return

    T = task_manager(db)

    lst = ['Create Task','Update Task','Delete Task','Retrieve Task']

    while True:
        for i, item in enumerate(lst, ):
            print(f"{i+1}) {item}")

        choice = int(input("Enter your choice: ").strip())
        if not  check_number_in_range(choice,len(lst)):
            print('choice must be an number from given choices')
            return

        if choice == 1:
            T.create_task()
        
        if choice == 2:
            T.update_task()

        if choice == 3:
            T.delete_task()()

        if choice == 4:
            T.retrieve_task()
                            



if __name__ == '__main__':
    
   
    trigger_task_management()