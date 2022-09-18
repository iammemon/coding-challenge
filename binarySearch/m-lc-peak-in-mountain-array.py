"""
problem: https://leetcode.com/problems/peak-index-in-a-mountain-array/ (mountain == bitonic array)
pattern: Last True element in array
 - mid == 0 is a edge case because it can be the possible last True element eg [5,3,1] => 5 is peak
 - if mid is greater than prev,store in var and go right for more possible last True element
 - otherwise move left for possible True element
 
    Example = 2 3 4 6 9 12 11 8 6 4 1 
              T T T T T T  F  F F F F
    there are possible 6 True element and the last True element is 12 which is also a peak/answer
 
"""

from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left = 0
        right = len(arr) - 1
        answer = -1
        
        while left<=right:
            mid = left + (right-left)//2
            
            if mid == 0 or arr[mid] > arr[mid-1]: 
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return answer

