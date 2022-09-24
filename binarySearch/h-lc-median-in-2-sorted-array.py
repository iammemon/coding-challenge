"""
problem : https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/
pattern: 
    - use binary search on smaller array
    - we use the mid point to partition both array
    - verify if the partition are correct such that all the left elements in both partition are smaller than the right partitions
        - check maxleft of both array is less than the minLeft of both array
    - if partition is valid then return the mid point based on odd or even length
    - if not then shrink or increase the partition based on the maxleft value
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        x = nums1
        y = nums2
        if len(y) < len(x):
            x,y = y,x
                 
        left = 0
        right = len(x)
        total = len(x) + len(y)
        
        while left<=right:
            
            partitionX = (left + right) // 2
            # adding 1 works well with both even and odd total
            partitionY = (total +1)//2  - partitionX
            # conditions if the pointer goes out of bound
            maxLeftX = float('-inf') if partitionX == 0 else x[partitionX-1]
            minRightX = float('inf') if partitionX == len(x) else x[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else y[partitionY-1]
            minRightY = float('inf') if partitionY == len(y) else y[partitionY]
                       
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if total % 2 == 0:
                    return (max(maxLeftX,maxLeftY) + min(minRightX,minRightY)) / 2
                else:
                    return max(maxLeftX,maxLeftY)
            
            elif maxLeftX > minRightY:
                right = partitionX - 1
            else:
                left = partitionX + 1
        
        return -1
                            