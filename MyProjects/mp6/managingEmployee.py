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
from datetime import datetime
from database import SqliteRepository
from database import PostgresRepository
from mp4helpers.validationHelper import check_name_validation
from mp4helpers.validationHelper import check_number_in_range
from mp4helpers.validationHelper import validate_due_date
from mp4helpers.validationHelper import validate_id
from mp4helpers.validationHelper import validate_choice
def start_employee_project_management_cli():
# ask user to choose database
    try:
        print("which database you want to use to store task:\n 1) Sqlite  \n 2) PostgreSQL")
        database_choice = int(input("enter your choice: "))
        if database_choice == 1:
            db = SqliteRepository()
            # create database object and call method to create tables
            db.create_table('employee',["employee_id INTEGER PRIMARY KEY AUTOINCREMENT","employee_name TEXT","set_of_skills TEXT","position TEXT"])
            db.create_table('project',["project_id INTEGER PRIMARY KEY AUTOINCREMENT","project_name TEXT","description TEXT","deadline INTEGER"])
            db.create_table('assign_project', ["employee_id","project_id"])
        elif database_choice == 2:
            db = PostgresRepository()
             # create database object and call method to create tables
            db.create_table('employee',["employee_id INTEGER PRIMARY KEY AUTOINCREMENT","employee_name TEXT","set_of_skills TEXT","position TEXT"])
            db.create_table('project',["project_id INTEGER PRIMARY KEY AUTOINCREMENT","project_name TEXT","description TEXT","deadline INTEGER"])
            db.create_table('assign_project', ["employee_id","project_id"])
        else:
            print('invalid choice')
            return
        # create object of class employee and projects
        e = Employee(db)
        p = Projects(db)
        
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
    except Exception as e:
        print(f"An error occurred")

# define class employee
class Employee:
    def __init__(self,db):
        # set database object to use in this entire class
        self.db = db

# define methods of employee class
    def add_employee(self):
        """
        Add a new employee to the database.
        - This method ask user to enter the employee's name, skills, and position.
        - display options to choose position and ask to user for its choice.
        - The employee information is inserted into the employee table in the database.
        - If the input is invalid (e.g., invalid name or position choice out of range),
        -an error message is displayed, and the method returns without adding the employee.
        """

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
        self.db.insert_query('employee',['employee_name','set_of_skills','position'], [employee_name,set_of_skills,employee_position[position_choice]])
    
    def assign_employee_to_project(self):

        # check employee already assigned to project then he's not able to assign any other project
        # one employee can assigne only three projects simultaneously
        # not more than five employee assigned to one project
        """
        Assign an employee to a project.
        ask user to enter the employee's ID and the project's ID.
        Performs the following validations:
        - Checks if the employee is already assigned to a project.
        - Checks if the employee has reached the maximum allowed projects (3 projects).
        - Checks if the project has reached the maximum allowed employees (5 employees).
        """

         # Ask user for employee_id to assign project
        employee_id = int(input("Enter employee_id: ").strip())
        if not validate_id(employee_id):
            print('invalid input. plese enter valid numeric value')
        # Ask user for project_id to assign to employee
        project_id = int(input("Enter project_id: ").strip())
        if not validate_id(project_id):
            print('invalid input. please enter valid numeric value')

        # If the employee has already reached the maximum allowed projects, return an error message
        result = self.db.retrieve_query('assign_project', 'employee_id', employee_id)
        if len(result) > 0 and result[0][0] >= 3:
            print("Employee has reached the maximum allowed projects.")
            return
        # Check if the project has already reached the maximum allowed employees
        elif len(result) > 0 and result[0][0] >= 5:
            print("Project has reached the maximum allowed employees.")
            return
        # check if the employee is already assigned to the project, return an error message
        elif len(result) > 0 and result[0][0] > 0:
            print('employee already assigned to project')
            return
        
        # insert the data into database
        result = self.db.insert_query('assign_project', ['employee_id','project_id'], [employee_id,project_id])
        print('project successfully assigned to employee')


    def retreiving_information_of_employee(self):
   
        """ Retrieve information of an employee based on specified criteria.
        ask user to choose the functionality for retrieving employee information:
        - 1. Retrieve by employee ID
        - 2. Retrieve by position
        - 3. Retrieve by set of skills
        - and the employee info is retrieved from database and printed in formatted manner.
        """

        print('choose retrieving employee information based of which fuctionality')
        # Define the options for retrieving employee information
        employee_position = {1:'employee_id',2:'posiotion',3:'skills'}
        
        # Print the options to the user
        for key,value in employee_position.items():
            print(key,value)
        # Ask the user to choose the functionality
        choice = int(input('enter based on which functionality you want to retrieve info of employee: ').strip())
        if not validate_choice(employee_position):
            print('Invalid choice. Please enter a valid option number.')
        if choice == 1:
            # Retrieve information based on employee_id
            employee_id = int(input('enter employee_id: ').strip())
            if not validate_id(employee_id):
                print('invalid input. please enter valide number')
            result = self.db.retrieve_query('employee','employee_id', employee_id)
            print(result)
            for row in result:
                employee_id,employee_name,set_of_skills,position = row
                print(f'{employee_id}\t{employee_name}\t{set_of_skills}\t{position}\t{position}')
            
        elif choice == 2:
            # Retrieve information based on position
            position =  {1:'developer',2:'analyst',3:'tester',4:'manager'}
            for key,value in position.items():
                print(key,value)
            choice =  int(input('enter by which position you want to retrive employee info: '))
            if not validate_choice(position):
                print('Invalid choice. Please enter a valid option number.')
            result = self.db.retrieve_query('employee','position',position[choice])
            print(result)
            for row in result:
                employee_id,employee_name,set_of_skills,position = row
                print(f'{employee_id}\t{employee_name}\t{set_of_skills}\t{position}\t{position}')
            
        elif choice == 3:
            # Retrieve information based on set of skills
            skill = input('enter skill that u want to retrieve employee info: ')
            if not check_name_validation(skill):
                print('invalid input.')
            result = self.db.retrieve_query('employee','set_of_skills', skill)
            print(result)
            for row in result:
                employee_id,employee_name,set_of_skills,position = row
                print(f'{employee_id}\t{employee_name}\t{set_of_skills}\t{position}\t{position}')
            

