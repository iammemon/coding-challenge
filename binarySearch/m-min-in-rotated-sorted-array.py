"""
 problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
 Pattern: binary search with slight variation
"""


from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        # storing default min value
        result = nums[0]
        
        while left <= right:
            """
            when the elements b/w two points are sorted,
            this means the left is min element and we break the loop here
            """
            if nums[left] < nums[right]:
                result = min(result,nums[left])
                break
        
            mid = left + (right-left)//2
            # its' possible the mid value can be the min element
            result = min(result,nums[mid])
            """
            we move towards pointer towards the unsorted partition
            we check if the left is smaller than the mid that means this partition is sorted
            and the min element is on the right side 
            otherwise we do our search on the left side            
            """
            if nums[left] <= nums[mid]:
                left = mid +1
            else:
                right = mid -1
        
        return result