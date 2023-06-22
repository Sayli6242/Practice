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
        - find the most expensive amount of category and print them using sql query
        - find average amount of category and print them using sql query
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
        if not expense_category:
            expense_category = 'others'

        elif not check_number_in_range(expense_category, len(self.categories)):
            print("Invalid category")
            return
        else:
            expense_category = self.categories[expense_category-1] 
        # print(z)

        query = "INSERT INTO expenses (amount, description, category) VALUES (?, ?, ?)"
        parameters = (expense_amount, expense_description, expense_category)
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
        expense_category = self.categories[expense_category-1]
        # print(expense_category)

        query = "UPDATE expenses SET category = ? WHERE expense_id = ?"
        parameters = (expense_id, expense_category)
        result = execute_query(query,parameters)
        
        click.echo("category successfully updated")

    def generate_report(self):
        # query to get sum of unique categories.
        query = "SELECT category, SUM(amount) FROM expenses GROUP BY category"
        result = execute_query(query) 
        # convert obtaines tuple into dict and print key and value of each pair.
        tuple_dict = dict(result[0])    
        for key,value in tuple_dict.items():
            print(key,':',value)
        # get total of all expenses and print total of all expenses.
        total_of_expenses = sum(tuple_dict.values())
        print('\nTotal of all expenses is: ',total_of_expenses )
        # query to get fix budget set in budget table for each category
        query = "SELECT category, amount FROM budget"
        result_budget = execute_query(query)
        # convert obtained tuple into dict 
        budget_dict = dict(result_budget[0])
        print('\nExpense report: ')
        # get key and value in tuple dict and print key and value.
        for category, amount in tuple_dict.items():
            print(f"Category: {category}, Expenses: {amount}")
            # check category as key is present in obtained budget dict 
            if category in budget_dict:
                budget_amount = budget_dict[category]
                # check expense amount of each category is greater than or equal to obtaine budget amount from budget table.
                if amount >= budget_amount:
                    print(f"Budget for category '{category}' exceeded")
                else:
                    print(f"Budget for category '{category}' is within limit")
            else:
                print(f"No Budget found for category '{category}'")

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
        expense_category = self.categories[budget_category-1]
    
        query = "INSERT INTO budget(amount,category) VALUES (?, ?)"
        parameters = (budget_amount, expense_category)
        result, expense_id = execute_query(query,parameters)   

        click.echo("budget set successfully")
        
    def analyze_expenses(self):
        query = '''SELECT *
                FROM expenses
                WHERE amount = (SELECT MAX(amount) FROM expenses)'''
        result = execute_query(query)
        nested_tuple = result
        first_element = nested_tuple[0]
        second_element = nested_tuple[1]

        inner_tuple = first_element[0]
        amount = inner_tuple[1]
        description = inner_tuple[2]
        category = inner_tuple[3]

        print(f"most expensive expense is {category} of amount {amount} ,{description}")

        query ="SELECT category, AVG(amount) FROM expenses GROUP BY category"    
        result = execute_query(query)
        print(result)
        nested_tup = result

        for first_element in nested_tup:
            # inner_value = first_element[0]
            avg = first_element[0]
            category = first_element[1]
        click.echo(f"Average Expenses per category are \n {category} : {avg}")

if __name__ == '__main__':
 
    e = Expenses_Tracker(['entertainment','food','elctricity',])   
    execute_table_queries()
    main()