class Projects:
    def __init__(self,db):
        self.db = db

    def add_project(self):
        """
        Add a new project to the database.
        - This method ask user to enter the project's name, description, and deadline.
        - ask user for project description
        - ask user for project deadline
        - Then project information is inserted into the project table in the database.
        - If the input is invalid (e.g., invalid name or deadline format),
        - an error message is displayed, and the method returns without adding the project.
        """
          # Ask project name from the user
        project_name = input('enter project name: ').strip()
        if not check_name_validation(project_name):
            print('invalid input')
            return

        # Ask project description from the user
        project_description = input('enter project description: ').strip()
        if not check_name_validation(project_description):
            print('invalid input')
            return

        # Ask project deadline from the user
        project_deadline = input('enter project deadline (YYYY-MM-DD)').strip()
        if not validate_due_date(project_deadline):
            print('Invalid date format. Please enter the date in the format YYYY-MM-DD.')
            return
        # Insert project information into the project table of the database
        self.db.insert_query('project',['project_name','description','deadline'], [project_name,project_description,project_deadline])

    def retreiving_information_of_project(self):

        """ 
        Retrieve project info based on project_id or project deadline.
        This method asks the user to choose the functionality for retrieving project information:
        - Option 1: Retrieve information based on project_id
        - Option 2: Retrieve information based on project deadline
        - ask user to enter the details, and the project information is retrieved from the database
        - and printed in a formatted manner.
        """
        # retreive project using project name or project deadline
        print('choose based on which functionality you want to retrieve project info: ')

        options = {1:'project_id',2:'project_deadline'}
        for key,value in options.items():
            print(key,value)
        
        choice = int(input('enter your choice: ').strip())
        if not validate_choice(options):
            print('Invalid choice. Please enter a valid option number. ')

        if choice == 1:
            # retreive information based on projet_id
            p_id = input('enter project id: ')
            if not validate_id(p_id):
                print('invalid input. please enter valid numeric value')
            result = self.db.retrieve_query('project','project_id', p_id)
            for row in result:
                project_id,project_name,description,deadline = row
                print(f'{project_id}\t{project_name}\t{description}\t{deadline}')

        elif choice ==2:
            # retrieve information based on project deadline
            p_deadline = input('enter project_deadline:')
            if not validate_due_date(p_deadline):
                print('Invalid date format. Please enter the date in the format YYYY-MM-DD.')
            result = self.db.retrieve_query('project', 'deadline', p_deadline)
            for row in result:
                project_id,project_name,description,deadline = row
                print(f'{project_id}\t{project_name}\t{description}\t{deadline}')

if __name__ == '__main__':
    start_employee_project_management_cli()