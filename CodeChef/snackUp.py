"""
This year CodeChef is organizing the SnackUp cooking contest. The favorite to win is of course our beautiful Chef Ada.

There are n judges in the contest, and for simplicity let's enumerate judges from 1 to n.

Ada has an uncountable repertoire of delicious recipes, but for the contest she choose only n of them. 
Let's also enumerate the recipes from 1 to n.

Ada is going to show off her cooking skills in many rounds, and we are going to help her organizing them! One round is structured as follows:

We will choose k distinct recipes and Ada will prepare two identical dishes for each of them.
We will choose k distinct judges for the round.

We will send k invitation letters (one for each of the chosen judges). Each letter must contain the number of the judge, 
and two distinct integers denoting the ids of the recipes that he is going to taste.

Two different judges can taste the same recipe, but it must be from different dishes.

Ada does not like to waste food, so the letters must be designed in such a way that every prepared dish is tasted.

You can arbitrarily decide the number of rounds and the number of invited judges in each round, 
but as a rule of the contest at the end of all rounds each judge must have tasted every recipe exactly twice.
"""
"""
1) 
2) 
3) 

"""
T = int(input())
for t in range(T):
    N = int(input())
    print(N)
    for i in range(N):
        dish_1=(i%N)+1

        dish_2=(i+1) % N+1
        print(N)
        for j in range(N):

            print(j+1,dish_1,dish_2)


