"""
Chef is working on his swap-based sorting algorithm for strings.

Given a string SS of length NN, he wants to know whether he can sort the string using his algorithm.

According to the algorithm, one can perform the following operation on string SS any number of times:

Choose some index ii (1 \leq i \leq N)(1≤i≤N) and swap the i^{th}i 
th
  character from the front and the i^{th}i 
th
  character from the back.
More formally, choose an index ii and swap S_iS 
i
​
  and S_{(N+1-i)}S 
(N+1−i)
​
 .
For example, \underline{\texttt{d}} \texttt{cb} \underline{\texttt{a}} 
d
​
 cb 
a
​
  can be converted to \underline{\texttt{a}} \texttt{cb} \underline{\texttt{d}} 
a
​
 cb 
d
​
  using one operation where i = 1i=1.

Help Chef find if it is possible to sort the string using any (possibly zero) number of operations.

Input Format
The first line of the input contains a single integer TT, denoting the number of test cases. The description of TT test cases follows.
The first line of each test case contains NN, the length of the string.
The second line contains a string SS of length NN consisting of lowercase letters of the Latin alphabet.
Output Format
For each test case, print \texttt{YES}YES if it is possible to sort the string by performing any number of operations. 
Otherwise, print \texttt{NO}NO.
"""
"""
1) check given string is already sorted or not.
2) sort given string using swap,last letter replace with first letter
3) again check for given string is equal to sorted_string
4) if given string is equal to sorted_string print YES
5) if given string is not equal to sorted_string print NO

"""
T = int(input())
for t in range(T):
    N=int(input())
    S=list(input())
    sorted_string=sorted(S)
    for i in range(len(S)-1):
        if S[i]!=sorted_string[i]:
            temp = S[i]
            S[i]=S[N-1-i]
            S[N-1-i]=temp
    if S==sorted_string:
        print("YES")
    else:
        print("NO")