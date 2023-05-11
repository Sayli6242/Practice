"""
Write a Python program to map two lists into a dictionary.

Input:
colors = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']


Output:
{'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}

"""


colors = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']

   # initialise function
def To_form_dictionary():
   # define empty list
    dict = { }
   # for loop to access each index in list
    
    for i in range(len(colors)):
        # assign the keys to values
        dict[colors[i]] = values[i]
        # Dictionary_Name[New_Key_Name] = New_Key_Value 
    return dict


def main():

    dict = To_form_dictionary()
    print('Dictionary is: ',dict)



main()