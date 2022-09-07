"""
 problem: https://leetcode.com/problems/largest-rectangle-in-histogram/
 pattern: find nearest smaller to right and left of an element, then calculate area 
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        #if there is no smallest to right or left the default value is 1 outside the index range
        right = [n] * n 
        left = [-1] * n
        
        # find nearest smallest to right:
        stack = []
        for i in range(n-1,-1,-1):
            h = heights[i]
            while stack and h <= heights[stack[-1]]:
                stack.pop()
                
            if stack:
                right[i] = stack[-1]
            
            stack.append(i)
        
        #find nearest smallest to left
        stack = []
        for i in range(n):
            h = heights[i]
            while stack and h <= heights[stack[-1]]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
            
        result = 0
        for i in range(n):
            diff = (right[i] - left[i])-1
            result = max(result,diff*heights[i])
        
        return result
            
        
