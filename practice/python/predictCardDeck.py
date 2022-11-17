"""
1) First by using random module pick random card for user.
2) Take prediction from user high or low as input.
3) Again by using random module print next card.
4) If next random card is higher than initial card user get +1 point.
5) else get -1 point.
6) make next card as initial card.

"""
import random

card_deck = ['Ace','2','3','4','5','6','7','8','9','10','jack','Queen','King']

initial_random_card = random.choice(card_deck)
print("your got this card: ", initial_random_card)


def To_choose_random_card_for_player(card_deck):
    score = 0
    for i in card_deck:
        # try:
            x = input('enter your prediction of card either high or low: ')
            choice_by_computer = random.choice(card_deck)
            print(choice_by_computer +" is your next card")
            index_of_intial_card = card_deck.index(initial_random_card)
            index_of_computer_card = card_deck.index(choice_by_computer)
        
            if index_of_computer_card > index_of_intial_card and x == "high":
                score +=1 #score = score + 1
            elif index_of_computer_card < index_of_intial_card and x == "low":
                score +=1
            elif index_of_computer_card == index_of_intial_card: 
                score = "tie"
            else:
                score -=1
            print("your score is : ",score)
        # except:    
        #     print('some error occured')
    return score

def main():
    card_deck = ['Ace','2','3','4','5','6','7','8','9','10','jack','Queen','King']
    score = To_choose_random_card_for_player(card_deck)

main()