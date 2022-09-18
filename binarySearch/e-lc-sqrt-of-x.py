"""
problem: https://leetcode.com/problems/sqrtx/submissions/
pattern:
    - we define range 1 to x and do binary search on it
    - if mid*mid <= x that means it's a possible answer and we store in a variable and continue search on right
    - else the mid is big look for smaller value on left side 
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1 # we don't want to divide by zero
        right = x
        result = 0
        if x == 0: # edge case
            return 0
        
        while left<=right:
            mid = left + (right-left) //2
            
            """
            the logic here is mid*mid <= x but mid*mid can be overflow
            so we divde the x with mid to prevent that
            mid <= x/mid 
            """
            if mid <= x/mid: 
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result