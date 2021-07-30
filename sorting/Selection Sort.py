"""
Program to implement selection sort in python

Time Complexity: O(n^2)  |  Space Complexity: O(1)
"""

def selection_sort(arr):
    n = len(arr)

    for i in range(n):

        min_pos = i

        for j in range(i+1,n):

            if arr[j] < arr[min_pos]:
                min_pos = j
            
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    
    return arr

List = [5,3,8,6,7,2]
print("List after selection sort:",selection_sort(List))