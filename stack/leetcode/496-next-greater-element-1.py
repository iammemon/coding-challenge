"""
 problem: https://leetcode.com/problems/next-greater-element-i/
 Common question also know as Nearest greater to Right
"""

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = dict()
        stack = []
        for i in range(len(nums2)-1,-1,-1):
            n = nums2[i]
            while stack and n > stack[-1]:
                stack.pop()
            mapping[n] = stack[-1] if stack else -1
            stack.append(n)
        
        result = []
        for n in nums1:
            result.append(mapping[n])
        
        return result