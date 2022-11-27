"""
Given an array of size n, a triplet (a[i], a[j], a[k]) is called a Magic Triplet
if a[i] < a[j] < a[k] and i < j < k.  
Count the number of magic triplets in a given array.

# Input: arr = [1, 2, 3, 4]
  Output: 4
  Explanation: Fours magic triplets are 
  (1, 2, 3), (1, 2, 4), (1, 3, 4) and 
  (2, 3, 4).

"""


def countTriplets(lst):
    # Code here
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                if i < j < k and lst[i] < lst[j] < lst[k]:
                    count = count + 1
                    print(count)
                    print(i, j, k)
    return count


def main():

    lst = [10, 2, 3, 4, 5]
    count = countTriplets(lst)


main()
