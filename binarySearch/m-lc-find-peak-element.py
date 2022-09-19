"""
problem: https://leetcode.com/problems/find-peak-element/
pattern: divide and conquer
 - normal binary search 
 - compare the mid with neighbours, if mid is greater than both, mid is the answer
 - move to the side which has higher value 

explanation: why binary search works here ?

if mid is greater than both neighbours than it a local peak and answer
if the mid is not the peak we chose the side which has higher value why ?
    - numbers might ascend and then descend, there would be a peak where the change happens
    - numbers might continue to ascend until the end of the array, we will find the peak at the end
chosing the side that has greater value than mid, gurantees that we will find our local peak eventually
"""

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        #edge cases
        if n == 1: return 0
        if nums[0] > nums[1]: return 0
        if nums[n-1] > nums[n-2]: return n-1
        
        left = 1
        right = n - 2
        
        while left<=right:
            m = left + (right-left) // 2
            if nums[m] > nums[m+1] and nums[m] > nums[m-1]:
                return m
            if nums[m] < nums[m+1]:
                left = m + 1
            else:
                right = m - 1
        
        return -1