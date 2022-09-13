"""
problem : https://www.geeksforgeeks.org/search-almost-sorted-array/ or https://www.educative.io/answers/how-to-search-in-a-nearly-sorted-array
pattern: use binary search,when checking the mid do check it's left and right element as well
"""
from typing import List

def search(nums:List[int],target:int)->int:
    left = 0
    right = len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if target == nums[mid]:
            return mid
        if mid > 0 and target == nums[mid-1]:
            return mid-1
        if mid < len(nums)-1 and target == nums[mid+1]:
            return mid+1

        if target > nums[mid]:
            left = mid + 2
        else:
            right = mid -2
    return -1 

# nums = [15, 20, 30, 25, 35]
# target = 25

# print(search(nums,target))