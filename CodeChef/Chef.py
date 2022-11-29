"""
- Chef and his girlfriend go on a date. Chef took XX dollars with him, 
- and was quite sure that this would be enough to pay the bill. At the end, the waiter brought a bill of YY dollars. Print "YES" if Chef has enough money to pay the bill, or "NO" if he has to borrow from his girlfriend and leave a bad impression on her.

Input Format
- The first line of input will contain a single integer TT, denoting the number of test cases.
- Each test case consists of a single line of input, containing two space-separated integers XX and YY.

"""

T = int(input())
for t in range(T):
    X, Y = input().split()
    if int(X) < int(Y):
        print("NO")
    else:
        print("YES")
