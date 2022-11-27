# Creating a Dictionary from list
# with each item as a Pair
# Dict = dict([(1, 'Geeks'), (2, 'For')])

"""
1. declare input list
2. iterate list
3. for each element use dictionary create syntax to add key and value to dict




"""

in_list = [(1, "Geeks"), (2, "For")]
result_dict = {}
for i in range(len(in_list)):
    print(in_list[i][0], in_list[i][1])
    # print(elem[0],elem[1])
    # result_dict[elem[0]] = elem[1]
    result_dict[in_list[i][0]] = in_list[i][1]

print(result_dict)
