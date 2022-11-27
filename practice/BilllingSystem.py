"""
# Write a Python Program to calculate sale bill for the selling items in a Fruit Shop.
# products = {
		"Apple":{'Price_per_kg':200},
		"Banana":{'Price_per_kg':80},
		"Grapes":{'Price_per_kg':300},
		"Lemon":{'Price_per_kg':70}
	}
# ask user in loop what items he wants to buy. add each item to his cart(sample dict)
# in the end when he says exit.  
# calculate the sum of values of all items in his cart.  
# print the total bill amount.  

1) get input from user on loop while he chosen to exit. add each item to sample dict.
2) if key of item gets repeated then count get increase. 
3) store them in a cart_dict. 
4) when user select exit then 
5) multiply the values of cart_dict and products and then add to each other. 
6) print the total sum. 
"""
def Perchase_items_and_Calculate_Bill(products):
    Options = {'A': 'Apple','B': 'Banana','C': 'Grapes', 'D':'Lemon','E':'exit' }
    total = 0
    i = 0
    cart_dict = { }

    while i <= 10:
        user_perchase = input("Enter items in your cart, select Options\n A. Apple \n B. Banana \n C. Grapes \n D. Lemon \n E. exit \nType your option here: ")
       
        fruit = Options[user_perchase]
        #    increase count of user input option (ex. A ) in cart
       

                
           
        # # multiply the each value of key in card_dict with value of key in products.
        # # dictionary_name.values()


def main():

    products = {
		"Apple":{'Price_per_kg':200},
		"Banana":{'Price_per_kg':80},
		"Grapes":{'Price_per_kg':300},
		"Lemon":{'Price_per_kg':70}
	}
    
    total_bill =  Perchase_items_and_Calculate_Bill(products)

main()