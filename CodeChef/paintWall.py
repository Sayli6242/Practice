"""
Professor Sahil is a master artist, he always finds creative ways to teach lessons to his students. 
Today in Painting class he took all the students of the class to a wall. 
Professor Sahil asked every student to paint the wall upto a certain integral height one by one 
(second boy starts once the first boy finishes painting) from the bottom with any color of their wish, 
except a student Mudit who was made to stand behind the wall and note down all the data i.e the height upto which each student painted and the color 
Ci every student used. At the end of the painting session Professor asked Mudit to tell how many distinct colors are there on the wall. 
Mudit being a weak student asked you for help.

Formally, given a wall of infinite height, initially unpainted. There occur 
N operations, and in ith operation, the wall is painted upto height Hi with color Ci. 
Suppose in jth operation (j>i) wall is painted upto height Hj with color Cj such that Hj >= Hi, 
the ℎ Cith color on the wall is hidden. At the end of N operations, you have to find the number of distinct colors(>=1) visible on the wall.

Help him find out the number of distinct colors on the wall.
"""

T = int(input())
for t in range(T):
    N , M = list(map(int,input().split()))
    height_of_wall = list(map(int,input().split()))
    paint_colors = list(map(int,input().split()))
    uniqe_colors = [ ]
    for i in range(N):
        count = 0
        for j in range(i+1,N):
            if height_of_wall[j] >= height_of_wall[i]:
                count += 1
                break
        if  count!=0:
            uniqe_colors.append(paint_colors[i])
    z = set(uniqe_colors)
    print(len(z))
