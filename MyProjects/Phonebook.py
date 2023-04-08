"""
1) get how many number of contact are added.
2) ask user for username
3) ask user for contacts
4) ask user for EmailId
5) after all steps display massage of 'contact added'.

"""
import click

@click.command()
@click.option('--contact',prompt="contact",default=1,help='enter contact,you want to add')
@click.option('--name',prompt='username',help ='enter username of contact')
@click.option('--email',prompt='Email',help ='enter Email address of contact')
@click.option('--contact',prompt="contact",default=1,help='enter contact,you want to add')
def phonebook(name,contact,email):
    for i in range(contact):
        click.echo(f'username : {name}')
        click.echo(f'contact : {contact}')
        click.echo(f'Email : {email}')


if __name__ == '__main__':
    phonebook()
