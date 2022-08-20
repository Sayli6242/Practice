"""
Take 10 integer inputs from user, Check if list contains duplicates

"""


def get_user_input():
    x = int(input('enter the length of list: '))
    lst = []
    for i in range(x):
        y = int(input(f'ente list values {i}: '))
        lst.append(y)
    return lst


def check_for_duplicate_elements(lst):
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
                    
    return len(dup_elem)!=0




# result = 0
#     new_lst = [ ]
#     for i in lst:
#         if i % 2 == 0:
#             new_lst.append(i)

def main():
    lst = get_user_input()

    new_lst = check_for_duplicate_elements(lst)

    print('list contain duplicates are as follows: ',new_lst)



main()