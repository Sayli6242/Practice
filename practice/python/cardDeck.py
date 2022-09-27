"""
1) Create a deck of cards using string concatenation.
2)  # 4 
    card_types = ["hearts", "clubs", ......so on]
    # 13
    cards = ["Ace", "2", "3", ......so on] 
3) Your list should have items like '2 of Hearts', '3 of Hearts', '4 of Hearts'
4) Print total **52 cards** (13*4)
"""
"""
1) Define given list l1 and l2.
2) Define empty list to store obtain list.
3) apply for loop on list l1 to access each element in it.
4) again apply for loop inside for to access each element in list l2.
5) then concatinate element of l1 with each element of l2. 
6) means concatinate j + i.
7) store result in new_lst .
8) append result to empty define list and store in it.
9) return lst.
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