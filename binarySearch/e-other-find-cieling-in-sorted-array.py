


"""
problem: https://www.geeksforgeeks.org/ceiling-in-a-sorted-array/
pattern: 
  - use simple binary search with one addtional change
  - when moving to left side store the mid index because it can be the possible ciel index
"""
from typing import List

def search(nums:List[int],target:int)->int:
    left =0 
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left)//2
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            result = mid # attention
            right = mid -1
        else:
            left = mid + 1
    
    return result




# nums = [1, 2, 8, 10, 10, 12, 19]
# target = 3

# print(search(nums,target))