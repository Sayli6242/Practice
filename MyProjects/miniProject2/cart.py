"""
shopping cart application
1) create dict to store items and prices.
2) define shopping_cart function
    - display welcome massage 
    - in while loop(break when user choose exit) 
        - display menu options(add_item , view_cart, calculate_total_price_of_items and exit), ask for user choice.
        - depending on user choice trigger the corresponding function.
        - if choice is exit then break the program
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

items = {'A':{"suger": 50},
             'B':{"flour": 30},
             'C':{"oil": 100},
             'D':{ "beans": 150}
             } 

selected_items = []

@click.command()
def shopping_cart():
    click.echo('welcome to shop, choose corresponding options')
    while True :
        click.echo('In which of the following operation you wants to perform:\n 1) add_items \n 2) view_Cart \n 3) calculate_total_price  \n 4) exit')
        option_as_input = input('Enter operation you wants to perform: ').strip()

        if option_as_input == 'add_items':
            add_items()

        elif option_as_input == 'view_cart':
            view_Cart()  

        elif option_as_input == 'calculate_total_price':
            calculate_total_price_of_items()

        elif option_as_input == 'exit':
            
            break

        else:
            print('invalid task. try again')


def add_items():
    print('A) suger = 50 \n B) flour = 30  \n C) Oil = 100 \n D) Beans = 150')

    user_input = input('enter options for items: ').strip()
    for key in items[user_input]:
        selected_items.append(key)
    print(selected_items)
    


def view_Cart():
    if selected_items == [ ]:
        pass

def calculate_total_price_of_items():
    pass




if __name__ == '__main__':
    
    shopping_cart()