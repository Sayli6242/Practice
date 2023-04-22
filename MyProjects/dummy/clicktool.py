import click

@click.command()
# count is for  number of greetings and help is for instructions to user
@click.option("--contact",prompt="phone" ,default=1, help="enter how many contact wants to be added.")
# name is to direct user to enter his name and help is for instructions to user
@click.option("--name", prompt="username", help="The person to greet.")
# creating a function name hello and pass parameter count and name 


def phonebook(name, contact):
    for i in range(contact):
        # echo is used instead of print and using format string print 'hello' message and name that user is entered.
        click.echo(f'username : {name}!')
        click.echo(f'phone : {contact}')


if __name__ == '__main__':
    # hello function get called
    phonebook()