"""
There's a zebra crossing appearing in the middle of nowhere with N blocks in it. 
The colors of the zebra crossing is represented by a binary string S,
where Si is 1 if the i-th block from the left is white, and 0 if the block is black.
Chef really wants to play with the zebra crossing.
Although the given zebra crossing might not have alternate black and white blocks, 
Chef wants to follow the alternating white-black color pattern while crossing it
Initially, Chef stands at block 1. Chef has to jump exactly K times, 
and in each jump he has to move forward and jump to a different color than that previously occupied by Chef. 
More formally, suppose that Chef is currently at block i and wants to jump to blockj then 
following conditions should hold:
1) i<j
2) Si = Sj
​Output:
    the farthest block Chef can reach with exactly K jumps. If Chef cannot jump exactly K times, output -1.
"""
"""
1) check black colour is in first index(i.e 1) 
2) check white colour indexex and jump on greater index of white colour 
3) while jumping num of moves get decrease by 1 after one jump
4) if moves is 0 then print current index
5) else again find opposite colour index than previous one and jump into it.
6) if both cases is not fullfilled then print -1.
"""
T = int(input())
for t in range(T):
    N,K = input().split()
    num_of_blocks = int(N)
    num_of_jumps = int(K)
    s=input()
    position = 0
    next_position =1
    while next_position < num_of_blocks and num_of_jumps > 1:
        if s[next_position] != s [position]:
            position = next_position
            num_of_jumps -= 1
        next_position+=1

    if num_of_jumps ==1:
        for i in range(num_of_blocks-1,position,-1):
            if s[i]!=s[position]:
                num_of_jumps-=1
                position =i
                break

    if num_of_jumps == 0:
        print(position+1)
    else:
        print(-1)