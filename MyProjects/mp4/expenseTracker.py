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
from mp4helpers.sqliteHelper import create_table_if_not_exist
from mp4helpers.sqliteHelper import execute_query
from mp4helpers.validationHelper import  check_number_in_range
from mp4helpers.validationHelper import check_name_validation
from mp4helpers.validationHelper import check_amount_validation
from mp4helpers.validationHelper import check_validation_of_provide_ID
@click.command()
def main():
    lst = ['Add Expenses','Categories Expenses','Generate Report','Set Budget','Analyze Expenses']
    

    while True:
    
        
        for i, item in enumerate(lst, ):
            click.echo(f"{i+1}) {item}")

        
        choice = int(input("Enter your choice: ").strip())
        if not  check_number_in_range(choice,len(lst)):
            print('choice must be an number from given choices')
            return


        if choice == 1:
           e.add_expenses()
        
        elif choice == 2:
            e.categories_expenses()

        elif choice == 3:
            e.generate_report()

        elif choice == 4:
            e.set_budget()
        
        elif choice == 5:
            e.analyze_expenses()



def execute_table_queries():
        create_table_expenses = "CREATE TABLE IF NOT EXISTS expenses(expense_id INTEGER PRIMARY KEY AUTOINCREMENT,amount INTEGER,description TEXT,category TEXT)"
        create_table_if_not_exist("expenses", create_table_expenses)

        create_table_budget = "CREATE TABLE IF NOT EXISTS budget(category TEXT, amount INTEGER)"
        create_table_if_not_exist("budget", create_table_budget)



class Expenses_Tracker:
    def __init__(self,categories):
        self.categories = categories

    def add_expenses(self):
        expense_amount = int(input("Enter expense amount: ").strip())
        if not check_amount_validation(expense_amount):
            print("Amount cannot be negative")
            return
            

        expense_description = input("Enter expense description: ").strip()
        if not check_name_validation(expense_description):
            print("Invalid description")
            return

        for i, category in enumerate(self.categories,start=1):
            click.echo(f"{i}) {category}")

        expense_category = int(input("Enter expense category: ").strip())
        if not check_number_in_range(expense_category, len(self.categories)):
            print("Invalid category")
            return
        z = self.categories[expense_category-1] 
        print(z)

        query = "INSERT INTO expenses (amount, description, category) VALUES (?, ?, ?)"
        parameters = (expense_amount, expense_description, z)
        result, expense_id = execute_query(query,parameters)

        click.echo(f'Expense added successfully with ID: {expense_id}')
        return

    def categories_expenses(self):
        
        expense_id = input("enter expense_id: ").strip()
        if not check_validation_of_provide_ID(expense_id):
            print("Invalid expense_id")
            return

        for i, category in enumerate(self.categories, start=1):
            click.echo(f"{i}) {category}")
      

        expense_category = int(input("Enter expense category: ").strip())
        if not check_number_in_range(expense_category, len(self.categories)):
            print("Invalid category")
            return
        z = self.categories[expense_category-1]
        print(z)

        query = "UPDATE expenses SET category = ? WHERE expense_id = ?"
        parameters = (expense_id, z)
        result = execute_query(query,parameters)
        
        click.echo("category successfully updated")

    def generate_report(self):

        query = "SELECT category, SUM(amount) FROM expenses GROUP BY category"
        result = execute_query(query)
        print(result)
       
        my_dict = { }

        # for (self.categories), amount in result:
            
        #     if (self.categories) not in my_dict:
        #         my_dict[self.categories] = [ ]
        #         my_dict[self.categories].append(amount)
        
        # print(my_dict)

        for category, amount in result:
            if category not in my_dict:
                my_dict[category] = []
            my_dict[category].append(amount)

        print(my_dict)
            


    def set_budget(self):
        budget_amount  = int(input("enter budget amount: ").strip())
        if not check_amount_validation(budget_amount):
            print("Amount cannnot be negetive")
            return

        for i, category in enumerate(self.categories, start=1):
            click.echo(f"{i}) {category}")
      
        budget_category =int(input("Enter category: ").strip())
        if not check_number_in_range(budget_category,len(self.categories)):
            print("Invalid category")
        z = self.categories[budget_category-1]
    
        query = "INSERT INTO budget(amount,category) VALUES (?, ?)"
        parameters = (budget_amount, z)
        result, expense_id = execute_query(query,parameters)   

        click.echo("budget set successfully")
        
    def analyze_expenses(self):
        pass


if __name__ == '__main__':
    execute_table_queries()
    e = Expenses_Tracker(['entertainment','food','elctricity',])
   
    main()

