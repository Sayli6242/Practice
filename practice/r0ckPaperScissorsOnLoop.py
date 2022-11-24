"""
# Rock Paper Scissors game on loop.


select 1 option 
A: Rock
B: Paper
C: Scissors

# Type your option here (A or B or C)

1) take user input.
2) Print if user Win or Lose or its Draw.
3) write if else logic using rock paper scissors game.
4) Compare user input(A B or c) with computer random input.
5) print result
6) again take user input
7) repeat on loop

"""
import random


def check_computer_player_moves(choices):
    i = 0
    result = 0
    while i <= 10:
        player_choice = input(
            "Enter your choice, select 1 option\n Rock \n Paper \n Scissors \nType your option here: "
        )

        print(player_choice, " is your choice")

        computer_choice = random.choice(choices)
        print(computer_choice, "is computers choice")

        # new = choices.index("Rock")
        # # print(new)

        # new_two = choices.index(computer_choice)
        # # print(new_two)

        if player_choice == computer_choice:
            print("Match is DRAW ")

        elif player_choice == "Scissors":
            if computer_choice == "Paper":
                print("player is winner!,Scissors beat Paper")
            else:
                print("player is lost!, Rock beat Scissors")

        elif player_choice == "Rock":
            if computer_choice == "Scissors":
                print("player is winner!, Rock beat Scissors")
            else:
                print("player is lost!, Paper covers Rock")

        elif player_choice == "Paper":
            if computer_choice == "Rock":
                print("player is winner!, Paper covers Rock")
            else:
                print("player is lost, Scissors beat Paper")
    return result


def main():
    choices = ["Rock", "Paper", "Scissors"]
    result = check_computer_player_moves(choices)


main()
