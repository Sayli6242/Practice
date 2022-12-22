"""
-The strategy method is Behavioral Design pattern that allows you to define the complete family of algorithms, 
-encapsulates each one and putting each of them into separate classes and also allows to interchange there objects. 

"""


class Item:
    def __init__(self, price, discount):
        self.price = price
        self.discount = discount

    def price(self):
        self.price

    def setdiscount(self):
        self.discount


class discount(Item):
    pass


class discountOnSpecificItem(Item):
    pass


def main():
    Item = Item(discount)
    Item.discount = discountOnSpecificItem


main()
