"""
Chef Watson uses a social network called ChefBook, which has a new feed consisting of posts by his friends. 
Each post can be characterized by f - the identifier of the friend who created the post,
 p - the popularity of the post(which is pre-calculated by ChefBook platform using some machine learning algorithm) and 
 s - the contents of the post which is a string of lower and uppercase English alphabets.

Also, Chef has some friends, which he has marked as special.

The algorithm used by ChefBook for determining the order of posts in news feed is as follows:

Posts of special friends should be shown first, irrespective of popularity. 
Among all such posts the popular ones should be shown earlier.
Among all other posts, popular posts should be shown earlier.
Given, a list of identifiers of Chef's special friends and a list of posts, 
you have to implement this algorithm for engineers of ChefBook and output the correct ordering of posts in the new feed.

"""
"""
1) first check of chefs special friends and see who has more popularity for post.
2) then check on rest of post, who has most popularity shows next to fist step
3) and rest of them shows last.


"""
N ,M = input().split()
no_of_special_frnd = int(N)
no_of_post = int(M)
A = list(map(int, input().split()))
list_f = [ ]
list_p = [ ]
list_s = [ ]
for i in range(no_of_post):
    f,p,s = list(input().split())
    list_f.append(int(f))
    list_p.append(int(p))
    list_s.append(s)
special_frnd_lst = [ ]
for i in range(no_of_special_frnd):
    for j in range(len(list_f)):
        if A[i] == A[0]:
            special_frnd = list_f.pop(j)   
            special_frnd_lst.append(special_frnd) 
            break
