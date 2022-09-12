"""
 problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
 Pattern: do two binary search 
 1 - to find first occurence index,
 2 - to find second occurence index
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # find first index 
        start = 0
        end = len(nums)-1
        first_index = -1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                first_index = mid
                end = mid -1    
            elif nums[mid] > target:
                end = mid-1
            else:
                start= mid+1
        
        # find last index
        start = 0
        end = len(nums)-1
        last_index = -1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                last_index = mid
                start = mid +1    
            elif nums[mid] > target:
                end = mid-1
            else:
                start= mid+1
        
        return [first_index,last_index]