"""
1) Create a word guessing game.
 # wordle = ["DANCE", "ALARM", "APPLE" ...]
2) Make list of 10 words.
3) Print first 3 letters of a 5 letter word.
4) User needs to complete last 2 letters.

 # Below content is printed on console

5) Word is D.A.N._._
 - Type the remaining 2 letters below, by adding letters it should make a valid word in english  
6) CE (USER TYPES THESE 2 LETTERS)

!!! Correct word is DANCE

1) make list of 10 words.
2) iterate list to access each word.
3) use random module to get random word in list.
4) store random word in a varible.
5) split the word and make new_list.
6) print the first 3 latters of words and _._ for last two words.
7) ask user to guess last two words.
8) compare last two words to user input
9) print result.

"""


import random


def guess_the_word(lst):

    random_word = random.choice(lst)
    # print(random_word)

    # split the word using list iterators
    new_lst = list(random_word)

    # print first  letters of chosen word
    print(new_lst[0] + new_lst[1] + new_lst[2] + "_._")

    letters = input("enter last two letters: ")

    # make list to string using slicing
    # y = "".join(new_lst[3:5])

    if "".join(new_lst[3:5]) == letters:
        print("you win!")
    else:
        print(f"you lose!, the word is {random_word}")

    return new_lst


def main():

    lst = [
        "Dance",
        "Alarm",
        "Apple",
        "Words",
        "Watch",
        "Types",
        "These",
        "Valid",
        "Below",
    ]
    new_lst = guess_the_word(lst)


main()
