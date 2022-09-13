"""
problem: https://leetcode.com/problems/search-insert-position/
pattern: floor of the target element
- store the mid when you move towards right because it can be the floor of the search element

"""


from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                result = mid
                left = mid +1
            else:
                right = mid -1
                
        return result+1
                