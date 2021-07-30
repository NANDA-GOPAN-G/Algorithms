"""
Program to implement Insertion sort in python

Time Complexity: O(n^2)  |  Space Complexity: O(1)
"""

def insertion_sort(arr):

    for i in range(1,len(arr)):
        value_to_sort = arr[i]

        while arr[i-1] > value_to_sort and i>0:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1
    
    return arr

List = [5,3,8,6,7,2]
print("List after Insertion sort:", insertion_sort(List))