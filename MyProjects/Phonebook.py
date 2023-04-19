"""
1) get mode (add, search)
2) if add,
    - get contact details
    - store into file/database
3) if search,
    - ask for details to be search
    - search by detail
        - if found ,show details
        - else, show not found.

"""


import click

@click.command()
@click.option('--add', default = 1, help ='To add contact' )
@click.option('--contact',prompt="contact",default=1,help='enter contact,you want to add')
@click.option('--name',prompt='username',help ='enter username of contact')
@click.option('--email',prompt='Email',help ='enter Email address of contact')

# add & search = argument

def phonebook(name,contact):
    for i in range(contact):
        print(f'username : {name}')
        print(f'contact : {contact}')
       

def add(names,numbers):
    
    for i in range(num):
        name =  input('name: ')
        number = input('phone number')
        names.append(name)
        numbers.append(number)
        
    print('\nName \t \t \t phone number \n')


def search(num,names,numbers):
    for i in range(num):
        print('{}\t\t\t{}'.format(names[i], numbers[i]))

    search_term = input('\Enter search Term: ')
    print('search result')


    if search_term in names:
        index = names.index(search_term)
        number = numbers[index]
        print('Name {}, phone number: {},Email: {}'.format(search_term, number))
    
    else:
        print('Name not found')
    print('search')



if __name__ == '__main__':
    names = [ ]
    numbers = [ ]
    num = 3 
      
    add(names,numbers,num)
    search(num,names,numbers)
    phonebook()