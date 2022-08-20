"""
Make a list by taking 10 input from user. Now delete all repeated elements of the list.

output - list with only unique values

"""

def get_user_input():
    x = int(input('enter length of list'))
    lst = []
    for i in range(x):
        y = int(input(f'enter values for list{i}'))
        lst.append(y)
    return lst

def to_delete_all_elements_in_list(lst):
    dup_elem =[]
    for i in range(len(lst)):
        if i in dup_elem:
            continue
            
        for j in range(len(lst)):
            if i==j:
                pass
            else:
                print(i,j)
                if lst[i]==lst[j]:
                    dup_elem.append(j)
                    
    # create new list from existing list, with duplicate indexes skipped
    lst_without_duplicates =[]
    for i in range(len(lst)):
        if i in dup_elem:
            continue
        print(f"appending {lst[i]} to {lst_without_duplicates} list")
        lst_without_duplicates.append(lst[i])
    return lst_without_duplicates



def main():
    
    lst = get_user_input()

    lst_without_duplicates = to_delete_all_elements_in_list(lst)

    print('list with only unique values: ',lst_without_duplicates)

main()