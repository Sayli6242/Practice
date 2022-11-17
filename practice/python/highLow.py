

import random
# list of numbers taken
numbers = ['1','2','3','4','5','6','7','8','9','10']

# using random function take random value
initial_random_num = random.choice(numbers)
print("your got this number: ", initial_random_num)


def To_choose_random_num_for_player(numbers):
    score = 0
    # apply for loop 
    for i in numbers:
        # take input from user 
            x = input('enter your prediction of number either high or low: ')
            # using random function computer genrate random value
            choice_by_computer = random.choice(numbers)
            # print computer generated number
            print(choice_by_computer +" is your next number")
            # get index of numbers by using index
            index_of_intial_num = numbers.index(initial_random_num)
            index_of_computer_num = numbers.index(choice_by_computer)
        # comparing computer generated num and players num by using if 
            if index_of_computer_num > index_of_intial_num and x == "high":
                score +=1 #score = score + 1
            elif index_of_computer_num < index_of_intial_num and x == "low":
                score +=1
        # both numbers are same then tie  
            elif index_of_computer_num == index_of_intial_num: 
                score = "tie"        
            else:
                score -=1
        # print score 
            print("your score is : ",score)
       
    return score

def main():
    numbers = ['Ace','2','3','4','5','6','7','8','9','10','jack','Queen','King']
    score = To_choose_random_num_for_player(numbers)

main()