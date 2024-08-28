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
    freq_items = dic.items()
    def get_second_element(item):
        return item[1]
    sorted_freq_items = sorted(freq_items, key=get_second_element, reverse=True)  # Sort the items based on the second element (frequency)
    
    freq_list = list(sorted_freq_items)  