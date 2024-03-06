"""
1) 
2)
3)

"""
T = int(input())
for i in range(T):
    frqncy_sq =input()
    encrypt_txt = input()
    dic = {}
    alpha_letters = "abcdefghijklmnopqrstuvwxyz"
    for i in alpha_letters:
         dic[i] = 0
    for i in encrypt_txt:
        i = i.lower()
        if i in alpha_letters:
            dic[i] += 1