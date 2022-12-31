"""
Chef wants to order food from a food delivery app. He wishes to order once today, and buy three items costing A_1, A_2A 
1
​
 ,A 
2
​
  and A_3A 
3
​
  rupees, respectively. He'll also order once tomorrow, when he'll buy three items costing B_1, B_2B 
1
​
 ,B 
2
​
  and B_3B 
3
​
  rupees, respectively. There is an additional delivery charge of rupees DD for each order.

He notices that there is a coupon on sale, which costs rupees CC. If he buys that coupon, the delivery charges on any day, on an order of rupees 150150 or more shall be waived (that is, the DD rupees will not be added, if the sum of the costs of the items is \ge 150≥150).

Note that Chef is ordering the three items together on each day, so the delivery charge is charged only once each day. Also, note that it's only needed to buy the coupon once to avail the delivery fee waiver on both days.

Should Chef buy the coupon? Note that Chef shall buy the coupon only if it costs him strictly less than what it costs him without the coupon, in total.

###Input:

The first line of the input contains a single integer TT, denoting the number of test cases.
The first line of each test case contains two space-separated integers DD and CC, denoting the delivery charge, and the price of the coupon, respectively.
The second line of each test case contains three space-separated integers A_1, A_2A 
1
​
 ,A 
2
​
  and A_3A 
3
​
 , denoting the prices of the food items that Chef plans to order on Day 11, respectively.
The third line of each test case contains three space-separated integers B_1B 
1
​
 , B_2B 
2
​
  and B_3B 
3
​
 , denoting the prices of the food items that Chef plans to order on Day 22, respectively.
###Output: For each test case, output YES if Chef should buy the coupon, and NO otherwise, in a separate line.

"""

"""
1) calculate total price of day1 food items.
2) calculate total price of day2 food items.
3) calculate total of both days along with delivery_charge.
4) when chef buy cupon, calculate total price of day1,day2 along with cupon's price
5) compare total price along with cupon and total price along with delivery_charge.
6) when total price along with delivery_charge is more than total price of both days along with cupon, its better to chef to buy cupon.


"""

T = int(input())
for t in range(T):
    D, C = input().split()
    delivery_charge = int(D)
    price_of_cupon = int(C)
    price_of_day1 = list(map(int, input().split()))
    price_of_day2 = list(map(int, input().split()))

    total_of_day1 = sum(price_of_day1)

    total_of_day2 = sum(price_of_day2)

    if total_of_day1 < 150 and total_of_day2 < 150:
        total_of_both_days_with_cupon_price = (
            total_of_day1 + total_of_day2 + price_of_cupon + delivery_charge
        )

    elif total_of_day1 >= 150 and total_of_day2 >= 150:

        total_of_both_days_with_delivery_charge = (
            total_of_day1 + total_of_day2 + (delivery_charge * 2)
        )
        print(total_of_both_days_with_delivery_charge)

        total_of_both_days_with_cupon_price = (
            total_of_day1 + total_of_day2 + price_of_cupon
        )
        if (
            total_of_both_days_with_delivery_charge
            > total_of_both_days_with_cupon_price
        ):
            print("yes")
    else:
        print("no")
