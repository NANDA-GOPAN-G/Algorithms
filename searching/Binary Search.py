"""
Program to implement binary search in python

Time Complexity: O(log n)  |  Space Complexity: O(1)
"""

pos = -1  #global variable used for returning position of the searched element in the array

def binary_search(arr, t):
    global pos
    l = 0
    u = len(arr) - 1
    mid = 0

    while l <= u:
        mid = l + (u - l) // 2

        if arr[mid] == t:
            pos =  mid
            return True
        elif arr[mid] < t:
            l = mid + 1
        else:
            u = mid - 1
    
    return False
        
List = [4,7,8,12,45,99]
target = 99
if binary_search(List,target):
    print("Found at", pos)
else:
    print("Not Found")


    

        

