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

@click.command()
class expense_Tracker:
    def __init__(self,expense,category):
        self.expense = " "
        self.catagory = " "

