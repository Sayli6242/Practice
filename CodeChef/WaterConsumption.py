"""
- Recently, Chef visited his doctor. 
- The doctor advised Chef to drink at least 20002000 ml of water each day.
- Chef drank XX ml of water today. Determine if Chef followed the doctor's advice or not.

Input Format
- The first line contains a single integer TT — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains one integer XX — the amount of water Chef drank today.
Output Format
- For each test case, output YES if Chef followed the doctor's advice of drinking at least 20002000 ml of water. 
- Otherwise, output NO.

"""
T = int(input())
for t in range(T):
    x = int(input())
    if x >= 2000:
        print("YES")
    else:
        print("NO")
