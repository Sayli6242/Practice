'''
1) Take user input
2) Print if user Win or Lose or its Draw
3) write if else logic using rock paper scissors game
4) compare user input (A B or C) with computer generated random input.

'''
import random

choices = { 'A' :"Rock", 'B':"Paper",'C':"Scissors"}

def check_computer_player_moves_(choices):
  result = 0
  
  # for keys in choices:
  player_choice = input('select 1 option\n Rock \n Paper \n Scissors \nType your option here: ')
  
  print(player_choice,' is your choice')

  computer_choice = random.choice(choices)
  print(computer_choice, ' is computers choice')

  new = choices.index('Rock')
  print(new)

  new_two = choices.index(computer_choice)
  print(new_two)

  if player_choice == computer_choice:
    print('Match is DRAW ')

  elif player_choice == 'Scissors':
    if computer_choice == 'Paper':
      print('player is winner!,Scissors beat Paper')
    else:
      print('player is lost!, Rock beat Scissors')


  elif player_choice == 'Rock':
    if computer_choice == 'Scissors':
      print('player is winner!, Rock beat Scissors')
    else:
      print('player is lost!, Paper covers Rock')


  elif player_choice == 'Paper':
    if computer_choice == 'Rock':
      print('player is winner!, Paper covers Rock')
    else:
      print('player is lost, Scissors beat Paper')


  return result

def main():
  
  result = check_computer_player_moves_(choices)
  


main()
