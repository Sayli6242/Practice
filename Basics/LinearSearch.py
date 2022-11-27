"""
1) make a list
2) ask user for a num to be found
3) use for loop to iterate value in list
4) if found break the loop
5) if not found print result



"""
def get_user_input():
    lst_size = int(input('enter size of list'))
    lst = [ ]
    for i in range(lst_size):
        x = input('Enter the values of list')
        lst.append(x)

    return lst
    


def linear_Search(lst, lst_size, num):
    num = int(input('Enter num to be search'))
    x = 0
    for i in range(lst_size):
        if lst[i] == num:
            x = 1
            position = i + 1
            break
        if x ==1:
            print('number is found at', position)
        
        else:
            print('number is not found')


    



def main():

    lst = get_user_input()
    num = linear_Search(lst, num)
    
main()