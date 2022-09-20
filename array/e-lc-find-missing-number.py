"""
problem: https://leetcode.com/problems/missing-number/
pattern:
    - sum all the numbers in range
    - sum the actual numbers in the array
    - subtract to find the missing one 
space O(1)
time O(n)
"""


from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        expectedSum = 0
        for i in range(n+1):
            expectedSum +=i
            
        actualSum = sum(nums)
        
        return expectedSum - actualSum