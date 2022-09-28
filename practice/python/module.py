"""

"""
import random

date = str(random.uniform())
print(random)



"""
to obtain random 2 values from given list 
"""


greetings = ['hey','hello','hi','yupp','dear']
my_quote = random.choices(greetings, weights=[10,8], k=2)
print(my_quote)



"""
string concate with using random element in list
"""

import random
greetings = ['hey','hello','hi','yupp', 'dear']
my_quote = random.choice(greetings)
print(my_quote + ', Devanshu')




"""
to obtain 5 shuffeled list values in given range

"""

deck = list(range(1,53))
hand = random.sample(deck, k=5)
print(hand)