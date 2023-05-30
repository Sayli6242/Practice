"""
The program should provide various operations such as 
    - adding expenses 
    - categorizing expenses 
    - analyzing expenses
    - generating report
    - setting budgets

        1. catagories are pre-defined
        2. category and discription is not mandatory while adding expense.

1) create table to store expenses and their catagory
2) create table for define fixed budget.
3) define function add_expenses.
        - ask user for expense_amount, description and category
        - only input for expense_amount is mandatory.
        - store this details into expenses table by using "INSERT" query.
        - and generate autoincremental expenseID
4)  define categorize_expenses function.
        - ask user for expenseID and category.
        - using sql query "UPDATE" update category of provided expenseID.
5)  define generate_report function.
        - get unique categories
        - then sum of their values 
        - gerate a dictionary
            - dict = {
                category1:[sum of values]
                category2:[sum of values]
            }
        - generate total of all expenses 
        - compare sum of values of unique catagories with categories and expenses define in budget table
        - and show budget is exceeding or not.
6) define set_budget function.
        - define table budget for this function
        - using INSERT set fix amount for expense_amount of define category.
7) define analyze_expenses function.
        - 
"""
import click
from sqliteHelper import create_table_if_not_exist
from sqliteHelper import execute_query
from validationHelper import check_validation_for_option_as_input

@click.command()
class main:
       
    def __init__(self,database):
        self.database = database

    def take_user_choice(self,choice):
        while True:
            self.display_menu_choices()
            choice = input("Enter your choice: ").strip
            running = self.display_menu_choice(choice)
            if not check_validation_for_option_as_input(choice):
                print('choice must be an number from given choices')
                return


    def display_menu_choices(self,choice):

        click.echo("Choose Options : \n 1) Add Expenses \n 2) Categories Expenses \n 3) Generate Report \n 4) Set Budget \n 5) Analyze Expenses")

        if choice == 1:
            self.add_expenses()
        
        elif choice == 2:
            self.categories_expenses()

        elif choice == 3:
            self.generate_report()

        elif choice == 4:
            self.set_budget()
        
        elif choice == 5:
            self.analyze_expenses()



    def execute_table_queries():
        create_table_expenses = "CREATE TABLE IF NOT EXISTS expenses(expense_id INTEGER PRIMARY KEY AUTOINCREMENT,amount INTEGER,description TEXT,category TEXT)"
        create_table_if_not_exist("expenses", create_table_expenses)

        create_table_budget = "CREATE TABLE IF NOT EXISTS budget(category TEXT, amount INTEGER)"
        create_table_if_not_exist("budget", create_table_budget)



class Expenses_Tracker:
    def __init__(self):
        self.amount = 0
        self.description = ""
        self.category = ""

    def setAmount(self,amount):
        self.amount = amount

        self.description = description
        self.category = category

    def add_expenses():
        query = "INSERT INTO expenses (amount, description, category) VALUES (?, ?, ?)"
        parameters = (amount, Category, description)
        result, expense_id = execute_query(query)
        click.echo(f'Expense added successfully with ID: {expense_id}')
        

    def categories_expenses():
        pass


    def generate_report():
        pass


    def set_budget():
        pass


    def analyze_expenses():
        pass
