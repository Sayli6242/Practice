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
@click.argument('entity',help= ' enter entity ,can be "contact"')
@click.argument('operation', help = 'enter mode, it can be "search"/ "add"')
def phonebook(entity,operation):


    click.echo(entity,operation)



# @click.command()
# @click.argument('input', type=click.File('c'))
# @click.argument('output', type=click.File('wb'))
# def inout(input, output):
#     """Copy contents of INPUT to OUTPUT."""
#     while True:
#         chunk = input.read(1024)
#         if not chunk:
#             break
#         output.write(chunk)



# import click

# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo(f"Hello {name}!")


if __name__ == '__main__':
    phonebook()















