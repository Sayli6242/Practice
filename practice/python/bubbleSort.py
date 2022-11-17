"""
We are creating a list of element, which stores the integer numbers
list1 = [5, 3, 8, 6, 7, 2] by using Bubble Sort
1) compare first two elements in list 
2) if first element is greater than second then swap the element 
3) and make new list 
4) make 




"""

# lst = [5, 3, 8, 6, 7, 2]
# def bubble_sort(lst):
 
#     for i in range(len(lst)-1):
#         for j in range(len(lst)):
#             if lst[j] > lst[j + 1]:
#                 temp = lst[j]
#                 lst[j] = lst[j + 1]
#                 lst[j + 1] = temp

#     return lst


# def main():
#     lst = [5, 3, 8, 6, 7, 2]

#     lst = bubble_sort(lst)
#     print('the sorted list is: ', lst)

# main()

# Python program for implementation of Bubble Sort

def bubbleSort(arr):
	n = len(arr)
	
	for i in range(n-1):
		for j in range(n-1):
			if arr[j] > arr[j + 1]:
			
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    arr = bubbleSort(arr)
    print("Sorted array is: ", arr)
main()

