"""





"""

T = int(input())
for t in range(T):
    n,x,s = input().split()
    number_of_boxes = int(n)
    coin_in_box_position = int(x)
    number_of_swaps = int(s)
    a,b = input().split()
    swap_a = int(a)
    swap_b = int(b)
    for swap in range(number_of_swaps):
        for i in range(number_of_boxes):

            temp = swap_a
            swap_b = swap_a
            swap_b = temp
            print(coin_in_box_position)