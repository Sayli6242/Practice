"""
A set of integers is called good if there does not exist three distinct elements a, b, c in it such that a + b = c.

Your task is simple. Just output any good set of n integers. All the elements in this set should be distinct and should lie between 1 and 500, both inclusive.

Input
The first line of the input contains an integer T denoting number of test cases. The descriptions of T test cases follow.
The only line of each test case contains an integer n, denoting the size of the needed good set.
Output
For each test case, output a single line containing n integers denoting the elements of the good set, in any order. 
There can be more than one possible good set, and you can output any one of them.
"""

"""
1) take set of numbers in given range
2) make all possible combinations of them
3) obtain sum of those combinations
4) check those combination contain sum is equal to next numbers
5) avoid those num and take next num in a set
6) hence those set is said to be good
7) print those set

"""
