"""
problem: https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/
pattern: 
 - do a while loop to find the correct range for the target
 - and then do normal binary search
"""

from typing import List

def findPosition(nums:List[int],target:int)->int:
    left = 0
    right = 1 # we don't know the the end because it's infinite

    # go right until the target is in range
    while target > nums[right]:
        left = right
        right*=2

    # normal binary search
    while left<=right:
        mid = left + (right-left)//2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            left = mid +1
        else:
            right = mid -1

    return -1

# nums = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
# print(findPosition(nums,9))