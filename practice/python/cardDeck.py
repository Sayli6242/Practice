"""
1) Create a deck of cards using string concatenation.
2)  # 4 
    card_types = ["hearts", "clubs", ......so on]
    # 13
    cards = ["Ace", "2", "3", ......so on] 
3) Your list should have items like '2 of Hearts', '3 of Hearts', '4 of Hearts'
4) Print total **52 cards** (13*4)

"""
def given_lst():
    l1 = ['hearts','clubs','diamond','spades']
    l2 = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    return l1, l2

def create_card_deck(l1,l2):    
    lst = [ ]
    for i in l1:
       for j in l2:
        new_lst = (j + ' of ' + i)
        lst.append(new_lst)
    return lst

def main():
    l1,l2  = given_lst()
    lst = create_card_deck(l1, l2)
    print("This are total 52 cards: ", lst)

main()