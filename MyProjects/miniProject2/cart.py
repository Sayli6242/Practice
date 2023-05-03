"""
shopping cart application
1) create dict to store items and prices.
2) define shopping_cart function
    - display welcome massage 
    - in while loop(break when user choose exit) 
        - display menu options(add_item , view_cart and exit), ask for user choice.
        - depending on user choice trigger the corresponding function.
        - if choice is exist then break the program
3) if add items
    - display items and prices to user
    - get user input as options (ex: A) B) C))
    - get value based on user input as key.
    - store selected key as string in selected_items list.

3) if view_cart items
    - check if cart is empty 
        -display massage('cart is empty)
    - if not, display items and their count by iterating the list. 

4) calculate total price of items
    - multiply the count of each item with their price.
    - and display addition of all items.

"""
import click
@click.command()
@click.argument('entity')
@click.argument('operation')
def shopping_cart(entity,operation):
    if operation == 'add':
        add_contact()   

items = {"suger": 50, "flour": 30, "oil": 100, "beans": 150} 
selected_items = [] 


def add_contact():
    pass


















if __name__ == '__main__':
    shopping_cart()