"""
problem: https://www.geeksforgeeks.org/find-index-first-1-infinite-sorted-array-0s-1s/
pattern: 
 - do a while loop to find the correct range for the target
 - and then do normal binary search
"""

from typing import List

def findPosition(arr:List[int])->int:
    left = 0
    right = 1
    target = 1

    while target > arr[right]:
        left = right
        right*=2
    
    index = 0
    while left<=right:
        mid = left + (right-left)//2

        if target == arr[mid]:
            index = mid
            right = mid -1
        else:
            left = mid + 1

    return index

    

# arr = [0, 0, 0, 0, 1, 1]
# print(findPosition(arr))