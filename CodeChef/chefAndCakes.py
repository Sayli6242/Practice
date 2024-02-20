"""
Chef has bought N robots to transport cakes for a large community wedding. He has assigned unique indices, from 1 to N, to each of them. How it will happen?

Chef arranges the N robots in a row, in the (increasing) order of their indices. Then, he chooses the first M robots and moves them to the end of the queue. Now, Chef goes to the robot at the first position in the row and hands it one cake. He then notes this robot's index (say k) in his notebook, and goes to the kth position in the row. If the robot at this position does not have a cake, he give him one cake, notes his index in his notebook, and continues the same process. If a robot visited by Chef already has a cake with it, then he stops moving and the cake assignment process is stopped.

Chef will be satisfied if all robots have a cake in the end. In order to prepare the kitchen staff for Chef's wrath (or happiness :) ), you must find out if he will be satisfied or not? If not, you have to find out how much robots have a cake, so that the kitchen staff can prepare themselves accordingly.

"""
"""
1) define array name " robots" to represent arrangement of robots 1 to N.
2) define array "robots_With_cake" to track each robot has cake.
3) move first M robots to end of array by slicing method.
4) start from 0 th index and assing cakes
    - check if robot has already assign cakes then break the loop
    - if not then assign cake and note its index and note its index and move to noted index.
5) then check if all robots have a cake.
    - if all robots have cake print "yes"
    - if not print "No" and print robot count with cakes
"""


T = int(input())
for i in range(T):
    N,M = map(int, input()).split()
    robots = []
    
    # define array to represent arrangement of robots 1 to  N.
    for i in range(1, N+1):
        robots.append(i)
     # Define array to track whether each robot has a cake
    for i in range(N):
        robots_with_cake.append(False)
    
     # Move first M robots to the end of the array
    robots = robots[M:] + robots[:M]
      # Cake assignment process
    current_position = 0
    while not robots_with_cake[current_position]:
        # Assign cake
        robots_with_cake[current_position] = True

        # Move to the noted index
        current_position = robots[current_position] - 1
          # Check satisfaction
    if robots_with_cake:
        print("Yes")
    else:
        print(f"No {robots_with_cake.count(True)}")
