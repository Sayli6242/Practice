"""
1) Calculate the sum of all N elements in the remaining sequence.
2) Calculate the sum of the original sequence before deletion using the arithmetic average V.
3) Calculate the sum of the deleted elements.
4) Determine if it is possible for the deleted elements to have the same value.
    - If the sum of the deleted elements (Sum_deleted) is divisible by K, it means that the deleted elements had a common value.
    - If the sum is not divisible by K, then there is a mistake, and the scenario described is impossible.
5) If the deleted elements had a common value, divide the sum of the deleted elements by K to obtain the value of the deleted elements.
6) print the value of the deleted elements if it exists, or output that the scenario is impossible if the sum is not divisible by K.
"""

T = int(input())
for t in range(T):
    n , k , v = input().split()
    num_of_elements = int(n)
    num_of_deleted_elements = int(k)
    avg_of_all_elements = int(v)
    lst = list(map(int, input().split()))
    sum_of_all = sum(lst)
    
    sum_of_original_seq = avg_of_all_elements*(num_of_elements + num_of_deleted_elements)
    
    deleted_element_sum = sum_of_original_seq - sum_of_all
    if deleted_element_sum % num_of_deleted_elements == 0:
        deleted_value = deleted_element_sum // num_of_deleted_elements
        print(deleted_value)
    else:
        print(-1)
        
        
        
    
    




