
# items = {'A':{"suger": 50},
#              'B':{"flour": 30},
#              'C':{"oil": 100},
#              'D':{ "beans": 150}
#              }

# count_of_each_item = {'suger': 2, 'flour':1 , 'oil': 3}

# for item in count_of_each_item:
#     z = count_of_each_item[item]
#     y = items[item.keys()]

#     print(z,y)

items = {'A':{"suger": 50},
         'B':{"flour": 30},
         'C':{"oil": 100},
         'D':{ "beans": 150}
         }

selected_items = ['suger', 'oil', 'suger']

total_price = 0

for item in selected_items:


    for key, value in items.items():

        if item in value.keys():

            total_price = total_price + value[item]
            break

print(total_price)