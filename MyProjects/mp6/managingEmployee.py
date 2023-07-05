"""Building a CLI Application for Managing Employees and Projects"""
"""
1) we have two entites employee and projects
    - for store data of employee and projects we have to create tables.
    - this program performs various operations
        - add_employee()
        - add_project()
        - assign_employee_to_project()
        - retreiving_info_of_employee()
        - retreiving_info_of_project()

2) add_employee
    - ask input for name, set_of_skills and disply various options for position and ask user to choose one
    - then insert this data into database table using insert query and get employee_ID.

3) add_project
    - ask input for project_name, description and a deadline. 
    - then insert this data into database table using insert query and get project_ID.

4) assign_employee_to_project
    - ask for employee_ID to user and ask for project_ID to user and 
    - assign project of provided project_ID to employee of provided employee_ID using database query.
    - validation is 
        - one employee cannot be assigned to same project multiple times.
        - one employee cannto be assigned more than theree projects simultaneously.
        - one project cannot have more than five employees assigned to it.


5) retreiving_information_of_employee
    - ask user for employee_ID and display option of positons to retrieve and ask for choice
    - then filter employees according to user need using database query and display to user.

6) retreiving_information_of_project
    - ask user for project_ID and shows all information about project of provided project_ID 
    - using database queries.


"""
from database import sqlite_Repository
from database import postgreSQL_Repository
from mp4helpers.validationHelper import check_name_validation
from mp4helpers.validationHelper import check_number_in_range
from mp4helpers.validationHelper import validate_due_date

def managing_employee_and_project():
# ask user to choose database
        print("which database you want to use to store task:\n 1) Sqlite  \n 2) PostgreSQL")
        database_choice = int(input("enter your choice: "))
        if database_choice == 1:
            db = sqlite_Repository()
            # create database object and call method to create tables
            db.create_table('employee',["employee_id INTEGER PRIMARY KEY AUTOINCREMENT","employee_name TEXT","set_of_skills TEXT","position TEXT"])
            db.create_table('project',["project_id INTEGER PRIMARY KEY AUTOINCREMENT","project_name TEXT","description TEXT","deadline INTEGER"])
            db.create_table('assign_project', columns)
        elif database_choice == 2:
            db = postgreSQL_Repository()
             # create database object and call method to create tables
            db.create_table('employee',["employee_id INTEGER PRIMARY KEY AUTOINCREMENT","employee_name TEXT","set_of_skills TEXT","position TEXT"])
            db.create_table('project',["project_id INTEGER PRIMARY KEY AUTOINCREMENT","project_name TEXT","description TEXT","deadline INTEGER"])
        else:
            print('invalid choice')
            return
        # create object of class employee and projects
        e = employee(db)
        p = projects(db)
        
        lst = ['add employee','add project','assign employee to project','retriving info of employee','retriving info of project']
        # display option to user which operation they want to perform 
        while True:
            for i, item in enumerate(lst, ):
                print(f"{i+1}) {item}")
            # take user input and validate it.
            choice = int(input('enter choice for which operation you want to perform: ').strip())
            if not check_number_in_range(choice, len(lst)):
                print('invalid choice')
                return
            # match user input with choice and jump on  those class method.
            elif choice == 1:
                e.add_employee()
            elif choice == 2:
                p.add_project()
            elif choice == 3:
                e.assign_employee_to_project()
            elif choice == 4:
                e.retreiving_information_of_employee()
            elif choice == 5:
                p.retreiving_information_of_project()
            else:
                print('invalid choice')
# define class employee
class employee:
    def __init__(self,db):
        # set database object to use in this entire class
        self.db = db

# define methods of employee class
    def add_employee(self):
        # ask employee name to user
        employee_name = input("enter name of employee: ").strip()
        if not check_name_validation(employee_name):
            print('invalid input')
            return
        # ask set of skills of employee to user
        # set_of_skills = input("Enter skills (separated by comma): ").strip().split(",")
        set_of_skills = input('enter skill of employee: ')
        if not check_name_validation(set_of_skills):
            print('invalid input')
            return
        
        # display position options to user
        employee_position = {1:'manager',2:'developer',3:'tester',4:'analyst'}

        positions = ['manager','developer','tester','analyst']
        for i, item in enumerate(positions):
            print(f"{i+1}) {item}")
        # ask user to choose employee position
        position_choice = int(input("enter position of employee: ").strip())
        if not check_number_in_range(position_choice, len(positions)):
            print('number out of range')
            return
        # insert all info in employee table of database
        self.db.insert_query('employee',['employee_name','set_of_skills','position'], [employee_name,set_of_skills,positions[position_choice]])
    
    def assign_employee_to_project(self):
        # ask user for employee_id to assign project
        # ask user for project_id assign to employee
        get_employee_id = input('enter employee_id: ')
        get_project_id = input('enter project_id: ')
        self.db.insert_query(table_name, columns, values)



    def retreiving_information_of_employee(self):
   
        # ask user to retrieve info of employee based on id , based on position ,based on set of skills
        # ask user to provide 
        print('choose retrieving employee information based of which fuctionality')

        employee_position = {1:'employee_id',2:'posiotion',3:'skills'}

        for key,value in employee_position.items():
            print(key,value)

        choice = int(input('enter based on which functionality you want to retrieve info of employee').strip())

        if choice == 1:
            employee_id = int(input('enter employee_id ').strip())
            self.db.retrieve_query('employee','employee_id', employee_position[choice])

        elif choice == 2:
            position =  {1:'developer',2:'analyst',3:'tester',4:'manager'}
            for key,value in position.items():
                print(key,value)
            choice =  int(input('enter by which position you want to retrive employee info'))
            self.db.retrieve_query('employee','position',position[choice])
        
        elif choice == 3:
            skill = input('enter skill that u want to retrieve employee info: ')
            self.db.retrieve_query('employee','set_of_skills', skill)


class projects:
    def __init__(self,db):
        self.db = db

    def add_project(self):
        project_name = input('enter project name: ').strip()
        if not check_name_validation(add_project):
            print('invalid input')
            return

        project_description = input('enter project description: ').strip()
        if not check_name_validation(project_description):
            print('invalid input')
            return
        
        project_deadline = int(input('enter project deadline (YYYY-MM-DD)').strip())
        if not validate_due_date(project_deadline):
            print('Invalid date format. Please enter the date in the format YYYY-MM-DD.')
            return
        z = self.db.insert_query('project',['project_name','description','deadline'], [project_name,project_description,project_deadline])

    def retreiving_information_of_project(self):
        # retreive project using project name or project deadline
        print('choose based on which functionality you want to retrieve project info')

        options = {1:'project_name',2:'project_deadline'}
        for key,value in options.items():
            print(key,value)
        
        choice = int(input('enter your choice').strip())
        if choice == 1:
            p_name = input('enter project_name: ')
            self.db.retrieve_query('project','project_name', p_name)
        elif choice ==2:
            p_deadline = input('enter project_deadline:')
            self.db.retrieve_query('project', 'deadline', p_deadline)

if __name__ == '__main__':
    managing_employee_and_project()