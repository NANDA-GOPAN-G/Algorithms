"""
Program to implement linear search in python

Time Complexity: O(n)  |  Space Complexity: O(1)
"""

pos = -1  #global variable used for returning position of the searched element in the array

def linear_search(arr, t):
    global pos
    i = 0

    while i < len(arr):
        if arr[i] == t:
            pos = i
            return True
        i += 1

    return False


List = [1,2,3,4,5]
target = 4
if linear_search(List, target):
    print("Found at index", pos)
else:
    print("Not found")

