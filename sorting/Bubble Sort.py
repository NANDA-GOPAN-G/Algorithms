"""
Program to implement bubble sort in python.

Time Complexity: O(n^2)  |  Space Complexity: O(1)
"""

def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr


List = [10,5,3,8,6,7,2]
print("Array after using Bubble Sort:",bubble_sort(List))
