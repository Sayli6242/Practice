
"""
1) take A and B 
2) multiply A with '0' and B with "1"
3) rotate obtained string from right and with each rotation check obtain string is palindrome or not
4) to check palindrome revesed the obtain string and matched with each other 
5) if matched then go to next step if not then print no and end program
5) if string is palindrome then rotate original string from left and with each rotation check obtained string is palindrome or not 
6) if yes then print yes or not then print no

"""
def check_palindrome(A, B,T):
    # Multiply A with '0' and B with '1'
    string = '0' * int(A) + '1' * int(B)

    # Rotate obtained string from right and check for palindrome
    rotated_strings = []
    for _ in range(len(string)):
        rotated_string = string[-1] + string[:-1]
        rotated_strings.append(rotated_string)
        string = rotated_string
        print(rotated_string)

        for i in range(len(string)):
            reversed_string = rotated_string[::-1]
            if rotated_string == reversed_string:
                print('yes') 
        
    
    print('No') 

def main():
    T = int(input())
    for  t in range(T):
        A =(input())
        B = (input())

        result = check_palindrome(A, B,T)
    print(result)

main()